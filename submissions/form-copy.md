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
| MCP URL | https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,onboarding |

Long description:

> Connect your AI assistant to your Genfeed workspace. Inspect brands and connected
> channels, prepare content drafts, generate images, video or voice, request
> scheduled releases, and review content performance. Sign in with Genfeed OAuth;
> a Genfeed account and the relevant workspace permissions are required. Generation
> can consume Genfeed credits. Drafting and scheduling can create pending approvals;
> an authorized Genfeed reviewer must approve them before execution. Linking social
> accounts requires browser authorization. Availability depends on connected
> providers and permissions.

Starter prompts:

1. List my Genfeed brands and check their publishing readiness.
2. Prepare a LinkedIn draft for my selected brand without publishing it.
3. Show my content calendar and recent performance.

Use [brand assets](../assets/README.md); the owner also has PNG exports for portals
that require PNG. Recheck each portal's current upload dimensions. Credentials and
contact-only personal information belong in private form fields, never the repo.

## OpenAI — ChatGPT and Codex

Use the [With MCP route](openai.md) at https://platform.openai.com/plugins.
Attach genfeed-skills-0.1.2.zip from the final clean build if including the skill.
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

## Claude remote connector — field preparation

See [the official form guide](https://claude.com/docs/connectors/building/submission).
A Team organization with an Owner is sufficient; Enterprise is not mandatory.
Individual Pro does not expose this organization submission portal.

| Form step | Prepared answer / evidence |
| --- | --- |
| Introduction | Genfeed connects an assistant to the user's Genfeed content workspace. |
| Connection | Universal URL above; remote Streamable HTTP. Do not switch to a hidden discovery-only profile to evade media review. |
| Tools | Run a fresh scan, review titles/schemas/annotations, reconcile [the tool worksheet](tool-acceptance.csv) to the actual returned list. |
| Listing | Common copy, icon, public docs/privacy/support; proposed permanent slug genfeed, subject to availability and owner confirmation. |
| Use cases | Inspect a chosen brand's connected channels; prepare a draft with approval; inspect calendar/performance. Disclose media generation and scheduling too. |
| Company | Decoders Labs Ltd, Malta. Registered address/number and submitter authority must come from company records if requested. |
| Authentication | OAuth; advertised dynamic client registration, confirmed by a real portal connection. Private reviewer credentials are separate from OAuth client credentials. |
| Data handling | Genfeed's own API, with user-requested operations delivered through configured social/media providers. Complete the answers below after production review. |
| Test & launch | Reviewer setup, sample data, every exposed tool's actual outcome and cleanup; not just the eight OpenAI scenarios. |
| Compliance | Resolve each acknowledgement below before checking it. |
| Review | Confirm the real scan, legal answers, reviewer login and policy clearance; submit only when authorized. |

Seven acknowledgement review notes:

- Directory guidelines: review the current linked policy against the actual scan.
- First-party API: Genfeed operates the MCP/API; disclose downstream provider use.
- Financial transactions: generation can consume credits. Check the scanned tools
  for billing, purchases or transfers; do not equate no checkout UI with no cost.
- AI media generation: image, video and audio are core capabilities. Obtain express
  written eligibility clearance using [the request draft](claude-exception.md).
- Prompt injection: use the permission/isolation tests and server evidence. A skill
  instruction alone is not a security control or proof of compliance.
- Conversation data: tools receive task inputs; no permission to harvest unrelated
  chats. Check server logging, stored approvals and provider flows before attesting.
- Public documentation: publish the reviewed package docs and current privacy terms.

Do not mark health-data or sponsored-content answers from the product name alone:
the intended use is content operations, but prompts may contain personal data and
some toolsets expose ads. Confirm the actual exposed functionality and contractual
restrictions. Do not list third-party media hosts as owned allowed-link origins.
There is no MCP App UI in this package, so app screenshots are not applicable.

## Claude Code is a separate route

The community plugin form is https://platform.claude.com/plugins/submit. It accepts
the repository route described in [claude.md](claude.md); it is not the remote
Claude.ai connector submission and does not by itself require buying Team.
Native plugin/marketplace validation establishes packaging only. Media eligibility,
authenticated functionality and truthful disclosures remain separate gates.

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
Package validation, native installation, OAuth login and completed workflows are
different evidence. Leave not-run rows unfilled rather than manufacturing a pass.
The board tracks owners and dates; this pack intentionally carries no completion claims.
