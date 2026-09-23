# Install Genfeed for an agent

Do these steps in order. Stop on the first failure and report it. Do not generate, schedule, or publish during setup.

1. The server is Streamable HTTP at `https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand`. Use that URL. The bare URL without `toolsets` lists about 120 tools and is the wrong default. Do not add toolset names the server may not serve yet (`onboarding` until the next deploy); an unknown name is rejected before login and looks like a broken server.

2. Add it to the client you are running in.
   - Claude Code: `claude mcp add --transport http genfeed --scope user "https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand"`, then tell the user to open `/mcp`, select genfeed, and finish browser sign-in.
   - Codex: `codex mcp add genfeed --url "https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand"`, then `codex mcp login genfeed` if the browser did not open.
   - Cursor: install the plugin from this repo, or add the same URL as a remote MCP server and choose OAuth.
   - Gemini CLI: `gemini extensions install https://github.com/genfeedai/agent`.
   - Anything that reads Agent Plugins: `npx skills add genfeedai/agent`.

3. Prefer OAuth. Use an API key only when that client cannot do OAuth. Ask the user to run `genfeed login`, then `genfeed keys create -n "mcp" -p mcp` (`gf` is the same CLI). Configure `Authorization: Bearer <key>` as a header, or Codex `--bearer-token-env-var GENFEED_API_KEY`. Never put the key in the URL. Never search the filesystem, the environment, or the chat for an existing key.

4. If any call returns 401, stop. Tell the user to finish sign-in. Do not retry with a different credential you found yourself.

5. Read `skills/genfeed/SKILL.md` and follow it. Tool names you have not seen there are in `skills/genfeed/references/tools.md`. Call `describe_tool` before using one.

6. Check the connection with two read-only calls: `get_account_info`, then `list_brands`. Setup succeeded when both return without an auth error. Report the account and the brand names. Do not call a write tool, a generation tool, or `resolve_approval` as part of this check.
