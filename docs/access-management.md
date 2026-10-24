# Repository access and protection

**Transfer update, October 24, 2026:** GitHub identifies `QGI-Lab` as the personal
account owning this repository. `zhongnz` has Write access and remains listed in
CODEOWNERS. That account can manage issues, review student PRs and merge when the
required checks are satisfied; it does not have administrator access. Owner-only
settings and any administrator exception must be handled with the appropriate owner
permissions. The local canonical remote is now `QGI-Lab/Fall26VIP_Agentic_Risk`.

## How we work

Students contribute through their own accounts, forks, Individual tasks, and PRs.
The repository is public, so reading and cloning need no invitation. Joining the
roster does not grant write access. Multiple students may attempt the same agreed
assignment: each owns a separate task and evidence under their Pair case or the shared cohort goal. Pair membership does not grant repository permissions.

| Person | Access / responsibilities |
| --- | --- |
| Student contributor | Start with the public fork workflow. Open issues and PRs, comment, and give peer feedback. Ask a maintainer to set labels, milestones, and assignments. |
| Appointed reviewer / maintainer | The owner grants write access only when the person needs to manage issues, provide required approvals, or merge reviewed PRs. Follow the same protected-main workflow. |
| Repository owner | `@QGI-Lab` manages invitations, permissions, branch rules, Actions settings, and exceptional recovery. |
| Current policy reviewer | `@zhongnz` has Write access and is listed in CODEOWNERS; routine student PR review and issue management continue through this account. |

Write access is broader than permission to leave a review: it permits modifying
repository branches and managing work. Student peer feedback remains useful without
write access; a required merge approval must come from an eligible reviewer with
write access, and covered files also require a code owner. See GitHub's
[protected-branch review rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

This repository belongs to a personal account. “Instructor” and “maintainer” in
our documents describe responsibilities; they do not automatically grant GitHub
permissions or create organization teams. See GitHub's
[personal repository access guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository).

## Onboarding, changes, and removal

1. Each student opens an onboarding task under [#5](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/5)
   and submits the roster-entry PR. Fork contributions can begin immediately.
2. If someone needs write access, record the requested responsibility and username
   in their task. The owner confirms the person's identity and role with the course
   team, then uses **Settings → Collaborators** to invite that account. An invitation
   remains pending until accepted; a roster entry alone is not authorization.
3. Verify the accepted permission in Settings before relying on the person for
   required reviews. Add appointed policy reviewers to the relevant entries in
   [CODEOWNERS](../.github/CODEOWNERS) through a PR. Code owners must have write
   access; listing a username alone does not grant it. See
   [GitHub's CODEOWNERS guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
4. During the semester, the owner reviews accepted and pending access when roles
   change. At [#9 handoff](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/issues/9),
   retain only people with a continuing responsibility and remove unused invitations
   or write access. Preserve their commits, task evidence, and attribution.

Students can name themselves as task owner even before the GitHub assignee field
is set. A maintainer sets eligible assignees; students should open/comment on their
task first. See [GitHub's assignment rules](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/assigning-issues-and-pull-requests-to-other-github-users).
Onboarding, setup help and optional starter practice do not wait for a permission change.

## Main protection and the historical settings snapshot

**Current partial check, October 24:** `main` is protected, with required
`test (3.11)` and `test (3.13)` checks. The Write-level token cannot read the full
protection configuration. The owner should use Settings to verify detailed rules.

The table below is the **September 23 snapshot before transfer**, retained as
history rather than a fresh claim about all current settings. At that earlier
check `zhongnz` was the owner and only active collaborator.

| Control | Last full snapshot (before transfer) |
| --- | --- |
| Visibility / default branch | Public / `main` |
| Review before merge | PR required; one approving review |
| Code-owner review | Required for files covered by `.github/CODEOWNERS` |
| New changes after approval | Stale approvals dismissed |
| Required CI | `test (3.11)` and `test (3.13)`, expected source GitHub Actions |
| Base branch | PR branch must be up to date with `main` |
| Review discussions | Must be resolved |
| Force push / deletion of main | Disabled |
| Merge method | Merge commits enabled; squash and rebase disabled |
| Administrator enforcement | **Disabled: owner can bypass protections** |

That snapshot used classic branch protection. The required checks run the unit
tests and pilot smoke test. Policy/workflow paths currently list `zhongnz` as code owner.
Student PRs follow review and CI even
when the author has write access; work goes on a branch or fork, not directly on main.

### Owner PRs and the bootstrap exception

The former `zhongnz` owner exception does not grant that account administrator
rights after transfer. A maintainer cannot approve their own PR; arrange another
eligible code owner or ask the actual owner to handle a necessary merge under the
current rules. Prepare the update and pass checks before requesting that action.

Historically, with only the owner available as an eligible reviewer, owner-authored setup PRs
cannot obtain an independent approval from that same person. The existing
[bootstrap exception](../CONTRIBUTING.md#repository-review-settings) permits an
administrator merge after checks pass, with the reason recorded in the PR. This
is a real bypass capability, not an enforced review guarantee for owner actions.

Once an additional trusted reviewer is appointed and available, confirm write
access and code-owner coverage so owner-authored policy changes can receive an
independent approval. Then the owner should enable protection for administrators
under **Settings → Branches → main → Do not allow bypassing the above settings**.
That transition needs an actual eligible reviewer; it is not enabled by this document.
Record any later emergency rule change, reason, and restoration in the affected PR.

## CI and external access

The current workflow runs on `push` and `pull_request` with `contents: read`;
it does not approve PRs. Fork runs may require approval under the current Actions
settings. A maintainer
inspects the proposed code/workflow before approving a waiting run; approving a run
does not approve the PR. Later runs remain subject to the current GitHub policy.
See [approving fork workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks).

For a student PR showing **no checks** or **awaiting approval**, inspect its changes,
then use **Approve workflows to run** in the PR's merge status panel. If GitHub
requires the branch to be updated with `main`, update it and recheck the latest run:
the new commit may need workflow approval again. Confirm both required checks pass
on the latest revision and that the approving review is still valid before merging.
Students should keep the existing PR and ask for help there; no replacement PR,
write-access grant or protection bypass is needed for this normal onboarding path.

Repository write access does not grant model credits, data access, or course-system
access. Agree those separately with the instructor. Keep credentials out of issues,
commits, and public artifacts; the current deterministic CI needs no model API key.

## Owner's check locations

- [Collaborators and invitations](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/settings/access)
- [Branch protection](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/settings/branches)
- [Actions permissions](https://github.com/QGI-Lab/Fall26VIP_Agentic_Risk/settings/actions)

Settings links require sufficient access. Students use the
[student guide](student-start.md) and [task workflow](issue-workflow.md).
