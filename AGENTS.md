# Genfeed agent package

This repository packages Genfeed for AI agents: the playbook skill, client manifests,
and the MCP Registry entry. The server lives in `genfeedai/genfeed.ai` at
`apps/server/mcp` and is hosted at `https://mcp.genfeed.ai/mcp`.

- Do not invent tool names. `skills/genfeed/references/tools.md` is generated from the monorepo curated catalog. Live schemas and caller permissions take precedence over this snapshot.
- Never commit credentials or put them in URLs. Reviewer credentials belong only in the platform's private submission fields.
- Root `plugin.json` is the release-version authority. Match every client manifest and skill `metadata.version` to it.
- `create_post` stays a draft tool. Publishing uses scheduler tools and existing approval gates. Do not weaken those gates through skill wording.
- Run `python3 scripts/validate.py` and `python3 -m unittest discover -s scripts -p 'test_*.py'` on an authorized verification host after installing `scripts/requirements.txt`.
- `submissions/` contains reusable publishing materials, not a task backlog. Do not mark authenticated checks, identity verification, approvals, or directory publication complete without evidence.
