"""Build and verify a small, source-complete course submission (standard library).

Prepare a candidate, validate its extracted source, then finalize with receipts.
Never recursively copy the workspace or delete research/environment files.
"""
import argparse
import ast
import hashlib
import json
import re
import shutil
import uuid
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOTS = ("src", "tests", "evaluation", "scripts", "reports")
BLOCKED = {"__pycache__", ".git", ".venv", ".venv-check", ".uv_cache", ".pytest_cache", "artifacts", "dist"}
PURPOSES = {
    "cli": "Single-run/batch CLI arguments, execution and exit status.",
    "settings": "Validated settings, environment loading and configuration fingerprint.",
    "prompts": "Actual planner/verifier/corrector system instructions.",
    "formulas": "Ten registered metrics, dependencies, units and deterministic menu planning.",
    "financial_concepts": "Canonical concepts, reported-label aliases and supported XBRL tags.",
    "state": "Serializable graph-state field declarations.",
    "evidence": "Typed filing, evidence-row and numeric-fact provenance models.",
    "task": "Task-plan schema and registry/period/dependency validation.",
    "results": "Verification, correction and calculation schemas; Python verdict aggregation.",
    "finbert": "Batched masked-mean/L2 encoder, device choice and process cache.",
    "local_decoder": "Ollama HTTP/JSON adapter, model diagnostics and bounded retries.",
    "finbert_retriever": "Content/version-keyed row embedding cache.",
    "lexical_retriever": "Alias, token overlap and XBRL-name support signals.",
    "hybrid_retriever": "FinBERT/lexical/XBRL score fusion and retrieval diagnostics.",
    "sufficiency": "Structural evidence sufficiency decisions.",
    "planner": "Free-question mapping to registered tasks and explicit-period checks.",
    "verifier": "One-row decoder review and bounded contract repair.",
    "verification_contract": "Per-request open checks, dynamic schemas and source-quote validation.",
    "corrector": "Allowed replacement/expansion decisions and candidate-ID enforcement.",
    "workflow": "Fourteen-node LangGraph construction and allowed edges.",
    "routing": "Terminal-status versus next-node route selection.",
    "pipeline": "Full orchestration, component iteration, review/guards, finalization and audit.",
    "batch": "Sequential ticker-by-metric runs with source pinning and JSON/CSV output.",
    "audit": "Per-run state/model-call receipts and recovery snapshots.",
    "cache": "SHA-256 and UTF-8 atomic JSON persistence with finite Windows retries.",
    "progress": "Node labels and observational progress summaries.",
    "html": "BeautifulSoup/lxml parsing adapter.",
    "sec_client": "Identified, restricted-host SEC acquisition, ticker resolution and batch JSON cache.",
    "filing_loader": "Local/SEC HTML loading, content cache, hashes and DEI metadata.",
    "filing_parser": "Logical tables, statement classification, fiscal columns and evidence construction.",
    "xbrl": "Inline XBRL contexts, units, dimensions, sign/scale and supported transformations.",
    "evidence_builder": "Compact retrieval text preserving distinct numeric cells.",
    "numeric_parser": "Conservative financial-cell parsing, complete parentheses and label normalization.",
    "input_inventory": "Required component-by-year coverage matrix.",
    "supporting_filing": "Opt-in complete same-company supporting-source selection.",
    "statement_origin": "Internal TOC/heading/table binding and entity-specific consolidation evidence.",
    "concept_validation": "Unit-aware concept assessment and optional Decimal gross-profit identity.",
    "validation": "Early dimension eligibility, row guards and cross-input compatibility.",
    "calculator": "Registered Python metric arithmetic and period comparisons.",
    "streamlit_app": "Main Streamlit form, mode settings, uploads and live execution progress.",
    "components": "Result/evidence/diagnostic panels and audit-state download.",
    "batch_components": "Multiple-ticker/metric UI, progress and export downloads.",
    "fixtures": "Development filing paths and post-execution numeric references; no runtime gold input.",
    "doubles": "Explicit scripted decoder/retriever doubles for offline workflow demonstrations.",
    "review_double": "Source-shaped verification observations used by test doubles.",
    "runner": "Self-contained offline success, recovery and missing-evidence demonstrations.",
    "metrics": "Post-run outcome/value/component comparisons against evaluation references.",
    "live_demo": "Optional live-model scenarios, including deliberately controlled ranking stress.",
    "freeze_development": "Optional notebook snapshot utility; requires an external notebook argument.",
    "prepare_submission": "Allowlisted ZIP builder, Python-completeness/hash checks and validation receipts.",
    "build_project_encyclopedia": "Optional generator requiring the research encyclopedia manuscript.",
    "build_evidence_index": "Optional historical-audit index requiring manuscripts, audits and an old XML receipt.",
    "run_nine_cell_experiment": "Optional historical three-ticker live experiment using SEC/Ollama.",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def python_files():
    files = [ROOT / "app.py"]
    for name in PYTHON_ROOTS:
        files.extend(p for p in (ROOT / name).rglob("*.py") if not (set(p.relative_to(ROOT).parts) & BLOCKED))
    return sorted(set(files))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def xml_receipt(source, target):
    tree = ET.parse(source)
    for parent in tree.iter():
        parent.attrib.pop("hostname", None)
        # Pytest's skipped-test text can contain absolute Windows source paths.
        # Strip that prefix while preserving the test file and skip reason.
        def public_text(value):
            return re.sub(r"[A-Za-z]:(?:\\+|/).*?[\\/]+tests[\\/]+", "<project>/tests/", value)
        parent.attrib.update({key: public_text(value) for key, value in parent.attrib.items()})
        if parent.text:
            parent.text = public_text(parent.text)
        for child in list(parent):
            if child.tag in {"system-out", "system-err", "properties"}:
                parent.remove(child)
    suites = list(tree.getroot().iter("testsuite"))
    counts = {key: sum(int(s.get(key, "0")) for s in suites) for key in ("tests", "failures", "errors", "skipped")}
    if not counts["tests"] or counts["failures"] or counts["errors"]:
        raise ValueError("Submission requires a complete passing regression receipt")
    counts["passed"] = counts["tests"] - counts["skipped"]
    target.parent.mkdir(parents=True, exist_ok=True)
    tree.write(target, encoding="utf-8", xml_declaration=True)
    return counts


def guide(files):
    lines = ["# Python File Guide", "", "Every project Python file is included. Paths are relative to this submission.",
             "Application entry points are app.py and the CLI. Test/demonstration/report helpers are not additional runtime agents.",
             "", "| File | Purpose |", "|---|---|"]
    for p in files:
        relative = p.relative_to(ROOT).as_posix()
        if p.name == "__init__.py":
            purpose = "Package boundary (no standalone command)."
        elif relative == "app.py":
            purpose = "Streamlit launcher importing the packaged UI."
        elif relative.startswith("tests/"):
            purpose = "Regression tests: " + p.stem.removeprefix("test_").replace("_", " ") + "."
        else:
            purpose = PURPOSES.get(p.stem)
            if purpose is None:
                raise ValueError("Add a file-guide explanation for " + relative)
        lines.append(f"| [{relative}]({relative}) | {purpose} |")
    lines += ["", "## Supporting non-Python files", "",
              "- `pyproject.toml`: package metadata, dependencies, CLI entry point and pytest paths.",
              "- `requirements-lock.txt`: Windows dependency snapshot; packages themselves are not included.",
              "- `.env.example`: placeholder local/SEC configuration, with no personal credentials.",
              "- `config/research.json`: optional version/digest-pinned configuration, not required for quick start.",
              "- `evaluation/fixtures/demo.html`: artificial offline control-flow input.",
              "- `evaluation/fixtures/apple_2025_10k.html`: retained development filing for parser/calculator regression.",
              "- `evaluation/fixtures/converted_apple_2026_10k.html`: converted-HTML compatibility fixture.",
              "- `reports/README.md`: input requirements and limits of optional historical Python utilities.",
              "- `validation/`: current test receipts, package checks and sanitized real-model smoke output.",
              "- `SUBMISSION_MANIFEST.json`: release file hashes and complete Python inventory.", ""]
    return "\n".join(lines)


def live_receipt(stage):
    path = ROOT / "artifacts/submission-validation/live-smoke-full-state.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data["final_status"] != "SUCCESS" or not data.get("audit_complete") or not data.get("decoder_call_count"):
        raise ValueError("The real-model smoke run has not succeeded with a complete audit")
    receipt = {"date": "2026-11-16", "mode": "Real FinBERT/Qwen on retained Microsoft SEC HTML; no fresh SEC download",
               "status": data["final_status"], "filing_metadata": data["filing_metadata"],
               "source_hash": data["filing_hash"], "calculation": data["calculation_result"],
               "decoder_calls": data["decoder_call_count"], "corrections": data["correction_count"],
               "model_versions": data["model_versions"], "runtime_versions": data["runtime_versions"],
               "seconds": data["timings"]["total_seconds"],
               "privacy": "No personal .env, SEC contact, full config, raw call log or local source path is distributed."}
    write_json(stage / "validation/live-smoke.json", receipt)
    return receipt


def manifest(stage, label, source_files):
    files = sorted(p for p in stage.rglob("*") if p.is_file() and p.name != "SUBMISSION_MANIFEST.json")
    for p in files:
        rel = p.relative_to(stage)
        if set(rel.parts) & BLOCKED or (p.name.startswith(".env") and p.name != ".env.example"):
            raise ValueError("Forbidden release path: " + str(rel))
        if p.is_symlink():
            raise ValueError("Do not submit symlinks")
        if p.suffix == ".py":
            ast.parse(p.read_text(encoding="utf-8"), filename=str(rel))
        if p.suffix in {".py", ".md", ".json", ".txt", ".toml", ".xml"} or p.name == ".env.example":
            text = p.read_text(encoding="utf-8")
            if re.search(r"[\u3400-\u9fff]", text):
                raise ValueError("Review non-English source text in " + str(rel))
            patterns = [r"gh[pousr]_[A-Za-z0-9]{30,}", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
                        r"\bAKIA[A-Z0-9]{16}\b", r"C:[/\\]Users[/\\]\w+"]
            if any(re.search(pattern, text) for pattern in patterns):
                raise ValueError("Review possible credential or private local path in " + str(rel))
    expected = {p.relative_to(ROOT).as_posix() for p in source_files}
    actual = {p.relative_to(stage).as_posix() for p in files if p.suffix == ".py"}
    if actual != expected:
        raise ValueError("Python completeness mismatch: " + str(expected ^ actual))
    for p in source_files:
        if sha(p) != sha(stage / p.relative_to(ROOT)):
            raise ValueError("Source changed after staging: " + str(p.relative_to(ROOT)))
    info = {"release": label, "project": "SEC_Agent", "python_file_count": len(expected),
            "python_files": sorted(expected), "file_count_excluding_manifest": len(files),
            "files": [{"path": p.relative_to(stage).as_posix(), "bytes": p.stat().st_size, "sha256": sha(p)} for p in files],
            "excluded": ["environments", "models", "personal .env", "Git history", "historical artifacts", "old markdown reports", "disk scans"],
            "manifest_note": "The manifest does not hash itself. This is file integrity, not a digital signature."}
    write_json(stage / "SUBMISSION_MANIFEST.json", info)
    return files + [stage / "SUBMISSION_MANIFEST.json"], info


def zip_stage(stage, target, files):
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for p in files:
            archive.write(p, (Path("SEC_Agent") / p.relative_to(stage)).as_posix())
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP CRC verification failed")


def prepare(label):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", label):
        raise ValueError("Use a YYYY-MM-DD release label")
    base = ROOT / "artifacts/submission-validation" / ("package-" + uuid.uuid4().hex)
    stage = base / "staging/SEC_Agent"
    stage.mkdir(parents=True)
    sources = python_files()
    extras = [ROOT / name for name in ("README.md", "pyproject.toml", "requirements-lock.txt", ".env.example", ".gitignore",
              "config/research.json", "reports/README.md", "evaluation/fixtures/demo.html",
              "evaluation/fixtures/apple_2025_10k.html", "evaluation/fixtures/converted_apple_2026_10k.html")]
    for p in sources + extras:
        target = stage / p.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
    (stage / "FILE_GUIDE.md").write_text(guide(sources), encoding="utf-8")
    working = xml_receipt(ROOT / "artifacts/submission-validation/working-tree-tests.xml", stage / "validation/working-tree-tests.xml")
    live = live_receipt(stage)
    (stage / "validation/VALIDATION.md").write_text(
        "# Submission validation\n\nCandidate prepared; extracted-source verification is required before final release.\n",
        encoding="utf-8")
    files, inventory = manifest(stage, label, sources)
    candidate = base / "candidate.zip"
    zip_stage(stage, candidate, files)
    unpacked = base / "unpacked"
    with zipfile.ZipFile(candidate) as archive:
        for name in archive.namelist():
            if not name.startswith("SEC_Agent/") or ".." in Path(name).parts:
                raise ValueError("Unsafe archive member")
        archive.extractall(unpacked)
    state = {"label": label, "base": str(base), "stage": str(stage), "unpacked_root": str(unpacked / "SEC_Agent"),
             "candidate": str(candidate), "working_tests": working, "live_status": live["status"],
             "python_files": inventory["python_files"]}
    write_json(base / "state.json", state)
    print(json.dumps({"state": str(base / "state.json"), "unpacked_root": state["unpacked_root"],
                      "python_files": len(sources), "candidate_bytes": candidate.stat().st_size}, indent=2))


def finalize(state_path, output_name=None):
    state = json.loads(Path(state_path).read_text(encoding="utf-8"))
    base, stage = Path(state["base"]), Path(state["stage"])
    extracted = xml_receipt(base / "extracted-tests.xml", stage / "validation/extracted-tests.xml")
    smoke = json.loads((base / "extracted-smoke.json").read_text(encoding="utf-8"))
    if not smoke.get("all_checks_passed") or not smoke.get("imported_from_extracted_source"):
        raise ValueError("Extracted-source smoke verification failed")
    write_json(stage / "validation/extracted-smoke.json", smoke)
    text = f'''# Submission Validation — {state['label']}

- Working tree: {state['working_tests']['passed']} passed, {state['working_tests']['skipped']} skipped.
- Candidate ZIP extracted to a separate directory: {extracted['passed']} passed, {extracted['skipped']} skipped.
- No project `.env`, old artifacts, environments or original source folders were copied into that directory.
- Child processes imported application modules from the extracted `src` and used the included fixtures.
- CLI help/status and the offline scripted success/recovery/missing scenarios were checked.
- Real-model Microsoft revenue-growth smoke: SUCCESS with FinBERT and Qwen on retained source HTML.
- Python completeness, source SHA-256 identity, syntax, selected sensitive patterns, ZIP CRC and manifest checks passed.

The two default skips are opt-in live FinBERT parity/CUDA tests. The separate live smoke really ran the models.
Tests validate covered software behavior; they are not a held-out financial accuracy benchmark.
The extracted run reused the existing installed third-party dependencies through PYTHONPATH isolation;
it did not repeat dependency downloads or establish compatibility on a new operating system.
Model weights and installed dependencies remain external. Exact live-model output can vary with model/runtime identity.

JUnit receipts and sanitized live output are in this directory. No personal SEC contact or full local audit/config is included.
'''
    (stage / "validation/VALIDATION.md").write_text(text, encoding="utf-8")
    sources = python_files()
    files, inventory = manifest(stage, state["label"], sources)
    if output_name and not re.fullmatch(r"[A-Za-z0-9_.-]+\.zip", output_name):
        raise ValueError("Output name must be a plain ZIP filename")
    target = ROOT / "dist" / (output_name or f"SEC_Agent_Code_{state['label']}.zip")
    if target.exists():
        target = target.with_name(target.stem + "_" + uuid.uuid4().hex[:6] + ".zip")
    zip_stage(stage, target, files)
    with zipfile.ZipFile(target) as archive:
        for item in inventory["files"]:
            content = archive.read("SEC_Agent/" + item["path"])
            if hashlib.sha256(content).hexdigest() != item["sha256"]:
                raise ValueError("Final archive hash mismatch")
    receipt = {"zip": str(target), "bytes": target.stat().st_size, "sha256": sha(target),
               "python_files": inventory["python_file_count"], "files": len(files),
               "working_tests": state["working_tests"], "extracted_tests": extracted,
               "live_smoke": state["live_status"], "extracted_smoke": smoke}
    write_json(target.with_suffix(".verification.json"), receipt)
    target.with_suffix(".sha256").write_text(sha(target) + "  " + target.name + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--label", required=True)
    p = sub.add_parser("finalize")
    p.add_argument("--state", required=True)
    p.add_argument("--output-name", help="Optional plain ZIP filename")
    args = parser.parse_args()
    prepare(args.label) if args.action == "prepare" else finalize(args.state, args.output_name)


if __name__ == "__main__":
    main()
