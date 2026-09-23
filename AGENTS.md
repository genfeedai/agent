# Genfeed agent package

This repository packages Genfeed for AI agents: the playbook skill, client manifests, and the MCP Registry entry. The MCP server is not in this repo. It lives in `genfeedai/genfeed.ai` at `apps/server/mcp` and is hosted at `https://mcp.genfeed.ai/mcp`.

- Do not invent tool names. `skills/genfeed/references/tools.md` is generated from the monorepo curated catalog.
- Do not put a key, token, or secret in a URL or a commit.
- `version` is `0.1.0` in `skills/genfeed/SKILL.md` and in every manifest that has a version. CI fails when they disagree.
- `create_post` stays a draft tool in the skill. Headless publishing stays on the scheduler tools.
