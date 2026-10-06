# Workbranch isolation

Version: v2
Previous version: [v1](../archive/rules/multi_agent_workbranches_v1.md)
Change summary: Reconcile exact source receipts and document reservations before integration.

For substantive repository modification, **one active agent task = one isolated workbranch**. This rule applies even when only one agent is currently writing, so another agent can work without sharing its writable branch. Multiple agents must never make substantive writes on the same branch concurrently.

Before writing, inspect the current branch, working-tree status, whether the intended branch exists, ownership of uncommitted work, and relevant divergence from the integration branch. Treat unexpected changes as potentially belonging to the user or another agent. Do not discard, overwrite, reset, stash, or absorb unexplained work to clear the tree.

Create or use a dedicated branch such as `work/<task-slug>`; add an agent or task discriminator when names could collide, such as `work/<agent-or-task-id>/<task-slug>`. One active task owns its branch. Do not write directly on `main` or another protected integration branch unless explicitly authorized. Do not silently switch into or modify another active task's branch, rewrite another agent's branch history without an explicit task, mix unrelated changes, or share a writable branch across worktrees. Keep commits scoped to the task. Planning terms in branch names do not authorize planning-derived names in durable production code.

Before integration, reconcile live candidate commit/tree, tested and reviewed source, finding dispositions and authorization through a [source receipt](../workflows/source_receipts.md). Blocked, superseded or nonmatching candidates stop. Coordinate permanent document-ID reservations and recheck collisions across active workers. A passing diagnostic grants no merge authority.

Before integration, finish and verify the branch, update required durable records, ensure its contents are coherent, and report the changes and checks. Integrate only through the adopting repository's established process. Unless that repository explicitly authorizes it, multiple agents must not independently merge into `main`. If no integration rule exists, leave the verified branch for the controlling user or designated integration agent to review and integrate. A workbranch is an execution boundary, not product authority; surface conflicts with repository-specific Git governance and follow that repository's governing rule.
