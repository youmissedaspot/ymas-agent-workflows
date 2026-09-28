# Systems map checklist

Use after the relevant product rules are accepted. Map existing authoritative architecture where it exists; do not create a parallel authority merely to fill this checklist.

- [ ] Name the major systems and their responsibilities without detailing every operation.
- [ ] Assign ownership of writes, reads, and cross-system decisions.
- [ ] Show data and control flows, interfaces, dependencies, external integrations, and lifecycle relationships.
- [ ] Identify invariants crossing boundaries and the owner that enforces each one.
- [ ] Separate accepted architecture from proposals, unresolved ownership, and implementation evidence.
- [ ] Trace the map to governing product rules and flag contradictions for the authority owner.

The map describes major structure and authority. Detailed behavior belongs in system specifications.
