# Pair cases, cohort goals, and Individual tasks

**One shared case per pair; one owner per Individual task.** Issues and PRs are the
contribution record. Do not create an issue for every meeting, comment, or weekly update.

The instructor may adapt team size. Keep the existing **Pair case** issue type,
name all actual members, and give each member their own tasks and report. Record
announced course/assessment arrangements in #24; the case name does not fix team size.

## Find individual and pair assignments

The issue title and assignment label show **who produces the deliverable**:

| In the issue list | What it means | Current issues |
| --- | --- | --- |
| **[Individual assignment]** · `individual-assignment` | Instructions for each student's own work. | Onboarding #5, focused reading #2, individual report #23; **optional** starter #1. |
| **[Pair assignment]** · `pair-assignment` | Instructions for one shared output per pair. | Registration #3, method/feasibility #7, midterm #21, analysis #8, report #9, final presentation #22. |
| **[Resource]** | Optional examples or shared help. | Candidate A #4 and resources/setup help #6. |
| **[Course]** | Course arrangements; no student submission. | #24. |

Browse [individual assignments](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20label%3Aindividual-assignment)
or [pair assignments](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20label%3Apair-assignment).
The `optional` label marks work you may skip. Starter #1 has no required deadline
or grade penalty; existing substantive contributions remain creditable.

These are shared instruction issues. Your own **[Individual]** task records what
you did; your **[Pair]** case keeps your pair's outputs together. Each partner's
work on a pair assignment remains individually attributable. Assignment labels
describe responsibility, not grading weights: only the midterm and final report
have separate shared pair marks under the [75/25 proposal](grading-proposal.md).

## Which issue do I create?

| Issue type | Purpose | Ownership and completion |
| --- | --- | --- |
| **Pair case** | One pair's workflow, question, plan, report links, and adjustable checkpoint checklist. Create after partners agree; register its link in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). | Names both partners; add peer reviewers when arranged. Both partners may be assigned. Stays open until the agreed case outputs are reviewed. Assignment alone does not allocate individual credit. |
| **Individual task** | One student's meaningful contribution or independent attempt. | Exactly one student owner; separate evidence and review. Name collaborators separately. |
| **Cohort goal (maintainer)** | Shared instructions titled Individual assignment, Pair assignment, or Resource as above. | Maintainer coordinates required coverage or optional support; it is not a single research project or cohort-wide grade. |
| **Course notes (#24)** | Current arrangements, instructor announcements and adjustments. | Maintainers record changes; no instructor task checklist or separate approval queue. Grades stay private. |

GitHub calls the templates **Pair case**, **Individual task**, and **Cohort goal (maintainer)**.
The parent is an issue link in the form; native GitHub sub-issues or a Project board
are optional. No multi-select enrollment field is needed. Multiple assignees on a
pair issue identify partners; personal credit still comes from one-owner tasks.

Students create the first two types. **Cohort** means the whole class: its existing
issues explain shared assignments and check coverage. One Pair case holds all of
a pair's shared checkpoints; individual tasks describe each partner's actual work.
The internal label `group-goal` is retained for cohort issues and existing filters.
That label alone does not identify who delivers the work; use the assignment
title and labels above. There is no shared cohort grade.

### Where does my task belong?

| What you are doing | What you create or update |
| --- | --- |
| Joining the repo | Your own Individual task, parent #5, with your roster PR. |
| Choosing optional starter practice | If you want feedback or contribution credit, use your own Individual task, parent #1, with your attempt/error and observation. No required submission. |
| Starting with a partner | One Pair case, created by either partner; register it in #3. |
| Reading, designing, coding, analyzing or preparing pair outputs | Your Individual task under that Pair case. Put shared output links in its checkpoints. |
| Writing your personal contribution report | Your own Individual task, parent #23; also link it from the Pair case. |
| Posting a weekly update or a small review/help contribution | Comment in the existing relevant task and link the evidence. |

Enter the parent's issue number in **Primary parent issue** and link your task
in that parent; a comment is enough if you cannot edit its body. Research tasks
stay under the Pair case as they progress through #7, #8, #9, #21 and #22; these
cohort issues describe/check outputs and do not require another personal task.
Use the [student guide](student-start.md#two-issue-types-you-create) for an example.

## Simple student workflow

1. Onboard with your Individual task under [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5). Starter practice under [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1) is optional; it is not a prerequisite for the next steps.
2. When partners agree, **one partner** opens **New issue → Pair case**,
   names both partners, and links it in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). Start with a small scope; the instructor
   can adjust pairings or direction. Choose a stable short slug such as `retail-refunds`.
3. Each partner opens **Individual tasks** under that Pair case for their meaningful
   work. Select its assessment category and include deliverable, done criteria, target, and a peer reviewer when arranged. Reuse a task
   across weeks; no minimum number of tasks is required.
4. Link the artifact and review in the Individual task. Keep the pair's shared
   output links beside its Pair case checkpoints. Register the case once in #3;
   cohort collection goals use that registry to find the outputs. No repeated
   output posts under #7, #8, #9, #21 and #22 are needed.
5. A PR uses `Closes #YOUR_INDIVIDUAL_TASK` only when complete and `Relates to
   #YOUR_PAIR_CASE`. A joint PR may close multiple personal tasks after each is
   checked. It must not automatically close the pair or a cohort collection goal.
6. Write your individual report under [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23) and link it from the Pair case as well.

A task has **one primary parent**. Related goals may link it without requiring a
second task. Shared resource work can belong directly to [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6), or [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7) when agreed;
link it from the benefiting pair. Assignees/labels/milestones can be set by a
maintainer; missing edit permissions do not prevent starting agreed work.

## Management view

Open the [management page](management.md) for live queues, the current case overview
and maintainer research follow-ups. The detailed workflow below explains the fields.

Start with the registry and attention queues below. The issue body and linked
evidence are the record; a separate Project board or activity spreadsheet is optional.

| Need | View / action |
| --- | --- |
| Pair membership and checkpoint progress | [Registry #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) → each Pair case's checklist and individual task links; [all Pair cases](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20label%3Apair-case) |
| One student's evidence, including completed work | [All Individual tasks](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20label%3Aindividual-task); add `assignee:USERNAME` to the search |
| Evidence awaiting a peer check | [Needs review](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aneeds-review) |
| Blockers or support requests | [Help wanted](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22help%20wanted%22) |
| Working targets and repository merges | [Milestones](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones) and [open PRs](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pulls?q=is%3Apr%20is%3Aopen) |
| Personal tasks missing routing information | [No assignee](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aindividual-task%20no%3Aassignee) / [no milestone](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues?q=is%3Aissue%20is%3Aopen%20label%3Aindividual-task%20no%3Amilestone%20-label%3Acandidate%20-label%3Astretch%20-label%3Aoptional) |

These use GitHub's [issue filters](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests).
The all-task view includes open and closed work. Check the body when an assignee
has not been set; `author:USERNAME` can help find self-created issues. A missing
field is a routing problem, not a missing contribution.

### Attention and completion

- **Working or planned:** keep the existing short evidence/next-step/blocker update.
- **Needs help:** describe the blocker and help needed in the task; use `help wanted`.
- **Ready for review:** link the evidence and say what needs checking; use
  `needs-review`. This requests a check, not a grade or declaration of completion.
- **Completed:** close after the agreed output and review are linked. If work is
  dropped, close as **not planned**, explain why and retain useful evidence.
  GitHub's [closure reasons](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/closing-an-issue)
  distinguish these outcomes; neither reason determines marks.

Students without label permissions state the request in their existing update;
a maintainer applies the label. Remove resolved attention labels on open issues.
Both can apply when a partial result needs review and a later step is blocked.
Check recent comments too; there is no automatic status sync.

### A short coordination pass

At an appropriate check-in, a maintainer reviews help/review requests, checks new
task owners and targets, and follows the registry into relevant Pair cases. Form
answers do not set GitHub's assignee/milestone fields automatically. Set them from
the student's record, and add `individual-task` to tasks created outside the form.
Ask only if the record is ambiguous; routine work proceeds during this housekeeping.
Keep assignment guide titles and their `individual-assignment` or `pair-assignment`
labels aligned. Mark starter practice and its personal tasks `optional`; leave
their milestone unset unless the student chooses a working checkpoint. Optional
practice has no class-wide completion requirement.

The repository owner handles routing until another coordinator agrees to it.
A Cohort goal assignee coordinates coverage and does not own students' work.
Partners maintain case links; peers check evidence. Instructors choose their
feedback cadence and retain private grading authority.

Milestone percentages mix collection issues and personal tasks; they do not measure
student performance. Pair cases sit in M5, so use their checklist for earlier
checkpoints. No new issue for every graded component or per-student quota is required.

For assessment, follow the [task map](#complete-task-and-assessment-map), the student's
tasks/reviews and individual report, and the pair's shared outputs. Check all four
work stages, collaboration and the report, then the two shared components.
Category weights apply across the semester, not once per issue. Record marks
privately using announced policy. Existing tasks with a clear stage remain valid;
no resubmission is required for the new dropdown.

## Multiple students doing the same assignment

Any number of students may independently do the same agreed assignment. Each uses
a separate Individual task under the same parent, with their own evidence and review.
They can each earn full individual credit; credit is not divided between assignees.
For example, optional starter critiques from several students belong under [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1).

Partners doing joint work choose **Contribution to shared work**, describe their
actual parts, and link each other's tasks. They may use the same code, table, or PR.
Do not describe a joint artifact as independent results. A planned replication by
another pair needs an agreed purpose; there is no requirement that every topic differ.

## Complete task and assessment map

Cohort issues are retained to keep existing links and show coverage. Students do
**not** open tasks under every row. Most research work belongs under the Pair case.

| Work / output | Primary student task parent | Cohort coordination / target | Proposed assessment |
| --- | --- | --- | --- |
| Roster and onboarding | [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) | [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5); M1 Sep 25 | Access/attribution; setup alone is not research credit |
| Optional starter attempt and critique | [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), if recording an attempt | Optional; no required milestone or deadline | Possible Foundation evidence; skipping it has no penalty |
| Reading / business workflow | Pair case (or [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2) for shared resources) | [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2) resources; M2 Oct 9 | Foundation 10 |
| Question and evidence plan | Pair case | [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) case registry; outline M2, working method and feedback M3 Oct 16 | Question 10 |
| Optional reusable examples / setup help | Pair case for case-specific work; [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) for a shared resource contribution | Share when useful; no required teaching package or fixed delivery date | Credit for actual contribution; no additional assignment |
| Feasibility and execution | Pair case | [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7) validation; M3 then M4 | Execution 25 |
| Analysis | Pair case | [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8) first analysis; M4 Oct 30 | Execution or Synthesis; distinct outputs, no double counting |
| Midterm case/question presentation | Pair case; reuse design task if it covers the role | [#21](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/21) tracks decks/feedback via registered Pair cases; M3 Oct 16 | Pair 10 |
| Final report and reproducible evidence | Pair case | [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9); draft Nov 6, final M5 Nov 20 | Synthesis 10 individually; integrated pair package 15 |
| Final presentation | Pair case; reuse report task if it covers the role | [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22); M5 Nov 20 | Required, feedback only; no separate weight |
| Individual contribution report | [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23); cross-link Pair case | [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23); draft Nov 6, final Nov 20 | Individual 10 |
| Collaboration and substantive peer review | Existing relevant task; substantial review package may have its own task | Ongoing, with cross-pair review before M5 | Individual 10 |
| Course arrangements and adjustments | Course notes [#24](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/24); no student administration tasks | Updated when arrangements change; not a milestone deliverable | Announced policy; private instructor assessment |
| Candidate A practical gate | Pair case only if explicitly adopted; related [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) | [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) deferred, no delivery milestone | Optional scope; no additional points |

The [grading proposal](grading-proposal.md) defines the rubric and stage boundaries.
The two assessments of individual contribution and integrated pair output serve
different purposes; closing issues does not award points.

## Who reviews what?

- **Personal task:** an agreed reviewer other than its owner checks the evidence;
  a partner can provide this review. A substantial cross-pair review is useful too.
- **Study plan and method changes:** partners record the method and changes, seek
  peer feedback and proceed within their scope. No instructor sign-off or appointed
  mentor is required. Ask for guidance when the question or evidence remains unclear.
- **Final handoff:** a peer, preferably from another pair, checks the analysis/source
  trail. Record the actual check and any limits; an instructor need not perform it.
- **PR merge:** an eligible GitHub reviewer approves according to [access rules](access-management.md).
  Peer feedback does not automatically grant merge permissions. A routine research
  step need not wait for a documentation PR to merge; retain the dated issue record.
- **Grades:** the instructor assesses evidence privately using announced policy.

## Milestones, review, and closing

Each Individual task uses the milestone for its next agreed output; optional
practice may have none. A semester-long
Pair case uses M5 and keeps its M2–M5 checklist in the body; do not create five
separate pair issues. Cohort collectors use their relevant milestone. Milestones
organize work, not new assignments.

A reviewer checks a student's evidence separately from the pair's overall progress.
The pair may proceed with a recorded method and feasibility check, arranging peer
feedback as work develops, without waiting for instructor approval or the cohort's
[#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3)/#7 to close. A maintainer closes collection goals only after every required
participant/pair is covered or an explicit scope adjustment is recorded.

Use one short weekly update in each active task: evidence, next step, blocker. Keep
completed links visible. No duplicate portfolio, public gradebook, or weekly report.
If course direction uses a weekly workbook, reuse its update or an accessible link;
keep task evidence and current blockers visible without a second narrative.
When a dependency blocks progress, preserve the existing work, narrow the next
task and record why. Ask the instructor for unresolved workload/partnership issues
or changes to assessed expectations. Late joiners get suitable targets. Course
adjustments follow the [adaptation rules](semester-plan.md#adaptation-and-decision-making).

## Transition from the previous plan

Existing student [#28](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/28), [#30](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/30), and PR [#29](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/29) remain valid. Do not rewrite student-authored
records or require resubmission. Existing research tasks can be re-parented by agreement,
with a note and original evidence retained. Previous cohort goals become coordination
and output collections; [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) stays optional. No pair membership or completed result is
inferred from an old assignment. Agree partners, create the Pair case, then register
its link in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3).
