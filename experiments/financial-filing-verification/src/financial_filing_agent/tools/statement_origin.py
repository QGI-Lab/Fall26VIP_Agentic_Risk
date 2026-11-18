"""Source-bound primary-statement provenance, without issuer-specific rules."""
import re
from urllib.parse import unquote

from .numeric_parser import normalize


TITLE_TYPES = {
    "incomestatements": "operations", "statementsofincome": "operations",
    "statementofincome": "operations", "statementsofoperations": "operations",
    "statementofoperations": "operations", "balancesheets": "balance", "balancesheet": "balance",
    "cashflowsstatements": "other", "cashflowstatements": "other", "statementsofcashflows": "other",
    "comprehensiveincomestatements": "other", "statementsofcomprehensiveincome": "other",
    "stockholdersequitystatements": "other", "statementsofstockholdersequity": "other",
}


def title_type(text):
    # HTML can split letters into spans: "INC OME STATEMENTS" is source text.
    compact = re.sub(r"[^a-z]", "", text.lower())
    if compact.startswith("consolidated"):
        compact = compact[len("consolidated"):]
    return TITLE_TYPES.get(compact)


def primary_statement_origins(soup, filing):
    """Bind TOC heading targets to the immediately following source table.

    Attach a document policy ONLY to those tables, and ONLY when it explicitly
    names the filing entity and subsidiaries. Notes do not inherit this policy.
    """
    policy = None
    entity = normalize(filing.metadata.get("entity") or "")
    if entity:
        pattern = (r"\bconsolidated financial statements include the accounts of " + re.escape(entity)
                   + r" and (?:its |their |our )?subsidiaries\b")
        for index, paragraph in enumerate(soup.find_all("p")):
            text = paragraph.get_text(" ", strip=True)
            if len(text) <= 300 and re.search(pattern, normalize(text)):
                policy = {"quote": text, "paragraph": index}
                break
    origins = {}
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        toc_text = anchor.get_text(" ", strip=True)
        toc_kind = title_type(toc_text)
        if toc_kind is None or not isinstance(href, str) or not href.startswith("#"):
            continue
        target = soup.find(id=unquote(href[1:]))
        if target is None or target.find_parent("table") is not None:
            continue
        heading = target.get_text(" ", strip=True)
        kind = title_type(heading)
        if kind is None or toc_kind != kind or len(heading) > 120:
            continue
        table = target.find_next("table")
        if table is None:
            continue
        before, reached = [], False
        for node in table.previous_elements:
            if node is target:
                reached = True
                break
            if getattr(node, "name", None) == "table":
                break
            if isinstance(node, str) and node.strip():
                before.append(str(node).strip())
                if sum(map(len, before)) > 300:
                    break
        # Reject intervening prose/tables: an old heading must not bind a note.
        if not reached or " ".join(reversed(before)).strip() != heading:
            continue
        origin = {"role": "primary_statement", "statement": kind, "heading": heading,
                  "heading_id": target.get("id"), "toc_text": toc_text, "toc_href": href,
                  "filing_hash": filing.content_hash}
        if policy and kind in {"operations", "balance"}:
            origin["consolidation_quote"] = policy["quote"]
            origin["consolidation_paragraph"] = policy["paragraph"]
        origins[id(table)] = origin
    return origins


def scope_context(row):
    """Bounded review view; never append a file policy to an unbound note."""
    origin = row.statement_origin
    if (origin.get("role") == "primary_statement" and origin.get("filing_hash") == row.filing_hash
            and origin.get("statement") == row.statement and origin.get("consolidation_quote")):
        return origin["heading"] + "\n" + origin["consolidation_quote"]
    return row.nearby_context[-250:]
