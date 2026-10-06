# Implementation plan and adversarial review

Use when the relevant specification layers are settled enough to plan. Apply the review depth to the change's complexity; a narrow, already specified edit does not need a ceremonial review.

## Plan contract

- Link governing SPEC/SPECARC, integrated systems map, and established product, system, and increment sources as applicable. Mark unresolved decisions instead of silently choosing them.
- Name affected components, ownership boundaries, implementation order, interfaces, migrations, and integration points.
- Identify affected capability IDs, accepted-source assertions, reachable entrypoints, dependencies/neighbors and maintained scenario/tool/evidence. Use the [Feature Map](../../../docs/workflows/feature_maps.md) where adopted; record gaps and scoped freshness updates.
- State tests and other verification, failure risks, justified compatibility needs, and explicit exclusions.
- Compare current code, tests, schemas, and relevant history with the governing specifications. Treat those observations as evidence.

## Adversarial review

Challenge the plan for missing requirements, contradictory authority, hidden coupling, ownership violations, incorrect assumptions, migration and failure gaps, edge cases, concurrency, security, inadequate tests, uncontrolled fixtures, unsafe seed/reset/cleanup, command descriptors mistaken for permission, maps overriding requirements, stale provenance, planning labels leaking into production, unnecessary compatibility machinery, and work assigned to the wrong system.

Record each finding with its source and status: verified gap, inference, proposal, or unresolved question. Route missing product rules to the appropriate specification owner. A reviewer may reject or request revision of a plan but may not invent accepted product behavior.

Outcome: ready for bounded implementation / revise the plan / return to a specification layer / await an authority decision. Rerun affected review after a material upstream correction.
