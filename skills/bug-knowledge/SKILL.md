---
name: bug-knowledge
description: Log a casually reported software bug as a durable record, investigate it using prior bug evidence, and distill recurring engineering lessons into knowledge references.
---

# Bug knowledge

Use when the user says to log or investigate a bug, update its record, or mine prior defects for reusable lessons. Follow the repository's own documentation rules; use the paths and family names below only when that project adopted this workflow.

## Intake

Accept a natural-language report without asking for an ID, severity, taxonomy, path, or formal reproduction. Search existing and legacy bug locations for duplicates and the highest `BUG_###`; allocate the next unused ID without reusing archived IDs. Create an individual record in `docs/engineering/bugs/` using [the bug template](assets/bug_record_template.md), populated only with known facts. Mark other fields `Unknown` or `Not yet investigated`. Ask a question only when missing information materially blocks understanding or distinguishing the defect.

Use evidence-based states such as Reported, Confirmed, In Progress, Verification, Closed, Deferred, Not Reproducible, and Not a Bug. Code changes alone do not close a bug; closure requires verification. Do not infer a root cause from symptoms.

## Investigation and repair

Before a repair, establish governing authority, inspect affected implementation and tests, and inspect relevant history. Search prior `BUG_###` records and engineering `REF_###` documents for materially similar failures. Prior records are evidence, not product authority. For an evidence-backed repair, follow `audit-repair`'s smallest-unit contract and three-failure stop rule.

Classify only when evidence supports it. Possible categories include state synchronization, authority boundary, validation, transactionality, concurrency, conversion, presentation, stale state, persistence, migration, API contract, type misuse, null handling, lifecycle sequencing, ownership, invariant, UI interaction, test gap, specification gap, and architecture.

## Knowledge mining

When multiple bugs establish a recurring underlying pattern, or one case establishes an unusually important reusable lesson, update an existing engineering reference or create a `REF_###` in `docs/engineering/knowledge/`. Use [the knowledge template](assets/knowledge_reference_template.md). Do not create one for every ordinary bug. If a lesson becomes a mandatory engineering requirement, promote it to the governing workflow, architecture, ADR, invariant, test strategy, or repository instruction. The knowledge base remains evidence and institutional memory.

Report the record ID and path, what is known versus unknown, any verification, and whether a knowledge reference changed.
