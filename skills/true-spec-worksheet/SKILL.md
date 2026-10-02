---
name: true-spec-worksheet
description: Prepare a structured decision worksheet for a requested idea, product behavior, or architecture concern with consequential unresolved choices before formal specification. Use existing authority to avoid reopening settled decisions; do not write final specifications or implementation plans.
---

# True Specification worksheet

Prepare a useful decision aid for the subject established by the user or conversation. Inspect the repository's instructions, authority hierarchy, index, relevant current product and system specifications, architecture specifications, existing systems map, operational context, and accepted decisions before generating questions. Read only the material relevant to the subject. Missing specifications or a missing map do not force a new project to invent architecture or block independent discovery.

Record settled decisions with their actual sources and owners. Do not reopen them without a changed requirement, demonstrated conflict, or explicit request. Separate governing authority and accepted decisions from facts, implementation evidence, observations, inference, proposals, recommendations, and unresolved questions. Surface conflicting authoritative sources and the owner who must resolve them; do not silently choose a winner.

For each consequential unresolved product or architecture topic, prefer:

**Question → recommendation → reasoning → meaningful alternatives → downstream consequences → decision**

Order questions by dependency so upstream choices precede dependent ones. Include a recommendation when supported and useful, explaining its assumptions and tradeoffs. Alternatives should expose real choices, not fill a quota. Describe consequences for product behavior, ownership, architecture, interfaces, other specifications, or acceptance where they matter. Do not ask questions whose answers follow from existing authority or treat routine implementation choices as new product decisions. Mark genuinely undefined consequential choices for the project's human decision owner. If no consequential choices remain, report that result and identify the specification stage rather than manufacturing questions.

Use the [worksheet template](assets/true_spec_worksheet_template.md) when helpful. Finish with decision capture: each choice, its status, owner, acceptance source, affected subjects, dependencies, and remaining gaps. Only explicit acceptance through the project's process can mark a decision accepted; recommendations, preselected options, silence, and worksheet completion do not establish approval.

Return the worksheet in conversation by default. If saving is requested, use the project's provisional design location and naming/version rules, such as its adopted `OPS_SPECDEF` family; do not impose YMAS on an unrelated repository. The worksheet remains non-authoritative source material even after it records accepted decisions. Keep the actual acceptance sources traceable.

Stop at the worksheet and decision capture. Do not write final SPEC or SPECARC documents, update `systems.md`, or implement work under this skill. Once the user requests formalization of settled decisions, normal routing can use [spec-driven-development](../spec-driven-development/SKILL.md); use [the development method](../../docs/workflows/specification_driven_development.md) for the broader lifecycle.
