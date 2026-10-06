Pair case — Financial Filing Verification
Pair case issue: 
Partners / GitHub usernames: @ezhu001, @ziqianz360
Dated plan revision: 2026-10-09

1. Business workflow
Financial analysts use public-company filings to identify reported financial values, compare performance across periods, calculate financial measures, and form research conclusions. The SEC explains that Form 10-K contains detailed information about a company's business, risks, operating results, financial results, and management's discussion of those results. Public 10-K filings are accessible through SEC EDGAR.
In the proposed workflow, a financial-research agent receives a bounded question and a specified 10-K, retrieves the relevant filing information, identifies source values and fiscal periods, performs a calculation, and produces a short derived financial conclusion. The study simulates this research-assistant workflow and does not evaluate investment recommendations or stock-price predictions.
Sources: SEC — How to Read a 10-K; SEC EDGAR — Search Filings.

2. Risk question
An agent can produce a plausible but incorrect financial conclusion if it selects the wrong line item, uses the wrong fiscal period, copies a value incorrectly, or performs the required calculation incorrectly.
Our question is:
Does a structured source-and-recalculation verification step reduce incorrect derived numerical claims in an agent's 10-K analysis without materially reducing useful task completion?
The proposed improvement requires the agent, before finalizing a derived claim, to re-check the underlying filing values and fiscal periods and independently recompute the result.

3. Prior work
FinQA (Chen et al., 2021) uses real financial reports, expert-written questions, and gold reasoning programs to study numerical reasoning over financial data.
TAT-QA (Zhu et al., 2021) similarly studies arithmetic and composed reasoning over financial tables and text. These works show that financial-document analysis can require checkable multi-step numerical reasoning, but they do not test our proposed verification intervention.
AI Agents That Matter (Kapoor et al., 2024) highlights reproducibility, held-out evaluation, and the importance of considering cost and useful performance rather than accuracy alone. For our study, this motivates matched baseline/treatment runs and a useful-completion measure alongside the risk outcome.

4. Evidence and comparison
The initial evidence route will use a fixed set of public SEC 10-K filings and bounded numerical-analysis questions with manually checked reference values, calculations, and conclusions.
The baseline agent will retrieve filing information, calculate the requested measure, and answer the question. The verification condition will use the same task, model, filing access, and answer requirements but add a structured source-and-recalculation check before final submission.
The primary risk outcome will be whether the required derived numerical result or directional conclusion is incorrect relative to the checked reference answer. Useful task completion will record whether the agent supplies the required source values, calculation, and conclusion rather than avoiding or omitting the task.

5. Feasibility and individual roles
SEC filings are publicly accessible through EDGAR, so the source documents do not require company access. The smallest development probe will use one 10-K and approximately three bounded numerical questions. We will first confirm that reference answers can be checked, genuine model runs can access the required evidence, traces can be retained, and baseline and verification conditions can both run end to end.
@ziqianz360 will own Sections 1–3, including business grounding, question refinement, and focused prior-work reading. @ezhu001 will own Sections 4–5, including comparison design, evidence accessibility, and the smallest feasibility probe. Model/API choice, later evaluation sample, and any cost requirements remain to be finalized.
