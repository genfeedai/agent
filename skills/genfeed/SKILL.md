---
name: genfeed
description: >-
  Operate a Genfeed workspace through the hosted MCP server. Use when
  connecting an agent to Genfeed, drafting or scheduling posts, generating
  image, video, or voice, checking brands, credits, or channels, or handling
  a pending Genfeed approval.
license: MIT
metadata:
  version: "0.1.12"
---

# Genfeed

The MCP server is hosted. This skill is the playbook. Tool names, arguments, and approval flags are in `references/tools.md`. Do not invent a tool.

Every tool except `find_tools`, `get_assets` and `resolve_approval` takes an `action` and one `input` object: `tool(action=..., input={...})`. A retired tool name fails at once and names its replacement; call `find_tools` with `name` to read the live schema of any tool or action before the first call.

## Hard rules

1. Authenticate first. If a call returns 401, stop. Do not search the filesystem, the environment, or the chat for a credential. Do not put a key, token, or secret in the URL. OAuth is the default. An API key is sent only as an `Authorization: Bearer` header, after the user creates one with `genfeed login` and `genfeed keys create -n "<label>" -p mcp` (`gf` is the same CLI).
2. Never guess a brand, an organization or a channel. Call `get_context` with `action: brands` and pass the selected brand's returned `id` as `brandId`. When `get_context` with `action: organizations` lists several organizations, every call must also pass `organization` (name, slug or id). Take `credentialId` from `check_channel` with `action: readiness` and `input: {brandId}`. To connect a channel, call `setup_brand` with `action: connect_account` (or `action: connect_oauth`, which also returns a connect button) and `input: {platform, brandId}`, let the owner finish browser consent, and poll `check_channel` with `action: connection_status`. Do not invent either id.
3. Before scheduling, call `check_channel` with `action: capabilities` and `input: {platform}`, then `action: validate` with the proposed target in `input`. Do not schedule a target that comes back with errors.
4. Posts stay drafts. `save_post` saves a draft and never publishes or schedules. Headless publishing goes through `schedule_release`, `get_content` (`action: release`) and `control_release`. A call that changes publishing (`schedule_release` with a scheduled status or date, `control_release` with publish-now, resume or publish) changes nothing on the first call and returns what to confirm. Show the person that, and repeat the call with `confirmed: true` in `input` only after they agree in this conversation to exactly that call. Never set `confirmed` on your own.
5. Media comes from `generate_media` with `action: media` and `input.type` set to `image`, `video`, `voice`, `music` or `avatar`, or from a URL the user already has. Inspect `get_generation_catalog` with `action: options` (pass `input.type` for a credit estimate) before choosing models, settings or a credit budget, and poll `check_job` with `action: job` and `input: {jobId}` until the job ends. Local-file uploads use `upload_media` with `action: request` and the file details in `input`, transfer bytes to the returned upload URL using its method and headers (`PUT` for bytes or `POST_JSON` for `localUpload` with base64 bytes in `localUpload.source.data`), then `upload_media` with `action: complete` and `input: {assetId}`; never invent an asset ID or URL.
6. A pending approval is the user's decision. It is decided in the Genfeed review inbox, never by the agent. `resolve_approval` is listed only on the staff endpoint (`/mcp/admin`); a standard connection does not list it, so do not look for it or work around its absence. Tell the user an approval is pending, with its link or ID, and stop. Never claim that a pending action has completed.
7. Call `get_context` with `action: account` (it returns the credit balance and usage) before batch generation or batch scheduling.
8. Connect to `https://mcp.genfeed.ai/mcp`. The server ignores the `toolsets` and `profile` query (checked against genfeedai/genfeed.ai v0.3.8), so every connection lists every tool its endpoint and the caller's role allow; the packaged URL keeps the query only so installed clients stay valid. Use `find_tools` without arguments to list the tools, with `query` to search by tool or action name, and with `name` to inspect one schema, its permissions and its credit cost. Do not guess a tool name.

## Connect

Streamable HTTP. Preferred URL:

`https://mcp.genfeed.ai/mcp?toolsets=core,scheduler,content,generation,analytics,brand,knowledge,onboarding`

The server lists the same tools with or without the query; `find_tools` tells you what the connected endpoint serves.

## Library and missing tools

Use `get_assets` to show the Library as native gallery cards. Its required `type` selects image, video, music, avatar, character, voice or digital_twin; `limit` and `offset` paginate media. Use the intended brand's returned `id` as `brandId`, or omit it for the connection's current scope. Use the tool's gallery before opening the browser.

If a discovered tool is absent from the client's callable tools, describe it with `find_tools` and `name`. Refresh the client's MCP tools or reconnect to the same URL; discovery describes tools but does not load them into the client. Preserve endpoint restrictions and authentication. Reinstallation and wider permissions do not repair a stale list.

OAuth, from the product connect helper:

- Claude Code: `claude mcp add --transport http genfeed --scope user <url>`, then `/mcp`, select genfeed, and finish browser sign-in.
- Codex: `codex mcp add genfeed --url <url>`, then `codex mcp login genfeed` if the browser did not open.
- Any other client: add the URL as a remote Streamable HTTP server and choose OAuth.

API key, only when the client has no OAuth. The user runs `genfeed login`, then `genfeed keys create -n "<label>" -p mcp`, and the client sends `Authorization: Bearer <key>`. Codex can store that as `--bearer-token-env-var GENFEED_API_KEY`. Never append the key to the URL.

## Schedule

1. `get_context` with `action: brands`, then keep `brandId`.
2. `check_channel` with `action: readiness` and `input: {brandId}`. Keep `credentialId` for a healthy channel. If the user still needs to connect, start `setup_brand` with `action: connect_account` and poll `check_channel` with `action: connection_status`.
3. `check_channel` with `action: capabilities` and `input: {platform}`, then `action: validate` with the target in `input`.
4. `get_context` with `action: account` when this is one of several posts.
5. `schedule_release` with `action: create` and `input: {release: {title, baseContent, timezone, targets: [{credentialId, platform}]}}`, or `input: {releases: [...]}` for a batch of one post per channel; never put the release fields at the top of `input`. Leave `status` as `draft` unless the user asked to schedule, and pass `scheduledDate` (ISO 8601 with offset) for a scheduled one.
6. A scheduled create returns what to confirm and changes nothing. Show it, and after the user agrees repeat the same call with `confirmed: true`. Then read the state back with `get_content` with `action: release` and `input: {releaseId}`.
7. `control_release` with `action: control` and `input: {releaseId, action}` (`cancel`, `pause`, `resume` or `publish-now`; resume and publish-now need confirmation, cancel and pause do not). `schedule_release` with `action: update` for edits.

## Draft and generate

`save_post` with `action: post` writes a draft. It has no `confirmed` flag; a pending approval is decided in the Genfeed review inbox. Copy comes from you, using `get_context` with `action: brand_context` and `input: {brandId, contentType, platform}` for the writing rules, or from `generate_text` with `action: content`, which saves a draft and returns a `postId`. Attach media by calling `save_post` again with `input: {postId, brandId, mediaUrls}`, using hosted URLs from `generate_media`, `get_assets`, or a URL the user supplied. `save_post` with `action: article` imports reviewed HTML as an unpublished article draft; publishing it is `control_release` with `action: publish`.

## Check

A setup is done when `get_context` with `action: account` and with `action: brands` both return without an auth error. Do not generate or schedule as the connection test.
