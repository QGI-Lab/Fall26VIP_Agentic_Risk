# Contributing

This is the canonical Fall 2026 VIP workspace. New students begin with the
[student guide](docs/student-start.md). Orientation and setup support begin at the
September 18 kickoff, with onboarding targeted for September 25; no repository submission
is due at kickoff. The [semester plan](docs/semester-plan.md) and [selection guide](docs/studies/README.md)
support the tasks agreed after kickoff. Each pair develops its own case; no platform or study is adopted automatically.

## Your first contribution

1. Follow the [student quick start](docs/student-start.md) after kickoff, with setup help as needed. Advance preparation is optional.
2. Use your own GitHub account. With repository write access, create a branch here; otherwise fork the repository and open a pull request back to this repository's `main`.
3. Follow the [enrollment guide](docs/contributors/README.md#first-contribution) to add your public roster entry. No personal profile file is required. Share only your preferred display name and GitHub username.
4. Open your own Individual task under #5, then submit the introduction PR with `Closes #YOUR_TASK_NUMBER` and `Relates to #5` (use your actual task number). No completed research result is required. A maintainer reviews onboarding and can arrange repository access separately.
5. Choose your Pair case (or a shared cohort goal) and open an **Individual task** for your own work. Agree a small scope with your partner and arrange peer feedback as needed; routine work does not wait for a maintainer assignment. Follow [the issue guide](docs/issue-workflow.md): multiple students attempting the same assignment each use their own task under the same goal.

## Workflow

This repository primarily tracks evolving research. Useful outlines, notes and
development snapshots can merge with unfinished next steps clearly recorded.
Acceptance records progress; it does not require a finished protocol, completed
experiments or a publishable result. Research feedback can guide later updates.

Use the same task/PR workflow for onboarding and later work. An introduction PR
needs a roster change, a short introduction, its Individual task link, and
`Relates to #5`; it can omit the research interpretation and detailed evidence sections.
Starter practice is optional and is not a prerequisite for this PR or later pair
work. A roster PR can be made in the browser without installing Git or Python.

1. Start from an Individual task with one student owner, a parent Pair case or cohort goal, an assessment category, a milestone or optional/backlog status, acceptance criteria, and planned evidence. Name collaborators and reviewer separately. The Pair case names both partners; the Cohort goal's assignee coordinates cohort coverage; each Individual task's sole assignee owns that student's work. Introduction tasks use #5 as their parent; the [task map](docs/issue-workflow.md#complete-task-and-assessment-map) covers all deliverables and grading components.
2. Create a short-lived branch from current `main`, such as `work/12-trace-analysis`. Do not work directly on `main`.
3. Make one focused change and document assumptions. Link deliverables and substantive reviews in your Individual task. Keep the evidence there; no separate contribution log is required.
4. For code or experiment changes, run `python -m unittest discover -s tests -v` plus the relevant experiment. For documents, check references, links, and claims. CI runs for every pull request.
5. Open a pull request with its issue, milestone, evidence, and a brief attribution statement where needed. For shared work, identify each person’s part and link their tasks. No duplicate portfolio update is required.
6. Obtain review from someone other than the author. A contributor from another pair or the instructor should review methodological changes. Resolve review discussions and pass CI before merging.
7. Merge with a **merge commit** to preserve individual commit authors. Use `Closes #123` for a completed Individual task and `Relates to #456` for its Pair case or cohort goal, substituting actual numbers. One student's PR does not close the Cohort goal. A joint PR closes each student's task only after that task's own criteria are checked.

For each active Individual task, keep a short evidence/next-step/blocker update. If the course uses a weekly workbook, reuse the same text or an accessible link rather than writing another weekly narrative. Keep shared output links in the Pair case; cohort collections find them through registry #3. State help/review requests in the existing task, following the [management view](docs/management.md). Keep work status in Issues and pull requests; milestone completion records delivery. Use the [meeting guide](docs/meetings/README.md) to capture decisions and assign follow-up actions.

Organize work as `To Do`, `In Progress`, `Review`, and `Done` if a Project board is enabled. Issues and pull requests are sufficient to start. An issue should have at least one of these labels:

- `research`: literature, hypotheses, design, analysis, or writing;
- `engineering`: experimental environment or instrumentation;
- `experiment`: a configured, executed, or analyzed study;
- `bug`: behavior that contradicts the documented design;
- `documentation`: onboarding, contribution reports, presentations, or administrative documentation.

Issues marked `stretch` are optional extensions; focus on the current case before adding scope. For a case-specific change, record the reason, affected evidence and any feedback in the existing Pair case; routine refinements need no instructor sign-off. The instructor can adapt course arrangements through an announcement or discussion. Maintainers record the change once and synchronize affected guidance through normal PR review; the course adjustment does not wait for a merge. See [adaptation rules](docs/semester-plan.md#adaptation-and-decision-making).

Issues marked `candidate` are optional proposals, with no delivery milestone until
explicitly adopted by a pair and reviewer. Candidate A (#4) is an advanced example,
not a cohort requirement. Early exploratory work counts when its evidence and
purpose are clear, even if the idea is rejected. Each pair records its working
method and evaluation rules, seeks peer checks and records changes. Shared
collection issues and an unassigned mentor do not block progress.

## Make your contributions visible

The [roster](CONTRIBUTORS.md) identifies students and their GitHub accounts; Individual tasks and linked PRs record their work. Literature synthesis, experiment design, reproductions, datasets, analysis, validation, writing, reviews, and presentations all count as visible work when they link to an inspectable artifact. Commit counts and lines of code are not measures of research value or a grading rubric.

Use a commit email associated with your own GitHub account; GitHub's private `noreply` address works. Configure it for this checkout, rather than using a shared team identity. Copy the exact address from your GitHub email settings; do not guess it or put private addresses in the roster. GitHub also has [other conditions for profile contributions](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/troubleshooting-missing-contributions), including the branch and repository relationship. Task evidence and substantive review links capture work that a commit graph cannot express.

For work jointly authored in one commit, use `Co-authored-by` trailers with each person's chosen account-associated address. Confirm the credit with them first. See [GitHub's co-author instructions](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors). Link reviews and other contributions in the relevant tasks even when they do not justify commit co-authorship.

Keep original authors when integrating student changes. If a maintainer must cherry-pick or import work, preserve author metadata and link the original PR. Do not replace students' work with a maintainer-authored aggregate commit. If tools materially assisted the work, describe their role and what the contributor verified; credit named people only for their actual work.

## Repository review settings

The [access guide](docs/access-management.md) records current GitHub settings,
onboarding and removal of access, reviewer eligibility, and the owner bypass.

`main` is protected and requires passing `test (3.11)` and `test (3.13)` CI checks.
Follow the PR merge panel for current approval, code-owner and conversation
requirements; new commits may require a fresh review. Use a merge commit to
preserve the original student contribution history. The access guide distinguishes
the current permission check from the full pre-transfer protection snapshot.

Changes to workflow configuration and core research/semester policy require a code-owner review. `@zhongnz` remains the listed policy reviewer; the repository owner is now `@QGI-Lab`. Update `.github/CODEOWNERS` through review when actual maintainers are appointed. No student access or role is assumed from appearing in the public roster.

The owner manages any administrator exception allowed by the actual branch settings.
`@zhongnz` now has Write access and cannot use the former owner bypass. Ordinary
student work follows the review path. Document any exceptional bypass and its reason
in the relevant issue or pull request; account permissions govern what is possible.

## Experiment changes

A research result is reviewable only when another person can identify exactly what produced it. Include:

- the research question and hypothesis or quantity to estimate;
- the treatment, evidence groups, or comparison, including what stays fixed;
- defensible reference labels and any fault/perturbation definition where applicable;
- configuration, code revision, source data/trace revisions, and transformations;
- backend, model, prompts, sampling parameters, and seeds for new model runs;
- source records or trial traces and analysis with explicit units and denominators;
- negative results, limitations, and known threats to validity.

Do not describe deterministic fixture runs as LLM evidence. Do not treat an ideal verifier with direct access to truth as a deployable control. See [the experiment record](docs/experiment-record.md) before interpreting results.

## Code changes

- Keep the core experiment readable before adding abstractions.
- Add a focused test for behavior that could change a research conclusion or corrupt provenance.
- Never commit credentials, API keys, local `.env` files, or generated caches.
- Use synthetic or approved public data only. Do not commit personal, confidential, regulated, or proprietary data.
- Avoid adding services, frameworks, or dependencies until a concrete experiment requires them.

## Durable handoff

An issue is done when its code or document is reviewed, its validation is recorded, and its result can be located without private context. At the end of a research package, update the open questions and preserve the configuration, code, traces, findings, limitations, and next hypotheses.

Discuss authorship expectations before manuscript work begins. Use plain role descriptions in tasks and the final report’s contribution summary. CRediT labels are optional; see the [cohort guide](docs/cohort-guide.md#credit-and-authorship).
