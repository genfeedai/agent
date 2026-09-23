# Changelog

## 0.1.1 - 2026-09-23

- Connect URL profile is now `core,scheduler,content,generation,analytics,brand`. Production rejected the previous `onboarding` segment (`Unknown toolset(s): onboarding`) because that toolset has no deployed MCP tools yet; the new profile works on today's deploy and after the next one.
- Skill: fallback when the connection tools are absent; `resolve_approval` described as admin-gated.
- Added `.grok-plugin/` (plugin, mcp, marketplace) and root `.mcp.json` for Grok Build; README section for Grok.
- Validate workflow checks every manifest carries the same connect URL.

## 0.1.0 - 2026-09-23

- Initial package: playbook skill, Claude Code marketplace and plugin, Cursor plugin, Gemini CLI extension, Agent Plugins layout, MCP Registry `server.json`, and install docs.
- The MCP server stays in the genfeed.ai monorepo. Manifests point at the hosted Streamable HTTP endpoint.
