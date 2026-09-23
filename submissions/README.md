# Submission pack

Prepared against official documentation reviewed 2026-09-23. This is reusable
publishing documentation. It does not attest to an account's verification status,
client acceptance results, or an approved marketplace listing.

## Files to use

| Destination | Guide | Submission input |
| --- | --- | --- |
| Cursor Marketplace | [Cursor](cursor.md) | Public repository URL, listing copy and logo |
| Claude Code community marketplace | [Claude](claude.md) | Plugin repository, client validation and media-policy clearance |
| Claude Connectors Directory | [Claude](claude.md) | Remote endpoint; media-policy clearance required |
| ChatGPT and Codex public directory | [OpenAI](openai.md) | With MCP submission plus skills archive |
| Grok Build marketplace | [Grok](grok.md) | Generated SHA-pinned catalog entry and upstream PR |
| Grok chat custom connector | [Grok](grok.md) | Remote endpoint; separate from Grok Build listing |
| MCP Registry | [Registry](registry.md) | `server.json` and publisher ownership verification |

[listing.json](listing.json) contains ready-to-copy product copy and public URLs.
Use [reviewer setup](reviewer-setup.md), [acceptance cases](test-cases.md),
[data-handling notes](data-handling.md), and the [Claude exception draft](claude-exception.md).
Use [portal copy](form-copy.md), the [recording script](demo-script.md), and the
[per-tool worksheet](tool-acceptance.csv). The worksheet is seeded from the repository
catalog; add/remove rows to match the authenticated scan before every-tool testing.
Existing [brand assets](../assets/README.md) are included.

## Build deliverables

After committing a clean revision, run `python3 scripts/build_submission.py` with
`scripts/requirements.txt` installed, or download the `genfeed-submission` CI artifact:

- `genfeed-<version>.zip`: portable plugin with client manifests, skill, references, assets and linked submission documentation.
- `genfeed-skills-<version>.zip`: a portable plugin manifest, `skills/`, referenced assets and license, without MCP configuration; attach it to the With MCP submission.
- `grok-catalog-entry.json`: external marketplace entry pinned to the built commit.
- `release.json`: version, source commit and archive hashes; not a test attestation.
- `submissions/` and `assets/`: form copy and upload assets.

Build artifacts are ignored by Git. Before public submission, prefer artifacts
built from the final merged `main` revision, and verify the pinned commit is public.
A PR artifact is a review preview and may refer to GitHub's synthetic merge commit.

## Owner-only inputs (do not invent or commit credentials)

| Input | Where to complete it |
| --- | --- |
| Verified legal publisher identity | OpenAI organization / relevant portal |
| Review contact and permitted launch countries | Private portal fields; confirm `listing.json` null fields |
| Domain ownership challenge | Exact token issued by the portal, deployed by the owning website/server project |
| Reviewer account, sample workspace and credits | Genfeed test workspace; credentials only in private review fields |
| OAuth login, refresh/revoke and real tool outcomes | Execute cases and record client version, commit and sanitized results |
| Anthropic generation-policy exception | Obtain written clearance before attesting compliance for this full connector |
| Data handling and provider retention confirmation | Product/privacy owner reviews [data-handling notes](data-handling.md) |
| Platform terms and attestations | Submitter completes after all statements are true |

A public endpoint and passing package validation are not substitutes for these inputs.
Do not mark the full connector ready for Claude directory submission while the
media-policy question remains unresolved.

## Public discovery evidence

[public-endpoint-check.json](public-endpoint-check.json) records the public server
card and the expected unauthenticated 401 for the full connection profile, including
`onboarding`. It establishes that the earlier unknown-toolset rejection is resolved.
The server exposes a protocol/service version, not a deployment commit; that field
is null rather than guessed. This is not authenticated workflow evidence.
