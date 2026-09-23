# Cursor submission

Portal: https://cursor.com/marketplace/publish
Official checklist: https://cursor.com/docs/reference/plugins#submitting-a-plugin

Submit repository `https://github.com/genfeedai/agent` after the final revision is
merged. This is a single plugin, so no Cursor marketplace catalog is required.
Use `Genfeed` as display name, `genfeed` as identifier, the tagline and description
from [listing.json](listing.json), and [logo.svg](../assets/logo.svg).

The root Agent Plugins manifest and `.cursor-plugin/plugin.json` support the same
skill and server. Native Cursor MCP configuration infers transport from `url`;
portable `mcp.json` declares `streamable-http`. Paths stay inside the package.

Before applying, test installation in Cursor and complete OAuth, read-only discovery,
and the supported draft/scheduling cases in [test-cases.md](test-cases.md). Record
Cursor version and tested commit. Confirm the Genfeed skill and MCP tools appear once
and no duplicate connector is left from an earlier manual install. Attach accurate
results; package validation alone is not this installation test.

Submission copy: “Genfeed connects Cursor to a user's Genfeed workspace for brand
context, content drafts, media generation, scheduling requests and analytics. It
bundles one playbook skill and a hosted OAuth MCP connection, with no local hooks or
background process. Generation can consume credits and writes respect Genfeed approvals.”
