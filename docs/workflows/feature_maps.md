# Derived Feature Maps

Version: v1

A **Feature Map** is compact repository-owned operational knowledge about user-visible
and system-visible capabilities. It helps an agent find governing clauses, actual
entrypoints, prerequisites, dependencies, implementation and verification without
rediscovering them from conversation. Reuse an existing structured owner where possible;
adopt the [JSON schema](../../skills/spec-driven-development/assets/feature_map.schema.json)
when useful. The [empty template](../../skills/spec-driven-development/assets/feature_map_template.json)
declares no coverage. Populate only the needed scope; the
[self-contained neutral example](../../skills/spec-driven-development/assets/feature_map_example/feature_map.json)
and its maintained executable illustrate the shape without supplying product rules.

## Provenance and authority

Canonical accepted requirements → implementation → derived feature/system maps →
verification scenarios/tools → runtime evidence describes **derivation**, not automatic
authority transfer. Requirements govern expected behavior directly. Implementation may
be defective; maps must preserve that discrepancy rather than redefine requirements.
Scenarios trace assertions to governing clauses, not merely to existing code behavior.
Recorded acceptance/status is a claim with provenance, not authentication of acceptance.

Follow the adopting repository's actual authority and approval process. SPEC and SPECARC
remain siblings. The complete current specification-set review and integrated
`systems.md` remain intact; a capability map does not replace either or become another
architecture authority. Link architectural/system owners instead of copying their rules.
Keep proposals, observations, unknown authority and unresolved relationships visible.
Return consequential conflicts to their owners and stop only dependent work.

The repository holds durable contracts, maps, tools and evidence references. Task context
is a scoped projection of them; conversations are source material, not a substitute for
accepted repository authority. See [source navigation](source_navigation.md),
[task context](task_context.md) and [source receipts](source_receipts.md).

## Compact representation and typed edges

Schema version identifies the data contract; document version identifies the map's
edition under the local versioning rules. IDs use enduring domain terms, scoped by
`map_id`; retain identity across revisions and preserve retirement/history. Never put
roadmap, release, milestone or other planning labels into feature IDs, APIs, modules,
types or verification commands. Do not require a universal application taxonomy.

| Record | Information retained |
| --- | --- |
| Coverage | Actual scope and omissions; an empty or partial map does not claim completeness |
| Source | Stable ID, role, repository-relative path, relevant locator, raw SHA256, status and acceptance provenance |
| Feature | Stable ID, purpose, observed/planned/partial/retired status, user/system entrypoints, prerequisites, gotchas and limits |
| Scenario | Known-state setup, exercise, accepted-source expectations, required evidence, cleanup, readiness and limits |
| Tool | Maintained source, illustrative argv, capabilities, effects, approved target description, preview and limits |
| Relation | Explicit endpoints, type, specified/observed/unresolved basis and supporting source IDs |

Store subfeatures and dependencies in the relation list instead of parallel prose-only
registers. Relationships are: `contains` (feature → feature), `depends_on` (feature →
feature), `governed_by` (feature → requirement/architecture source), `implemented_by`
(feature → implementation/tool source), `verified_by` (feature → scenario), and
`uses_tool` (scenario → tool). `contains` must be acyclic; dependency cycles need
architectural interpretation rather than automatic deletion. Source-linked edges serve
the demonstrated impact/verification need, not speculative graph construction.

Command descriptors are **data**. The checker never invokes them, mutates targets,
authenticates acceptance, follows remote references or grants permissions. Exact commands
and capabilities are repository-specific. Destructive tools should expose preview where
practical and retain approval/ownership checks in the actual executable. Tool availability,
error handling and authorization must still be checked before use. Missing accepted
authority blocks a ready scenario. Unsupported scenarios remain limits, not passes.

Typed nodes/edges can be exported as JSON without parsing prose. Consumers must preserve
map scope, provenance, source status, coverage and evidence limits. This is a generic graph
format; no Graphify dependency, adapter, identity merger or serving system is included.
The initial checker handles explicit local source files only. Record remote/omitted
contracts as coverage gaps and use authorized original sources; do not claim they were
checked or cache revoked content to fill the gap.

## Event-driven maintenance and drift inspection

After a relevant feature change, inspect the affected entrypoints, clauses and map entries.
After controllability/verification changes, update the affected tool/scenario and its tests.
After dependency changes, inspect explicit edges and reverse dependents as candidate
neighbors, then derive actual affected callers from implementation. Maps are navigation,
not proof of exhaustive reachability; fall back to source inspection when incomplete.

The [read-only checker](../../scripts/check_feature_map.py) offers:

```text
python scripts/check_feature_map.py validate <map.json>
python scripts/check_feature_map.py check <map.json> --repo <authorized-root>
python scripts/check_feature_map.py graph <map.json> --repo <authorized-root>
```

`validate` checks structure, stable identities, typed references and declared constraints.
`check` additionally compares raw bytes for every declared source inside the explicit root;
metadata/frontmatter and line-ending changes count. `graph` requires those checks to pass
and returns deterministic typed nodes/edges. JSON findings include corrective action;
failures exit nonzero. No files are written. Python 3.12 and the package's existing
`jsonschema` development dependency are required for this optional checker.

The verdict states scope and separates structure/freshness from semantics. Matching hashes
prove only that declared inputs match recorded bytes at inspection time. They do not prove
complete coverage, correct clauses, valid acceptance, executable availability or runtime
behavior. Path checks reject traversal, absolute paths and symlink sources/parents; they
are snapshot diagnostics, not an OS sandbox or lock against concurrent filesystem changes.

For a changed/missing source, follow its IDs to affected features, relations and scenarios,
read the original authority/implementation, and classify the drift. Update only reconciled
hashes and meaningful semantic changes; never bless current hashes without inspection.
An unchanged meaning can require only provenance refresh, with that conclusion recorded
in the task receipt. A byte-only change does not force unrelated map/document revisions.
Preserve the adopted version/history rules for substantive map changes. Do not blindly
regenerate every day or rewrite unaffected entries. For a requested audit, use the existing
audit scope, failure classification and smallest-unit repair rules; drift findings do not
authorize unrelated repair or a new audit target.

## Design check for an affected feature

| Agent question | Source to inspect |
| --- | --- |
| What feature changes? | Stable feature ID, purpose and coverage |
| What requirements govern it? | `governed_by` source clauses and actual acceptance |
| What does it depend on? | `depends_on`, prerequisites and original contracts |
| How is it reached? | User/system entrypoints and inspected implementation |
| What deterministic tool exercises it? | Scenario `uses_tool`, executable source and preflight |
| Which scenario proves behavior? | `verified_by` and accepted-source expectations |
| What evidence is needed? | Scenario capture instructions and exact-source receipt |
| Which neighbors may change? | Reverse dependencies/containment plus actual callers |
| Is the map still accurate? | Raw-hash check and scoped semantic inspection |
| Can relationships be exported? | Explicit typed nodes/edges, with coverage/provenance intact |

Missing answers are explicit gaps to resolve or defer under the governing process; neither
a schema pass nor a graph export completes verification. Follow
[maintained boundary verification](verification_boundaries.md) for actual behavior,
required independent/adversarial review, narrow repair, the three-failure planning
escalation and separate human acceptance.
