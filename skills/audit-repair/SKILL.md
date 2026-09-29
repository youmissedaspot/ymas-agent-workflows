---
name: audit-repair
description: Audit, investigate, or repair a target supplied by the user's request or clearly established conversation, using governing requirements and evidence. Do not choose a target from repository state; a bare invocation without a conversational target requires asking for scope.
---

# Audit and repair

Use when asked to audit, investigate a failed verification, or repair a demonstrated defect. For initial bug intake and durable bug records, use `bug-knowledge`.

## Target Selection Rule

`audit-repair` requires an audit or repair target supplied by the user's current request or clearly established conversational context.

Repository artifacts may help **scope and understand** that target, but they must not independently create it.

Do not select an audit target merely because it appears in:

- `OPS_NEXT_###`
- `OPS_STATE_###`
- latest task records
- open bug records
- failing tests
- recent commits
- TODOs
- backlog items
- roadmap documents
- other repository state

A bare invocation such as:

`$audit-repair`

with no clear current conversational target must not trigger an autonomous repository audit.

If no target can be established from the user's request or current conversation, ask for the target or scope.

Good inference:

The user says:

> The shipbuilding integration evidence looks incomplete.

and then invokes:

`$audit-repair`

The skill may use shipbuilding as the target.

Not allowed:

The user invokes:

`$audit-repair`

with no task context, and the agent selects the highest `OPS_NEXT_###` or another repository artifact as the audit target.

Repository state is evidence and context, not user intent.

## Workflow

1. Bootstrap into the repository: read applicable instructions, governing authority, current context, affected implementation and tests. Treat documented requirements and inferred expectations separately. Inspect relevant Git history when a behavior's purpose is non-obvious.
2. Report findings with precise evidence, affected boundary, and severity where supported. Do not create a requirement from a surprising observation alone.
3. Before editing after a verified failure, state the failed unit, expected behavior, observed behavior, evidence, allowed repair scope, and boundaries to preserve.
4. Repair the smallest unit that explains the failure. Keep neighboring correct behavior intact; avoid unrelated cleanup.
5. Rerun the relevant verification and report actual results. If the same narrowly scoped unit fails three repair attempts, stop patching and reconsider specification interpretation, task decomposition, authority, architecture, and implementation strategy before a fourth attempt.

In the completion report, distinguish what was implemented, what was verified, tests run, observed results, and any remaining manual acceptance. Compilation or green unit tests establish only what they actually cover.
