# Pair case — Verification failures in retail order agents

- Pair case issue: [#58](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/58)
- Partners / GitHub usernames: Pin-Ray Liao (@bill255203), Yusuke Katsuki (@katsukii)
- Peer feedback / reviewer: maintainer review on this PR (2026-10-13); peer reviewer to be arranged
- Status: pre- and post-verifier built and unit-tested (midterm, 2026-11-05); comparison not started
- Dated plan revision and available feedback: 2026-10-07 initial outline for M2; 2026-10-13 maintainer feedback; 2026-10-14 sections 4–5 updated with the repeated pilot and the task 4 trace review; 2026-11-17 midterm code and slides added (maintainer note at the end)
- Individual task links: @katsukii [#62](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62); @bill255203 [#64](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/64)

## 1. Business workflow

We study a retail customer-service agent that receives customer requests, checks order information and policies, and uses tools to perform permitted actions such as cancellations, returns, and exchanges. The agent must determine which actions are required and whether their results justify reporting completion.

We plan to explore two small proofs of concept: a synthetic inventory scenario and multi-request retail tasks from τ-bench.

Sources: the retail domain [policy](https://github.com/sierra-research/tau2-bench/blob/main/data/tau2/domains/retail/policy.md) and tools of [τ²-bench](https://github.com/sierra-research/tau2-bench). The setting is simulated: the store, customers and orders are synthetic, and customers are played by an LLM. Real store data and payments are outside the study.

## 2. Risk question

Can a final completeness check reduce missed requests or premature completion claims in retail order workflows?

These failures could leave customers believing an order change was completed when it was not, potentially causing additional support requests, delayed refunds, and lost trust.

Our proposed check asks the agent to compare each customer requirement with available tool results before reporting completion. This week, we will first inspect a small baseline to determine whether these failures occur. If feasible, we will try the check on a small sample and record task outcomes and additional tool calls. We do not yet claim that the check improves performance.

## 3. Prior work

Our starting references are [τ-bench](https://arxiv.org/abs/2406.12045) (Yao et al., 2024; code: [τ²-bench](https://github.com/sierra-research/tau2-bench)), [MAST](https://arxiv.org/abs/2503.13657) ([code](https://github.com/multi-agent-systems-failure-taxonomy/MAST)), and [Who&When](https://arxiv.org/abs/2505.00212) ([code](https://github.com/ag2ai/Agents_Failure_Attribution)). We will review τ-bench for reusable retail tasks and outcome evaluation, MAST for failure classification, and Who&When for failure attribution.

These provide starting points for evaluating outcomes and interpreting traces, but do not by themselves establish whether our proposed completeness check helps in the selected tasks. This week, we will confirm relevant methods and limitations and use the baseline traces to narrow the study.

## 4. Evidence and comparison

We use τ²-bench's retail domain (commit `5bfa7e37b366`): its tasks, tools, policy, simulated customer and state-based scoring. Each task's reference actions and goal database state serve as ground truth.

- **Development vs. evaluation.** Failure-seeking runs (repeating known failures, harder settings, cheaper models) are development work and are not reported as representative failure rates. Before any comparison, we will state the evaluation task subset, selection rule, models and trials, and keep them fixed across conditions.
- **Comparison.** The same agent without and with the completeness check: the agent re-checks each request against tool results before reporting completion; a separate verifier agent is a candidate design. Tasks, models, simulated customer, tools, policy, step limits and evaluator stay fixed.
- **Measures (per task, with denominators).** Task success under τ²-bench scoring; omitted requests; completion claims while a request is open; tool calls, tokens and cost. Infrastructure failures are recorded separately.
- **Labels.** Exact matching of expected tool calls only flags candidate failures, because equivalent calls can reach the correct state. Each omission is confirmed against the task's required final state and the trace, and we record whether the simulated customer actually conveyed the request.
- **Failure analysis without new runs.** τ²-bench publishes full runs of four models (`data/tau2/results/final`). After checking task-version compatibility, we will label their candidate failures before choosing evaluation tasks.

## 5. Feasibility and individual roles

- **POC 1 (exploratory, 2026-10-03).** A synthetic stock re-check in Colab with Gemini ran end to end, but its outcome mostly depended on what our setup showed the agent, so it says little about the agent's own decisions ([#62](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62)). We focus on τ²-bench, whose retail tasks, data, tools and scoring are public (MIT license).
- **Development run 1 (2026-10-07).** [Notebook](../../experiments/tau2-retail/tau2_retail_baseline.ipynb): tasks with two or more expected state-changing tool calls; first five by ID (4, 11, 14, 16, 22); one trial each. All five were solved, assembled from four attempts whose other outcomes were infrastructure errors ([details](../../experiments/tau2-retail/README.md)).
- **Development run 2 (2026-10-07, repeated pilot).** [Notebook](../../experiments/tau2-retail/tau2_retail_pilot.ipynb): tasks whose reference solution changes two or more items (59 of 114); first ten by ID (0, 2, 4, 11, 13, 14, 16, 20, 21, 22); four trials each. The plan and decision rule were posted before running ([#62](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62#issuecomment-6049640445)). 39/40 solved; all four trials solved in 9/10 tasks; 0 infrastructure errors.
- **Task 4 trace review.** The single failure came from the simulated customer, who asked about only one of two orders; in the passing trials the customer asked for all orders. It is a simulator issue, not an agent omission, so neither run shows a confirmed omission yet ([trace](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62#issuecomment-6183015987)).
- **Settings and deviations.** Agent, simulated customer and judge: `gemini/gemini-3.8-flash`. τ²-bench's default judge (OpenAI gpt-4.1) was replaced, and a code fence is stripped before parsing the judge's JSON. Across the 40-run pilot, averages were about 56 seconds, 101K input tokens, 4.7K output tokens and $0.092 per run for the agent and simulated customer; judge usage is excluded. Run files are kept locally with SHA-256 checksums ([README](../../experiments/tau2-retail/README.md)).
- **Next.** The [τ-bench reading note](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62#issuecomment-6064619007) is posted. Next, label candidate failures in the published runs; agree the evaluation subset, rules and a capped API plan (no course budget is provided; see [#74](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/74)). These runs show feasibility, not a failure rate or the effect of the check.
- **Roles.** @bill255203 drafted sections 1–3 ([#64](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/64)); @katsukii drafted sections 4–5 and ran the experiments ([#62](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62)). Next responsibilities are being agreed.

### Midterm code and slides — November 17 maintainer note

The pair presented on 5 November 2026 ([slides](../reports/pair-retail-order-agents-midterm.pdf)). The code behind the presentation is in [`experiments/tau2-retail/online-verifier/`](../../experiments/tau2-retail/online-verifier/): the pair's added files and one patch for τ²-bench at the same base commit, `5bfa7e37b366` ([setup](../../experiments/tau2-retail/online-verifier/SETUP.md)). It matches the fork [`bill255203/tau2-bench`](https://github.com/bill255203/tau2-bench) at commit `c583eff`.

- **Question at the midterm.** Some order changes cannot be undone, and agents may claim completion too early. Can a check catch these mistakes before the agent acts?
- **Motivating failures.** Three failures from @bill255203's October runs with Qwen 3.5 9B, one detailed run each: in task 34 the agent kept saying it would look up the order but never called the tool; in task 20 it changed the wrong item, which could not be fixed; in task 41 it reported both issues resolved while two changes were still missing. The slides name each with a MAST failure mode, some provisionally.
- **Pre-verifier (@katsukii).** Before each model call, it hides tools that do not fit the conversation so far. Rule `v1` is fixed: for example, 3 of 16 tools are shown until the customer is identified, and order actions only when the order's status allows them. Rule `v2` adds one model call that keeps the order actions that fit the request; it had not been run on real tasks at the midterm.
- **Post-verifier (@bill255203).** An LLM checks each proposed reply or tool call against the policy and the committed history before it runs. It returns PASS, REVISE or BLOCK; REVISE allows one private retry, and only PASS commits. @katsukii's commit `bfe21d5` removed the task data (expected actions, answers and the customer's hidden instructions) from the verifier's input.
- **Evidence so far.** Both checks are built and unit-tested. On 2026-11-17, after rebuilding the code from upstream, the README's test command gave 110 passed, with 2 upstream tests that call OpenAI deselected. No comparison has been run. The verifier example in the slides is hypothetical. The 1.0 reward in `ONLINE_VERIFIER_LOCAL_RUN_REPORT.md` comes from a version before `bfe21d5`, when the verifier could see the task's answers, so it is not evidence that the check works.
- **Not in this repository.** Unchanged τ²-bench files and the October run outputs; both are in the fork at `c583eff` (run outputs under `data/simulations/`).
- **Next (from the slides).** Audit the context, verifier usage and cost; then run a controlled comparison with fixed tasks and models, tracking success, errors, latency and cost. As in the October pilot, state the task subset, trials and decision rule before running.
