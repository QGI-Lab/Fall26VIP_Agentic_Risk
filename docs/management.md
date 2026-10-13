# Fall 2026 management view

Use this page to find team cases, individual evidence, support needs and research
follow-ups. [Registry #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3)
links the cases; each case and its Individual tasks remain the working record.
The repository owner maintains this overview. Students update their existing work.
An open outline PR does not block agreed development work; respond to feedback in
the existing case/branch while the PR receives its repository review.

## Live queues

These searches reflect GitHub's current issue fields and PR state automatically.

| What to check | Open the view |
| --- | --- |
| Team cases and shared checkpoints | [Case issues](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Apair-case) |
| Individual contributions, including completed work | [Individual tasks](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20label%3Aindividual-task); add `assignee:USERNAME`, or check the owner in the body if assignment is unavailable |
| Evidence asking for a check | [Needs review](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aneeds-review) |
| Access, setup or scope support | [Help wanted](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22help%20wanted%22) |
| PRs authors have marked ready | [Open non-draft PRs](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pulls?q=is%3Apr%20is%3Aopen%20draft%3Afalse) |
| Work still being developed | [Draft PRs](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pulls?q=is%3Apr%20is%3Aopen%20draft%3Atrue) |
| Personal tasks needing routing | [Missing assignee](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aindividual-task%20no%3Aassignee%20-label%3Aoptional) / [missing milestone](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aindividual-task%20no%3Amilestone%20-label%3Aoptional%20-label%3Acandidate%20-label%3Astretch) |
| Maintainer research and resource work | [Owner tasks](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20assignee%3Azhongnz%20-label%3Aindividual-task%20-label%3Apair-case) / [research and access plan #74](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/74) |

Case assignees may identify only the eligible coordinator; the body names all
members. GitHub may require a participant to comment before that person can be
assigned. Missing assignment does not erase work or require repository write access.
Neither issue counts nor milestone completion percentages are grades.

## Case overview — checked October 13

This is a dated summary, not an automatic status feed. Links point to the current
records. Development counts below are student-reported, not independently rerun
or estimates of an intervention's effectiveness. Update this table after a
substantive scope/support decision, rather than copying every weekly report.

| Case / members | Evidence and current scope | Next useful action for M3 |
| --- | --- | --- |
| [Retail completion #58](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/58): @katsukii, @bill255203 | [Draft outline/notebook #63](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/63); tasks [#62](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/62), [#64](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/64). The team changed from stale inventory to a final request-completeness check. #62 reports 39/40 baseline successes across 10 tasks with four runs each, and possible simulated-customer involvement in the failure. | Check the failure trace and scoring; state the next task-selection/model rule and budget before more runs. Keep failure-seeking work as development; compare the check on declared evaluation tasks with the same baseline conditions. |
| [Financial filings #59](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/59): @ezhu001, @ziqianz360 | [Outline #60](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/60); tasks [#61](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/61), [#69](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/69), [#70](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/70). #61 reports correct baseline and verification results for three development tasks; calculations are deterministic Python and the model extracts values. | Peer-check the notebook/reference evidence. Define held-out filings/tasks, source/period/unit labels and numeric tolerances; pin the model version and settings. Measure extraction and incorrect agreement explicitly; this probe does not test model-generated arithmetic. |
| [Citation grounding #65](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/65): @geenana, @zq2082 | [Draft outline #68](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/68); tasks [#66](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/66), [#67](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/67). Initial plan compares cited answers with a post-generation check; no experiment results are recorded. | Check a small source/question/reference set and a genuine baseline run. Define claim labels, treatment of ambiguous claims and useful answer coverage, so deleting claims does not look like better task performance. |
| [Trading evaluation #71](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/71): @lisasiliu, @sm11t, @arghyas2; reported team of three | [Outline #72](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/72) lists four candidate questions; individual research tasks and a feasibility result are not yet linked. | Select one primary question, with the others as follow-ups. Give each member a contribution within that question and link their task. Check one affordable ticker/date run or record the blocker before expanding. |

An additional temporal-contamination proposal appears in the weekly-report
context but has no registered case/account mapping in GitHub at this check.
Register its actual members and scope before treating it as a tracked project;
consider the overlap with #71 when discussing a manageable question.

M3's **October 16** date remains a working target until the instructor confirms
the presentation slot. Teams should bring one question, a feasibility result or
diagnosed blocker, evidence links, next individual responsibilities and support
needs. The [semester plan](semester-plan.md#calendar-and-working-targets) gives
the subsequent October 30, November 6 and November 20 working targets.

## A short maintenance pass

1. Read the review/help queues and case updates. Resolve access and scope blockers
   first; a missing result is not automatically missing effort.
2. Route new tasks from their declared owner, parent and target. Personal tasks
   have one owner; semester-long cases use M5 and their checklist for earlier work.
3. Review ready PRs and give draft feedback without changing authors' readiness.
   Check the latest commit, CI and discussions before merging. Preserve student
   authors; close only tasks whose own evidence/review criteria are satisfied.
4. Check each active case's next action and each member's attributable work.
   Keep findings, untested recommendations and development results distinct.
5. Record shared research/resource decisions in #74 and course arrangements in
   [#24](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/24). Refresh this
   overview only when it helps a reader locate a changed question or support need.

If the course uses a weekly workbook, reuse that update or an accessible link in
the relevant task; do not write a second weekly narrative. Keep artifact links and
current blockers discoverable in GitHub. The raw workbook, meeting access details,
private student information and unrelated legacy tabs are not needed for this view.

## Connecting the cases to the research plan

The broad [research scope](research-plan.md#shared-theme) remains the course focus.
Several current cases investigate checks on evidence or task completion; trading
evaluation may contribute complementary findings about validity. Use a common
question/comparison/evidence/utility/limitations vocabulary, while retaining each
case's appropriate measures. Pool results only when units and conditions are
compatible; see [shared-study guidance](cohort-guide.md#sharing-an-experiment).

Maintainer task #74 covers a focused synthesis question, related-work comparison,
a research brief, a bounded model/data-access request and outreach preparation.
These support the cohort; they add no student deliverable. Publication and external
partnerships depend on evidence and actual arrangements. Student credit and any
later authorship follow real contributions, including shared methods and synthesis.

For model selection, match capability to the task: the commonly referenced
[ProsusAI FinBERT](https://github.com/ProsusAI/finBERT) is a financial sentiment
classifier, not a replacement for a generative filing-extraction agent. For a
temporal-contamination question, dated inputs and paper trading alone do not isolate
training-data contamination; document the model revision, cutoff evidence and
point-in-time information access. Relevant starting sources are
[Glasserman and Lin](https://arxiv.org/abs/2309.17322) and
[Look-Ahead-Bench](https://arxiv.org/abs/2601.13770); assess their assumptions before
selecting a design.

## Optional GitHub Projects board

A native Projects board can later mirror the same issues: create a project owned
by `zhongnz`, link this repository and add existing cases, Individual tasks and #74.
Use a table grouped by assignee for contributions and a board grouped by status
(To do, In progress, Review, Done); retain labels for support needs and issue types.
Keep the issue evidence as the record. Board status is not a grade or a peer check.

On October 13, the API rejected Projects access because the current CLI token lacks
`read:project`; managing a board requires `project` permission. No board was created
by this maintenance pass. If the owner chooses CLI management, authorize that scope
with `gh auth refresh -h github.com -s project`, then create/link the board. See
[GitHub's Projects API guidance](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects).
