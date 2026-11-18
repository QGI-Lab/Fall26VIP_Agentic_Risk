# Submission Validation — 2026-11-16

- Working tree: 131 passed, 2 skipped.
- Candidate ZIP extracted to a separate directory: 131 passed, 2 skipped.
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
