# Systems map checklist

Use after formalizing the True Specification conversation and accepted decisions into specification documents. Create or update one integrated `systems.md` at its established current path. Architecture may have its own specification, but this map must take all current specifications into account and relate them to the whole architecture.

- [ ] Inventory all current specifications through the project's index and relevant functional directories, including architecture specifications and those unchanged by the latest conversation. Distinguish current documents from archives.
- [ ] Record each specification's stable ID/path, version (or unversioned status), decision status, and mapped systems. Account for each document; flag missing, conflicting, or unmapped requirements.
- [ ] Name the major systems and their responsibilities without detailing every operation.
- [ ] Map each specification to the systems needed to satisfy it; trace each system to supporting specifications.
- [ ] Map specifications to one another through shared contracts, constraints, and dependencies. Link architecture specifications for detail while keeping the whole-system map here.
- [ ] Assign ownership of writes, reads, and cross-system decisions.
- [ ] Show data, commands, events, resources, and state crossing boundaries, interfaces, upstream/downstream dependencies, external integrations, and lifecycle relationships.
- [ ] Identify invariants crossing boundaries and the owner that enforces each one.
- [ ] Separate accepted architecture from proposals, unresolved ownership, and implementation evidence.
- [ ] Trace the map to governing product rules and flag contradictions for the authority owner.
- [ ] Return missing decisions to the conversation or owning specification, then refresh the map. Do not silently settle them in `systems.md` or claim full coverage while consequential gaps remain.
- [ ] Identify overlaps and integration gaps and check whether the architecture implied by the entire specification set forms a coherent whole.
- [ ] Review and update the map in the same specification cycle whenever specifications materially change boundaries, ownership, dependencies, interfaces, or architecture. Report a review that requires no meaningful change without bumping its version mechanically.
- [ ] For a substantive map revision, keep its ID and current path, record the new document version, and archive the complete predecessor under the project's [versioning rules](../../../docs/workflows/document_versioning.md).

The map describes the integrated architecture and relationships derived from the specifications. Detailed behavior and architecture decisions can belong in specification documents; `systems.md` brings those documents together.
