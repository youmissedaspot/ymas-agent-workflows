# OPS_TASK_014 - Agent verification and derived Feature Maps

Status: Implemented on isolated task branch; integration, allocation reconciliation and distribution pending.
Version: v1
Previous version: None; new chronological task record.
Change summary: Extend maintained verification and add bounded structured capability navigation.
ID allocation: Branch-local provisional OPS_TASK_014; the integration coordinator must reconcile concurrent reservations before integration. Current/archive/legacy records in the inspected source end at OPS_TASK_013.

## Source and scope

This task starts from unmerged [candidate PR #13](https://github.com/youmissedaspot/ymas-agent-workflows/pull/13),
commit `cd41c538e153e293e728932bd9804e2effb93c86`, tree
`dfb468a8989222fbd93592572623a306d934827c`. It retains that dependency and does
not claim these foundations are on main. No release-branch, installed runtime or adopting
repository change is part of this task. Publication, version selection, installation and
integration remain separately coordinated; inherited package version is not evidence of
equivalent installed bytes or permission to distribute this changed source.

## Implementation

Extend [boundary verification](../../workflows/verification_boundaries.md) with promotion
criteria and maintained health/state/exercise/inspection/evidence/cleanup capabilities.
Exact repository interfaces remain optional and specific to their actual reproducibility
need. Approval, isolation, independent review, acceptance and narrow-repair stops remain.

Add [Feature Map guidance](../../workflows/feature_maps.md), a JSON schema and empty
template, a self-contained synthetic example, and a read-only structural/freshness/graph
checker. Typed edges retain source provenance and declared coverage. Expected behavior
traces to accepted requirements; implementation and maps cannot override them. Command
descriptors never execute. Relevant changes trigger scoped maintenance without scheduling
or blind regeneration. Existing skills, context, source receipts and systems-map roles
remain the owners of their respective behavior.

Workflow revisions preserve complete predecessors: boundary verification v1 → v2,
execution loop v2 → v2.1, and behavioral checks v1 → v1.1. Package skill/template contracts
remain distribution artifacts. No historical document identity is renamed or normalized.
The fixture's narrow line-ending rule preserves its declared raw hashes across checkouts.

## Verification and limits

The source-specific handoff receipt retains final commit/tree, commands, outcomes,
artifacts and independent review outside the reusable package. Checks include the full
regression suite, package/schema/link validation, document diagnostics, schema/reference
negatives, raw metadata drift, source escape rejection, deterministic graph export,
command nonexecution and materialized example execution. Two new behavioral cases use
the existing grader; synthetic grader checks and observed replays remain distinct.

Matching hashes cover declared sources only and cannot authenticate acceptance, prove
semantic completeness, enforce filesystem isolation or establish application runtime
behavior. The example proves only its synthetic record lookup assertions. No Graphify
adapter, universal CLI, cloud orchestration, scheduled maintenance, token-savings claim
or additional skill is introduced. No push, merge, tag or installation is claimed here.
