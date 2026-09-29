# OPS_TASK_004 — Package validation and installation smoke test

Status: Complete on `work/package-validation-and-release-records`; integration pending.

Added a repeatable package check for the portable manifest, marketplace identity, all skill front matter, index routes, local Markdown links, and license. GitHub Actions runs the same check on pushes and pull requests. The validator downloads the manifest's declared schema, so that part of validation requires network access.

On Windows, `codex-cli 0.158.0` added the GitHub marketplace and installed plugin version `0.2.0` in a temporary `CODEX_HOME`. The installed package contained all four skills, the Canonical Specification and documentation templates, and the referenced workflow files. This was a package installation smoke test; skill invocation in a new chat and desktop installation were not tested. The machine's globally installed `codex-cli 0.101.0` still lacks the marketplace command.

Updated the prior task records to show their completed `main` integration and `v0.2.0` release. No skill workflow behavior or plugin version changed.
