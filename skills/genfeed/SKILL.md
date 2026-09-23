---
name: genfeed
description: >-
  Operate a Genfeed workspace through the hosted MCP server. Use when
  connecting an agent to Genfeed, drafting or scheduling posts, generating
  image, video, or voice, checking brands, credits, or channels, or handling
  a pending Genfeed approval.
license: MIT
metadata:
  version: "0.1.2"
  openclaw:
    emoji: "✦"
    homepage: https://github.com/genfeedai/agent
    install:
      - id: cli
        kind: node
        package: "@genfeedai/cli"
        bins:
          - genfeed
        label: Install the optional Genfeed CLI for login and API keys
---

# Genfeed

The MCP server is hosted. This skill is the playbook. Tool names, arguments, and approval flags are in `references/tools.md`. Do not invent a tool.

## Hard rules

1. Authenticate first. If a call returns 401, stop. Do not search the filesystem, the environment, or the chat for a credential. Do not put a key, token, or secret in the URL. OAuth is the default. An API key is sent only as an `Authorization: Bearer` header, after the user creates one with `genfeed login` and `genfeed keys create -n "<label>" -p mcp` (`gf` is the same CLI).
2. Never guess a brand or a channel. Call `list_brands` and pass the returned `brandId`. Take `credentialId` from `list_brand_publishing_readiness` for a brand that is already connected, and from `get_connection_status` while polling a connection you just started. If `connect_social_account` and `get_connection_status` are not on the server you are connected to (they ship with the `onboarding` toolset), tell the user to connect the channel at app.genfeed.ai and re-run `list_brand_publishing_readiness`. Do not invent either id.
3. Before scheduling, call `get_scheduler_capability` for the platform and `validate_scheduler_target` for the proposed target. Do not schedule a target that comes back with errors.
4. Headless publishing goes through `create_scheduled_release`, `get_scheduled_release`, and `control_scheduled_release`. `create_post` is a draft tool. Never set its `confirmed` flag. An MCP client does not render the publish card that flag expects.
5. Media comes from `generate_image`, `generate_video`, or `generate_voice`, or from a URL the user already has. No local upload tool exists.
6. A pending approval is the user's decision. Call `resolve_approval` only after they choose. First inspect its availability and required role with `describe_tool`. If it is unavailable to this account, or a call is rejected, stop and ask an authorized Genfeed reviewer to handle the approval. Never claim that a pending action has completed.
7. Call `get_credits_balance` before batch generation or batch scheduling.
8. Connect with `?toolsets=core,scheduler,content,generation,analytics,brand,onboarding` on `https://mcp.genfeed.ai/mcp`. An unknown toolset name is rejected before login; inspect the public server card and report a deployment mismatch instead of silently widening access. Use `list_toolsets`, `search_tools`, and `describe_tool` for anything outside that set. Do not guess a tool name.

## Connect

Streamable HTTP. Preferred URL:

`https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,onboarding`

The bare URL lists the full role-visible MCP catalog; the count changes with deployments. Prefer the toolset query. `list_toolsets` tells you which toolsets the connected server actually serves.

OAuth, from the product connect helper:

- Claude Code: `claude mcp add --transport http genfeed --scope user <url>`, then `/mcp`, select genfeed, and finish browser sign-in.
- Codex: `codex mcp add genfeed --url <url>`, then `codex mcp login genfeed` if the browser did not open.
- Any other client: add the URL as a remote Streamable HTTP server and choose OAuth.

API key, only when the client has no OAuth. The user runs `genfeed login`, then `genfeed keys create -n "<label>" -p mcp`, and the client sends `Authorization: Bearer <key>`. Codex can store that as `--bearer-token-env-var GENFEED_API_KEY`. Never append the key to the URL.

## Schedule

1. `list_brands`, then keep `brandId`.
2. `list_brand_publishing_readiness` with that `brandId`. Keep `credentialId` for a healthy channel. If the user still needs to connect, start `connect_social_account` or `initiate_oauth_connect` and poll `get_connection_status`.
3. `get_scheduler_capability` for the platform, then `validate_scheduler_target`.
4. `get_credits_balance` when this is one of several posts.
5. `create_scheduled_release` with `release.title`, `release.baseContent`, `release.timezone`, and `release.targets` (`credentialId`, `platform`). Pass `idempotencyKey` on retries.
6. If the result is pending approval, report its approval ID and stop this sequence. After approval actually executes and returns a release ID, call `get_scheduled_release` and read the state back. A pending approval ID is not a release ID.
7. `control_scheduled_release` only for cancel, pause, resume, or publish-now. `update_scheduled_release` for edits.

`create_scheduled_release`, `update_scheduled_release`, and `control_scheduled_release` are approval-required. Tell the user a pending approval exists. Do not call `resolve_approval` until they decide.

## Draft and generate

`create_post` writes a draft. Leave `confirmed` unset. Attach media with URLs from `generate_image`, `generate_video`, `generate_voice`, or a URL the user supplied.

## Check

A setup is done when `get_account_info` and `list_brands` both return without an auth error. Do not generate or schedule as the connection test.
