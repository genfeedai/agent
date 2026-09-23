# Data-handling answers for review

Public policy: https://genfeed.ai/privacy · Terms: https://genfeed.ai/terms ·
Support/security: https://genfeed.ai/contact · Privacy requests: privacy@genfeed.ai.

## Implementation facts

This repository contains instructions, client manifests and existing branding. It
installs no hooks, local server, background daemon or package telemetry. Its tools
connect to Genfeed's own hosted MCP endpoint. OAuth discovery identifies Genfeed's
API as issuer. Social-provider authorization and generation-provider jobs are
performed by the Genfeed service, not this package.

Depending on the selected tool, inputs can contain brand identifiers, prompts, draft
text, media URLs, scheduling targets and analytics filters. Responses can contain
account/brand information, draft/job/release identifiers, results and performance
metrics. Authentication credentials must be handled by the client/OAuth flow, not
embedded in instructions, repository files or URL parameters.

Draft portal answer: “Genfeed processes tool arguments and account-scoped results
to perform the content operation the user requests. It may invoke the social or
media provider needed for that operation. The package does not request bulk chat
history or scan local credentials. Writes respect server permissions and approval
checks; pending actions are reported as pending.”

## Confirm before making legal attestations

The privacy owner must confirm actual retention/deletion behavior, subprocessors,
provider data use, server telemetry and all applicable privacy disclosures. A
working privacy URL alone does not prove it adequately covers every MCP/media flow.
Do not claim zero retention, no training, specific residency, encryption properties,
or a provider list without verified policy and implementation evidence. Reviewer
sample data should be synthetic and isolated from customer workspaces.

Genfeed is a content service, not an advertising placement in the assistant.
Disclose any sponsored-content or advertising functionality accurately if included
in a platform's scanned tools. Confirm this against the live scan before submission.
