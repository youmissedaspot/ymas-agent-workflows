---
name: audit-repair
description: Audit repository behavior against its governing requirements and make evidence-backed, narrowly scoped repairs when an audit or verification identifies a defect.
---

# Audit and repair

Use when asked to audit, investigate a failed verification, or repair a demonstrated defect. For initial bug intake and durable bug records, use `bug-knowledge`.

1. Bootstrap into the repository: read applicable instructions, governing authority, current context, affected implementation and tests. Treat documented requirements and inferred expectations separately. Inspect relevant Git history when a behavior's purpose is non-obvious.
2. Report findings with precise evidence, affected boundary, and severity where supported. Do not create a requirement from a surprising observation alone.
3. Before editing after a verified failure, state the failed unit, expected behavior, observed behavior, evidence, allowed repair scope, and boundaries to preserve.
4. Repair the smallest unit that explains the failure. Keep neighboring correct behavior intact; avoid unrelated cleanup.
5. Rerun the relevant verification and report actual results. If the same narrowly scoped unit fails three repair attempts, stop patching and reconsider specification interpretation, task decomposition, authority, architecture, and implementation strategy before a fourth attempt.

In the completion report, distinguish what was implemented, what was verified, tests run, observed results, and any remaining manual acceptance. Compilation or green unit tests establish only what they actually cover.
