# Repository instructions

Follow `docs/OPS_WORKFLOW_001_documentation_standard.md` for documentation structure, IDs, project memory, authority, archival rules, and document creation.

Consult `INDEX.md` before broad repository documentation searches and load only the smallest relevant workflow and reference files.

For substantive work, follow the [agent execution loop](docs/workflows/agent_execution_loop.md) through verification, required durable updates, and completion even when the prompt states only an outcome. For repository writes, follow [workbranch isolation](docs/rules/multi_agent_workbranches.md): one active task per isolated branch, and preserve unexplained work.

For substantive product or system work with unresolved requirements, architecture, or authority boundaries, use `spec-driven-development` before implementation. Keep narrow, well-specified defect repairs in `audit-repair`.

This repository distributes reusable engineering workflows. Keep product rules and project-specific authority in the adopting repository; its governing authority takes precedence over shared procedures. The portable plugin manifest is the package contract; each `SKILL.md` is the behavioral contract for its workflow. Prefer small, focused edits and validate changed skills and packaging before release.
