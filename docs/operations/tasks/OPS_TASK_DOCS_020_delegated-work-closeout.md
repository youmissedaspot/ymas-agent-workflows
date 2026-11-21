# OPS_TASK_020 — Delegated work closeout

Status: Branch candidate; verification and publication evidence remain source-specific.
Version: v1
Previous version: None; new chronological task record.
Date: 2026-11-21

## Scope and evidence

This bounded workflow review extends the existing task-context owner. The current
guide records scope, source identity, resume invariants and roles, but does not
explicitly require the coordinator to reconcile a returned unit against the whole
latest request or identify the next actor. The execution loop requires completion;
source receipts bind verification and integration to exact source. The missing
return step is a static documentation gap, not evidence that every agent fails it.

Recent primary sources describe relevant host-level failures and remedies:

- [Codex CLI 0.171.0, November 20, 2026](https://learn.chatgpt.com/docs/changelog?type=codex-cli)
  preserves drafts and queued follow-ups with their original threads and fixes late
  completion events affecting newer approvals. These are shipped client fixes,
  not a guarantee that a workflow's requested outcome was delivered.
- [Cursor release notes, November 5 and 10, 2026](https://prod.cursor.com/docs/release-notes)
  distinguish an unreachable agent request from a late delivery, and fix cloud
  handoffs starting without unpushed local commits. These are vendor reports of
  their own products, not independent YMAS measurements.
- [METR's November 20, 2026 evaluation](https://metr.org/blog/2026-11-20-q4-2026-capability-update/)
  separates verifiable tasks from judgment-heavy tasks and reports model judges
  overestimating some outputs. Its task suites do not directly evaluate this
  workflow or establish which model should fill a local review role.

The adaptation is an inference: make return ownership and evidence limits explicit
in the existing context guide. No vendor service, new agent role, orchestration
system or permanent parallel status register is required.

## Change and preserved authority

Task context becomes v1.2 at its stable path; its complete v1.1 predecessor is
[archived](../../archive/workflows/task_context_v1dot1.md). The coordinator checks
the returned artifact against latest steering and live source, names the next
owner, and distinguishes setup, execution, technical verification and acceptance.
An unreachable executor leaves current execution unknown; uncertain mutations
retain their identity rather than being replayed.

The existing grader gains three neutral cases: newer steering/source at return,
an unreachable executor, and setup without delivery. Behavioral-check guidance
becomes v1.4 with its complete
[v1.3 predecessor](../../archive/workflows/behavioral_checks_v1dot3.md) preserved.
Existing per-action negative controls cover the added cases. Package candidate
0.5.3 retains all nine skills and older installation catalog contracts. The
manifest increment prepares a distributable candidate; no release is made here.

Naming remains governed by
[OPS_WORKFLOW_001](../../OPS_WORKFLOW_001_documentation_standard.md).
The default family/category/ID/description order, sequence-first OPS_NEXT
exception, family-wide sequences and historical-name preservation are unchanged.
Inspection of live remote branches and current/archive/legacy records found
OPS_TASK_020 available at branch creation; recheck before integration.
Specification authority, small-unit repair, three-failure reassessment, independent
review where required and human acceptance remain with their existing owners.

## Verification and limits

Record exact final-source checks in the draft PR or task receipt rather than
copying full logs into each operational family. Required local checks are:

```text
python scripts/validate_package.py
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/diagnose_documents.py .
python scripts/smoke_install.py --source checkout
python scripts/smoke_install.py --source published
git diff --check
```

Package, link, edition, archive-preservation and synthetic grader checks establish
their declared structural properties. They do not establish live agent compliance,
reliable host delivery, automatic skill selection or improved collaboration.
Installation checks use disposable homes and must retain their actual result;
an unavailable CLI capability is a blocker, not a successful installation.
Platform CI and authenticated discovery require evidence for this exact candidate.

Manual review scenarios: a changed-source return stays unverified until reconciled;
an unreachable worker is reported with last-confirmed evidence and a next owner;
a configured report stays undelivered until its artifact is verified. A small
settled edit can still use an inline return without creating extra records.
No private conversation, project examples or personal operating preferences are
part of these public cases.

## Deferred and review threshold

No change is justified to naming grammar, architecture ordering, worksheet authority,
acceptance ownership or existing repair boundaries by this return gap. Do not add
another workflow skill, compulsory worksheet, universal CLI, swarm infrastructure,
telemetry collector or recurring automation. Host upgrades and optional adapters
need their own compatibility evidence and authorization.

For an optional five-handoff trial, compare similar tasks with unchanged authority,
model routing and permissions. Record coordinator minutes, owner correction prompts,
time to recover the next action, stale evidence caught and unresolved acceptance.
Keep the addition only if it prevents an evidenced omission or reduces measured
recovery effort without creating more owner work. Change no further rules when
there is no reproduced gap, credible new evidence or demonstrated net benefit.
These are proposed trial criteria, not measured savings or a new acceptance gate.
