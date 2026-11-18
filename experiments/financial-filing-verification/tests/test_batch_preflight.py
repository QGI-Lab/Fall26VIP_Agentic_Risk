import json
from pathlib import Path
from unittest.mock import Mock

import pytest

from financial_filing_agent.config.settings import Settings
from financial_filing_agent.config.formulas import registered_plan
from financial_filing_agent.schemas.evidence import EvidenceRow
from financial_filing_agent.services.batch import BatchRunner, batch_csv
from financial_filing_agent.services.pipeline import Pipeline
from financial_filing_agent.tools.input_inventory import inventory
from financial_filing_agent.tools.sec_client import SECClient
from financial_filing_agent.tools.validation import scope_eligible
from evaluation.doubles import ScriptedDecoder
from tests.test_metric_workflow import ConceptRetriever


DEMO = Path("evaluation/fixtures/demo.html")


def synthetic_rows(filing, dimensioned_only=False):
    common = dict(filing_hash=filing.content_hash, source=filing.source, statement="operations", table=0,
                  label="Total net sales", text="Total net sales 110 100",
                  nearby_context="CONSOLIDATED STATEMENTS OF OPERATIONS")
    facts = [dict(period=p, value=v, raw_value=str(v), unit="currency", currency="USD", cell=i)
             for i, (p, v) in enumerate([("FY2025", 110), ("FY2024", 100)])]
    good = EvidenceRow(evidence_id="primary", row=1, facts=facts, **common)
    bad = good.model_copy(deep=True)
    bad.evidence_id = "vie"
    for f in bad.facts:
        f.dimensions = {"srt:ConsolidatedEntitiesAxis": "us-gaap:VariableInterestEntityPrimaryBeneficiaryMember"}
        f.value = 1
    return ([bad] if dimensioned_only else [bad, good]), [{"table": 0, "type": "operations"}]


@pytest.mark.parametrize("dimensioned_only", [False, True])
def test_dimensioned_evidence_never_reaches_retrieval_or_qwen(tmp_path, monkeypatch, dimensioned_only):
    monkeypatch.setattr("financial_filing_agent.services.pipeline.parse_filing",
                        lambda html, filing: synthetic_rows(filing, dimensioned_only))
    class Retriever(ConceptRetriever):
        def rank(self, rows, component, periods, query):
            assert all(scope_eligible(row, periods) for row in rows)
            return super().rank(rows, component, periods, query)
    decoder = ScriptedDecoder()
    result = Pipeline(Settings(artifact_dir=tmp_path), decoder, Retriever()).run(
        "", str(DEMO), ["FY2025", "FY2024"], formula_id="revenue_growth")
    expected = "INSUFFICIENT_EVIDENCE" if dimensioned_only else "SUCCESS"
    assert result["final_status"] == expected, result["errors"]
    diag = result["retrieval_diagnostics"]["revenue"][0]["scope_preflight"]
    assert diag["excluded_count"] == 1 and diag["excluded"][0]["evidence_id"] == "vie"
    assert all(call["request"].get("proposed_evidence", {}).get("evidence_id") != "vie" for call in decoder.calls)
    if dimensioned_only:
        assert not decoder.calls and result["calculation_result"] is None
        assert result["input_inventory"][0]["status"] != "FOUND"
    else:
        assert result["calculation_result"]["value"] == 10
        assert result["correction_count"] == 0
        assert result["guard_results"]["revenue"][-1]["passed"]


def test_verifier_entry_point_blocks_dimensioned_proposal(tmp_path):
    from financial_filing_agent.schemas.evidence import Filing
    filing = Filing(source="test", content_hash="test", local_path="test")
    rows, _ = synthetic_rows(filing, True)
    path = tmp_path / "evidence.json"
    path.write_text(json.dumps([r.model_dump() for r in rows]), encoding="utf-8")
    decoder = Mock()
    pipeline = Pipeline(Settings(artifact_dir=tmp_path), decoder, ConceptRetriever())
    result = pipeline.verification(dict(evidence_artifact_reference=str(path), filing_hash="test",
        proposed_id="vie", active_component="revenue", required_periods=["FY2025", "FY2024"],
        guard_results={}, warnings=[], correction_attempts=0))
    decoder.complete.assert_not_called()
    assert result["guard_results"]["revenue"][0]["phase"] == "pre_verifier"
    assert not result["guard_results"]["revenue"][0]["passed"]


def test_dimensions_outside_requested_periods_do_not_reject_valid_years():
    from financial_filing_agent.schemas.evidence import Filing
    rows, _ = synthetic_rows(Filing(source="test", content_hash="test", local_path="test"))
    bad, good = rows
    extra = bad.facts[0].model_copy(deep=True)
    extra.period = "FY2023"
    good.facts.append(extra)
    assert scope_eligible(good, ["FY2025", "FY2024"])
    assert not scope_eligible(good, ["FY2023"])


def test_sec_json_cache_is_instance_scoped_and_returns_copies(monkeypatch):
    client = SECClient(Settings(sec_user_agent="Test test@example.com"))
    response = Mock(is_redirect=False)
    response.json.return_value = {"name": "Test"}
    get = Mock(return_value=response)
    monkeypatch.setattr(client.session, "get", get)
    first = client.get("https://data.sec.gov/test", True)
    first["name"] = "changed"
    assert client.get("https://data.sec.gov/test", True) == {"name": "Test"}
    assert get.call_count == 1


def test_batch_pins_source_once_isolates_failures_and_exports_periods(tmp_path):
    settings = Settings(artifact_dir=tmp_path, qwen_enabled=False)
    from financial_filing_agent.tools.filing_loader import load_filing
    filing, _ = load_filing(str(DEMO), settings)
    filing.metadata.update(form="10-K", fiscal_year="2025", entity="Demo", accession="demo-accession")
    calls = []
    def loader(ticker, settings, client):
        calls.append(ticker)
        if ticker == "BAD":
            raise ValueError("Ticker not found uniquely")
        return filing, ""
    def factory(settings):
        return Pipeline(settings, ScriptedDecoder(), ConceptRetriever())
    result = BatchRunner(settings, loader=loader, pipeline_factory=factory).run(
        ["test", "BAD", "TEST"], ["revenue_growth", "operating_margin"])
    assert calls == ["TEST", "BAD"]
    assert len(result["items"]) == 4
    assert result["outcomes"] == {"ERROR": 2, "SUCCESS": 2}
    growth, margin = result["items"][:2]
    assert growth["periods"] == ["FY2025", "FY2024"] and margin["periods"] == ["FY2025"]
    assert growth["value"] == 10 and margin["value"] == pytest.approx(30 / 110 * 100)
    assert growth["audit_path"] != margin["audit_path"]
    assert Path(result["manifest_path"]).is_file() and Path(result["csv_path"]).is_file()
    assert json.loads(Path(result["manifest_path"]).read_text(encoding="utf-8"))["status"] == "COMPLETED"
    assert "FY2025 FY2024" in batch_csv(result["items"])
    assert all(item["value"] is None for item in result["items"][2:])


@pytest.mark.parametrize("tickers,metrics,periods", [([], ["revenue_growth"], None),
    (["TSLA"], ["unknown"], None), (["TSLA"], ["revenue_growth"], ["FY2025"]),
    (["TSLA"], ["current_ratio"], ["FY2025", "FY2024"]),
    (["TSLA"], ["current_ratio"], [])])
def test_batch_rejects_invalid_requests_before_network(tmp_path, tickers, metrics, periods):
    loader = Mock()
    with pytest.raises(ValueError):
        BatchRunner(Settings(artifact_dir=tmp_path), loader=loader).run(tickers, metrics, periods)
    loader.assert_not_called()
