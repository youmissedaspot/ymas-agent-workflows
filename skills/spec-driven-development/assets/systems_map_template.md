# Systems architecture map

Filename: systems.md at the project's established current architecture path
Status: Draft / Accepted under the adopting project's process
Document version: [v1 for a new map; next major/minor revision for the existing map]
Previous version: [archive link, or none for a new map]
Change summary: [initial architecture map or substantive changes]
Architecture owner and precedence: [project-defined]

Write this map after turning the True Specification conversation and decisions into specification documents. Take all current specifications into account, including architecture specifications and those unchanged by the latest conversation. This document integrates their required architecture and relationships. Do not silently invent missing decisions or let the map override accepted specifications.

## Specification coverage

| Specification ID and current path | Document version | Status: accepted / draft / unresolved | Required capabilities or constraints | Mapped systems or unresolved gap |
| --- | --- | --- | --- | --- |

[Account for every current specification; exclude archived predecessors from current authority. Note unversioned inputs explicitly.]

## Systems and responsibilities

| System | Responsibility | Ownership of reads, writes, and decisions | Supporting specifications |
| --- | --- | --- | --- |

## Relationships between specifications and systems

| Source specification/system | Related specification/system | Contract, dependency, shared constraint, or data/control flow | Enforcing owner | Supporting specification and decision status |
| --- | --- | --- | --- | --- |

[Map specifications to each other as well as to systems. Explain interfaces, upstream/downstream dependencies, data/commands/events/resources/state crossing boundaries, external integrations, lifecycle relationships, and cross-system invariants. Add a diagram if it makes the relationships clearer. Link architecture specifications for detailed design without replacing this whole-system map.]

## Coverage gaps, conflicts, and unresolved architecture

| Gap, conflict, or proposed decision | Affected specifications and systems | Status | Decision owner and required resolution |
| --- | --- | --- | --- |

Return missing decisions to the conversation or owning specification, then refresh this map. Include specification overlaps and unresolved integration questions. Do not claim complete coverage while consequential gaps remain. Check whether the architecture implied by the entire specification set forms a coherent whole.

Review and update this map as part of completing any specification cycle that materially changes boundaries, ownership, dependencies, interfaces, or architecture. If a review finds the map still accurate and requires no meaningful revision, report that result without mechanically incrementing its version.

Follow [document versioning](../../../docs/workflows/document_versioning.md): keep the newer `systems.md` at its current path and archive the complete predecessor before replacement. Specification sequence IDs remain identities, not revisions.
