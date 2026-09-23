# Grok distribution

## Grok chat

https://grok.com/connectors → New Connector → Custom → URL from [listing.json](listing.json)
→ complete authentication. Use [test-cases.md](test-cases.md) to verify your account.
[Official connector documentation](https://docs.x.ai/grok/connectors).

## Grok Build marketplace

The official [marketplace](https://github.com/xai-org/plugin-marketplace) is a Grok
Build catalog. A Build listing is not evidence of a consumer Grok catalog listing.
The repo includes `.grok-plugin/plugin.json`, one skill and root `.mcp.json`.

Follow [upstream contributing instructions](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md):
fork upstream, append `build/grok-catalog-entry.json` to `.grok-plugin/marketplace.json`,
regenerate the component index, validate, then open the PR. Generate our entry from
the final public clean revision; do not substitute `main`, a tag or a short SHA.

```bash
python3 scripts/generate-plugin-index.py
python3 scripts/validate-catalog.py
python3 scripts/generate-plugin-index.py --check
```

These commands run in the xAI marketplace checkout, not this repo. No upstream PR
is submitted by our packaging script. Keywords are deliberately brand-scoped.

Prepared PR body:

> Add Genfeed from its official organization repository, pinned to the submitted
> commit. The package supplies one playbook skill and a hosted OAuth MCP connection
> for Genfeed content operations. It installs no hooks or local server and contains
> no credentials. Media jobs can consume Genfeed credits; writes retain approval
> controls. Documentation, privacy policy and support links are included.

Add actual upstream validation output and the pinned SHA before sending. For a
consumer catalog listing beyond custom MCP, obtain the current xAI process directly;
no equivalent public submission path is established by the Build documentation.
