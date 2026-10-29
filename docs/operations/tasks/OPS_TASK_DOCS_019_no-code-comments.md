# OPS_TASK_019 - No code comments in YMAS workflows

Status: Implemented and locally validated; exact-source installation and CI tracked in the PR.
Version: v1
Previous version: None; new chronological task record.
Date: 2026-10-29

## Authority and scope

Philip explicitly directed no comments in code for YMAS and implementation in its
Git workflows. Business explanations, design rationale and non-obvious
implementation reasoning belong in specification documents. An implementation
hazard exception was explicitly rejected. GitHub branch publication and a draft
PR are authorized. Philip subsequently explicitly approved merging this focused
change into main after validation passes. Merge authorization does not permit a
GitHub approval review or bypassing branch protection. Deployment, release tags
and changes to a user's normal installation remain outside this task.

The checkout is `youmissedaspot/ymas-agent-workflows`, initially clean on branch
`work` at main commit `1708dfa64a05c94ce0c20a21ee004f50ebd2599a`.
Refreshed `origin/main` matched that commit. This task uses the isolated branch
`policy/no-code-comments`; the existing local `work` ref prevents the usual
`work/<slug>` namespace. The next available task identity is OPS_TASK_019 after
inspection of current, archive and legacy records. Recheck before integration.

## Implementation

The shared [code-comment rule](../../rules/code_comments.md) owns the policy,
reasoning preservation, scope, verification and handling of actual conflicts.
`AGENTS.md` and `INDEX.md` route to it. The execution loop becomes v2.3 at its
stable path, with the complete v2.2 predecessor preserved in
[the archive](../../archive/workflows/agent_execution_loop_v2dot2.md).

Project bootstrap establishes the rule during authorized adoption. Specification
development, repair and implementation review link to the shared owner. Detailed
system and architecture templates provide a home for reasoning. Package artifacts
follow plugin conventions without separate document editions. The manifest uses
patch candidate `0.5.2` because the README requires a version bump before merging
changes distributed through the main-branch catalog. Installation catalog checks
retain `0.5.1` and all older supported contracts alongside the new candidate.

Only the manifest version and installation catalog regression expectations change
outside the workflow documentation. Existing Python comments and docstrings
remain outside this focused workflow implementation; no comments are added.
Markdown prose is preserved. No actual legal-notice or tool-directive conflict
was found in the changed documentation. The new rule
requires reporting such conflicts rather than granting an exception.

## Verification and handoff

Local package validation passes for nine skills, 78 Markdown files and 295 links.
All 52 deterministic regressions pass. Document diagnostics report only the eight
existing unversioned legacy-record warnings, with no ID collision. Comparing the
archive with its original source after reversing link rebasing confirms the
complete predecessor is preserved. Diff review confirms no new code comments,
no exception for hazards or JSDoc, and no unrelated cleanup.

Exact-source installation checks, platform CI, source receipt and publication
details are recorded in the PR. These checks verify packaging and documentation,
not future model compliance. Authenticated client discovery remains separate
from installed-file validation and must not be inferred from it; no release tag
or normal installation refresh is part of this task.
Merge requires passing applicable checks and live source reconciliation. Do not
tag, deploy, submit an approval review or refresh a user's normal installation.
