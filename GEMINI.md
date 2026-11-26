# Genfeed

Follow `skills/genfeed/SKILL.md`. The hosted server is Streamable HTTP.

Connect to `https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding`.

OAuth is the default. On 401, stop. An API key is an `Authorization: Bearer` header only, never a URL parameter. Do not guess a brand (`get_context` with `action: brands`, then `brandId`) or a channel (`credentialId` from `check_channel` with `action: readiness`; to connect one, `setup_brand` with `action: connect_account`, then poll `check_channel` with `action: connection_status`). Validate with `check_channel` (`action: capabilities`, then `action: validate`, parameters in `input`) before `schedule_release`. `save_post` is a draft tool. A call to `schedule_release` or `control_release` that publishes returns what to confirm and changes nothing; set `confirmed: true` only after the person agrees in this conversation. Local files go through `upload_media` with `action: request` and file details in `input`; transfer bytes using the returned method and headers, then use `action: complete` with `input: {assetId}`. A pending approval is decided in the Genfeed review inbox, never by the agent. Call `get_context` with `action: account` for the credit balance before batch work.

A setup check is `get_context` with `action: account` and with `action: brands`, both read-only.
