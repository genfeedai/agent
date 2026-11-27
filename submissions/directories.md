# Directory status and next steps

Observed 2026-11-27 in the owner's signed-in browser sessions (read-only except where noted). This is the
current state; the older files in this folder record what was prepared in September and October. A listing
is not claimed until its portal shows it.

| Directory | State now | What moves it |
| --- | --- | --- |
| Claude connector (`mcp.genfeed.ai`, `/mcp/claude`) | **Published.** Updated Nov 17; three accounts used a tool in the last 30 days | Nothing. Media generation stays off it until Anthropic answers ticket #145749261 in writing |
| Claude plugin (`genfeedai/agent`, `plugins/claude`) | **Published**, live v0.1.9, 475 installs. v0.1.12 (`4c7acb9`) passed the scan with warnings and shows Approved, but **Publish update is refused**: "held for the directory team" | Ask the directory team to clear the hold (below) |
| OpenAI ChatGPT and Codex plugin directory | **Never submitted.** Portal reachable in the Genfeed.ai organization; the Plugins page has no drafts | Upload the ZIP, connect the server, complete the review fields, submit (below) |
| Cursor Marketplace | **Application not locatable.** The form at `cursor.com/marketplace/publish` is open for an individual account and there is no status page | Resend only after the status check below |
| Grok Bot | No directory of its own; inherits Cursor's marketplace | Follows Cursor |
| Meta Muse | **Never applied** | [muse.md](muse.md) |

## Claude plugin hold

The portal's notices: v0.1.11 `933ce83` was blocked by directory policy ("Not allowed"), `b9c558b` was held
("Policy review didn't complete"), and since then `ae9637c` and `4c7acb9` passed with warnings only. The
listing-level hold remains, so the portal says: "Needs the directory team... Contact the directory team to
publish or relist it". Ask for the hold to be lifted and v0.1.12 published. Suggested text:

> Subject: Genfeed plugin: please clear the review hold and publish v0.1.12
>
> The Genfeed plugin (genfeedai/agent, folder plugins/claude, submission 51dddc88-f28f-479c-80b1-52dbf278f117)
> is live at v0.1.9. v0.1.12 (4c7acb9) passed the scan with directory policy warnings only, and the portal
> shows it Approved, but Publish update answers that the listing is held for the directory team. The earlier
> blocked version (933ce83) was replaced by ae9637c and 4c7acb9. Please clear the hold, or tell us which
> finding still applies. The v0.1.12 change is documentation only: the playbooks now name the tools the server
> lists today and state that the Claude connector does not generate media.

The portal's Help and appeals page has no appeal form for this case yet, so it goes by email from the review
contact mailbox, the same way as the media request (tickets #141813151 and #145749261).

Verified status (Help and appeals) needs a DNS TXT record on `genfeed.ai`; it is optional and unrelated to the
hold, but it is a quick listing upgrade for the owner of the DNS zone.

## OpenAI plugin directory

OpenAI replaced the "With MCP" form. The flow today (https://developers.openai.com/plugins/deploy/submission):

1. Build the package: `python3 scripts/build_submission.py`, then use `build/genfeed-openai-<version>.zip`
   (manifest, MCP configuration, skill and assets only). `plugin.json` already carries the five positive and
   three negative cases and the release notes, so the portal imports them.
2. Plugins, **Upload new or existing plugin**, choose the verified developer identity, upload the ZIP.
3. **Metadata & Skills**: resolve findings, upload a corrected ZIP if needed.
4. **MCPs**: Connect. The portal shows a domain challenge token. The server must return exactly that token as
   plain text at `https://mcp.genfeed.ai/.well-known/openai-apps-challenge`. The token is only issued after the
   upload, and serving it is a code change plus a release in genfeedai/genfeed.ai.
5. Authorize the connection (OAuth with dynamic client registration) and read the scan. Every tool needs honest
   read-only, destructive and open-world annotations.
6. **Review details**: demo recording URL, reviewer credentials, sign-in steps. Run the cases first and enter
   what happened, not what was expected ([test-cases.md](test-cases.md)).
7. **Submit for review**: the submitter confirms the policy attestations.

Blockers that stay with the owner: the demo recording (genfeedai/genfeed.ai#5032 is on standby), a reviewer
account with a connected test channel (case P5), and the attestations.

## Cursor

The docs say plugins are submitted through the Cursor team and manually reviewed, and point community plugins
at cursor.directory. A 23 September application was reported but never tied to the current account, and the
form offers only an individual owner. Before sending a second application, ask for the status of the first:

> To: marketplace-publishing@cursor.com
> Subject: Status of the Genfeed plugin application
>
> We applied to publish the Genfeed plugin (https://github.com/genfeedai/agent) around 23 September and see
> no status. Could you confirm the application is in the queue, or tell us if it needs to be sent again? The
> repository carries `.cursor-plugin/plugin.json` and an OAuth remote MCP configuration.

If the reply is a resend, the form values are in [cursor.md](cursor.md) and [form-copy.md](form-copy.md). The
submitter accepts the Publisher Terms, including the exclusion of plugin data from model training.

## Grok Bot

No application exists. Once Genfeed is in Cursor's marketplace, confirm it appears as a plugin in a Grok Bot
session, then change `/grok-bot` so it stops telling users to paste a prompt.
