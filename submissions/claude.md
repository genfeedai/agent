# Claude submission

There are two review routes; neither is completed by adding our self-hosted marketplace.

## Claude Code community plugin

Submit `https://github.com/genfeedai/agent` at https://platform.claude.com/plugins/submit
or the directory plugin form in a Team/Enterprise organization. Validate both files:

```bash
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

The marketplace references the package; skills and `.mcp.json` use conventional
discovery. There are no duplicated component declarations or `strict:false` override.
The documented submission route targets `claude-community`, not guaranteed inclusion
in Anthropic's separately curated official marketplace.

Source: https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace

## Claude chat / Cowork connector directory

Follow the submission portal linked from
https://claude.com/docs/connectors/building/submission. Remote submissions require a
Team/Enterprise organization and directory-management access. Use the universal URL,
OAuth and the ready copy in [listing.json](listing.json). Review all scanned tools and
supply private test access and actual results for each exposed tool. The full form
also collects company, use cases, data handling and policy acknowledgments.

Use cases: brand/channel readiness (P1), content planning (P2), and draft/scheduling
requests (P3/P5). Include the generation use case (P4) explicitly when requesting
policy clearance. This package has no MCP App UI; screenshot requirements for MCP
Apps do not describe this connector.

## Media-policy gate

The server and playbook expose image, video and audio generation, including batch
and workflow routes beyond the `generation` toolset. Anthropic's
[Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)
restricts AI media generation, with a limited design-workflow exception. Do not sign
an unsupported compliance attestation. Use [the exception request](claude-exception.md)
or obtain approval for a genuinely restricted server offering. A narrower `toolsets`
query only changes discovery and must not be described as an enforcement boundary.
Do not hide capabilities from reviewers. Apply this review to both directory routes.
