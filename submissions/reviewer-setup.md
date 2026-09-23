# Reviewer access and execution

Prepare a dedicated Genfeed test account and workspace, with synthetic brands,
example drafts, sample analytics and a channel you control. Keep it separate from
customer data. Ensure generation credits are available for the specifically agreed
review cases. Do not create real public posts as a setup check.

Provide the reviewer the sign-in URL, private credentials, MFA/login instructions,
workspace selection, permitted write targets and cleanup steps in the portal's
private review fields. Never commit them here. Confirm the login works without
access to the submitter's browser, mailbox or production session.

1. Install the candidate package or create the remote connector in the target client.
2. Sign in through OAuth. Record client version and package commit.
3. Call `get_account_info` and `list_brands`; verify the intended workspace and role.
4. Save the actual `tools/list` inventory and annotations, sanitized of private data.
5. Run [test-cases.md](test-cases.md), recording expected versus observed outcomes.
6. For pending mutations, use a separately authorized Genfeed reviewer. Do not elevate
   the test account to conceal a normal-user approval limitation. If the account
   cannot complete a case, mark it blocked rather than successful.
7. Test token refresh/expiry, revoke the connector in Genfeed, and verify old access
   fails. Reconnect cleanly. Disconnecting only the client is not proof of revocation.
8. Cancel test schedules, remove test outputs through supported controls, disconnect
   test social accounts and rotate/revoke reviewer access after review is complete.

Where a platform requires every tool to be exercised, create a worksheet from its
actual scanned inventory: tool name, title, annotations, required role/scopes,
inputs/fixture, expected result, observed result, pass/fail/blocked, timestamp, client
version and server revision. The bundled tool reference helps prepare fixtures but
is not an authenticated inventory or test receipt. Do not claim all-tool coverage
from the eight representative workflows alone.
