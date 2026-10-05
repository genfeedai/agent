---
name: genfeed
description: >-
  Operate a Genfeed workspace through the hosted MCP server. Use when
  connecting an agent to Genfeed, drafting or scheduling posts, generating
  image, video, or voice, checking brands, credits, or channels, or handling
  a pending Genfeed approval.
license: MIT
metadata:
  version: "0.1.4"
---

# Genfeed

The MCP server is hosted. This skill is the playbook. Tool names, arguments, and approval flags are in `references/tools.md`. Do not invent a tool.

## Hard rules

1. Authenticate first. If a call returns 401, stop. Do not search the filesystem, the environment, or the chat for a credential. Do not put a key, token, or secret in the URL. OAuth is the default. An API key is sent only as an `Authorization: Bearer` header, after the user creates one with `genfeed login` and `genfeed keys create -n "<label>" -p mcp` (`gf` is the same CLI).
2. Never guess a brand or a channel. Call `get_brands` and pass the selected brand's returned `id` as `brandId`. Take `credentialId` from `list_brand_publishing_readiness` for a brand that is already connected, and from `get_connection_status` while polling a connection you just started. `get_connection_status` and `connect_social_account` belong to `onboarding`, included in this package’s profile. If a connected client still lacks them, check its profile and permissions and report the limitation. The user can connect the channel at app.genfeed.ai and re-run `list_brand_publishing_readiness`. Do not invent either id.
3. Before scheduling, call `get_scheduler_capabilities` for the platform and `validate_scheduler_target` for the proposed target. Do not schedule a target that comes back with errors.
4. Headless publishing goes through `create_scheduled_release`, `get_scheduled_release`, and `control_scheduled_release`. `create_post` is a draft tool. Never set its `confirmed` flag. An MCP client does not render the publish card that flag expects.
5. Media comes from `generate` with `type` set to `image`, `video`, `voice`, or `music`, or from a URL the user already has. Inspect `get_generation_options` before choosing models, settings or a credit budget. Local-file uploads use `request_media_upload`, upload the file to its returned presigned URL, then `complete_media_upload`; never invent an asset ID or URL.
6. A pending approval is the user's decision. Call `resolve_approval` only after they choose. First inspect its availability and required role with `find_tools`. If it is unavailable to this account, or a call is rejected, stop and ask an authorized Genfeed reviewer to handle the approval. Never claim that a pending action has completed.
7. Call `get_account` with `include: ["credits"]` before batch generation or batch scheduling.
8. Connect with `?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding` on `https://mcp.genfeed.ai/mcp`. An unknown toolset name is rejected before login; inspect the public server card and report a deployment mismatch instead of silently widening access. Use `find_tools` without arguments to list toolsets, with `query` or `toolset` to search, and with `name` to inspect a full schema and permissions for tools outside that set. Do not guess a tool name.

## Connect

Streamable HTTP. Preferred URL:

`https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding`

The bare URL lists only the bounded `default` profile (core, scheduler and content), so always use the toolset query. `find_tools` tells you which toolsets the connected server actually serves.

OAuth, from the product connect helper:

- Claude Code: `claude mcp add --transport http genfeed --scope user <url>`, then `/mcp`, select genfeed, and finish browser sign-in.
- Codex: `codex mcp add genfeed --url <url>`, then `codex mcp login genfeed` if the browser did not open.
- Any other client: add the URL as a remote Streamable HTTP server and choose OAuth.

API key, only when the client has no OAuth. The user runs `genfeed login`, then `genfeed keys create -n "<label>" -p mcp`, and the client sends `Authorization: Bearer <key>`. Codex can store that as `--bearer-token-env-var GENFEED_API_KEY`. Never append the key to the URL.

## Schedule

1. `get_brands`, then keep `brandId`.
2. `list_brand_publishing_readiness` with that `brandId`. Keep `credentialId` for a healthy channel. If the user still needs to connect, start `connect_social_account` or `initiate_oauth_connect` and poll `get_connection_status`.
3. `get_scheduler_capabilities` for the platform, then `validate_scheduler_target`.
4. `get_account` with `include: ["credits"]` when this is one of several posts.
5. `create_scheduled_release` with `release.title`, `release.baseContent`, `release.timezone`, and `release.targets` (`credentialId`, `platform`). Pass `idempotencyKey` on retries.
6. If the result is pending approval, report its approval ID and stop this sequence. After approval actually executes and returns a release ID, call `get_scheduled_release` and read the state back. A pending approval ID is not a release ID.
7. `control_scheduled_release` only for cancel, pause, resume, or publish-now. `update_scheduled_release` for edits.

`create_scheduled_release`, `update_scheduled_release`, and `control_scheduled_release` are approval-required. Tell the user a pending approval exists. Do not call `resolve_approval` until they decide.

## Draft and generate

`create_post` writes a draft. Leave `confirmed` unset. Attach media with URLs from `generate` (select the required `type`), or a URL the user supplied.

## Check

A setup is done when `get_account` and `get_brands` both return without an auth error. Do not generate or schedule as the connection test.
