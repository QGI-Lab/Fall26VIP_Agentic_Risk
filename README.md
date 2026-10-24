# Agentic AI for Risk Management

This is the **canonical Fall 2026 VIP repository**. Students work in pairs to
investigate agentic workflows in real business use cases, assess their risks, and
use evidence to evaluate possible improvements.

The research focus is **risk assessment and improvement of agentic business
workflows**. Possible
directions include reliability, decision quality, oversight, permissions,
security/privacy, accountability and propagation. Each pair chooses one bounded
question. See the [research scope](docs/research-plan.md#shared-theme).

**One pair → one business workflow → one risk question → one bounded case study.**
The cohort shares teaching resources, research standards, reusable tools, and peer
review. Each pair produces its own report; each student owns visible individual work.

## Start here

Read the [student guide](docs/student-start.md) first. It explains this week's work,
setup, resources, and submissions. Kickoff was scheduled for **September 18, 2026**;
the first working checkpoint is **September 25**. Add your roster entry, share a
business interest or support need, and agree a small next step. **Starter practice
is optional**: use it if helpful, with no required submission or deadline. Existing work counts; no resubmission
is needed because the plan changed. Students agree partners and register their case;
the instructor can adjust pairings or help when needed. You can onboard first.

The roadmap provides starting targets. Students own their plans and seek peer
feedback; routine progress does not need instructor sign-off. The instructor can
adapt scope, timing and activities through course announcements or discussion.
Maintainers keep the repository aligned. See [how adjustments work](docs/semester-plan.md#adaptation-and-decision-making).

## What students will do

1. Learn the basics through focused reading and discussion; the guided starter is optional.
2. In a pair, choose a business workflow and one answerable risk question.
3. Present the case, question, evidence plan, and initial feasibility around midterm.
4. Complete a small experiment, replication, or structured analysis of genuine agent traces.
5. Submit a pair report and evidence; each student submits an individual contribution report.

A simulation must be grounded in documented business needs or policies; it is not
proof of effectiveness in a real deployment. Positive results, publication, and a
large software system are not required. The [research standards](docs/research-plan.md)
explain what makes a small study rigorous.

## Resources and where work lives

| Need | Location |
| --- | --- |
| What to do now, weekly goals, setup help | [Student guide](docs/student-start.md) |
| Dates, milestones, instructor support | [Semester plan](docs/semester-plan.md) |
| Choose and plan a pair case | [Case guide](docs/studies/README.md) and [short template](docs/studies/_case-template.md) |
| Find registered pairs and cases | [Case registry issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) |
| Track personal work and shared outcomes | [Issue workflow and task map](docs/issue-workflow.md) |
| Manage team progress, individual evidence and research follow-ups | [Management view](docs/management.md) with live queues and a dated case overview |
| Tentative 75% individual / 25% pair grading | [Grading proposal](docs/grading-proposal.md) |
| Beginner concepts, reading, and platform candidates | [Resource guide](docs/literature.md) |
| Agent Assurance as a source of hypotheses | [Source map](docs/agent-assurance-bridge.md) — optional reference |
| Code and setup | [Run the pilot](#run-the-pilot), [source](src/agentic_risk/), [tests](tests/) |
| Optional trace practice | [Guided starter walkthrough](docs/starter-walkthrough.md), including a worked example if setup is blocked |
| Evidence and reports | [Experiment record](docs/experiment-record.md), [results policy](results/README.md), [pair reports](docs/reports/README.md) |
| Individual report | [Guide](docs/contributors/README.md) and [template](docs/contributors/_individual-report-template.md) |
| Roster, contributing, access | [Roster](CONTRIBUTORS.md), [contributing](CONTRIBUTING.md), [access](docs/access-management.md) |
| Shared working practices and decisions | [Cohort guide](docs/cohort-guide.md), [decision log](docs/decisions.md), [meetings](docs/meetings/README.md) |

## What is ready

| Item | Status |
| --- | --- |
| Optional scripted credit-limit starter | Runnable with tests and traces; no model API needed. Teaching apparatus, not empirical agent evidence. |
| Optional external examples and genuine saved traces | Share useful resources in [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) as cases need them. No central package, adopted platform or paid access is promised. |
| Pair membership, questions, and study plans | Partners record these in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) and their Pair case; refine with feedback as work develops. |
| Candidate A: runtime containment | Optional advanced example, unselected and unimplemented; not the standard an early student outline must match. |
| Findings | To be produced and reviewed by each pair. |

The starter is deterministic. Lower authority caps cannot execute by construction,
and its verifier reads the expected answer. These are useful limitations to critique;
the output does not demonstrate real-model behavior or a practical defense.
See [pilot definitions](docs/research-plan.md#current-scripted-pilot).

## Run the pilot

**Optional practice.** Running the starter is not required for onboarding, pair
work or full Foundation credit. If you choose to run it, use Python 3.11 or later
and Git. The starter has no runtime dependencies;
installation may download Python build tools. No model account or API key is needed.

Clone once (macOS/Linux terminal or Windows PowerShell):

```bash
git clone https://github.com/zhongnz/Fall26VIP_Agentic_Risk.git
cd Fall26VIP_Agentic_Risk
```

If already cloned, open a terminal in that folder. Then choose your operating system.

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m agentic_risk --config experiments/pilot.toml --output results/local/pilot
python -m unittest discover -s tests -v
```

**Windows PowerShell** — these commands use the virtual environment directly,
so activation is not required:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m agentic_risk --config experiments/pilot.toml --output results/local/pilot
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

For a macOS/Linux checkout without installation, prefix the run and test commands
with `PYTHONPATH=src` and use `python3`. If blocked, post the exact command and error
in your starter task without credentials or private paths; setup help is part of onboarding.

The output directory must be new. Each run creates:

- `trials.jsonl`: one complete, structured trace per trial;
- `summary.csv`: condition-level counts, denominators, and rates;
- `manifest.json`: configuration, source, environment, and artifact provenance;
- `config.toml`: the exact configuration used for the run.

Local artifacts are ignored by Git. Promote only reviewed, documented result snapshots into version control.

The checks should report 10 passing tests. The default run writes 480 scripted
trials and 12 summary rows. Open `summary.csv`, then inspect a trial in `trials.jsonl`.
The [walkthrough](docs/starter-walkthrough.md) explains how to select a trace and
interpret the outputs.
For another run, choose a new output path such as `results/local/pilot-02`; existing
runs are deliberately not overwritten.

## Repository map

```text
src/agentic_risk/     experiment engine and command-line entry point
experiments/          versioned experiment configurations
tests/                behavior and reproducibility checks
results/              policy for reviewed result snapshots
docs/                 research plan, cohort guide, records, and literature
.github/               issue, pull-request, and CI workflow templates
```

## Working together

Each pair has one **Pair case** issue. Each student opens **Individual tasks** for
meaningful contributions under that case. Cohort onboarding and individual reports
use their existing assignment guides. Shared instructions are titled
**[Individual assignment]** or **[Pair assignment]** so you can see who delivers
the work. **[Individual]** identifies one student's task; **[Pair]** identifies
one pair's case. [Browse assignments by responsibility](docs/issue-workflow.md#find-individual-and-pair-assignments). Start with the student guide's
[two issue types](docs/student-start.md#two-issue-types-you-create) and
[weekly goals](docs/student-start.md#weekly-goals). Multiple students may attempt the same
agreed assignment independently, with separate evidence and review. Shared artifacts
state who did what. See the [issue guide](docs/issue-workflow.md).

Keep the software scope small. Code, scenario design, label checking, trace analysis,
literature synthesis, and reproducibility work can all be substantive contributions.
Both partners should understand the method and findings. Reuse teaching resources
and review another pair's work without creating an additional cohort-wide report.

`main` is the current project record. Dates and grading are working proposals;
formal course policy, grades, and private feedback remain in official course channels.
The repository contains no production integration. Use synthetic or approved public data.
