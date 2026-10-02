# True Specification — [product or system]

Status: Discussion / Accepted under the adopting project's process
Version: [v1 for a new document; next major/minor revision for an existing owner]
Previous version: [archive link, or none for a new document]
Change summary: [initial specification or substantive changes]
Decision owner: [named by the project]

Use the [True Spec worksheet](../../true-spec-worksheet/assets/true_spec_worksheet_template.md) when consequential product or architecture choices remain unresolved. The worksheet is a decision aid; this template records intent and accepted decision sources. Formalize an accepted architectural concern in sibling SPECARC where appropriate rather than treating this product-intent artifact as the mandatory first architecture design.

## Product intent and user experience

[What this is, for whom, and the experience it must provide.]

## Major rules and invariants

[What must always be true. Keep implementation mechanisms out of this layer.]

## Scope and exclusions

[What is inside, outside, and deliberately unspecified.]

## Decision register

| Topic | Statement or question | Status: accepted / proposal / unresolved | Decision owner or source |
| --- | --- | --- | --- |

## Supporting evidence

[Observations or implementation evidence that informed discussion; neither is automatically product authority.]

Only explicitly accepted product decisions move into the Canonical Specification. Do not convert unresolved questions or proposals into rules by rewriting them confidently.

Turn accepted decisions into SPEC and/or SPECARC in the order the design requires, then review the complete current set for `systems.md` integration. Create or update a useful map when architecture or relationships change; record early deferral when the available specifications cannot yet support meaningful integration. Return consequential gaps or conflicts to their decision owners. Follow [document versioning](../../../docs/workflows/document_versioning.md) for the specifications and map: keep newer revisions at their stable live paths and IDs, and archive the complete predecessor using its own version in filename form.
