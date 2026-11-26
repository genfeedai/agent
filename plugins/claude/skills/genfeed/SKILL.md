---
name: genfeed
description: Manage Genfeed brand context, draft posts and articles, schedule existing assets, and read content analytics from Claude. This connector does not generate images, video or audio.
license: MIT
metadata:
  version: "0.1.12"
---

# Genfeed for Claude

Connect with browser OAuth to `https://mcp.genfeed.ai/mcp/claude`. Use the schemas actually returned by this connector. It lists ten tools, and every one but `find_tools` and `get_assets` takes an `action` plus one `input` object. Start with `get_context` (`action: account`, then `action: brands`); if onboarding is incomplete, use `setup_brand` with `action: onboard` and the user. When `get_context` with `action: organizations` lists several organizations, pass `organization` on every call.

## Content operations

- Read the chosen brand with `get_context` (`action: brand_context`, `input: {brandId, contentType, platform}`). Write copy in Claude using the brand's voice and the writing rules it returns.
- Save posts with `save_post` (`action: post`) and articles with `save_post` (`action: article`, then `action: article_update` to edit). These are drafts and `save_post` never publishes. When a call returns “approval_pending”, give the user the review link and wait; do not bypass the approval or claim the draft already exists. Attach existing media by calling `save_post` again with `input: {postId, brandId, mediaUrls}`.
- Use `get_assets` to show existing media in the native Library gallery. Use `get_content` (`action: posts`, `action: release`, `action: articles` or `action: article_preview`) to review existing content.
- Check `check_channel` with `action: readiness` and `input: {brandId}`, then `action: capabilities` with `input: {platform}` and `action: validate` with the proposed target in `input`, before preparing a release. Only schedule when the user explicitly asks. `schedule_release` (`action: create` or `update`) uses existing assets and the user's connected channels; a scheduled create changes nothing on the first call and returns what to confirm, so show it and repeat with `confirmed: true` in `input` only after the user agrees in this conversation. `control_release` (`action: control` or `publish`) follows the same confirmation for publish-now, resume and publish.
- Read `get_insights` (`action: overview`, `action: content`, `action: video`, `action: linkedin`, `action: performance` or `action: trends`) to plan the next content cycle. Use `find_tools` to discover other allowed content operations.

## Create media in Genfeed

For image, video, voice or music requests, say plainly that this connector does not generate them and offer what it can do: write a brief or caption. Do not send the user to another page or tool. When the user has assets, find them with `get_assets` and continue drafting or scheduling in Claude.

This connector cannot generate media, execute workflows or batches, remix assets, run arbitrary agent conversations, or decide approvals (they are decided in the Genfeed review inbox). Never switch to the standard endpoint, CLI or REST API to bypass these restrictions. Changing profile/toolsets cannot unlock them. Never request a password or API key in chat.

If an allowed tool is missing from Claude's callable tools, use `find_tools` with its `name` to inspect discovery. When `connection.isListed` is true, refresh the client tool list or reconnect to the same `/mcp/claude` endpoint. Discovery describes tools; it does not attach them to the client. Keep this connector's endpoint and permissions.

Genfeed is available as a custom connector and this self-hosted plugin marketplace. Public directory publication requires review and is not claimed here.
