"""Reproduce a real-model three-ticker / three-metric batch; retain all outcomes."""
import hashlib
import json
import math
import uuid
from datetime import datetime, timezone
from decimal import Decimal as D
from pathlib import Path

from financial_filing_agent.config.settings import Settings
from financial_filing_agent.services.batch import BatchRunner, batch_csv
from financial_filing_agent.services.cache import atomic_json


def main():
    settings = Settings()
    if not settings.qwen_enabled:
        raise RuntimeError("This experiment requires Qwen enabled; no silent deterministic fallback")
    tickers = ["MSFT", "AMZN", "NVDA"]
    metrics = ["revenue_growth", "operating_margin", "current_ratio"]
    experiment = Path("reports/experiments") / ("nine-cell-" + uuid.uuid4().hex)
    experiment.mkdir(parents=True, exist_ok=False)
    print("EXPERIMENT " + str(experiment.resolve()), flush=True)
    prior = []
    for path in Path("artifacts/runs").glob("*/audit.json"):
        try:
            state = json.loads(path.read_text(encoding="utf-8")).get("state", {})
            metadata = state.get("filing_metadata", {})
            if metadata.get("entity"):
                prior.append({"entity": metadata["entity"], "cik": str(metadata.get("cik", ""))})
        except (ValueError, OSError):
            continue
    config = {"created_utc": datetime.now(timezone.utc).isoformat(), "tickers": tickers,
              "metrics": metrics, "qwen_enabled": True, "period_policy": "latest_filing_fiscal_years",
              "previous_entities": list({(p["entity"], p["cik"]) for p in prior}),
              "source_manifest": {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in Path("src/financial_filing_agent").rglob("*.py")
                                  if "__pycache__" not in p.parts}}
    atomic_json(experiment / "experiment.json", config)

    def progress(event):
        receipt = {"utc": datetime.now(timezone.utc).isoformat(), **event}
        with (experiment / "progress.jsonl").open("a", encoding="utf-8") as output:
            output.write(json.dumps(receipt, ensure_ascii=False) + "\n")
        if event["phase"] in {"source_started", "source_completed", "item_started", "item_completed"}:
            print(json.dumps({k: event.get(k) for k in ("phase", "ticker", "formula_id", "periods", "status", "value", "error")}, ensure_ascii=False), flush=True)

    result = BatchRunner(settings).run(tickers, metrics, on_progress=progress)
    for item in result["items"]:
        if item["status"] != "SUCCESS":
            item["independent_check"] = {"status": "NOT_APPLICABLE", "reason": "No successful numeric answer"}
            continue
        calc = item["calculation"]
        values = calc["inputs"]
        years = item["periods"]
        number = lambda c, p: D(str(values[c][p]))
        if item["formula_id"] == "revenue_growth":
            new, old = years
            expected = (number("revenue", new) - number("revenue", old)) / number("revenue", old) * 100
        else:
            numerator, denominator = (("operating_income", "revenue") if item["formula_id"] == "operating_margin"
                                      else ("current_assets", "current_liabilities"))
            expected = number(numerator, years[0]) / number(denominator, years[0])
            if item["formula_id"] == "operating_margin":
                expected *= 100
        audit = json.loads(Path(item["audit_path"]).read_text(encoding="utf-8"))
        state = audit["state"]
        rows = {r["evidence_id"]: r for r in json.loads(Path(state["evidence_artifact_reference"]).read_text(encoding="utf-8"))}
        evidence = {}
        valid = True
        for component, ident in state["accepted_evidence"].items():
            row = rows[ident]
            facts = [f for f in row["facts"] if f["period"] in years]
            checks = {"unique_periods": all(sum(f["period"] == p for f in facts) == 1 for p in years),
                      "empty_dimensions": all(not f["dimensions"] for f in facts),
                      "values_match_calculator": all(f["value"] == values[component][f["period"]] for f in facts),
                      "source_hash_matches": row["filing_hash"] == item["source_hash"]}
            valid = valid and all(checks.values())
            evidence[component] = {"id": ident, "label": row["label"], "statement": row["statement"],
                                   "facts": facts, "checks": checks}
        arithmetic = math.isclose(float(expected), calc["value"], rel_tol=1e-12, abs_tol=1e-12)
        item["independent_check"] = {"status": "PASS" if arithmetic and valid else "FAIL",
            "decimal_result": str(expected), "arithmetic_matches": arithmetic, "accepted_evidence": evidence,
            "scope": "Stored-input arithmetic and source-record consistency; not independently annotated financial ground truth"}
        item["scope_preflight"] = {c: [{k: d.get("scope_preflight", {}).get(k) for k in ("input_count", "eligible_count", "excluded_count")}
                                       for d in records] for c, records in state["retrieval_diagnostics"].items()}
        item["model_versions"] = state["model_versions"]
        item["audit_complete"] = state.get("audit_complete")
    atomic_json(experiment / "results.json", result)
    (experiment / "results.csv").write_text(batch_csv(result["items"]), encoding="utf-8-sig", newline="")
    lines = ["# Three Previously Untested Stocks × Three Metrics: Live Experiment", "",
             "Experiment date: November 11, 2026 (America/New_York).", "",
             "## Protocol", "",
             "Tickers: MSFT, AMZN, NVDA. Metrics: revenue_growth, operating_margin, current_ratio. "
             "Previous canonical user-run audits contained Apple and Tesla only. Each ticker was resolved to its latest SEC 10-K. "
             "Fiscal years were derived from explicit filing metadata. FinBERT and Qwen were actually used; no scripted doubles, "
             "no analyst agent, no prompt or policy changes, and no silent decoder-off fallback. "
             "Different companies can have different fiscal periods; this is execution evidence, not an aligned investment comparison.", "",
             f"Batch ID: `{result['batch_id']}`. Total time: {result['seconds']:.2f} seconds. Outcomes: `{result['outcomes']}`.", "",
             "## Results", "",
             "| Ticker | Metric | Fiscal years | Status | Value | Unit | Qwen calls | Corrections | Seconds |",
             "|---|---|---|---|---:|---|---:|---:|---:|"]
    for i in result["items"]:
        value = f"{i['value']:.9f}" if i["value"] is not None else "—"
        lines.append(f"| {i['ticker']} | {i['formula_id']} | {', '.join(i['periods'])} | {i['status']} | {value} | {i['unit']} | {i.get('decoder_calls', '—')} | {i.get('corrections', '—')} | {i.get('seconds', 0) or 0:.2f} |")
    lines += ["", "## Source and audit records", ""]
    for i in result["items"]:
        lines += [f"### {i['ticker']} / {i['formula_id']}", "",
                  f"- Period end: `{i.get('period_end')}`; accession: `{i.get('accession')}`.",
                  f"- Source: {i.get('source')}", f"- SHA-256: `{i.get('source_hash')}`.",
                  f"- Audit: `{i.get('audit_path')}`.",
                  f"- Independent consistency check: `{i['independent_check']['status']}`.",
                  "- Errors: " + json.dumps(i.get("errors", []), ensure_ascii=False),
                  "- Warnings: " + json.dumps(i.get("warnings", []), ensure_ascii=False), ""]
    lines += ["## Interpretation limits", "",
              "SUCCESS means the implemented evidence and calculation gates passed, not that every Qwen interpretation was independently proven. "
              "Decimal recomputation validates arithmetic from stored inputs. The extra checks validate requested-period uniqueness, "
              "empty dimensions, matching input values and source hashes. They do not establish held-out financial-answer accuracy. "
              "Any ERROR/INSUFFICIENT_EVIDENCE is retained rather than omitted or converted into an answer.", "",
              "## Saved files", "", "- [Detailed results and consistency checks](results.json)",
              "- [CSV table](results.csv)", "- [Progress events](progress.jsonl)",
              "- [Experiment configuration and source hashes](experiment.json)",
              f"- Original batch manifest: `{result['manifest_path']}`.",
              f"- Original batch CSV: `{result['csv_path']}`.", ""]
    (experiment / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print("FINISHED " + str((experiment / "REPORT.md").resolve()), flush=True)
    print(json.dumps(result["outcomes"]), flush=True)


if __name__ == "__main__":
    main()
