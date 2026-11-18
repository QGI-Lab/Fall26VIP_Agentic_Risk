"""Sequential ticker × registered-metric execution; no cross-company analyst.

Each cell keeps its own ordinary Pipeline audit. The batch pins one resolved
10-K per ticker, reuses SEC JSON within the batch, and reports fiscal years
explicitly. Failures are isolated; results are never ranked or interpreted by AI.
"""
import csv
import io
import logging
import re
import time
import uuid
from datetime import datetime, timezone

from ..config.formulas import FORMULAS
from ..config.settings import Settings
from ..tools.filing_loader import load_filing
from ..tools.sec_client import SECClient
from .cache import atomic_json
from .pipeline import Pipeline


CSV_FIELDS = ["ticker", "entity", "formula_id", "status", "periods", "value", "unit",
              "old_value", "new_value", "absolute_change", "relative_change_percent",
              "period_end", "accession", "source", "source_hash", "decoder_calls",
              "corrections", "seconds", "audit_path", "warnings", "errors"]


def batch_csv(items):
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CSV_FIELDS)
    writer.writeheader()
    for item in items:
        row = {key: item.get(key) for key in CSV_FIELDS}
        row["periods"] = " ".join(item.get("periods", []))
        for key in ("warnings", "errors"):
            row[key] = " | ".join(str(x) for x in item.get(key, []))
        # CSV is a data export; prevent a source label/message becoming a formula.
        row = {k: "'" + v if isinstance(v, str) and v.startswith(("=", "+", "-", "@")) else v
               for k, v in row.items()}
        writer.writerow(row)
    return output.getvalue()


class BatchRunner:
    def __init__(self, settings=None, *, pipeline_factory=Pipeline, loader=load_filing,
                 client_factory=SECClient):
        self.settings = settings or Settings()
        self.pipeline_factory, self.loader, self.client_factory = pipeline_factory, loader, client_factory

    def run(self, tickers, formula_ids, periods=None, on_progress=None):
        tickers = list(dict.fromkeys(t.strip().upper() for t in tickers if t.strip()))
        formulas = list(dict.fromkeys(formula_ids))
        if not tickers or any(not re.fullmatch(r"[A-Z][A-Z0-9.-]{0,14}", t) for t in tickers):
            raise ValueError("Provide one or more valid SEC ticker symbols")
        if not formulas or any(f not in FORMULAS for f in formulas):
            raise ValueError("Select one or more registered metrics")
        if periods is not None and (not periods or any(not re.fullmatch(r"FY\d{4}", p) for p in periods)
                                    or len(set(periods)) != len(periods)):
            raise ValueError("Explicit fiscal years must be distinct FYyyyy tokens")
        ordered = sorted(periods, reverse=True) if periods is not None else None
        if ordered and any(len(ordered) < FORMULAS[f].periods for f in formulas):
            raise ValueError("Not enough explicit fiscal years for the selected metrics")
        if ordered and len(ordered) > max(FORMULAS[f].periods for f in formulas):
            raise ValueError("Too many fiscal years for the selected metrics")
        batch_id = uuid.uuid4().hex
        directory = self.settings.artifact_dir / "batches" / batch_id
        manifest = directory / "batch.json"
        data = {"batch_id": batch_id, "created_utc": datetime.now(timezone.utc).isoformat(),
                "status": "RUNNING", "tickers": tickers, "formula_ids": formulas,
                "period_policy": "explicit_newest_years_per_metric" if ordered else "latest_filing_fiscal_years",
                "explicit_periods": ordered, "qwen_enabled": self.settings.qwen_enabled,
                "config_hash": self.settings.fingerprint(), "items": [],
                "manifest_path": str(manifest.resolve()), "csv_path": str((directory / "results.csv").resolve())}
        atomic_json(manifest, data)
        started = time.perf_counter()

        def notify(event):
            if on_progress:
                try:
                    on_progress(event)
                except Exception:
                    logging.getLogger(__name__).exception("Batch progress callback failed")

        client = self.client_factory(self.settings)
        try:
            for ticker in tickers:
                notify({"phase": "source_started", "ticker": ticker})
                acquisition = time.perf_counter()
                filing = None
                source_error = None
                try:
                    filing, _ = self.loader(ticker, self.settings, client=client)
                    if filing.metadata.get("form") != "10-K":
                        raise ValueError("Resolved source is not a 10-K")
                    source_year = str(filing.metadata.get("fiscal_year", ""))
                    if ordered is None and not re.fullmatch(r"\d{4}", source_year):
                        raise ValueError("Filing has no explicit fiscal year; provide fiscal periods")
                except Exception as exc:
                    source_error = {"type": type(exc).__name__, "message": str(exc)}
                acquisition_seconds = time.perf_counter() - acquisition
                notify({"phase": "source_completed", "ticker": ticker, "error": source_error,
                        "source": filing.source if filing else None, "seconds": acquisition_seconds})
                for formula in formulas:
                    spec = FORMULAS[formula]
                    years = ordered[:spec.periods] if ordered else (
                        [f"FY{int(source_year) - i}" for i in range(spec.periods)] if not source_error else [])
                    item = {"ticker": ticker, "formula_id": formula, "periods": years,
                            "status": "ERROR", "value": None, "unit": spec.unit,
                            "audit_path": None, "warnings": [], "errors": [],
                            "acquisition_seconds": acquisition_seconds,
                            "entity": filing.metadata.get("entity") if filing else None,
                            "period_end": filing.metadata.get("period_end") if filing else None,
                            "accession": filing.metadata.get("accession") if filing else None,
                            "source": filing.source if filing else None,
                            "source_hash": filing.content_hash if filing else None}
                    notify({"phase": "item_started", "ticker": ticker, "formula_id": formula, "periods": years})
                    if source_error:
                        item["errors"] = [source_error]
                    else:
                        try:
                            result = self.pipeline_factory(self.settings).run(
                                "", filing.source, years, formula_id=formula,
                                on_progress=lambda event, t=ticker, f=formula: notify(
                                    {**event, "ticker": t, "formula_id": f}))
                            calc = result.get("calculation_result") or {}
                            comparison = calc.get("comparison", {})
                            item.update(status=result["final_status"], value=calc.get("value"),
                                        audit_path=result.get("audit_path"),
                                        decoder_calls=result.get("decoder_call_count", 0),
                                        corrections=result.get("correction_count", 0),
                                        seconds=result.get("timings", {}).get("total_seconds"),
                                        warnings=result.get("warnings", []), errors=result.get("errors", []),
                                        accepted_evidence=result.get("accepted_evidence", {}),
                                        calculation=calc or None)
                            for key in ("old_value", "new_value", "absolute_change", "relative_change_percent"):
                                item[key] = comparison.get(key)
                            # Use the source actually analyzed, not merely the requested ticker.
                            item["source"] = result.get("filing_source", filing.source)
                            item["source_hash"] = result.get("filing_hash", filing.content_hash)
                        except Exception as exc:
                            item["errors"] = [{"type": type(exc).__name__, "message": str(exc)}]
                    data["items"].append(item)
                    atomic_json(manifest, data)
                    notify({"phase": "item_completed", **item})
        finally:
            client.session.close()
        data["seconds"] = time.perf_counter() - started
        data["status"] = "COMPLETED"
        data["outcomes"] = {status: sum(i["status"] == status for i in data["items"])
                            for status in sorted({i["status"] for i in data["items"]})}
        (directory / "results.csv").write_text(batch_csv(data["items"]), encoding="utf-8-sig", newline="")
        atomic_json(manifest, data)
        return data
