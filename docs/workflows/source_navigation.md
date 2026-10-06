# Optional concept-to-source navigation

Version: v1

Use an existing index or systems map to offer task-relevant source paths before loading
full contents. For a larger corpus, an optional compact entity/concept directory can
connect accepted definitions, dependencies, decisions and current evidence. Adapt the
existing owner; do not duplicate specifications or require a graph for a small repository.

Research motivation: [Follow the Entities: A Corpus Map for Agentic Search, v1](https://arxiv.org/html/2609.37226v1),
September 29, 2026, links resolved entities to original documents. Table 8 reports
496.4k input tokens without candidate paths, versus 206.5k for raw search and 88.1k
with relevant entity-linked document paths in one tested setting. Additional direct
entity-to-entity edges enlarged pages 27–52% with little recall gain there. These results
motivate testing relevant entry points; they establish no YMAS savings or general graph
benefit. The following is a bounded workflow adaptation, not the paper's retrieval engine.

## Reuse the existing index

For a recurring concept, keep identity/type/owner and source-grounded observed aliases;
scope aliases to their evidence. Same names are not identity. Preserve separate records
when sources do not justify resolution, with unresolved candidates visible. A shared
source lineage is not independent corroboration. Do not merge an architectural concern
with a similarly named product rule or merge sibling specifications by title alone.

An optional entry in the existing index can use this shape:

| Stable concept / identity scope | Observed alias and source | Candidate source path/ID | Edition/hash and status | Relevance / authority / freshness |
| --- | --- | --- | --- | --- |
| Storage read contract / accepted specification | "Read access" in owning clause | Actual canonical source | Current edition/hash; accepted or provisional | Owning invariant; last checked against source |
| Storage read adapter / implementation | "Read access" in adapter comments | Actual implementation/test path | Exact source commit | Implementation evidence; distinct identity |

Use real repository paths at adoption, never copies of private project records in this
package. Link claims to original clauses and preserve original sources in their existing
homes. A directory entry is navigation/evidence, not new authority. Prefer concept-to-source
links; add direct concept relationships only for a demonstrated retrieval need already
grounded in specifications. Do not import universal domain names or entity taxonomies.

## Select candidates, then inspect

Start with the request, governing owner and affected boundary. Offer a small relevant set
of source paths/IDs with why each matters: owning accepted rule, dependent interface,
decision qualification, caller/test and current receipt. Preserve ambiguous alternatives.
Inspect full relevant clauses and consequential dependencies; candidate paths do not
authorize omitting whole-set review or settle conflicts. A poor or stale directory falls
back to authorized source search. Documents without an entry remain discoverable.

Check source editions/hashes, accepted status, renamed/deleted paths and access at use.
When a source changes, invalidate affected summaries/aliases/candidate links until
reconciled; record retirement rather than keeping a deleted source's claims current.
Respect current access revocation: do not retrieve or repeat revoked content from stale
cached summaries, expose forbidden paths via a directory, or request broader persistent
access to keep it alive. Use only authorized current sources and report the coverage gap.
Local read-only diagnostics help find missing paths; they do not implement remote ACLs.

Compare candidate-assisted retrieval with the current index on matched authorized tasks:
relevant source/dependency coverage, wrong identity merges, stale authority, unavailable
sources, reader effort and supported aggregate usage. Include ambiguous names, irrelevant
starters and changed/revoked sources as negative cases. Preserve full source access within
existing permissions and stop decisions; efficiency alone is insufficient acceptance.
Automatic extraction/ranking, graph construction, sync and permission-aware serving are
deferred. This package adds no service, collector, external publication or mandatory index.
