# Setup: rebuild and run the presented code

The pair's code is a modified copy of [τ²-bench](https://github.com/sierra-research/tau2-bench)
(Sierra Research, MIT license). This folder does not repeat the benchmark. It keeps only
the pair's changes. You clone upstream at a fixed commit, add the new files and apply one patch.

## What this folder holds

| Path | Contents |
| --- | --- |
| `README.md` | The student's README (a marked case-study note added at the top; university ID replaced by GitHub username). |
| `tau2-bench/` | The 23 files the pair added, at the same relative paths as in τ²-bench. |
| `tau2-bench.patch` | The pair's changes to 13 existing τ²-bench files (858 lines added, 28 removed). |
| `LICENSE-tau2-bench.txt` | τ²-bench's MIT license. Keep it with these files. |
| [`docs/reports/pair-retail-order-agents-midterm.pdf`](../../../docs/reports/pair-retail-order-agents-midterm.pdf) | Midterm slides (5 Nov 2026), converted from the submitted `.pptx`. |

## Where the code comes from

- **Upstream base:** `sierra-research/tau2-bench` commit
  `5bfa7e37b36656b37dc6d022156be6563c1007f3` (28 Sep 2026; package version 1.0.1).
- **Pair's fork:** `bill255203/tau2-bench` commit
  `c583eff625a50ac72a5d7bd10eae5773b015245a` (3 Nov 2026; merge of the fork's PR #3,
  branch `experiment/pre-verifier-model`). The fork's branches have moved on since then, so
  pin this commit.
- **Submission:** `VIP_Midterm_Code_Yusuke_Katsuki.zip` (SHA-256
  `e6b35f743bd260830f97f38c3d5614a163c56978c22314b8962c86589b33be4d`). All 1,318 files in
  its unpacked `tau2-bench/` folder are identical to the fork commit (compared by git blob
  hash). The submission leaves out `data/simulations`, `data/tau2/results`, `data/voice`,
  `web/` and `figs/`.
- **Check (17 Nov 2026):** the upstream base plus `tau2-bench/` plus `tau2-bench.patch` gives
  exactly the fork commit's tree, apart from `data/simulations`.

## 1. Rebuild the code

```bash
CASE=/path/to/this/folder          # the folder that holds this SETUP.md
git clone https://github.com/sierra-research/tau2-bench.git
cd tau2-bench
git checkout 5bfa7e37b36656b37dc6d022156be6563c1007f3
cp -R "$CASE/tau2-bench/." .
git apply "$CASE/tau2-bench.patch"
git status --short                 # 13 modified files, plus the new files and folders
```

The upstream repository also stores about 600 MB of leaderboard runs. To skip them, replace
the `git clone` and `git checkout` lines above with:

```bash
git clone --filter=blob:none --no-checkout https://github.com/sierra-research/tau2-bench.git
cd tau2-bench
git sparse-checkout set --no-cone '/*' '!/data/tau2/results/' '!/data/voice/' '!/web/' '!/figs/'
git checkout 5bfa7e37b36656b37dc6d022156be6563c1007f3
```

Another way is to clone the pair's fork and run
`git checkout c583eff625a50ac72a5d7bd10eae5773b015245a`. This gives the same code plus
Pin-Ray's October run outputs (`data/simulations/`).

## 2. Install

Requires Python 3.12 or 3.13 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --extra dev
uv pip install websockets   # tests/conftest.py imports a voice module that needs it
```

## 3. Models and API keys

- **Unit tests** need no key, no GPU and no model. The verifier models are mocked.
- **Default runs** use a local Ollama model. The patch changes the agent and user
  defaults to `ollama_chat/qwen3.5:latest` at `http://127.0.0.1:11435`:

  ```bash
  OLLAMA_HOST=127.0.0.1:11435 ollama serve
  ollama pull qwen3.5:latest
  ```

- **Hosted models:** pass any LiteLLM model name to `--agent-llm`, `--user-llm`,
  `--verifier-model` or `--pre-verifier-model`. Put the provider key (for example
  `OPENAI_API_KEY` or `GEMINI_API_KEY`) in a local `.env` file, starting from upstream's
  `.env.example`. `.env` is git-ignored; never commit it.
- **Scoring judge:** some tasks are scored partly by natural-language assertions (retail tasks
  4 and 16, for example). τ²-bench checks these with OpenAI `gpt-4.1-2025-04-14`
  (`DEFAULT_LLM_NL_ASSERTIONS` in `src/tau2/config.py`). The patch leaves this default
  unchanged, and no command-line flag sets it. A fully scored run of such a task therefore
  needs `OPENAI_API_KEY`, unless you edit that constant.

## 4. Run

These commands come from the student's README. Each run is saved to
`data/simulations/<save-to>/results.json`. Verifier and pre-verifier records are stored
under each simulation's `info`.

```bash
# Retail task 4, once, with no checks (baseline)
uv run tau2 run --domain retail --task-ids 4 --num-trials 1 --max-concurrency 1 --seed 300 --save-to baseline

# Add the post-verifier (online verifier)
uv run tau2 run --domain retail --task-ids 4 --num-trials 1 --max-concurrency 1 --seed 300 \
  --verifier-model ollama_chat/qwen3.5:latest \
  --verifier-llm-args '{"temperature": 0, "api_base": "http://127.0.0.1:11435"}' \
  --save-to post

# Add the pre-verifier (v1 = rules only; v2 = rules + one model call)
uv run tau2 run --domain retail --task-ids 4 --num-trials 1 --max-concurrency 1 --seed 300 \
  --pre-verifier v2 --save-to pre-v2

uv run tau2 view   # browse saved runs
```

## 5. Tests

```bash
uv run pytest tests/test_pre_verifier.py tests/test_domains/test_retail_stock tests/test_llm_utils.py \
  --deselect tests/test_llm_utils.py::test_generate_no_tool_call \
  --deselect tests/test_llm_utils.py::test_generate_tool_call
```

Expected result: `110 passed, 2 deselected`. This was checked on 17 Nov 2026 with Python
3.12.15 and the locked dependencies, after rebuilding as in step 1. 90 of the 110 tests are
in `tests/test_pre_verifier.py`. The two deselected tests are original τ²-bench tests that
call a real OpenAI model; without `OPENAI_API_KEY` they fail.

## Who wrote what

Authors come from the fork's commit history between the upstream base and `c583eff`.

| File | Change | Author(s) |
| --- | --- | --- |
| `src/tau2/agent/pre_verifier.py`, `tests/test_pre_verifier.py` | added | Yusuke Katsuki |
| `src/tau2/runner/helpers.py` | patched | Yusuke Katsuki |
| `src/tau2/agent/llm_agent.py`, `src/tau2/cli.py`, `src/tau2/data_model/simulation.py`, `src/tau2/orchestrator/orchestrator.py`, `src/tau2/runner/build.py` | patched | Yusuke Katsuki (pre-verifier wiring) and Pin-Ray Liao (verifier wiring) |
| `src/tau2/verifier/base.py`, `src/tau2/verifier/llm_verifier.py`, `tests/test_domains/test_retail_stock/test_online_verifier.py` | added | Pin-Ray Liao. Yusuke Katsuki's commit `bfe21d5` keeps task data out of the verifier. |
| `src/tau2/verifier/__init__.py`, `src/tau2/verifier/models.py` | added | Pin-Ray Liao |
| `src/tau2/config.py`, `src/tau2/utils/llm_utils.py`, `tests/test_llm_utils.py` | patched | Pin-Ray Liao |
| `retail_stock` domain: `src/tau2/domains/retail_stock/*`, `data/tau2/domains/retail_stock/*`, `tests/test_domains/test_retail_stock/__init__.py`, `tests/test_domains/test_retail_stock/test_retail_stock.py` | added | Pin-Ray Liao |
| `src/tau2/registry.py`, `src/tau2/data_model/tasks.py`, `src/tau2/evaluator/evaluator_action.py`, `src/tau2/evaluator/evaluator_communicate.py` | patched | Pin-Ray Liao (`retail_stock` domain) |
| `ONLINE_VERIFIER_LOCAL_RUN_REPORT.md`, `RETAIL_HARD_TASKS_FAILURE_REPORT.md`, `RETAIL_HARD_TASKS_FAILURE_REPORT_ZH_TW.md`, `online-verifier-agent-feasibility-en.md`, `online-verifier-phase1-implementation-report.md` | added | Pin-Ray Liao (October reports) |

The `retail_stock` domain was an earlier experiment and is not part of the presentation.
`registry.py` registers it, so it stays in this folder for the code to import.

## Not included

- **Unchanged τ²-bench files.** Get them from upstream at the commit above.
- **`data/simulations/`:** Pin-Ray's October run outputs (659 files, about 11 MB). They are
  not in the submitted zip but are in the fork at `c583eff`. `RETAIL_HARD_TASKS_FAILURE_REPORT.md`
  cites them, including the three failures on the slides (tasks 20, 34 and 41, in
  `retail-hardest-10-qwen35-4trials-v2/`). `ONLINE_VERIFIER_LOCAL_RUN_REPORT.md` cites a
  folder, `retail-stock-local-verifier-revalidation-v6/`, that is not in the fork.
- **`data/tau2/results`, `data/voice`, `web/`, `figs/`:** upstream material that is also not in the zip.
- **The submitted zip and `.pptx`.** The slides are included as a PDF.
- **Pre-verifier run outputs.** The submission has none. The student's 16 Nov smoke run (retail
  task 4 with both checks, local Qwen 3.5 9B, `--max-steps 8`) was not saved in the zip.

## Reading the October reports

The October reports describe the verifier as it was before commit `bfe21d5`. Until that
commit, the verifier also received the task object: its expected actions and answers, and
the simulated customer's hidden instructions. The 1.0 reward reported in
`ONLINE_VERIFIER_LOCAL_RUN_REPORT.md` comes from that earlier version. The presented code
sends the verifier only the policy, the committed history and the proposed action.

## License

τ²-bench is distributed under the MIT License, Copyright (c) 2025 Sierra Research. The
patch and added files change and extend τ²-bench, and the patch contains lines of its
source. Keep `LICENSE-tau2-bench.txt` with these files.
