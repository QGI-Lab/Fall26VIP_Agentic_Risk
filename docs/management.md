# Fall 2026 management view

This repository primarily tracks the cohort's evolving work. Useful outlines,
reading notes, development snapshots and progress reports can be accepted while
methods and experiments are still being refined. Merging records a contribution;
future work stays visible in the existing case/tasks. Grades follow course policy.

Start with [registry #3](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/3).
Students keep their own evidence and short updates; maintainers route work and
refresh this overview when a direction changes. No duplicate weekly report is needed.

## Live queues

| What to check | View |
| --- | --- |
| Team cases and checkpoints | [Case issues](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Apair-case) |
| Individual contributions, including completed work | [Individual tasks](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20label%3Aindividual-task); add `assignee:USERNAME`, or check the owner named in the body |
| Submitted work asking for a check | [Needs review](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aneeds-review) |
| Access, setup or scope support | [Help wanted](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22help%20wanted%22) |
| Ready PRs / working drafts | [Ready](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/pulls?q=is%3Apr%20is%3Aopen%20draft%3Afalse) / [drafts](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/pulls?q=is%3Apr%20is%3Aopen%20draft%3Atrue) |
| Tasks needing routing | [Missing assignee](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aindividual-task%20no%3Aassignee%20-label%3Aoptional) / [missing milestone](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aindividual-task%20no%3Amilestone%20-label%3Aoptional%20-label%3Acandidate%20-label%3Astretch) |
| Maintainer research and resource planning | [#74](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/74) |

Case bodies name all members; an assignee may identify only the coordinator GitHub
allows us to assign. Missing assignment does not erase a contribution. Counts,
checkboxes and issue closure are tracking signals, not grades.

## Case overview — October 24

This is a dated summary; issue links carry later updates. Experimental outcomes
below are reported development work, not independent reruns or general effect estimates.

| Case / members | Recorded progress | Next step as work develops |
| --- | --- | --- |
| [Retail workflow #58](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/58): @katsukii, @bill255203 | [Outline and notebooks](studies/pair-retail-order-agents.md), merged in [#63](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/pull/63). The Oct 7 Gemini pilot remains 39/40 with zero confirmed agent omissions. Oct 22 updates add difficult Qwen/HPC tasks and provisional failure classification. [#64](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/64) now links an online verifier implementation, five reported tests and one successful local demonstration. | Continue linking traces and checking failure labels; record which verifier runs only observe and which intervene. Compare conditions when ready. Hand-picked hard tasks are not directly comparable with the earlier pilot. |
| [Financial filings #59](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/59): @ezhu001, @ziqianz360 | [Case document](studies/financial_filing_verification.md), merged in #60. The [M3 update](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/59#issuecomment-6178074517) adds a FinBERT encoder ranker, controlled evidence-selection stress and two verification approaches. The earlier Qwen extraction probe is separate development history. Reading/design records are linked in #61/#69/#70/#76. | Add further filings and link the next notebook/results. Keep the known-target-alias verifier labeled as a diagnostic upper bound and retain the limits of the small development set. |
| [Wealth management #65](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/65): @geenana, @zq2082 | [Revised outline](studies/pair-wealth-management-agents.md), merged in [#68](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/pull/68). The team records professor feedback and a move from citation verification to intake, portfolio construction/risk control and independent review. Python scaffolding is reported; systematic evaluation remains pending. | Link the implementation and a small synthetic example when available; refine prompts and outcome labels as the workflow develops. Keep contributions visible through #66/#67 and later work records. |
| [Trading evaluation #71](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/71): @lisasiliu, @sm11t, @arghyas2 | [Exploratory outline](studies/pair-trading-agent-risk.md), merged in [#72](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/pull/72). Four candidate directions are recorded. Scope, roles and feasibility remain open; no experimental findings are claimed. | Record the team's next manageable step and each member's contribution when agreed. The current proposal can evolve in the same case; it does not need another registration or a completed protocol to remain visible. |

Retail implementation evidence lives in the student's
[online-verifier branch/report](https://github.com/bill255203/tau2-bench/blob/experiment/online-verifier/ONLINE_VERIFIER_LOCAL_RUN_REPORT.md).
It is linked progress, not code incorporated into this repository or a general
validation of the verifier. Some shared analysis files require NYU sign-in.

The additional temporal-contamination proposal mentioned in weekly reports still
has no registered case/account mapping here. Record actual membership and scope if
it proceeds; no project or completed contribution is inferred from a placeholder.

## A short maintenance pass

1. Read recent case/task updates and help requests. Accept useful progress with a
   clear artifact or concise record; let questions and methods evolve.
2. Set owners, parents and working milestones from the student's record. Keep one
   case per team and one owner per Individual task; no issue-count quota applies.
3. Merge useful submissions after required repository checks. Mark a working draft
   or proposal as such and leave its research follow-ups visible. A merge does not
   complete every task linked from the PR.
4. Close completed reading/design packages with a short acceptance note; keep
   ongoing experiments and semester-long cases open. Preserve original student authors.
5. Use #74 for shared research/access planning and [#24](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/24)
   for course arrangements. Reuse workbook updates rather than maintaining a second log.

The next roadmap targets are [October 30, November 6 and November 20](semester-plan.md#calendar-and-working-targets).
They remain adaptable working targets. A progress note's heading or milestone label
does not automatically establish completion of a presentation, final report or course requirement.

## Research connection and access

The [broad research scope](research-plan.md#shared-theme), compatible evidence
practices and peer feedback connect the cases. Propagation is optional; teams may
use different methods and measures. Pool results only when the evidence supports
it. [#74](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/74) tracks potential
synthesis and resource/outreach preparation without adding student assignments.

The repository is now owned by `QGI-Lab`; `zhongnz` has Write access and remains a
listed code owner. See the [access guide](access-management.md). Routine student PRs
can be reviewed and merged by an eligible maintainer. Owner settings and exceptions
require the appropriate account permissions. A separate Projects board is optional;
these issue views work without creating duplicate cards or forms.
