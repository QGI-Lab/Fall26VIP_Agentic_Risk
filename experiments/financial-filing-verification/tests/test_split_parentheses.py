import pytest

from financial_filing_agent.schemas.evidence import Filing
from financial_filing_agent.tools.evidence_builder import retrieval_text
from financial_filing_agent.tools.filing_parser import parse_filing
from financial_filing_agent.tools.numeric_parser import number


@pytest.mark.parametrize("raw", ["(4,901", "( 4,901", "4,901)", "(", ")", "(4,901))", "((4,901)"])
def test_incomplete_parentheses_are_unresolved_not_positive_numbers(raw):
    assert number(raw) is None


@pytest.mark.parametrize("raw,expected", [("(4,901)", -4901), ("( 4,901 )", -4901),
    ("($4,901.25)", -4901.25), ("-4,901", -4901), ("4,901", 4901),
    ("0", 0), ("—", 0)])
def test_complete_financial_numbers_keep_sign_and_value(raw, expected):
    assert number(raw) == expected


def test_split_display_text_is_preserved_without_crashing():
    cells = ["Other income (expense), net", "(4,901", ")", "(1,646", ")"]
    assert retrieval_text(cells) == "Other income (expense), net | (4,901 | ) | (1,646 | )"


def test_msft_style_split_parentheses_preserve_authoritative_xbrl_negative():
    html = '''<html><body>
    <xbrli:context id="c"><xbrli:period><xbrli:startDate>2024-07-01</xbrli:startDate>
    <xbrli:endDate>2025-06-30</xbrli:endDate></xbrli:period></xbrli:context>
    <xbrli:unit id="usd"><xbrli:measure>iso4217:USD</xbrli:measure></xbrli:unit>
    <p>CONSOLIDATED STATEMENTS OF INCOME in USD millions</p><table>
    <tr><th>Line item</th><th>2025</th><th></th><th>2024</th></tr>
    <tr><td>Revenue</td><td>110</td><td></td><td>100</td></tr>
    <tr><td>Operating income</td><td>30</td><td></td><td>25</td></tr>
    <tr><td>Other income (expense), net</td><td>(<ix:nonFraction
    name="us-gaap:NonoperatingIncomeExpense" contextRef="c" unitRef="usd"
    format="ixt:num-dot-decimal" scale="6" sign="-">4,901</ix:nonFraction></td><td>)</td><td>100</td></tr>
    </table></body></html>'''
    rows, _ = parse_filing(html, Filing(source="test", content_hash="hash", local_path="test"))
    expense = next(r for r in rows if r.label == "Other income (expense), net")
    assert expense.facts[0].value == -4_901_000_000
    assert expense.facts[0].raw_value == "4,901"
    assert expense.facts[0].context_id == "c"
    assert "( 4,901" in expense.raw_cells and ")" in expense.raw_cells
    revenue = next(r for r in rows if r.label == "Revenue")
    assert [f.value for f in revenue.facts] == [110, 100]


def test_plain_html_partial_negative_is_not_guessed():
    html = '''<p>CONSOLIDATED STATEMENTS OF OPERATIONS in USD</p><table>
    <tr><th>Line item</th><th>2025</th><th></th><th>2024</th></tr>
    <tr><td>Revenue</td><td>110</td><td></td><td>100</td></tr>
    <tr><td>Operating income</td><td>(10</td><td>)</td><td>25</td></tr></table>'''
    rows, _ = parse_filing(html, Filing(source="test", content_hash="hash", local_path="test"))
    row = next(r for r in rows if r.label == "Operating income")
    assert [(f.period, f.value) for f in row.facts] == [("FY2024", 25)]
