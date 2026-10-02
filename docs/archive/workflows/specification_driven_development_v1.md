> Status: Historical — superseded; not current authority.
> Document version: v1 (assigned to the previously unversioned baseline).
> Superseded by: v2 at the [current document](../../workflows/specification_driven_development.md).
> The original text follows; embedded status statements describe that historical revision.

# Specification-driven development

Use these layers for substantive product or system changes when important rules, boundaries, or staged scope remain unresolved. They are roles, not prescribed filenames or automatic authority in an adopting repository. Map them to that repository's governing documents, scale them to the change, and preserve its product authority. A small, well-defined task need not create every layer.

## Specification hierarchy

| Layer | Question it owns | Boundary |
| --- | --- | --- |
| **1. True Specification** | What is the product or system meant to be for its users? State intended experience, major rules, fundamental invariants, scope, exclusions, and unresolved decisions. | Product constitution under discussion and explicit acceptance; no implementation design. |
| **2. Canonical Specification** | Which accepted product decisions are durable authority? Formalize them with unambiguous language and stable terminology; separate settled rules from open questions. | Do not invent decisions while formalizing or let conversational notes silently become authority. |
| **3. Systems Architecture / Map** | What major systems exist, who owns responsibilities and reads/writes, and how do data, control, interfaces, dependencies, integrations, and lifecycles cross boundaries? | Major structure and authority, not each system's detailed behavior. |
| **4. Detailed System Specifications** | How does each system behave? Define relevant invariants, inputs/outputs, states, ownership, APIs and read models, edge cases, failures, concurrency, persistence, migrations, observability, security, validation, verification, and acceptance cases. | System behavior, not an increment schedule. |
| **5. Milestone / Increment Specifications** | Which subset of already specified systems is in this increment? Reference higher authority, dependencies, entry/exit conditions, deferrals, and acceptance criteria. | Scope selection only; never redefine product or system truth. Planning labels stay in plans and history, not durable production names. |

Discussion and acceptance settle the True Specification before canonical formalization. The adopting repository determines the actual approval mechanism and precedence. If authority is silent or contradictory on a consequential choice, surface it to the owner; lower layers and implementation plans cannot supply missing product rules.

In every layer, label the governing authority, accepted decisions, unresolved questions, proposals, recommendations, implementation evidence, and verification results when they appear. Evidence and recommendations do not become product truth without the project's acceptance process.

## Transition to implementation

6. **Inspect repository reality.** After the relevant specification layers are sufficiently settled, inspect current architecture, implementation, tests, schemas, interfaces, and unusual behavior's relevant Git history. Compare them with authority; history and code are evidence, not product authority. Earlier exploratory inspection may inform design without silently settling requirements.
7. **Plan.** Translate the specifications into affected components, order, ownership boundaries, migrations, tests, risks, integration points, justified compatibility needs, and exclusions. If this exposes a product gap, return to its specification owner.
8. **Review adversarially when complexity warrants.** Challenge the plan for missing requirements, contradictions, authority violations, hidden coupling, incorrect ownership, failure and concurrency gaps, migrations, security, tests, naming leaks, unjustified compatibility, and divergence from intent. A reviewer may identify gaps, not invent product decisions. Use the [plan review rubric](../../../skills/spec-driven-development/references/implementation_plan_review.md).
9. **Implement and verify.** Use bounded units, the [execution loop](../../workflows/agent_execution_loop.md), and isolated workbranches. Inspect before editing, verify each meaningful unit, repair the smallest failed unit, and reassess after three failures on that unit. Never relax accepted product rules merely because implementation is difficult.
10. **Prepare human acceptance.** Agent tests, code review, logs, schemas, and API exercises provide verification evidence. Where the project reserves final product acceptance to a human owner, prepare a concise [manual checklist](../../../skills/spec-driven-development/references/human_acceptance_checklist.md) and leave sign-off to that owner unless the repository establishes another authority model.

If detailed design or planning reveals an earlier error, repair the smallest incorrect authoritative unit, propagate the correction to dependent layers, and rerun affected review. Do not rewrite unrelated settled work or force progress through a known bad assumption.
