# Agentic Financial Filing Analysis

Course code submission — November 16, 2026.

This project answers supported financial-metric questions from SEC 10-K HTML.
FinBERT retrieves candidate rows; three Qwen roles plan, verify and recover
financial evidence; a fourteen-node LangGraph workflow controls execution.
Registered Python functions perform **all authoritative arithmetic and comparisons**.
The focus is **Agentic AI Risk Management**: constrain model authority, check
source evidence, recover within budgets, and abstain when inputs are unsupported.

## 1. Install

Use **Python 3.11** (tested: 3.11.13). Run commands from this folder after unzipping.
Examples below use Windows PowerShell; on macOS/Linux replace
`.venv/Scripts/python.exe` with `.venv/bin/python`, create the environment with
`python3 -m venv .venv`, and use `cp .env.example .env` instead of `Copy-Item`.

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

Dependencies and model weights are installed separately; they are intentionally
absent from the ZIP. `requirements-lock.txt` preserves the Windows dependency
snapshot. To use that snapshot instead of resolving the package ranges:

```powershell
.venv/Scripts/python.exe -m pip install -r requirements-lock.txt
.venv/Scripts/python.exe -m pip install -e .
```

For a different platform, prefer the first installation method. CPU operation is
supported; CUDA is optional. Do not copy an existing virtual environment between computers.

## 2. Quick verification without downloading models

After installing the dependencies, run:

```powershell
.venv/Scripts/python.exe -m evaluation.runner
.venv/Scripts/python.exe -m pytest tests -q
```

The first command uses explicitly labeled **scripted test doubles**, not live AI.
Expected demonstration outcomes: success, recovered success, and insufficient
evidence. The regression suite runs without SEC access, Ollama, or model weights;
the two live-model checks skip unless explicitly enabled. See `validation/` in the
submission ZIP for the actual preparation-time test receipts.

## 3. Run the real application

Install Ollama separately, start its local service, and download Qwen:

```powershell
ollama pull qwen2.5:latest
.venv/Scripts/python.exe -m financial_filing_agent.cli --status
.venv/Scripts/python.exe -m streamlit run app.py
```

FinBERT (`yiyanghkust/finbert-pretrain`, pinned revision in settings) downloads on
first real retrieval if not already cached. Internet access is needed for that
initial download. The default Ollama endpoint is `http://localhost:11434`.

In the UI, upload HTML or enter a ticker, select a registered metric, enter fiscal
years when required, and run. The batch panel supports multiple tickers/metrics.
**Qwen OFF** removes decoder roles but still uses FinBERT retrieval and all guards.
For live SEC acquisition, edit `.env` and replace the example contact in
`FFA_SEC_USER_AGENT` with your own identifying contact email. Local HTML does not
require an SEC contact. Never submit your personal `.env`.

CLI examples:

```powershell
# Real retrieval/review on an included development filing
.venv/Scripts/python.exe -m financial_filing_agent.cli --source evaluation/fixtures/apple_2025_10k.html --formula current_ratio_change --periods FY2025 FY2024

# Registered calculation without Qwen; FinBERT is still used
.venv/Scripts/python.exe -m financial_filing_agent.cli --source evaluation/fixtures/apple_2025_10k.html --formula revenue_growth --periods FY2025 FY2024 --no-qwen

# Latest SEC 10-K for each ticker; requires SEC contact and local Qwen
.venv/Scripts/python.exe -m financial_filing_agent.cli --tickers MSFT AMZN NVDA --metrics revenue_growth operating_margin current_ratio
```

Batch years come from each filing's explicit fiscal year unless `--periods` is
provided. Companies can have different year ends; outputs show the years, dates,
accession and source hash. No analyst agent or AI-generated company comparison is implemented.

## 4. Project structure and file responsibilities

[FILE_GUIDE.md](FILE_GUIDE.md) lists **every included Python file** and its purpose.

| Path | Responsibility |
|---|---|
| `app.py` | Streamlit entry point |
| `src/financial_filing_agent/cli.py` | Single-filing and batch command-line interface |
| `config/` inside the package | Settings, formula registry, concept aliases/tags, actual model prompts |
| `schemas/` | Filing/fact/evidence/task/result models and shared workflow state |
| `models/` | FinBERT encoder and Ollama decoder adapter |
| `agents/` | Planner, verifier, corrector, and executable review contract |
| `retrieval/` | Embedding cache, lexical/XBRL signals, hybrid ranking, sufficiency |
| `tools/` | SEC loading, HTML/XBRL parsing, source provenance, inventory, guards and calculator |
| `graph/` | Fourteen allowed nodes and conditional routing |
| `services/` | Pipeline, batch coordination, audit/cache persistence and progress |
| `ui/` | Single-run form, batch form, result/evidence inspection |
| `evaluation/` | Fixtures, offline doubles, demonstration runners and evaluation metrics |
| `tests/` | Regression checks including parsing, scope, contracts, arithmetic and UI |
| `config/research.json` | Optional strict research configuration; freezes a specific Qwen digest |
| `scripts/` | Historical notebook snapshot helper and submission packager |
| `reports/*.py`, `reports/midterm/*.py` | Optional historical research/document generators; see [reports/README.md](reports/README.md) |

Workflow:

```text
Request → source → registered plan → parse → component/year inventory
  → retrieve → assess → verify → guard → next component
  → Python calculation/comparison → result and audit
```

Bounded expansion/correction returns to review. A replacement is reverified.
Planner/verifier/corrector share one Qwen model with separate roles, rather than
independent models. They cannot invent accepted source values or executable formulas.
Dimensions are filtered before model review; final guards still check periods,
units, source membership, reporting scope and denominators. Primary-statement
provenance prevents a note summary from winning solely through similarity.

Supported task IDs: `revenue_growth`, `operating_margin`,
`operating_margin_change`, `current_ratio`, `current_ratio_change`,
`gross_margin`, `gross_margin_change`, `rd_intensity`, `inventory_growth`,
`accounts_receivable_growth`.

## 5. Outputs, scope and submission contents

The application creates `artifacts/` as needed: per-run audits/evidence, downloaded
filings, embeddings, and `batches/<id>/batch.json` plus `results.csv`.
Terminal statuses distinguish SUCCESS, INSUFFICIENT_EVIDENCE, NEEDS_INPUT,
UNSUPPORTED_TASK and operational ERROR. A model PASS alone cannot release a number.

This is a research prototype for supported HTML/Inline XBRL structures and ten
registered formulas. It does not implement arbitrary financial reasoning, PDF/OCR,
forecasting, or investment recommendations. Unknown formats and missing facts can
abstain. The calculator uses floats; optional accounting identity checks use Decimal.
The example filings are development/regression fixtures, not held-out benchmarks.

The ZIP includes all project Python source, necessary fixtures, installation
metadata, configuration examples, and preparation-time validation receipts.
It excludes `.env`, environments, installed packages, model weights, Git history,
old repair reports, long research drafts, disk scans and historical raw run caches.
Historical Python utilities are retained for source completeness; some require
external notebooks/audits/drafts and are not part of the app/test quick start.

`SUBMISSION_MANIFEST.json` records file hashes and the complete Python inventory.
`validation/VALIDATION.md` states what was tested and the limits of those checks.
Your presentation is submitted separately; it is not included in this code ZIP.
