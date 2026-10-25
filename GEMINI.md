# Genfeed

Follow `skills/genfeed/SKILL.md`. The hosted server is Streamable HTTP.

Connect to `https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding`.

OAuth is the default. On 401, stop. An API key is an `Authorization: Bearer` header only, never a URL parameter. Do not guess a brand (`get_brands`, then `brandId`) or a channel (`credentialId` from `get_connection_status` or `list_brand_publishing_readiness`). Validate with `check_channel` (`action: capabilities`, then `action: validate`, parameters in `input`) before `create_scheduled_release`. `create_post` is a draft tool; never set `confirmed`. Local files go through `upload_media` with `action: request` and file details in `input`; transfer bytes using the returned method and headers, then use `action: complete` with `input: {assetId}`. Call `resolve_approval` only after the user decides. Call `get_account` with `include: ["credits"]` before batch work.

A setup check is `get_account` and `get_brands`, both read-only.
