# Changelog

## 0.1.4 - 2026-10-05

- Refresh the 142-tool snapshot from the current curated MCP catalog and expose role requirements.
- Update account, brand, discovery, media generation, upload and scheduler guidance to the current tools.
- Add a reproducible catalog refresh script and reject playbook and acceptance-inventory drift in package validation.
- Keep acceptance cases untested until actual reviewer evidence is recorded.
- Document the single-command Claude Code plugin install with the older-client fallback.

## 0.1.3 - 2026-10-03

- Connect URL profile adds `knowledge`: `core,scheduler,content,generation,analytics,brand,knowledge,onboarding`. The playbook tells agents to call `search_knowledge` before writing anything that must be accurate about the brand, and the previous profile did not list it. Production already serves the `knowledge` toolset (server card, 2026-09-23).
- Skill: correct the bare-URL note; the bare URL lists only the bounded `default` profile.
- `submissions/public-endpoint-check.json` keeps the recorded 2026-09-23 probe URL; re-record it with the outstanding live-client checks.

## 0.1.2 - 2026-09-23

- Enforce stricter OpenAI final listing lengths and supply a recording script, portal copy and per-tool evidence worksheet.
- Correct portable and Claude component declarations; add Codex marketplace discovery.
- Use standard skill metadata and keep optional CLI installation in the setup documentation.
- Include deployed onboarding tools in the shared connection profile.
- Add brand assets and platform submission materials, including honest acceptance and policy gates.
- Validate official schema snapshots, paths, versions and connection consistency; build submission archives in CI.
- Clarify pending approvals and prevent treating approval IDs as completed release IDs.

## 0.1.1 - 2026-09-23

- Connect URL profile is now `core,scheduler,content,generation,analytics,brand`. Production rejected the previous `onboarding` segment (`Unknown toolset(s): onboarding`) because that toolset has no deployed MCP tools yet; the new profile works on today's deploy and after the next one.
- Skill: fallback when the connection tools are absent; `resolve_approval` described as admin-gated.
- Added `.grok-plugin/` (plugin, mcp, marketplace) and root `.mcp.json` for Grok Build; README section for Grok.
- Validate workflow checks every manifest carries the same connect URL.

## 0.1.0 - 2026-09-23

- Initial package: playbook skill, Claude Code marketplace and plugin, Cursor plugin, Gemini CLI extension, Agent Plugins layout, MCP Registry `server.json`, and install docs.
- The MCP server stays in the genfeed.ai monorepo. Manifests point at the hosted Streamable HTTP endpoint.
