---
name: genfeed
description: Manage Genfeed brand context, draft posts and articles, schedule existing assets, and read content analytics from Claude. Use Genfeed Studio when the user needs images, video or audio.
license: MIT
metadata:
  version: "0.1.5"
---

# Genfeed for Claude

Connect with browser OAuth to `https://mcp.genfeed.ai/mcp/claude`. Use the schemas actually returned by this connector. Start with `get_account` and `get_brands`; if onboarding is incomplete, use `onboard_brand` with the user.

## Content operations

- Read the chosen brand with `get_brand_context`. Write copy in Claude using the brand's voice.
- Save posts with `create_post` and articles with `create_article_draft`. These are drafts. When a tool returns `approval_pending`, give the user the review link and wait; do not bypass the approval or claim the draft already exists.
- Use `list_assets` to find existing media. Use `get_posts` and `get_articles` to review existing content.
- Check `list_brand_publishing_readiness`, `get_scheduler_capabilities` and `validate_scheduler_target` before preparing a release. Only schedule when the user explicitly asks. Scheduling uses existing assets and the user's connected channels.
- Read `get_analytics` and `get_content_analytics` to plan the next content cycle. Use `find_tools` to discover other allowed content operations.

## Create media in Genfeed

For image, video, voice or music requests, write a brief and direct the user to [Genfeed Studio](https://app.genfeed.ai/studio/generate). The app resolves the user's current workspace and brand; confirm the desired brand in Studio. Opening the link does not start generation or spend credits. After the user creates assets, find them with `list_assets` and continue drafting or scheduling in Claude.

This connector cannot generate media, execute workflows or batches, remix assets, run arbitrary agent conversations, or redeem approvals. Never switch to the standard endpoint, CLI or REST API to bypass these restrictions. Changing profile/toolsets cannot unlock them. Never request a password or API key in chat.

Genfeed is available as a custom connector and this self-hosted plugin marketplace. Public directory publication requires review and is not claimed here.
