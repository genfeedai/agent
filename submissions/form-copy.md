# Portal copy and reviewer handoff

Prepared 2026-09-23. Copy confirmed product facts from [listing.json](listing.json).
This document prepares fields; it is not a legal attestation or submission receipt.

## Common fields

| Field | Value |
| --- | --- |
| Product | Genfeed |
| Short description | Create and schedule content |
| Publisher | Decoders Labs Ltd |
| Registered country | Malta (owner supplied; portal verification separate) |
| Category | Productivity; choose only matching categories offered by each portal |
| Website | https://genfeed.ai |
| Repository | https://github.com/genfeedai/agent |
| Documentation | https://github.com/genfeedai/agent#readme |
| Support | https://genfeed.ai/contact |
| Support email | support@genfeed.ai |
| Privacy | https://genfeed.ai/privacy |
| Terms | https://genfeed.ai/terms |
| Connection | Hosted remote MCP, Streamable HTTP, OAuth |
| MCP URL | https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding |

Long description (same copy as listing.json; usable in both portal description fields):

> Connect your AI assistant to your Genfeed workspace. Inspect brands and
> connected channels, prepare content drafts, generate images, video, voice or
> music, request scheduled releases, and review content performance. Genfeed
> runs the content jobs and scheduler behind your assistant. Sign in with
> Genfeed OAuth; a Genfeed account and the relevant workspace permissions are
> required. Generation can consume Genfeed credits. Drafting and scheduling
> can create pending approvals; an authorized Genfeed reviewer must approve
> them before execution. Browser authorization is required when linking social
> accounts. This connector does not bypass platform permissions or guarantee
> unattended publishing.

Starter prompts:

1. List my Genfeed brands and check their publishing readiness.
2. Prepare a LinkedIn draft for my selected brand without publishing it.
3. Show my content calendar and recent performance.

Use [brand assets](../assets/README.md); the owner also has PNG exports for portals
that require PNG. Recheck each portal's current upload dimensions. Credentials and
contact-only personal information belong in private form fields, never the repo.

## OpenAI — ChatGPT and Codex

Use the [With MCP route](openai.md) at https://platform.openai.com/plugins.
Attach genfeed-skills-0.1.7.zip from the final clean build if including the skill.
The repository URL alone is not that upload. The package build also creates a full
ZIP for other review needs; do not replace the skills upload with that full bundle.

Paste the common fields, three prompts and release notes from [openai.md](openai.md).
Provide five positive and three negative cases from [test-cases.md](test-cases.md),
with actual outcomes. Put the link produced by [demo-script.md](demo-script.md) in
the demo-recording field. These are functional evidence, not marketing claims.
No custom MCP UI is shipped; UI-only screenshot/CSP fields are not applicable.

Complete the portal-issued domain challenge and current tool scan. Every scanned
tool needs honest read/write, destructive and external-world annotations with
justifications based on its real behavior. A content write, queued approval or
paid generation is not read-only. Package checks do not validate the server's scan.

OAuth uses Genfeed's authorization flow. Dynamic registration is advertised by
discovery; select it only after the portal successfully discovers it. Do not invent
a static client secret or claim CIMD support. Enter dedicated reviewer credentials
only in private fields. Confirm usable sample data, permissions and credit budget.

## Cursor

Use https://cursor.com/marketplace/publish with the repository URL, common listing
copy and logo. The repository contains .cursor-plugin/plugin.json and its MCP
configuration. Keep the full served toolset visible in the product description.
Update an existing submission rather than creating a duplicate. A receipt proves
submission, not approval or that an unmerged PR is what reviewers will install.

## Claude plugin and remote connector

Use [Claude’s current guide](claude.md) and https://claude.ai/directory/manage.
Paid Pro, Max, Team and Enterprise accounts can publish. Reuse the existing Genfeed draft rather than creating a duplicate. The plugin source is the public repository with folder `plugins/claude`; the paired MCP submission uses `https://mcp.genfeed.ai/mcp/claude` with browser OAuth.

Claude-specific description:

> Connect Claude to your Genfeed brands, content drafts, existing assets, scheduling and analytics. Draft copy with Claude, request scheduled releases subject to Genfeed permissions and approvals, and inspect performance. Create images, video and audio separately in Genfeed Studio. This connector excludes media generation, batches, workflows, arbitrary agent execution and approval redemption. A Genfeed account and the relevant workspace permissions are required.

Do not paste the full creative description or standard MCP URL from the common fields into Claude. The restriction is enforced by the dedicated OAuth resource and server execution policy, rather than a discovery-only toolset profile. Deploy and verify the server before submission. The plugin and its remote MCP server require paired submissions under the same publisher.

Confirm the actual exposed tool scan, OAuth connection, sample data, reviewer access, legal publisher details and production data-handling disclosures. Public documentation and an offline package check do not establish live acceptance. Resolve each current policy acknowledgement before checking it. If seeking to expose Genfeed’s full media-generation offering in Claude later, obtain express written eligibility clearance using [the request draft](claude-exception.md).

## Data-handling copy for owner review

> Genfeed processes the tool inputs and account-scoped results needed to carry out
> the user's content request. Depending on the action, these include brand context,
> draft text, prompts, media, publishing targets and performance data. Genfeed may
> share the relevant inputs with the configured media or social provider to fulfill
> that action. Account records, content and operational records can be stored by the
> service. The agent package does not request bulk chat histories or scan local
> credentials. Genfeed enforces account permissions and approval requirements.

This paragraph needs to accompany, not replace, verified retention/deletion,
provider, telemetry, legal-entity and contact disclosures. Do not claim zero logs,
no training, a universal 30-day deletion period or a complete subprocessor list
without confirming production settings. See [data-handling.md](data-handling.md).

## Evidence ledger

Record the final source commit and server revision (or explicitly unavailable),
client/version, dated login/tool results, actual scan inventory, recording URL,
private reviewer-access verification, policy decision, and final submission receipt.
Keep completed evidence ledgers in private submission storage; never commit signed
links, credentials or real customer outputs into the public worksheet.
Package validation, native installation, OAuth login and completed workflows are
different evidence. Leave not-run rows unfilled rather than manufacturing a pass.
The board tracks owners and dates; this pack intentionally carries no completion claims.
