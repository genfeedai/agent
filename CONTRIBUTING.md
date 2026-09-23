# Contributing

This repo holds install manifests and the agent playbook. Product changes belong in `genfeedai/genfeed.ai`.

## Tool list

`skills/genfeed/references/tools.md` is generated from the monorepo:

- MCP rows are `CURATED_ACTION_CATALOG` entries whose `surfaces` include `mcp`.
- Description and top-level `required` come from `packages/actions/src/registry/source/**`.
- Approval is `MUTATION_POLICY_BY_NAME[name] === 'approval-required'`.

Regenerate that file when the catalog changes. Do not hand-edit a row to invent a tool.

## Versions

Keep `0.1.0` (or the next release) identical in:

- `skills/genfeed/SKILL.md` frontmatter `version`
- `.claude-plugin/marketplace.json` (`metadata.version` and the plugin `version`)
- `.claude-plugin/plugin.json`
- `.cursor-plugin/plugin.json`
- `gemini-extension.json`
- `plugin.json`
- `server.json`

## Credentials

Connect URLs point at `https://mcp.genfeed.ai/mcp`. A toolset query is fine. A key, token, or secret in any URL is not. API keys travel in an `Authorization` header.

## Checks

Pull requests run `.github/workflows/validate.yml`: every JSON manifest parses, versions agree, and no URL contains a credential pattern.
