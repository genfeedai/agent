# Install Genfeed for an agent

Follow these steps in order. Do not generate, schedule, publish or resolve approvals during setup.

1. Use `https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding` as a remote Streamable HTTP server.
2. Choose the current host's documented installation route in [README.md](README.md). A skill install, marketplace registration and authenticated MCP connection are distinct steps; do not claim all three after completing only one.
3. Prefer OAuth. Let the user finish browser authorization. For a client without OAuth, the user can create a key with `genfeed login` and `genfeed keys create -n "mcp" -p mcp`, then configure a bearer header (Codex: `--bearer-token-env-var GENFEED_API_KEY`). Do not search for credentials or put them in URLs or chat.
4. On 401 stop and request sign-in. On 403 report insufficient role/scopes. An unknown toolset is a deployment mismatch: read the public server card rather than guessing a wider profile.
5. Read [the playbook](skills/genfeed/SKILL.md). Use live discovery and `find_tools` for schemas; the bundled catalog is a snapshot.
6. Call `get_account`, then `get_brands`. Report the account and brands only after both succeed. A working URL or OAuth discovery document alone does not prove authenticated setup.


## Claude connector

Claude, Claude Code and Cowork: use `https://mcp.genfeed.ai/mcp/claude`, or install the Claude plugin from the marketplace above. It contains its own content-operations skill. Create images/video/audio in https://app.genfeed.ai/studio/generate; opening this link starts no generation. Do not use the standard endpoint or standalone full creative skill to bypass the Claude connector restriction. The Claude offering is not yet submitted or published.
