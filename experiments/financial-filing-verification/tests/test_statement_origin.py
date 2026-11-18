import pytest

from financial_filing_agent.agents.verification_contract import build_contract, validate_review, review_schema, VerifierContractError
from financial_filing_agent.config.settings import Settings
from financial_filing_agent.schemas.evidence import Filing
from financial_filing_agent.services.pipeline import Pipeline
from financial_filing_agent.tools.filing_parser import parse_filing
from financial_filing_agent.tools.statement_origin import scope_context
from tests.test_metric_workflow import ConceptRetriever
from evaluation.doubles import ScriptedDecoder


POLICY = "The consolidated financial statements include the accounts of Example Corporation and its subsidiaries."
HTML = '''<html><body><a href="#income">Income Statements</a><a href="#balance">Balance Sheets</a>
<a href="#cash">Cash Flows Statements</a>
<p id="income">INC OME STATEMENTS</p><table>
<tr><th>Line item</th><th>2025</th><th>2024</th></tr>
<tr><td>Total net sales</td><td>110</td><td>100</td></tr>
<tr><td>Operating income</td><td>30</td><td>25</td></tr></table>
<p id="balance">BALANCE SHEETS</p><table>
<tr><th>Line item</th><th>2025</th><th>2024</th></tr>
<tr><td>Total current assets</td><td>200</td><td>180</td></tr>
<tr><td>Total current liabilities</td><td>100</td><td>90</td></tr></table>
<p id="cash">CASH FLOWS S TATEMENTS</p><table>
<tr><th>Line item</th><th>2025</th></tr><tr><td>Revenue</td><td>9</td></tr>
<tr><td>Net income</td><td>4</td></tr></table>
<p>Segment revenue, operating expenses, and operating income were as follows:</p><table>
<tr><th>Line item</th><th>2025</th><th>2024</th></tr>
<tr><td>Total net sales</td><td>110</td><td>100</td></tr>
<tr><td>Operating income</td><td>30</td><td>25</td></tr></table>
<p>POLICY</p></body></html>'''.replace("POLICY", POLICY).replace("<body>", "<body><p>Amounts in USD</p>")


def parse(html=HTML, entity="Example Corporation"):
    return parse_filing(html, Filing(source="test", content_hash="hash", local_path="test",
                                    metadata={"entity": entity}))


def test_toc_primary_table_binding_and_policy_do_not_leak_to_notes():
    rows, statements = parse()
    primary = next(r for r in rows if r.table == 0)
    note = next(r for r in rows if r.table == 3)
    assert primary.statement_origin["heading"] == "INC OME STATEMENTS"
    assert primary.statement_origin["toc_href"] == "#income"
    assert primary.statement_origin["consolidation_quote"] == POLICY
    assert POLICY in scope_context(primary)
    assert not note.statement_origin
    assert POLICY not in scope_context(note)
    assert 2 not in {r.table for r in rows}, "TOC-bound cash-flow table must not enter operations pool"


@pytest.mark.parametrize("entity", [None, "Other Corporation"])
def test_missing_or_wrong_entity_cannot_certify_scope(entity):
    rows, _ = parse(entity=entity)
    row = next(r for r in rows if r.table == 0)
    assert "consolidation_quote" not in row.statement_origin
    assert POLICY not in scope_context(row)


@pytest.mark.parametrize("changed", [
    HTML.replace('<a href="#income">Income Statements</a>', ''),
    HTML.replace('<a href="#income">Income Statements</a>', '<a href="https://example.com/#income">Income Statements</a>'),
    HTML.replace('<p id="income">INC OME STATEMENTS</p>', '<p id="income">Unaudited pro forma income statements</p>'),
    HTML.replace('<p id="income">INC OME STATEMENTS</p>', '<p id="income">INC OME STATEMENTS</p><p>Segment-specific disclosure:</p>'),
])
def test_unbound_or_qualified_headings_do_not_inherit_global_policy(changed):
    rows, _ = parse(changed)
    row = next(r for r in rows if r.table == 0)
    assert not row.statement_origin
    assert POLICY not in scope_context(row)


def test_scope_context_requires_matching_hash_and_statement():
    rows, _ = parse()
    row = next(r for r in rows if r.table == 0)
    row.statement_origin["filing_hash"] = "foreign"
    assert POLICY not in scope_context(row)
    row.statement_origin["filing_hash"] = "hash"
    row.statement_origin["statement"] = "balance"
    assert POLICY not in scope_context(row)


def test_primary_supported_row_precedes_higher_score_note_without_hiding_scores(tmp_path):
    rows, _ = parse()
    class PreferNote(ConceptRetriever):
        def rank(self, rows, component, periods, query):
            ranked, diagnostic = super().rank(rows, component, periods, query)
            for r in ranked:
                r["fusion_score"] = 10 if ":t03_" in r["evidence_id"] else 1
            return sorted(ranked, key=lambda r: -r["fusion_score"]), diagnostic
    pipeline = Pipeline(Settings(artifact_dir=tmp_path), ScriptedDecoder(), PreferNote())
    ranked, diag = pipeline.rank_eligible([r for r in rows if r.statement == "operations"],
                                        "revenue", ["FY2025", "FY2024"], "revenue")
    assert ":t00_" in ranked[0]["evidence_id"] and ranked[0]["fusion_score"] == 1
    assert any(r["fusion_score"] == 10 for r in ranked)
    assert diag["primary_statement_preference"]["supported_count"] == 1


def test_policy_quote_is_reviewable_without_consolidated_word_in_heading():
    rows, _ = parse()
    row = next(r for r in rows if r.table == 0)
    pipeline = Pipeline(Settings(), ScriptedDecoder(), ConceptRetriever())
    request = {"proposed_evidence": pipeline.decoder_evidence(row, ["FY2025"]),
               "required_component": "revenue", "formula_id": "revenue_growth", "expected_statement": "operations",
               "required_periods": ["FY2025"], "deterministic_concept_assessment": {"status": "PASS"}}
    request["verification_contract"] = build_contract(request)
    from evaluation.review_double import review_checks
    checks = review_checks(request)
    checks[0]["evidence_quote"] = POLICY
    import json
    schema = review_schema(tuple(request["verification_contract"]["open_checks"]),
                           json.dumps(request["proposed_evidence"], sort_keys=True))
    # Schema permits actual bounded source snippets, not arbitrary invented text.
    checks[0]["evidence_quote"] = request["proposed_evidence"]["nearby_context"]
    result = schema.model_validate({"checks": checks, "confidence": 0.9, "reason": "Bound primary statement plus source policy"})
    validate_review(result, request)
    assert result.verdict == "PASS"
    result.checks[0].evidence_quote = "INC OME STATEMENTS"
    with pytest.raises(VerifierContractError):
        validate_review(result, request)
