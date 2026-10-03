# Systems map checklist

Use after formalizing accepted decisions into SPEC and/or SPECARC. Review one integrated `systems.md` at its established current path, creating it when the specification set supports a useful whole-system map. SPECARC defines an architectural concern and can precede the map; SPEC and SPECARC have no fixed ordering. Record an early deferral and its gaps rather than create a meaningless map.

- [ ] Inventory the complete current SPEC/SPECARC set or project-defined equivalents, including documents unchanged by the latest conversation. Distinguish accepted requirements, drafts, unresolved choices, and archives.
- [ ] Record each specification's stable ID/path, version (or unversioned status), decision status, and mapped systems. Account for each document; flag missing, conflicting, or unmapped requirements.
- [ ] Name the major systems and their responsibilities without detailing every operation.
- [ ] Map each specification to the systems needed to satisfy it; trace each system to supporting specifications.
- [ ] Map specifications to one another through shared contracts, constraints, and dependencies. Link architecture specifications for detail while keeping the whole-system map here.
- [ ] Identify governing specifications, responsibilities, state ownership, cross-boundary reads/writes, communication, and cross-system decisions.
- [ ] Show data, commands, events, resources, and state crossing boundaries, interfaces, upstream/downstream dependencies, external integrations, and lifecycle relationships.
- [ ] Identify invariants crossing boundaries and the owner that enforces each one.
- [ ] Separate accepted architecture from proposals, unresolved ownership, and implementation evidence.
- [ ] Trace the map to governing product rules and flag contradictions for the authority owner.
- [ ] Return missing decisions to the conversation or owning specification, then refresh the map. Do not silently settle them in `systems.md` or claim full coverage while consequential gaps remain.
- [ ] Identify overlaps and integration gaps and check whether the architecture implied by the entire specification set forms a coherent whole.
- [ ] After substantive SPEC or SPECARC creation/revision, review the complete set and update the map when architecture, ownership, boundaries, dependencies, interfaces, flows, or cross-system behavior change. Report a review that requires no meaningful change without bumping its version mechanically.
- [ ] For a substantive map revision, keep its ID and current path, record the new document version, and archive the complete predecessor under the project's [versioning rules](../../../docs/workflows/document_versioning.md).

The map describes the integrated architecture and relationships derived from the specifications. SPECARC defines concern-level architecture; ADR explains a specific decision and its rationale; SYS retains the adopting project's system-level documentation role. None is an automatic substitute for another or for `systems.md`.
