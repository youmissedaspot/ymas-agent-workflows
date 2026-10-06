---
name: workflow-orientation
description: Explain how to begin or resume work with YMAS when a user asks how the workflow works or where to start. Orientation only; do not execute development or replace an actual work request with onboarding.
---

# Getting started with YMAS

YMAS helps turn an idea or consequential change into accepted definitions, coherent architecture, and verified implementation under the project's own authority. This skill explains how to use that process; it does not run it.

Read the repository's instructions and index when available, then inspect only enough current authority and operational context to identify a useful starting stage. An existing project resumes from its settled decisions, specifications, or implementation; it does not restart discovery. If no project is available, give general orientation without inventing its state or creating a repository.

Give a short explanation of the lifecycle:

**Discuss → True Spec worksheet → Decide → SPEC / SPECARC → systems.md → Plan → Implement → Verify → Human Acceptance where applicable**

Explain the principal artifacts:

- **True Spec worksheet:** a structured aid for exploring consequential questions and capturing decisions; not product authority.
- **SPEC:** an accepted specification of what must be true for a product or system.
- **SPECARC:** an accepted architecture specification for a defined concern. SPEC and SPECARC are siblings and can be developed in either order.
- **systems.md:** the integrated architecture/system map derived from the complete current specification set, once that set supports a useful map.

Users can describe work naturally; they do not need to memorize skill names, IDs, or filing rules. Small or already-specified work skips unnecessary stages. The agent follows normal routing when actual work begins. Offer a relevant next prompt from examples such as:

- “I have an idea for an economic simulation.”
- “Help me figure out how shipping contracts should work.”
- “We need to define the architecture for event reconciliation.”
- “These decisions are settled; turn them into specifications.”
- “Update the architecture map from the current specifications.”

Use the [workflow index](../../INDEX.md) to explain the relevant next stage. End after orientation. Do not generate a decision worksheet, settle product choices, write specifications, adopt documentation rules, make a plan, or implement changes as part of this skill. `/start` is a temporary conversational label, not a registered command alias; the packaged skill name is `workflow-orientation`.

Use [human explanation and editorial judgment](../../docs/workflows/human_understanding.md) for readable explanations and documentation. Consider ordinary documentation purposes only where useful; do not reclassify canonical specifications or infer migration authority from editorial guidance.
