# Optional research utilities

These Python files are retained because the submission includes all project
Python source. They are **not required to install, run or test the application**.
The current operational instructions are the root README and FILE_GUIDE.

| File | Purpose and extra input |
|---|---|
| `build_project_encyclopedia.py` | Regenerates appendices in an existing `reports/PROJECT_ENCYCLOPEDIA.md` research manuscript. Requires that manuscript. |
| `midterm/build_evidence_index.py` | Indexes historical `artifacts/runs` audits and checks saved calculations. Requires historical audits, the original midterm manuscript, and its XML test receipt. |
| `run_nine_cell_experiment.py` | Reproduces a historical live three-ticker experiment using SEC and Ollama. Requires external services and may take several minutes. Its historical narrative is not a new benchmark protocol. |

Long manuscripts, machine-specific inventories and historical raw artifacts are
deliberately omitted from the lightweight code submission. Those inputs remain in
the author's research workspace; the application and regression fixtures do not
depend on them. Use `evaluation.runner` for the self-contained offline demo and
the CLI/UI for real analysis.
