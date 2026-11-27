# Meta Muse Connector Platform

Portal: https://platform.muse.ai (`muse.ai/platform` redirects there). Guidelines: https://platform.muse.ai/docs.
Checked 2026-11-27. The portal asks for a work email and a six-digit code, so the person who owns the
Decoders Labs Ltd mailbox starts the submission. Nothing here is an attestation or a receipt.

## What the form asks for (guidelines §5)

| Step | Input | Where it comes from |
| --- | --- | --- |
| 5.1 Connector overview | Intended users, supported tasks, how it beats the browser, restrictions | Copy below |
| 5.2 Business verification and terms | Legal name, website, brand assets, privacy and terms, support and security contacts, a developer contact, Muse developer terms | [listing.json](listing.json), [form-copy.md](form-copy.md); the submitter accepts the terms |
| 5.3 Data processing questionnaire | What data, why, protection, sharing, retention, deletion | [data-handling.md](data-handling.md) after the owner confirms retention |
| 5.4 Technical details | Choose MCP; endpoint, authentication, scopes, tool documentation with read/write and sensitive marks | Endpoint and table below |
| 5.5 Test account and demo | Dedicated test account, sign-in steps, sample data | [reviewer-setup.md](reviewer-setup.md); credentials only in the portal's private fields |
| 5.6 Tool annotation | Coming soon in the portal; put the marks in the tool documentation | Table below |

Meta does not answer status messages; the portal shows the review status.

## Connector overview (paste)

> Genfeed is an AI content studio for brands. The connector lets Muse read a user's Genfeed workspace
> (brands, connected channels, content calendar, performance), draft posts, generate images and video
> from the user's brand kit, and schedule a post on a channel the user has connected. It improves on
> the browser because the user's own brand context, drafts and connected channels live in the account:
> Muse completes the task there instead of sending the user to a web page. Requirements: a Genfeed
> account, OAuth sign-in, and the workspace permissions for the action. Generation spends the user's
> Genfeed credits and the cost is shown first. A post is scheduled only after the user confirms it.

## Technical details

| Field | Value |
| --- | --- |
| Type | MCP, remote Streamable HTTP |
| MCP endpoint | `https://mcp.genfeed.ai/mcp` |
| Authentication | OAuth 2.0 with dynamic client registration; no API key and no shared secret |
| Documentation | https://github.com/genfeedai/agent#readme and the table below |
| Access restrictions | Genfeed account required; free credits at signup, paid plans for more; no regional restriction declared |
| Environment | Production. Use a dedicated review workspace, not customer data |

## Tool classification (proposal)

Derived from the tool snapshot's `mutationPolicy` for genfeedai/genfeed.ai v0.3.8 (catalog revision
`9e77b08`). `resolve_approval` is staff-only and is not part of what Muse should list. A tool that mixes
reads and writes is classified as a write (guidelines §3.2). The marks are a proposal: check each
tool's actions against the live scan before submitting, and mark a tool sensitive when in doubt.

| Tool | Toolset | Class | Required role | Note |
| --- | --- | --- | --- | --- |
| `get_ads` | ads | Read | user |  |
| `create_brand_from_url` | brand | Write | admin | Admin role only; creates a brand from a website. |
| `get_video_projects` | clipper | Read | user |  |
| `run_video_project` | clipper | Write, sensitive | user | Spends credits and renders video. |
| `generate_text` | content | Write | user | Generates copy and saves a draft. |
| `get_content` | content | Read | user |  |
| `save_post` | content | Write | user | Saves a draft; never publishes. |
| `upload_media` | content | Write | user | Adds a file to the Library. |
| `check_job` | core | Read | user |  |
| `find_tools` | core | Read | user |  |
| `get_assets` | core | Read | user |  |
| `get_context` | core | Read | user |  |
| `setup_brand` | core | Write | user | Onboards a brand and starts channel connection (browser OAuth). |
| `generate_media` | generation | Write, sensitive | user | Spends Genfeed credits; the cost is shown first. |
| `get_generation_catalog` | generation | Read | user |  |
| `get_insights` | insights | Read | user |  |
| `find_inspiration` | inspiration | Write | user | Searches public inspiration; saves what the person picks. |
| `run_remix` | inspiration | Write, sensitive | user | Spends credits and generates media. |
| `save_remix` | inspiration | Write | user |  |
| `get_knowledge` | knowledge | Read | user |  |
| `manage_knowledge` | knowledge | Write | user | Adds or removes brand knowledge. |
| `check_channel` | scheduler | Read | user |  |
| `control_release` | scheduler | Write, sensitive | user | Cancels, pauses or publishes a scheduled release. |
| `schedule_release` | scheduler | Write, sensitive | user | Publishes to a social channel. Two steps: the first call changes nothing and returns what to confirm; `confirmed: true` only after the person agrees. |
| `manage_skill` | skills-pro | Write | user | Installs or edits skills. |
| `manage_social` | social-inbox | Write, sensitive | user | Replies or sends messages as the connected account. |
| `find_workflows` | workflows | Read | user |  |
| `manage_workflow` | workflows | Write, sensitive | user | Runs a saved workflow that can generate or publish. |
| `get_workspace` | workspace | Read | user |  |
| `manage_workspace` | workspace | Write | user | Changes workspace settings. |

## Before submitting

- Run the Muse-side check from a real Muse account: connect Genfeed as a custom connector, finish OAuth,
  `get_context` returns the brands, a draft is saved and nothing is published without confirmation.
- Do not claim Muse directory availability on `/muse` until Meta approves (growth#98 owns that copy).
- Meta bans using connector data for model training (§4.2). Genfeed's data-handling answer must say so only
  if production settings confirm it; see [data-handling.md](data-handling.md).
