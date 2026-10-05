# Claude submission

Use the current [publishing portal](https://claude.ai/directory/manage) from an eligible paid Claude account. [Publishing docs](https://claude.com/docs/directory/publish) allow Pro, Max, Team and Enterprise; Free accounts cannot submit. The old Console form is unsupported.

## Plugin and companion MCP connector

Repository: `https://github.com/genfeedai/agent`. Plugin folder: `plugins/claude`. Native manifest: `plugins/claude/.claude-plugin/plugin.json`. The self-hosted marketplace references this folder and contains no duplicated component definitions.

Submit the companion remote MCP connector with `https://mcp.genfeed.ai/mcp/claude`, browser OAuth and content-operations use cases: brands, drafts, existing assets, scheduling and analytics. Pair the plugin and connector from the same publishing organization. The standard media-generation server is a different offering and must not be substituted.

Create media in Genfeed Studio. The dedicated connector enforces an explicit tool allowlist on discovery and execution; OAuth grants retain the restriction across refresh and use on the standard transport. Workflows, batches, remix, arbitrary agent calls and approval redemption are unavailable. A profile/toolsets query on the standard endpoint is only a discovery filter and is not this restriction.

## Release and review gates

Wait for production deployment and a real Claude OAuth/connector check before submission. Supply actual reviewer access, live acceptance results, accurate operational data disclosures and any required policy acknowledgments. Do not attest these gates from package validation alone, or claim a public listing before approval.

The [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) restricts standalone third-party AI media generation without written permission. The full standard connector still needs eligibility review. Disclose the Studio handoff and product's full capabilities to reviewers; the restricted offering does not guarantee approval.

Plugin help: directory@anthropic.com. Companion MCP help: mcp-review@anthropic.com.
