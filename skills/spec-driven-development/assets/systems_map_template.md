# Systems architecture map

Filename: systems.md at the project's established current architecture path
Status: Draft / Accepted under the adopting project's process
Version: [v1 for a new map; next major/minor revision for the existing map]
Previous version: [archive link, or none for a new map]
Change summary: [initial architecture map or substantive changes]
Architecture owner and precedence: [project-defined]

Write this map when the current specification set supports useful whole-system integration. Review the complete current SPEC/SPECARC set or project-defined equivalents, including documents unchanged by the latest conversation. SPEC and SPECARC are siblings in either design order; this map integrates them and is not the first mandatory place to design architecture. Record early deferral instead of inventing a meaningless map. Do not invent missing decisions or let the map override newly accepted higher product decisions.

## Specification coverage

| Specification ID and current path | Document version | Status: accepted / draft / unresolved | Required capabilities or constraints | Mapped systems or unresolved gap |
| --- | --- | --- | --- | --- |

[Account for every current specification; exclude archived predecessors from current authority. Note unversioned inputs explicitly.]

## Systems and responsibilities

| System | Responsibility | State owned | Ownership of reads, writes, and decisions | Governing specifications |
| --- | --- | --- | --- | --- |

## Relationships between specifications and systems

| Source specification/system | Related specification/system | Contract, dependency, shared constraint, or data/control flow | Enforcing owner | Supporting specification and decision status |
| --- | --- | --- | --- | --- |

[Map specifications to each other as well as to systems. Explain communication, interfaces, upstream/downstream dependencies, data/control/event flows, commands/resources/state crossing boundaries, external integrations, lifecycle relationships, and cross-system invariants with their enforcing authorities. Add a diagram if it makes the relationships clearer. Link SPECARC for concern-level design without replacing this whole-system map.]

## Coverage gaps, conflicts, and unresolved architecture

| Gap, conflict, or proposed decision | Affected specifications and systems | Status | Decision owner and required resolution |
| --- | --- | --- | --- |

Return missing decisions to the conversation or owning specification, then refresh this map. Include specification overlaps and unresolved integration questions. Do not claim complete coverage while consequential gaps remain. Check whether the architecture implied by the entire specification set forms a coherent whole.

After substantive SPEC or SPECARC creation/revision, review the complete current set and update this map when architecture, ownership, boundaries, dependencies, interfaces, flows, or cross-system behavior change. Report a review that needs no meaningful revision without mechanically incrementing its version. Preserve existing SYS records and project-specific precedence; ADRs support decision rationale without replacing specifications.

Follow this project's adopted document-versioning rules: keep the newer `systems.md` at its current path and archive the complete predecessor before replacement. Specification sequence IDs remain identities, not revisions.

An adopted Feature Map may link capability IDs to these system/specification owners and maintained verification scenarios. Keep it derived, inspect freshness, and retain this complete-set architecture review; do not duplicate rules or substitute capability coverage for specification coverage.
