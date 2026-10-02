# Architecture Specification — [durable concern]

Filename: `SPECARC_<L2_CATEGORY>_<ID>_<l3-description>.md` under the project's adopted specification directory
Logical ID: SPECARC_[family-wide three-digit ID; unchanged across revisions]
Status: Draft / Accepted under the adopting project's process
Version: [v1 for a new document; next major/minor revision for an existing owner]
Previous version: [archive link, or none for a new document]
Change summary: [initial architecture specification or substantive changes]
Authority owner and precedence: [project-defined]
Governing accepted decisions and related specifications: [sources and versions; distinguish authority from evidence]
Supporting ADRs, if used: [decision context/rationale; not an automatic substitute for this specification]

Define only the architectural concern within this document's scope. SPEC and SPECARC are sibling specification types; this concern may be accepted before surrounding product specifications or a complete `systems.md` exist, provided it respects governing authority. Record missing consequential decisions explicitly. A draft or this template alone grants no authority.

## Scope and architectural boundaries

[What this concern defines, excludes, and depends on. Link product requirements in SPEC where appropriate; do not duplicate their ownership.]

## Components, ownership, and authoritative state

| Component/system | Responsibility | State owned and authority for writes/decisions | Reads and dependencies | Accepted source |
| --- | --- | --- | --- | --- |

## Interfaces, contracts, and flows

[Data/control/event flow, interfaces, integration mechanisms, dependency direction, and lifecycle interactions. Identify cross-boundary handoffs and their enforcing owners.]

## Consistency, reconciliation, and persistence

[Applicable consistency/reconciliation model, ordering, replay, idempotency, persistence ownership, and recovery responsibilities. State only accepted mechanisms; mark undefined choices.]

## Architectural invariants and failure behavior

| Invariant or relevant failure | Required architectural behavior | Enforcing owner | Accepted source | Verification/acceptance case |
| --- | --- | --- | --- | --- |

## Decision status and integration gaps

| Choice, overlap, or gap | Status: accepted / proposal / unresolved / evidence / recommendation | Decision owner and source | Affected specifications and systems |
| --- | --- | --- | --- |

## Verification and whole-system integration

[Observable contracts and acceptance cases for this concern. Distinguish agent verification from project-controlled human acceptance. Review the complete current specification set and update `systems.md` when this concern changes architecture, ownership, boundaries, dependencies, interfaces, flows, or cross-system behavior; record deferral if an early specification set cannot yet support a meaningful map.]

Keep implementation scheduling, task decomposition, and delivery plans in plans. SYS remains the adopting project's system-level documentation family. Follow [document versioning](../../../docs/workflows/document_versioning.md): preserve the logical ID and live path; archive a superseded `v3.1` as `_v3dot1.md` before publishing its successor.
