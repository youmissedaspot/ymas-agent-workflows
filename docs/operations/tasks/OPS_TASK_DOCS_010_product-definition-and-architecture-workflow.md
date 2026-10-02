# OPS_TASK_010 — Product definition and architecture workflow

Status: Complete
Version: v1
Branch: `work/product-definition-architecture`
Base: `2da6f33`, the specification handoff/versioning work from PR #8. PR #8 was merged externally while this task was running; this task does not merge or publish its own branch.
Scope: The user's October 2, 2026 workflow-evolution request, informed by the “Correct Specification Workflow” conversation. SPECARC is the accepted architecture-specification family name.

## Resulting behavior

**Discuss → True Spec Worksheet → Decide → SPEC and/or SPECARC → systems.md → Plan → Implement → Verify → Human Acceptance where applicable**

`workflow-orientation` explains how to begin or resume YMAS, the artifacts, and useful natural-language prompts. It ends after orientation, without executing discovery, specifications, plans, adoption, or implementation. `/start` remains a temporary conversational label, not a registered slash-command alias.

`true-spec-worksheet` inspects existing authority and accepted decisions, then prepares consequential product or architecture questions in dependency order. Each topic can contain a recommendation, reasoning, meaningful alternatives, downstream consequences, and a decision. It avoids reopening settled decisions without cause and ends in decision capture with explicit sources and owners. It remains provisional source material and does not write final specifications, update the map, or implement work.

SPEC defines required product/system behavior; SPECARC defines accepted architecture for a durable concern. These are sibling specification types with no fixed design order or automatic precedence. ADR records a particular architecture decision and its context/rationale. SYS retains its adopted system-level documentation role. `systems.md` integrates the complete current specification set, including both sibling types, into one architecture/system map. The adopting project owns approval and authority. An early incomplete specification set need not invent a meaningless map; a useful existing map must be reviewed and updated for affected architecture, ownership, boundaries, dependencies, interfaces, flows, or cross-system behavior.

Document IDs remain family-wide identities. Metadata uses `Version: v3.1`; filenames use `v3dot1`. A successor such as `v3.2` stays at the same live path and ID while the complete old v3.1 is archived as `_v3dot1.md`, marked historical, and linked to its owner. The workflow standard and specification method advance from v2 to v3, with complete v2 archives; the compatible version-notation correction advances the versioning procedure from v1 to v1.1, with its complete v1 archived.

The package is prepared as candidate `0.4.0` with eight skills. The marketplace identity and source remain unchanged. No release tag, branch publication, or merge is performed here.

## Files added relative to the task base

- [Orientation skill](../../../skills/workflow-orientation/SKILL.md).
- [Worksheet skill](../../../skills/true-spec-worksheet/SKILL.md).
- [Worksheet template](../../../skills/true-spec-worksheet/assets/true_spec_worksheet_template.md).
- [SPECARC template](../../../skills/spec-driven-development/assets/architecture_specification_template.md).
- [Documentation-standard v2 archive](../../archive/OPS_WORKFLOW_001_documentation_standard_v2.md).
- [Specification-workflow v2 archive](../../archive/workflows/specification_driven_development_v2.md).
- [Document-versioning v1 archive](../../archive/workflows/document_versioning_v1.md).
- This task record.

## Files modified relative to the task base

- [INDEX](../../../INDEX.md) and [README](../../../README.md).
- [Documentation standard](../../OPS_WORKFLOW_001_documentation_standard.md).
- [Specification method](../../workflows/specification_driven_development.md) and [document versioning](../../workflows/document_versioning.md).
- [Plugin manifest](../../../plugin.json) and [installation smoke contract](../../../scripts/smoke_install.py).
- [Bootstrap skill](../../../skills/project-bootstrap/SKILL.md) and [documentation template](../../../skills/project-bootstrap/assets/documentation_standard_template.md).
- [Consolidation skill](../../../skills/documentation-consolidation/SKILL.md).
- [Specification skill](../../../skills/spec-driven-development/SKILL.md).
- [True Specification template](../../../skills/spec-driven-development/assets/true_specification_template.md), [canonical SPEC template](../../../skills/spec-driven-development/assets/canonical_specification_template.md), [detailed system template](../../../skills/spec-driven-development/assets/detailed_system_specification_template.md), and [systems map template](../../../skills/spec-driven-development/assets/systems_map_template.md).
- [Systems map checklist](../../../skills/spec-driven-development/references/systems_map_checklist.md), [increment checklist](../../../skills/spec-driven-development/references/increment_specification_checklist.md), and [plan review rubric](../../../skills/spec-driven-development/references/implementation_plan_review.md).

## Verification and adversarial review

All eight skills passed the skill-creator front-matter/scaffold validation using Python UTF-8 mode on Windows. The first orientation check encountered a Windows default-codepage decoding error on typographic quotes; the UTF-8 rerun passed without changing the valid source. Final package validation passed for eight skills, 44 Markdown files, 135 Markdown links, index routes, manifest schema, and marketplace identity. The existing link-containment regression test passed. Installation checks using Windows Codex CLI `0.159.1` passed candidate fresh/repeated installation and removal/reinstallation; the final candidate rerun validated the same eight-skill/44-file/135-link package. Published-source checks passed installation, marketplace refresh, and removal/reinstallation for the existing six-skill release. Disposable Codex homes were used; the user's installed plugin and home were not changed.

Compared all three new archives against their exact branch-start Git documents after normalizing relative-link destinations. Complete predecessor content, qualifications, and original link targets were preserved; only historical notices and required rebasing were added.

An independent read-only behavioral simulation covered existing-project orientation, an event-reconciliation worksheet with accepted authority and an unaccepted operational proposal, and a compatible SPECARC v3.1 → v3.2 revision before surrounding specifications are complete. It found no actionable contract defect. This is simulated behavior under the instructions, not proof of automatic client selection or a live product acceptance run.

The final adversarial review checked all twelve requested risks: SPECARC versus ADR and SYS; architecture before the integrated map; worksheet authority; orientation scope; IDs versus versions and preserved identity; old and new revision locations; dotted metadata versus dot-encoded filenames; existing-project resumption; and narrow-task bypasses. Two older specification-template sentences still implied mandatory early map creation; those were corrected to the useful-map rule. Implementation planning, adversarial review, workbranch isolation, operational memory, smallest repair, three-failure escalation, verification, and project-controlled human acceptance remain in place.

Final package/link and whitespace checks passed. A comparison against the task base confirmed the complete transition-to-implementation section and existing execution-loop, workbranch, repair, bug, and human-acceptance contracts were preserved. No unresolved documentation-contract decision requires human resolution. Desktop discovery, automatic selection, and cross-platform candidate CI are not established by these Windows package checks.
