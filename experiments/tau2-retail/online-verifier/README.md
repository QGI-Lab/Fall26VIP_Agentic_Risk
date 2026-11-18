# VIP Midterm Code — Online Verification in Retail Order Handling

> **Case-study copy.** This note was added when the submission was prepared for this
> repository; it is not part of the student's README. This folder does not contain the full
> `tau2-bench/` tree described below. It holds only the files the pair added
> (`tau2-bench/`, same relative paths) and one patch for the 13 upstream files they changed
> (`tau2-bench.patch`). [SETUP.md](SETUP.md) rebuilds the presented code from upstream
> τ²-bench. The only other change is that the student's university ID in the next line was
> replaced by his GitHub username.

Yusuke Katsuki (@katsukii), with Pin-Ray Liao. VIP: Agentic AI in Risk Management, Fall 2026.

This zip holds the code behind our midterm presentation (Nov 5). We extended τ²-bench, a simulator in which an LLM service agent helps a simulated customer through store tools, with two checks around the service agent:

- **Pre-verifier** (my part): before each agent LLM call, it narrows the tool list the model sees. Rule `v1` is deterministic; rule `v2` adds one model call.
- **Post-verifier / online verifier** (Pin-Ray's part): after the agent proposes a reply or a tool call, an LLM checks it against the policy and the conversation and returns PASS, REVISE or BLOCK before anything is committed.

## What is in this zip

- `README.md` — this file.
- `tau2-bench/` — the full code as presented, with all Python files (349). It runs as is (see "How to use").
  - Source: <https://github.com/bill255203/tau2-bench>, commit `c583eff` (Nov 3, 2026; branch `experiment/online-verifier` at that time).
  - Based on [sierra-research/tau2-bench](https://github.com/sierra-research/tau2-bench) commit `5bfa7e3` (Sep 28, 2026).
  - Removed to keep the zip small (not code; all of it is in the GitHub repository): `data/tau2/results` (Sierra's leaderboard runs, about 600 MB), `data/voice` (audio files), `data/simulations` (our October run outputs), `web/` (leaderboard website) and `figs/`.

Most files are the original τ²-bench. The files we added or changed are listed below. Paths are inside `tau2-bench/`.

### Pre-verifier (Yusuke)

| File | What it does |
|---|---|
| `src/tau2/agent/pre_verifier.py` | New. Rule `v1`: before the customer's identity is confirmed, offer only the two identity lookup tools and the transfer to a human agent; after that, offer order write tools (cancel, modify, return, exchange) only when an order seen in a tool result is in a status that accepts them. Rule `v2`: runs `v1`, then, when two or more order write tools remain, one model call (`select_order_tools`) keeps the ones that fit the customer's current request. It only changes the copy of the request sent to the model; hidden tools still exist in the environment. Each turn is logged as a `PreVerifierRecord`. |
| `src/tau2/agent/llm_agent.py` | Calls the pre-verifier right before each model call (shared file; Pin-Ray added the verifier-guided revision here). |
| `src/tau2/runner/helpers.py`, `src/tau2/runner/build.py` | Pass the pre-verifier settings from the run config to the agent (`build.py` is shared). |
| `src/tau2/data_model/simulation.py` | Run-config fields `pre_verifier`, `pre_verifier_model`, `pre_verifier_llm_args` (shared file; Pin-Ray added the verifier fields). |
| `src/tau2/orchestrator/orchestrator.py` | Saves pre-verifier records next to the verifier records in the simulation result (shared file). |
| `src/tau2/cli.py` | Flags `--pre-verifier {v1,v2}`, `--pre-verifier-model`, `--pre-verifier-llm-args` (shared file). |
| `tests/test_pre_verifier.py` | Unit tests for `v1` and `v2`. The model is mocked, so no API key or GPU is needed. |

I also changed the online verifier so it never receives the task's answer data (commit `bfe21d5`, in `src/tau2/verifier/base.py`, `src/tau2/verifier/llm_verifier.py` and its test).

### Post-verifier / online verifier (Pin-Ray)

| File | What it does |
|---|---|
| `src/tau2/verifier/base.py` | `Verifier` interface. |
| `src/tau2/verifier/models.py` | `VerifierDecision` (PASS / REVISE / BLOCK), `VerifierVerdict`, `VerifierRecord`. |
| `src/tau2/verifier/llm_verifier.py` | `LLMVerifier`: sends the domain policy, the committed history and the proposed action to an LLM and reads back a JSON verdict. |
| `src/tau2/verifier/__init__.py` | Exports the classes above. |
| `src/tau2/orchestrator/orchestrator.py` | The agent proposes on a copied state, the verifier checks it, and only then the reply goes to the customer or the tool call to the environment. REVISE sends one private instruction back to the agent (`--verifier-max-revisions`, default 1). |
| `src/tau2/runner/build.py` | `build_text_orchestrator()` creates the `LLMVerifier` when `--verifier-model` is set. |
| `src/tau2/cli.py` | Flags `--verifier-model`, `--verifier-llm-args`, `--verifier-max-revisions`. |
| `src/tau2/config.py` | Defaults: local Ollama `qwen3.5:latest` at `http://127.0.0.1:11435`, temperature 0. |
| `src/tau2/utils/llm_utils.py` | Records the cost of each call, and sets Ollama's context size so long policies and tool lists are not cut off. |
| `tests/test_domains/test_retail_stock/test_online_verifier.py` | Tests for the online verifier. |
| `tests/test_llm_utils.py` | Tests for the `llm_utils` changes. |

Pin-Ray's October reports are in the repository root: `ONLINE_VERIFIER_LOCAL_RUN_REPORT.md`, `online-verifier-agent-feasibility-en.md`, `online-verifier-phase1-implementation-report.md`, `RETAIL_HARD_TASKS_FAILURE_REPORT.md` (and `_ZH_TW`).

### `retail_stock` domain (Pin-Ray, earlier experiment)

A small retail domain for stock questions, used before the verifier work. It is not part of the presentation, but it is in the same code.

| File | What it does |
|---|---|
| `src/tau2/domains/retail_stock/*.py` | Data model, tools and environment for the domain. |
| `data/tau2/domains/retail_stock/*` | Database, policy and tasks for the domain. |
| `src/tau2/registry.py` | Registers the domain. |
| `src/tau2/data_model/tasks.py` | `StockAnswerAssertion` for numeric answers. |
| `src/tau2/evaluator/evaluator_action.py`, `src/tau2/evaluator/evaluator_communicate.py` | Scoring for stock answers and forbidden claims. |
| `tests/test_domains/test_retail_stock/test_retail_stock.py` | Tests for the domain. |

## How to use

### Install

Requires Python 3.12 or 3.13 and [uv](https://docs.astral.sh/uv/).

```bash
cd tau2-bench
uv sync --extra dev
```

### Model

By default, both the service agent and the simulated customer use a local Ollama model (`ollama_chat/qwen3.5:latest`, Qwen 3.5 9B) at `http://127.0.0.1:11435`:

```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
ollama pull qwen3.5:latest
```

Any LiteLLM model also works through `--agent-llm`, `--user-llm` and `--verifier-model`, with the provider's API key set in `.env`.

### Run

Retail task 4, once, with no checks (baseline):

```bash
uv run tau2 run --domain retail --task-ids 4 --num-trials 1 --max-concurrency 1 --seed 300 --save-to baseline
```

Add the post-verifier:

```bash
uv run tau2 run --domain retail --task-ids 4 --num-trials 1 --max-concurrency 1 --seed 300 \
  --verifier-model ollama_chat/qwen3.5:latest \
  --verifier-llm-args '{"temperature": 0, "api_base": "http://127.0.0.1:11435"}' \
  --save-to post
```

Add the pre-verifier (`v1`, or `v2` with one extra model call; `v2` uses the agent's model unless `--pre-verifier-model` is given):

```bash
uv run tau2 run --domain retail --task-ids 4 --num-trials 1 --max-concurrency 1 --seed 300 \
  --pre-verifier v2 --save-to pre-v2
```

Each run is saved to `data/simulations/<save-to>/results.json`. The verifier and pre-verifier records are under each simulation's `info`. To browse a run:

```bash
uv run tau2 view
```

### Tests

```bash
uv pip install websockets   # tests/conftest.py imports a voice module that needs it
uv run pytest tests/test_pre_verifier.py tests/test_domains/test_retail_stock tests/test_llm_utils.py
```

Re-run on Nov 16, 2026, from this zip: 110 passed. Two tests in `tests/test_llm_utils.py` fail without an OpenAI API key (`test_generate_no_tool_call`, `test_generate_tool_call`). They are original τ²-bench tests that call a real model.

Also checked on Nov 16, from this zip: retail task 4 with `--verifier-model` and `--pre-verifier v2` on a local Qwen 3.5 9B (`--max-steps 8`) ran to the step limit and saved verifier verdicts and pre-verifier records.

## Status at the midterm

Both checks were implemented and unit-tested. No measured comparison was shown at the midterm; a controlled comparison was listed as a next step (slide 11).
