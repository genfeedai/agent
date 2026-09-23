# Genfeed for agents

Public package for connecting an AI agent to [Genfeed](https://genfeed.ai). The playbook skill, client manifests, and MCP Registry entry live here. The MCP server stays in the [genfeed.ai](https://github.com/genfeedai/genfeed.ai) monorepo (`apps/server/mcp`) and is hosted at `https://mcp.genfeed.ai/mcp`.

Connect with the distribution toolset profile so clients are not handed the full catalog (about 120 tools):

`https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand`

That profile lists about 50 tools and is accepted by production today. The `onboarding` toolset (`connect_social_account`, `get_connection_status`, `initiate_oauth_connect`) is on `master` but not yet deployed; production rejects `toolsets=...,onboarding` with `Unknown toolset(s)` until the next deploy. Add it after that. Unknown toolset names fail before login, so a wrong profile looks like a broken server.

## Authentication

OAuth 2.1 is the default. The server supports Dynamic Client Registration, PKCE, and protected-resource discovery. Finish sign-in in the browser when the client asks.

An API key is the fallback for a client with no OAuth support. Send it only as a header:

```http
Authorization: Bearer <key>
```

Create one with the CLI (`@genfeedai/cli`, binaries `genfeed` and `gf`):

```bash
genfeed login
genfeed keys create -n "mcp" -p mcp
```

Do not put the key in the URL. On HTTP 401, stop and ask the user to sign in. Do not search the machine for a credential.

## Install

### Claude Code

```text
/plugin marketplace add genfeedai/agent
/plugin install genfeed@genfeed
```

Or add the server directly, then authenticate with `/mcp`:

```bash
claude mcp add --transport http genfeed --scope user "https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand"
```

### Codex

```bash
codex mcp add genfeed --url "https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand"
codex mcp login genfeed
```

API-key fallback: add `--bearer-token-env-var GENFEED_API_KEY`.

### Cursor

Install this repository as a plugin (`.cursor-plugin/`), or add the root `mcp.json` server entry in Cursor's MCP settings. Choose OAuth. For an API key, set the `Authorization` header to `Bearer` plus the key. Do not embed the key in the URL.

### Gemini CLI

```bash
gemini extensions install https://github.com/genfeedai/agent
```

The extension manifest uses `httpUrl` and loads `GEMINI.md`.

### Codex, Cursor, Copilot, and VS Code via Agent Plugins

```bash
npx skills add genfeedai/agent
```

Root `plugin.json` and `mcp.json` are the Agent Plugins 1.0.0 layout. `skills/genfeed/SKILL.md` is the playbook.

### OpenClaw

The skill is `skills/genfeed` (`name: genfeed`, `metadata.openclaw` install block for the optional CLI). Point an existing OpenClaw install of `openclaw-integration` at this repository. Hosted MCP URL above. OAuth first.

### Grok

Grok Build reads `.grok-plugin/` (plugin, `mcp.json`, marketplace entry) and also the root `.mcp.json`. Consumer Grok: grok.com → Connectors → Custom, paste the MCP URL, choose OAuth. Listing in xAI's catalog is a pull request to `xai-org/plugin-marketplace` with this repo pinned to a commit SHA; not submitted yet.

### MCP Registry

`server.json` publishes `io.github.genfeedai/genfeed` as a remote `streamable-http` server. Publishing to the registry is a separate step from this repository and has not been done yet; the same is true for the Claude, Cursor, ClawHub and Grok directories.

## What the agent should do

Read [`skills/genfeed/SKILL.md`](skills/genfeed/SKILL.md). The tool list, required arguments, and approval flags are in [`skills/genfeed/references/tools.md`](skills/genfeed/references/tools.md). An agent-executable setup is in [`llms-install.md`](llms-install.md).

## License

MIT. See [LICENSE](LICENSE).
