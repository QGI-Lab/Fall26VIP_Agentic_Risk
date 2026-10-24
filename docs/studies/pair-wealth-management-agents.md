# Pair case — Multi-Agent Wealth Management

- Pair case issue: [#65](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/65)
- Partners / GitHub usernames: [@geenana](https://github.com/geenana), [@zq2082](https://github.com/zq2082) 
- Peer feedback / reviewer (when arranged; no mentor assignment needed to start): To be arranged 
- Status: outline 
- Dated plan revision and available feedback: 2026-10-07 — Initial short case outline completed. 2026-10-22 — Revised research focus to multi-agent wealth management following professor feedback and further literature review; no peer feedback yet. 
- Individual task links: [@geenana](https://github.com/geenana) - [#66](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/66); [@zq2082](https://github.com/zq2082) - [#67](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/67) 

Start with sections 1–5, about half a page. Expand this same document into the report.
Examples and pending work must not be represented as findings. Do not fill fields
with invented partners, approvals, sources, or results.

## 1. Business workflow

The study simulates a real-world wealth-management process using a multi-agent AI system. In practice, financial advisers, portfolio specialists, and risk professionals perform different tasks when developing personalized investment recommendations. Our system reflects this division of responsibilities through three specialized agents.

The intended workflow is: 

Client Information → Client Intake Agent → Portfolio Construction and Risk Control Agent → Independent Review Agent → Final Wealth Plan

**Agent 1 — Client Intake Agent**: Collects and structures client information, including financial goals, assets, liabilities, investment horizon, liquidity needs, risk preferences, and other constraints. Produces a structured client profile.

**Agent 2 — Portfolio Construction and Risk Control Agent**: Uses the client profile to develop a personalized asset allocation plan, assess risk tolerance and capacity, consider liquidity requirements, and apply portfolio risk controls.

**Agent 3 — Independent Review Agent**: Independently evaluates the proposed portfolio against the underlying client information, identifies unsupported assumptions or constraint violations, and determines whether the plan should be approved, revised, or returned for clarification.

The final output is a personalized wealth-management recommendation that has passed through the multi-agent workflow.

## 2. Risk question

**Risk**: Errors or uncertainty introduced during client intake may propagate through the multi-agent workflow and affect the final investment recommendation.

We focus on two potential risks:

- Information Propagation Risk: Incorrect or omitted client information may be trusted by downstream agents, resulting in a portfolio inconsistent with the client's actual financial situation.
- Loss of Uncertainty During Agent Handoffs: Ambiguous or incomplete information may become increasingly definite as agents pass information downstream, causing subsequent decisions to rely on assumptions that were never confirmed.
- Note: More risks might appear later. These two risks are what we proposed before starting the experiment and will be tested during experiments. 

**Research Question**: When material intake errors or unresolved uncertainty occur, how do they propagate into final wealth-management recommendations, and can an independent review agent detect and contain these risks without unnecessarily changing appropriate plans?

**Possible Improvement**: Introduce an independent review agent that checks client information, portfolio suitability, and unresolved uncertainty before the final recommendation is approved.

## 3. Prior work

- [Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate (Wynn et al., 2025)](https://arxiv.org/abs/2509.05396): Demonstrates that feedback between agents can introduce new errors rather than consistently improving accuracy. Motivates measuring reviewer correction rate and reviewer-induced error rate.
- [Position: Standard Benchmarks Fail — LLM Agents Present Overlooked Risks for Financial Applications (Chen et al., 2025)](https://arxiv.org/abs/2502.15865): Highlights risks overlooked by conventional financial-agent benchmarks. Informs our evaluation framework at the agent, workflow, and system levels. 
- [Using Large Language Models for Financial Advice (Fieberg et al., 2025)](https://www.ifo.de/en/cesifo/publications/2025/working-paper/using-large-language-models-financial-advice): Examines how LLM-generated financial advice varies with investor characteristics. Helps us design synthetic client profiles with different financial goals, risk preferences, investment horizons, and constraints. 
- [Benchmarking LLM Agents for Wealth-Management Workflows (Milsom, 2025)](https://arxiv.org/abs/2512.02230): Examines the reliability of LLM agents in realistic wealth-management tasks. Motivates evaluating performance across the full workflow rather than assessing portfolio generation alone.
- [Generative AI as an Investment Advisor: Same Client, Different Advice (Agliata & Hasso, 2026)](https://www.mdpi.com/2674-1032/5/2/54): Compares investment recommendations generated by different LLMs. Informs our model-selection decision; we will initially use Claude as the underlying model for all three agents. 

## 4. Evidence and comparison

We will construct a small initial dataset of synthetic client cases with predefined ground truth, including financial goals, risk preferences, investment horizons, liquidity requirements, and relevant constraints.

**Experiment conditions**:

- **Clean Intake**: Agents receive accurate and complete client information.
- **Perturbed Intake**: Selected material client facts are omitted, altered, or presented with unresolved uncertainty to test whether errors propagate through the workflow.

Each case will pass through the three-agent system. We will preserve the full trace, including the original client information, Agent 1's structured profile, Agent 2's proposed portfolio, Agent 3's review, and the final recommendation.

**Evaluation framework**:

- **Agent 1 — Client Profile Accuracy**: Evaluate whether the structured profile correctly preserves important client facts, constraints, and uncertainty.
- **Agent 2 — Portfolio Suitability**: Score the initial investment plan against a predefined rubric, including risk appropriateness, liquidity requirements, diversification, and constraint compliance.
- **Agent 3 — Review Effectiveness**: Evaluate whether the independent reviewer identifies existing errors, successfully improves the portfolio, or introduces unnecessary changes.

**Main measures**:

- **Error Propagation Rate**: Frequency with which introduced or observed upstream errors affect downstream recommendations.
- **Constraint Violation Rate**: Frequency of portfolio recommendations violating material client constraints.
- **Reviewer Correction Rate**: Proportion of identified pre-review errors successfully corrected after review.
- **Reviewer-Induced Error Rate**: Frequency with which the review process introduces errors that were not present in the initial recommendation.
- **Portfolio Quality Score**: Rubric-based evaluation of portfolio suitability before and after independent review.

The main outcome is whether the final recommendation is materially inconsistent with the client's true financial situation. Comparisons will focus on clean versus perturbed intake conditions and portfolio quality before versus after independent review.

## 5. Feasibility and individual roles

The experiment will use synthetic client cases and Claude as the initial underlying LLM. A basic Python implementation of the multi-agent workflow has been started. Further work is needed to refine prompts, finalize evaluation rubrics, run experiments, and analyze the results.

[@zq2082](https://github.com/zq2082) — Client Cases and Risk Evaluation
- Develop synthetic client profiles with predefined ground truth.
- Design clean and perturbed intake conditions.
- Identify material client constraints and potential information propagation risks.
- Help establish evaluation criteria for client profiling and portfolio recommendations.

Deliverable: Initial synthetic client dataset and evaluation framework.

[@geenana](https://github.com/geenana) — Multi-Agent Experiment Implementation
- Develop and refine prompts for the three agents.
- Implement the multi-agent workflow in Python using Claude.
- Run initial experiments and preserve outputs from each agent.
- Evaluate portfolio quality before and after independent review.
- Analyze initial results and identify potential improvements.

Deliverable: Initial multi-agent experiment implementation, recorded results, and preliminary evaluation.

## 6. Working method

As the study develops, record the applicable details below. This is a working
method, not an instructor approval form. State evaluation rules before applying
them, seek peer feedback and record changes after inspecting evidence.

- Evidence route; exact platform/data/model versions as applicable.
- Unit of analysis, data selection, development versus evaluation split; prior inspection and its effect on claims.
- Comparison and what remains fixed; labels and how they are checked.
- Measures with numerators/denominators; risk, utility and relevant cost.
- Sample/repetition plan, treatment of dependent observations, uncertainty/claim limits.
- Failure, exclusion, retry, stopping and analysis rules.
- Resources, validation evidence, available feedback, and dated changes with reasons.

For existing-trace work, specify labeling rules and an agreement check. Use only
applicable fields from the [experiment record](../experiment-record.md).

## 7. Results and interpretation

Add actual evidence links, counts, comparisons and appropriate uncertainty. Include
failures, missing data, null findings and deviations. State what the evidence supports,
what it does not establish, and whether the proposed improvement was actually tested.

## 8. Contributions, reproduction and next steps

Identify each student's work with task/PR links, including review and tool assistance.
Give artifact locations, exact analysis/run instructions and access requirements.
Link a peer's reproduction/source check, known limitations and next useful question.
Link midterm/final slides and both individual reports. Cite sources where used.
