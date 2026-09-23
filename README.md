# Genfeed for agents

Use Genfeed from an AI assistant to inspect brands, prepare content, generate media,
request scheduled releases, and read analytics. This package contains one playbook
skill and client manifests. The hosted MCP server lives in
[genfeedai/genfeed.ai](https://github.com/genfeedai/genfeed.ai/tree/master/apps/server/mcp).

## Connect

```text
https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,onboarding
```

Use Streamable HTTP and sign in with Genfeed OAuth when prompted. A Genfeed account,
workspace access and sufficient credits for paid generation are required. The shared
profile includes brand readiness and social-account onboarding. Tool availability
also depends on the deployed server and your role; counts are not fixed.

OAuth opens a browser for authorization. Social-channel linking also requires the
channel owner's browser consent. A pending Genfeed approval is not a completed
write; some accounts need an authorized reviewer in Genfeed before it can execute.
See [the playbook](skills/genfeed/SKILL.md) and [reviewer setup](submissions/reviewer-setup.md).

## Install by client

### Claude Code

```text
/plugin marketplace add genfeedai/agent
/plugin install genfeed@genfeed
```

The plugin loads the skill and root `.mcp.json`. Open `/mcp`, select Genfeed, and
complete OAuth. Direct MCP-only alternative:

```bash
claude mcp add --transport http genfeed --scope user "https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,onboarding"
```

### Cursor

Until a marketplace listing is approved, add this server to Cursor's MCP settings:

```json
{"mcpServers":{"genfeed":{"url":"https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,onboarding"}}}
```

Complete OAuth when prompted. This config connects tools; it does not install the
playbook. For skill-only installation use the command below. A published plugin
bundles both. [Cursor submission instructions](submissions/cursor.md).

### Codex

For the packaged skill and connector, register this repository's marketplace:

```bash
codex plugin marketplace add genfeedai/agent
```

Refresh/restart the supported desktop client, select the Genfeed source in Plugins,
and install Genfeed. Registration alone does not install it. Direct MCP-only setup:

```bash
codex mcp add genfeed --url "https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,onboarding"
codex mcp login genfeed
```

### ChatGPT

For development, enable Developer mode in Settings → Security and login, then open
[Plugins](https://chatgpt.com/plugins), add the MCP URL above and complete OAuth.
Availability depends on your account and workspace settings. For skill-plus-MCP
local testing, use OpenAI's registered connection workflow in
[the OpenAI guide](submissions/openai.md). Public listing is a separate review.

### Claude chat / Cowork

Add a custom remote connector using the MCP URL and complete OAuth. A custom MCP
connection exposes tools; the playbook must be installed as a skill/plugin where
supported. Read [Claude's guide](submissions/claude.md) before seeking a public
listing: the full connector includes AI media generation subject to directory policy.

### Grok

[Grok Connectors](https://grok.com/connectors) → New Connector → Custom → paste the
MCP URL and authenticate. This connects Grok chat. The `.grok-plugin/` catalog and
root `.mcp.json` separately package the skill and connector for Grok Build.
[Grok publishing instructions](submissions/grok.md).

### Gemini CLI

```bash
gemini extensions install https://github.com/genfeedai/agent
```

The extension uses `httpUrl` and loads `GEMINI.md`. Complete authentication in the
client; do not use a URL containing credentials.

### Skill-only installation

```bash
npx skills add genfeedai/agent
```

This installs the playbook into supported agents. It does **not** register the MCP
server, authenticate, or publish a marketplace listing. Configure the connector
separately. OpenClaw can use the same skill and hosted connector; its optional CLI
install metadata is included in the skill.

## API-key fallback

Use only when your client cannot use OAuth. Create a key using the optional CLI:

```bash
genfeed login
genfeed keys create -n "mcp" -p mcp
```

Send it in an `Authorization: Bearer <key>` header. Codex supports
`--bearer-token-env-var GENFEED_API_KEY`. Never store real credentials in the repo,
paste them into a chat, or append them to a URL. On 401, stop and sign in again.

## Verify and troubleshoot

Call `get_account_info`, then `list_brands`. Both must succeed. Do not generate,
schedule, publish, or resolve an approval during setup. On an unknown toolset error,
inspect the [public server card](https://mcp.genfeed.ai/.well-known/mcp/server-card.json)
and report a deployment mismatch. On 403, check the account's role/scopes; do not
retry with another account. Check availability with `list_toolsets` and `describe_tool`.

## Privacy and support

Tools send their arguments to `mcp.genfeed.ai`, backed by Genfeed's API and workers.
OAuth discovery identifies `api.genfeed.ai` as issuer. Social connections and media
jobs can contact the providers selected in Genfeed. This package installs no hooks,
local daemon, or telemetry. See the [privacy policy](https://genfeed.ai/privacy),
[terms](https://genfeed.ai/terms), and [support](https://genfeed.ai/contact).

## Distribution

[Submission pack](submissions/README.md) · [Contributing](CONTRIBUTING.md) ·
[Agent-executable setup](llms-install.md) · [Tool snapshot](skills/genfeed/references/tools.md).
`server.json` is an MCP Registry descriptor; committing it does not publish it.
Repository CI validates packaging and builds review artifacts, not authenticated
acceptance or directory approval. License: [MIT](LICENSE).
