# Genfeed for Claude

Manage brands, draft posts and articles, schedule existing assets and read analytics inside Claude, Claude Code or Cowork. Create images, video and audio in [Genfeed Studio](https://app.genfeed.ai/studio/generate), then return to Claude to manage your content.

## Install

In Claude Code: `/plugin install genfeed --marketplace genfeedai/agent` (Claude Code 2.1.275 or later). Complete browser OAuth from `/mcp`.

In Claude or Cowork, add `https://mcp.genfeed.ai/mcp/claude` as a custom connector and sign in with Genfeed OAuth. Reconnect older installations using this URL; older connections to the standard endpoint keep their original capabilities.

The plugin includes its own content-operations skill and restricted hosted MCP connector. Generation, workflows, batches, remix and approval redemption are unavailable. Opening Studio does not start generation or spend credits. Other clients use the standard Genfeed creative connector.

This is not yet a published public Claude directory listing. Source: [genfeedai/agent](https://github.com/genfeedai/agent). Published by Genfeed / Decoders Labs Ltd.

[Privacy policy](https://genfeed.ai/privacy) · [Terms](https://genfeed.ai/terms) · [Support](https://genfeed.ai/contact)
