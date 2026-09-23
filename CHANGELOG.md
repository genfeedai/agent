# Changelog

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
