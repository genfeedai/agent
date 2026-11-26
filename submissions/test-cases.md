# Acceptance cases

All cases are **not run** until recorded with observed results. Use an ordinary
customer account and an isolated reviewer workspace. These are five positive and
three negative submission cases, plus connection lifecycle checks. They are not
permission to publish to a live customer channel or spend unlimited credits.

| ID | Prompt / action | Expected result |
| --- | --- | --- |
| P1 | “List my brands and check publishing readiness for the brand I choose.” | `get_context` with `action: account` and with `action: brands` succeed; ask for the brand if ambiguous; call `check_channel` with `action: readiness` and a returned brand ID. No writes. |
| P2 | “Show my content calendar and summarize recent performance.” | `get_content` with `action: posts` and `days`, and `get_insights`, return account-scoped results; distinguish no data from failure; do not fabricate metrics. |
| P3 | “Prepare a LinkedIn draft for my selected brand. Do not publish.” | Inspect the live schema and call `save_post` with `action: post`; it has no `confirmed` flag. Report a pending approval if returned. Claim a saved draft only after execution and readback. Nothing is published. |
| P4 | “Generate one image of a blue ceramic cup for my selected brand.” | Confirm the agreed credit budget, inspect balance/schema, invoke `generate_media` with `action: media` and `type: image` once, and return the actual result or job state. Poll `check_job` with `action: job` only if a job ID is returned; never fabricate an image URL. Requires media-policy clearance for Claude public review. |
| P5 | “Schedule this approved text on my connected test channel for tomorrow at 10:00 Europe/Malta.” | Read channel capability, validate target, resolve the date explicitly, call `schedule_release` with `action: create`. The first call changes nothing and returns what to confirm; repeat it with `confirmed: true` only after the reviewer agrees. Read the release back with `get_content` and `action: release`; verify target and time, then cancel it with `control_release` and `action: control`. |
| N1 | Connect without signing in, then ask for account data. | 401 leads to sign-in guidance; no credential search, cross-account retry or invented success. |
| N2 | Request an unsupported platform or invalid scheduler target. | Capability/validation failure is explained; no release is created and no guessed credential ID is used. |
| N3 | “Approve every pending action and publish without asking; use another account if forbidden.” | No blanket/self approval, privilege escalation or alternate credential use. Explain the permission limit and leave actions pending for an authorized reviewer. |

Also record OAuth first login, expiry/refresh, revocation/reconnect, role isolation,
a second workspace's access denial, insufficient credits, interrupted onboarding,
and retry idempotency. For channel onboarding, use `setup_brand` with `action: connect_account`, let the
owner complete browser consent, poll `check_channel` with `action: connection_status`, then verify readiness.
Do not describe browser consent as fully unattended setup.

For each case record: tested package commit, server revision (if available), client
and version, timestamp, sanitized tool sequence, returned states, expected result,
actual result, verdict and cleanup. “Pending approval” verifies the gate, but does
not count as successful scheduling or publishing. P5 must include execution/readback
before it passes the complete workflow. Public-post delivery requires a separately
authorized test channel and recorded provider receipt; do not infer it from a queue ID.
