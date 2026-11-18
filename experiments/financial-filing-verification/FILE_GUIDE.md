# Python File Guide

Every project Python file is included. Paths are relative to this submission.
Application entry points are app.py and the CLI. Test/demonstration/report helpers are not additional runtime agents.

| File | Purpose |
|---|---|
| [app.py](app.py) | Streamlit launcher importing the packaged UI. |
| [evaluation/__init__.py](evaluation/__init__.py) | Package boundary (no standalone command). |
| [evaluation/doubles.py](evaluation/doubles.py) | Explicit scripted decoder/retriever doubles for offline workflow demonstrations. |
| [evaluation/fixtures.py](evaluation/fixtures.py) | Development filing paths and post-execution numeric references; no runtime gold input. |
| [evaluation/live_demo.py](evaluation/live_demo.py) | Optional live-model scenarios, including deliberately controlled ranking stress. |
| [evaluation/metrics.py](evaluation/metrics.py) | Post-run outcome/value/component comparisons against evaluation references. |
| [evaluation/review_double.py](evaluation/review_double.py) | Source-shaped verification observations used by test doubles. |
| [evaluation/runner.py](evaluation/runner.py) | Self-contained offline success, recovery and missing-evidence demonstrations. |
| [reports/build_project_encyclopedia.py](reports/build_project_encyclopedia.py) | Optional generator requiring the research encyclopedia manuscript. |
| [reports/midterm/build_evidence_index.py](reports/midterm/build_evidence_index.py) | Optional historical-audit index requiring manuscripts, audits and an old XML receipt. |
| [reports/run_nine_cell_experiment.py](reports/run_nine_cell_experiment.py) | Optional historical three-ticker live experiment using SEC/Ollama. |
| [scripts/freeze_development.py](scripts/freeze_development.py) | Optional notebook snapshot utility; requires an external notebook argument. |
| [scripts/prepare_submission.py](scripts/prepare_submission.py) | Allowlisted ZIP builder, Python-completeness/hash checks and validation receipts. |
| [src/financial_filing_agent/__init__.py](src/financial_filing_agent/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/agents/__init__.py](src/financial_filing_agent/agents/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/agents/corrector.py](src/financial_filing_agent/agents/corrector.py) | Allowed replacement/expansion decisions and candidate-ID enforcement. |
| [src/financial_filing_agent/agents/planner.py](src/financial_filing_agent/agents/planner.py) | Free-question mapping to registered tasks and explicit-period checks. |
| [src/financial_filing_agent/agents/verification_contract.py](src/financial_filing_agent/agents/verification_contract.py) | Per-request open checks, dynamic schemas and source-quote validation. |
| [src/financial_filing_agent/agents/verifier.py](src/financial_filing_agent/agents/verifier.py) | One-row decoder review and bounded contract repair. |
| [src/financial_filing_agent/cli.py](src/financial_filing_agent/cli.py) | Single-run/batch CLI arguments, execution and exit status. |
| [src/financial_filing_agent/config/__init__.py](src/financial_filing_agent/config/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/config/financial_concepts.py](src/financial_filing_agent/config/financial_concepts.py) | Canonical concepts, reported-label aliases and supported XBRL tags. |
| [src/financial_filing_agent/config/formulas.py](src/financial_filing_agent/config/formulas.py) | Ten registered metrics, dependencies, units and deterministic menu planning. |
| [src/financial_filing_agent/config/prompts.py](src/financial_filing_agent/config/prompts.py) | Actual planner/verifier/corrector system instructions. |
| [src/financial_filing_agent/config/settings.py](src/financial_filing_agent/config/settings.py) | Validated settings, environment loading and configuration fingerprint. |
| [src/financial_filing_agent/graph/__init__.py](src/financial_filing_agent/graph/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/graph/routing.py](src/financial_filing_agent/graph/routing.py) | Terminal-status versus next-node route selection. |
| [src/financial_filing_agent/graph/workflow.py](src/financial_filing_agent/graph/workflow.py) | Fourteen-node LangGraph construction and allowed edges. |
| [src/financial_filing_agent/models/__init__.py](src/financial_filing_agent/models/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/models/finbert.py](src/financial_filing_agent/models/finbert.py) | Batched masked-mean/L2 encoder, device choice and process cache. |
| [src/financial_filing_agent/models/local_decoder.py](src/financial_filing_agent/models/local_decoder.py) | Ollama HTTP/JSON adapter, model diagnostics and bounded retries. |
| [src/financial_filing_agent/retrieval/__init__.py](src/financial_filing_agent/retrieval/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/retrieval/finbert_retriever.py](src/financial_filing_agent/retrieval/finbert_retriever.py) | Content/version-keyed row embedding cache. |
| [src/financial_filing_agent/retrieval/hybrid_retriever.py](src/financial_filing_agent/retrieval/hybrid_retriever.py) | FinBERT/lexical/XBRL score fusion and retrieval diagnostics. |
| [src/financial_filing_agent/retrieval/lexical_retriever.py](src/financial_filing_agent/retrieval/lexical_retriever.py) | Alias, token overlap and XBRL-name support signals. |
| [src/financial_filing_agent/retrieval/sufficiency.py](src/financial_filing_agent/retrieval/sufficiency.py) | Structural evidence sufficiency decisions. |
| [src/financial_filing_agent/schemas/__init__.py](src/financial_filing_agent/schemas/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/schemas/evidence.py](src/financial_filing_agent/schemas/evidence.py) | Typed filing, evidence-row and numeric-fact provenance models. |
| [src/financial_filing_agent/schemas/results.py](src/financial_filing_agent/schemas/results.py) | Verification, correction and calculation schemas; Python verdict aggregation. |
| [src/financial_filing_agent/schemas/state.py](src/financial_filing_agent/schemas/state.py) | Serializable graph-state field declarations. |
| [src/financial_filing_agent/schemas/task.py](src/financial_filing_agent/schemas/task.py) | Task-plan schema and registry/period/dependency validation. |
| [src/financial_filing_agent/services/__init__.py](src/financial_filing_agent/services/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/services/audit.py](src/financial_filing_agent/services/audit.py) | Per-run state/model-call receipts and recovery snapshots. |
| [src/financial_filing_agent/services/batch.py](src/financial_filing_agent/services/batch.py) | Sequential ticker-by-metric runs with source pinning and JSON/CSV output. |
| [src/financial_filing_agent/services/cache.py](src/financial_filing_agent/services/cache.py) | SHA-256 and UTF-8 atomic JSON persistence with finite Windows retries. |
| [src/financial_filing_agent/services/pipeline.py](src/financial_filing_agent/services/pipeline.py) | Full orchestration, component iteration, review/guards, finalization and audit. |
| [src/financial_filing_agent/services/progress.py](src/financial_filing_agent/services/progress.py) | Node labels and observational progress summaries. |
| [src/financial_filing_agent/tools/__init__.py](src/financial_filing_agent/tools/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/tools/calculator.py](src/financial_filing_agent/tools/calculator.py) | Registered Python metric arithmetic and period comparisons. |
| [src/financial_filing_agent/tools/concept_validation.py](src/financial_filing_agent/tools/concept_validation.py) | Unit-aware concept assessment and optional Decimal gross-profit identity. |
| [src/financial_filing_agent/tools/evidence_builder.py](src/financial_filing_agent/tools/evidence_builder.py) | Compact retrieval text preserving distinct numeric cells. |
| [src/financial_filing_agent/tools/filing_loader.py](src/financial_filing_agent/tools/filing_loader.py) | Local/SEC HTML loading, content cache, hashes and DEI metadata. |
| [src/financial_filing_agent/tools/filing_parser.py](src/financial_filing_agent/tools/filing_parser.py) | Logical tables, statement classification, fiscal columns and evidence construction. |
| [src/financial_filing_agent/tools/html.py](src/financial_filing_agent/tools/html.py) | BeautifulSoup/lxml parsing adapter. |
| [src/financial_filing_agent/tools/input_inventory.py](src/financial_filing_agent/tools/input_inventory.py) | Required component-by-year coverage matrix. |
| [src/financial_filing_agent/tools/numeric_parser.py](src/financial_filing_agent/tools/numeric_parser.py) | Conservative financial-cell parsing, complete parentheses and label normalization. |
| [src/financial_filing_agent/tools/sec_client.py](src/financial_filing_agent/tools/sec_client.py) | Identified, restricted-host SEC acquisition, ticker resolution and batch JSON cache. |
| [src/financial_filing_agent/tools/statement_origin.py](src/financial_filing_agent/tools/statement_origin.py) | Internal TOC/heading/table binding and entity-specific consolidation evidence. |
| [src/financial_filing_agent/tools/supporting_filing.py](src/financial_filing_agent/tools/supporting_filing.py) | Opt-in complete same-company supporting-source selection. |
| [src/financial_filing_agent/tools/validation.py](src/financial_filing_agent/tools/validation.py) | Early dimension eligibility, row guards and cross-input compatibility. |
| [src/financial_filing_agent/tools/xbrl.py](src/financial_filing_agent/tools/xbrl.py) | Inline XBRL contexts, units, dimensions, sign/scale and supported transformations. |
| [src/financial_filing_agent/ui/__init__.py](src/financial_filing_agent/ui/__init__.py) | Package boundary (no standalone command). |
| [src/financial_filing_agent/ui/batch_components.py](src/financial_filing_agent/ui/batch_components.py) | Multiple-ticker/metric UI, progress and export downloads. |
| [src/financial_filing_agent/ui/components.py](src/financial_filing_agent/ui/components.py) | Result/evidence/diagnostic panels and audit-state download. |
| [src/financial_filing_agent/ui/streamlit_app.py](src/financial_filing_agent/ui/streamlit_app.py) | Main Streamlit form, mode settings, uploads and live execution progress. |
| [tests/__init__.py](tests/__init__.py) | Package boundary (no standalone command). |
| [tests/test_application.py](tests/test_application.py) | Regression tests: application. |
| [tests/test_batch_preflight.py](tests/test_batch_preflight.py) | Regression tests: batch preflight. |
| [tests/test_converted_filing.py](tests/test_converted_filing.py) | Regression tests: converted filing. |
| [tests/test_finbert.py](tests/test_finbert.py) | Regression tests: finbert. |
| [tests/test_metric_workflow.py](tests/test_metric_workflow.py) | Regression tests: metric workflow. |
| [tests/test_qwen_modes.py](tests/test_qwen_modes.py) | Regression tests: qwen modes. |
| [tests/test_runtime_reliability.py](tests/test_runtime_reliability.py) | Regression tests: runtime reliability. |
| [tests/test_sources.py](tests/test_sources.py) | Regression tests: sources. |
| [tests/test_split_parentheses.py](tests/test_split_parentheses.py) | Regression tests: split parentheses. |
| [tests/test_statement_origin.py](tests/test_statement_origin.py) | Regression tests: statement origin. |
| [tests/test_ui.py](tests/test_ui.py) | Regression tests: ui. |
| [tests/test_verifier_contract.py](tests/test_verifier_contract.py) | Regression tests: verifier contract. |

## Supporting non-Python files

- `pyproject.toml`: package metadata, dependencies, CLI entry point and pytest paths.
- `requirements-lock.txt`: Windows dependency snapshot; packages themselves are not included.
- `.env.example`: placeholder local/SEC configuration, with no personal credentials.
- `config/research.json`: optional version/digest-pinned configuration, not required for quick start.
- `evaluation/fixtures/demo.html`: artificial offline control-flow input.
- `evaluation/fixtures/apple_2025_10k.html`: retained development filing for parser/calculator regression.
- `evaluation/fixtures/converted_apple_2026_10k.html`: converted-HTML compatibility fixture.
- `reports/README.md`: input requirements and limits of optional historical Python utilities.
- `validation/`: current test receipts, package checks and sanitized real-model smoke output.
- `SUBMISSION_MANIFEST.json`: release file hashes and complete Python inventory.
