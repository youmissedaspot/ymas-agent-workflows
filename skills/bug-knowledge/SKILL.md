---
name: bug-knowledge
description: Log a casually reported software bug as a durable record, investigate it using prior bug evidence, and distill recurring engineering lessons into knowledge references.
---

# Bug knowledge

Use when the user says to log or investigate a bug, update its record, or mine prior defects for reusable lessons. Follow the repository's own documentation rules; use the paths and family names below only when that project adopted this workflow.

## Intake

Accept a natural-language report without asking for an ID, severity, taxonomy, path, or formal reproduction. Search current, archived, and legacy bug locations across all Level 2 categories for duplicates and the highest `BUG` family ID; allocate the next unused three-digit ID without reusing archived IDs.

Inspect the adopting repository's Level 2 vocabulary and established context, then reuse its canonical token for the bug's durable area. Name a new record `BUG_<L2_CATEGORY>_<ID>_<l3-description>.md` in its adopted bug directory, using [the bug template](assets/bug_record_template.md). Use hyphens inside the lowercase final description and underscores only between structural segments. Reuse the same Level 2 token that tasks, audits, or references use for that area, so `_<L2_CATEGORY>_` retrieves them together. Do not invent a synonym or infer product taxonomy from symptoms or roadmap labels. If classification is genuinely unresolved, follow the project's documented fallback or mark it unresolved and seek the governing category decision before naming a file; do not require the reporter to supply taxonomy. Populate only known facts and mark other fields `Unknown` or `Not yet investigated`. Ask a question only when missing information materially blocks understanding or distinguishing the defect.

Use evidence-based states such as Reported, Confirmed, In Progress, Verification, Closed, Deferred, Not Reproducible, and Not a Bug. Code changes alone do not close a bug; closure requires verification. Do not infer a root cause from symptoms.

## Investigation and repair

Before a repair, establish governing authority, inspect affected implementation and tests, and inspect relevant history. Search prior `BUG` records and engineering `REF` documents for materially similar failures. Prior records are evidence, not product authority. For an evidence-backed repair, follow `audit-repair`'s smallest-unit contract and three-failure stop rule.

Classify failure mechanisms only when evidence supports them; this classification is separate from the filename's Level 2 area. Possible mechanisms include state synchronization, authority boundary, validation, transactionality, concurrency, conversion, presentation, stale state, persistence, migration, API contract, type misuse, null handling, lifecycle sequencing, ownership, invariant, UI interaction, test gap, specification gap, and architecture.

## Knowledge mining

When multiple bugs establish a recurring underlying pattern, or one case establishes an unusually important reusable lesson, update an existing engineering reference or create `REF_<L2_CATEGORY>_<ID>_<l3-description>.md` in the adopted engineering knowledge directory. Use the same canonical Level 2 token as other families for that domain, without reference-only synonyms, and the next family-wide `REF` ID across all categories and legacy locations; use [the knowledge template](assets/knowledge_reference_template.md). Do not create one for every ordinary bug. If a lesson becomes a mandatory engineering requirement, promote it to the governing workflow, architecture, ADR, invariant, test strategy, or repository instruction. The knowledge base remains evidence and institutional memory.

Report the record ID and path, what is known versus unknown, any verification, and whether a knowledge reference changed.
