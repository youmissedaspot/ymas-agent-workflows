---
name: spec-driven-development
description: Use for substantive product or system development when unresolved requirements, architecture, ownership, or increment boundaries need authoritative specification before implementation.
---

# Specification-driven development

Use this workflow to carry a consequential product or system change from intent to accepted implementation. For a narrow defect with established expected behavior, use `audit-repair`; routine maintenance, cosmetic edits, and work already specified at the needed level do not require the full specification path.

1. Read the adopting repository's instructions, authority hierarchy, and current context. Use its existing authoritative documents and names; this package supplies a [development method](../../docs/workflows/specification_driven_development.md), not product truth.
2. Settle only the relevant specification layers for the requested scope: product constitution, accepted canonical rules, system map, detailed system behavior, and increment scope. Label accepted decisions, proposals, open questions, and evidence. Escalate consequential product gaps to their owner instead of filling them in.
3. When useful, load only the needed aid: [True Specification template](assets/true_specification_template.md), [Canonical Specification template](assets/canonical_specification_template.md), [systems map checklist](references/systems_map_checklist.md), [detailed system template](assets/detailed_system_specification_template.md), or [increment checklist](references/increment_specification_checklist.md). Do not create every document for every task.
4. Once the relevant layers are sufficiently settled, inspect implementation, tests, schemas, interfaces, and explanatory Git history. Build an implementation plan from authority and repository reality, then use the [plan and adversarial review rubric](references/implementation_plan_review.md) when complexity warrants review. Return missing product decisions to the owning specification layer.
5. Implement in bounded units through the [agent execution loop](../../docs/workflows/agent_execution_loop.md) and [workbranch rule](../../docs/rules/multi_agent_workbranches.md). Verify actual behavior, repair narrowly, and keep the three-failure escalation boundary. Do not reinterpret product truth to simplify code.
6. Prepare [human acceptance guidance](references/human_acceptance_checklist.md) where the project reserves final acceptance to a human owner. Report agent verification and human acceptance separately.

When a downstream layer exposes an upstream error, correct the smallest authoritative unit, propagate its effects forward, and repeat affected review. Keep project-specific decisions in the adopting repository.
