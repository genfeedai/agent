# Genfeed

Follow `skills/genfeed/SKILL.md`. The hosted server is Streamable HTTP.

Connect to `https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand`.

OAuth is the default. On 401, stop. An API key is an `Authorization: Bearer` header only, never a URL parameter. Do not guess a brand (`list_brands`, then `brandId`) or a channel (`credentialId` from `get_connection_status` or `list_brand_publishing_readiness`). Validate with `get_scheduler_capability` and `validate_scheduler_target` before `create_scheduled_release`. `create_post` is a draft tool; never set `confirmed`. There is no local upload tool. Call `resolve_approval` only after the user decides. Call `get_credits_balance` before batch work.

A setup check is `get_account_info` and `list_brands`, both read-only.
