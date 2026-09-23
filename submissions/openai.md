# ChatGPT and Codex submission

Portal: https://platform.openai.com/plugins
Sources: [submission](https://developers.openai.com/plugins/deploy/submission),
[packaging](https://developers.openai.com/plugins/build/plugins),
[server review](https://developers.openai.com/plugins/deploy/app-review).

Choose **With MCP**, then the universal HTTPS URL in [listing.json](listing.json).
Upload the built skills archive alongside the server. Root `plugin.json` uses the
portable format; `extensions.com.openai.interface` contains presentation metadata.
An MCP-only submission is possible, but omits the packaged playbook.

## Portal preparation

Use the listing's name, descriptions, category, website/support/privacy/terms URLs,
logo and three starter prompts. Confirm the verified developer identity and launch
countries. The submitter needs Apps Management write access. Configure OAuth and
reviewer access; complete any domain challenge at `/.well-known/openai-apps-challenge`
on the verified host. The portal issues the token; this repo cannot supply it.

Scan tools and inspect titles, descriptions, schemas and `readOnlyHint`,
`destructiveHint`, `openWorldHint`. Use [the five positive and three negative cases](test-cases.md).
Provide observed results, not just expected outcomes. This connector has no custom
UI, so do not fabricate UI screenshots or UI CSP settings. Publish only after review approval.

## Local rehearsal

The repo marketplace is `.agents/plugins/marketplace.json` with its source at `./`.
Run `codex plugin marketplace add genfeedai/agent`, then install from the Genfeed
source in a supported desktop client. For ChatGPT development, register the server
in Developer mode. If testing skills tied to that registered connection, use the
real `plugin_asdk_app...` ID and OpenAI's plugin-creator workflow to create the local
mapping. No `.app.json` with an invented integration ID is shipped here.

Public submission supplies the MCP URL and review materials directly; a local
registered ID or existing integration reference is not a replacement.

Release notes: “Initial Genfeed connector submission: one content-operations
playbook and a hosted OAuth MCP service for brands, drafts, media, scheduling and
analytics. Package validation, client manifests, installation guidance and review
materials are included. Write actions retain Genfeed's existing permission and approval checks.”
