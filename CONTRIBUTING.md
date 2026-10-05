# Contributing

This repo holds install manifests, the agent playbook and submission materials.
Product changes belong in `genfeedai/genfeed.ai`.

## Tool catalog

`skills/genfeed/references/tools.md` is generated from the monorepo curated MCP
catalog, source definitions and mutation policy. Do not hand-edit rows or invent
tools. Counts and permissions may differ by server revision and caller role;
`tools/list` and `find_tools` are authoritative for the active connection.

Refresh the assembled catalog from a monorepo checkout with committed actions sources:

```bash
python3 scripts/refresh_tools.py /path/to/genfeed.ai
```

This records the source actions revision, updates the JSON snapshot and renders
the Markdown reference. Reconcile `submissions/tool-acceptance.csv` with the new
inventory; do not carry forward a passing result without checking the changed
schema and behavior. Package validation rejects obsolete tool names in the
playbook/setup/acceptance instructions and worksheet metadata drift.

## Release

Use root `plugin.json` version as the authority. Update all client versions,
marketplace versions, `server.json`, skill `metadata.version`, and CHANGELOG together.
Standard client manifests use the shared URL, including `brand` and `onboarding` toolsets.
Grok discovers root `.mcp.json`; Codex and other portable hosts discover `mcp.json`.
Claude loads only `plugins/claude/.mcp.json`, which uses the dedicated `/mcp/claude` OAuth resource.
Cursor's native manifest points to `.cursor-plugin/mcp.json`.

## Verification and packaging

On your authorized verification host:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
.venv/bin/python scripts/build_submission.py
claude plugin validate plugins/claude/.claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

CI runs schema and semantic validation, regression tests, and packaging. Its
`genfeed-submission` artifact includes plugin and skills ZIPs, submission documents,
and a commit-pinned Grok catalog entry. No package script signs in or publishes.
Before a directory submission, run the manual acceptance cases in
`submissions/test-cases.md`. A green packaging job is not authenticated acceptance.

Refresh upstream schemas using `schemas/sources.json`; retain origin and digest.
Never commit `.env` files, reviewer credentials, private test reports or auth logs.

Schema checks cover Agent Plugins, portable MCP, Cursor and MCP Registry. Native
Claude/Grok/Codex/Gemini formats also receive package-specific semantic checks;
run each actual client rehearsal before submission rather than treating those
checks as a complete vendor schema or runtime validation. Portable skill metadata
follows https://agentskills.io/specification.
