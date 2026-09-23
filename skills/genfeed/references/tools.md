# Genfeed MCP tools

Generated from `packages/actions/src/registry/curated-action-catalog.ts` (entries whose `surfaces` include `mcp`) joined with definitions in `packages/actions/src/registry/source/**` and `MUTATION_POLICY_BY_NAME`.

Count: 123. Toolsets: ads, agent-chat, analytics, brand, clips, content, core, generation, inspiration, knowledge, onboarding, scheduler, skills-pro, social-inbox, workflows.

Approval means `mutationPolicy: 'approval-required'`. Calling that tool queues a pending approval. Call `resolve_approval` only after the user decides.

| Tool | Toolset | Required | Approval | Description |
| --- | --- | --- | --- | --- |
| `compare_meta_campaigns` | ads | `campaignIds` | no | Compare performance metrics side-by-side for multiple Meta campaigns |
| `get_ad_research_detail` | ads | `adId`, `source` | no | Inspect one ad from ads research and return its creative, metrics, and reusable pattern explanation. |
| `get_ads_ad_insights` | ads | `platform`, `credentialId`, `adAccountId`, `adId` | no | Get performance insights for a single ad on any connected ads platform (Meta ad, Google Ads ad, TikTok ad, or X ad) through the platform-generic ads gateway |
| `get_ads_adset_insights` | ads | `platform`, `credentialId`, `adAccountId`, `adSetId` | no | Get performance insights for one ad set on any connected ads platform (Meta ad set, Google Ads ad group, TikTok ad group, or X ad group) through the platform-generic ads gateway |
| `get_google_ads_adgroup_insights` | ads | `customerId`, `adGroupId` | no | Get performance insights for a Google Ads ad group |
| `get_google_ads_campaign_metrics` | ads | `customerId`, `campaignId` | no | Get detailed metrics for a Google Ads campaign including impressions, clicks, cost, conversions, CTR, and CPC |
| `get_google_ads_keyword_performance` | ads | `customerId` | no | Get keyword performance report with quality scores, clicks, impressions, and cost |
| `get_google_ads_search_terms` | ads | `customerId`, `campaignId` | no | Get search terms report showing actual search queries that triggered your ads |
| `get_meta_ad_insights` | ads | `adId` | no | Get performance insights for an individual Meta ad including creative details |
| `get_meta_adset_insights` | ads | `adSetId` | no | Get performance insights for a Meta ad set |
| `get_meta_campaign_insights` | ads | `campaignId` | no | Get detailed performance insights for a Meta ad campaign including spend, impressions, clicks, CTR, CPC, CPM, and conversions |
| `get_meta_top_performers` | ads | `adAccountId`, `metric` | no | Get top performing Meta ads sorted by a specific metric (CTR, ROAS, CPC, etc.) |
| `get_tiktok_campaign_insights` | ads | `credentialId`, `adAccountId`, `campaignId` | no | Get detailed performance insights for a TikTok ad campaign including spend, impressions, clicks, CTR, CPC, CPM, and conversions |
| `list_ads_research` | ads | — | no | List top-performing public and connected ads by niche, platform, source, metric, and timeframe. |
| `list_google_ads_campaigns` | ads | `customerId` | no | List Google Ads campaigns with optional status filter |
| `list_google_ads_customers` | ads | — | no | List accessible Google Ads customer accounts |
| `list_meta_ad_accounts` | ads | — | no | List connected Meta (Facebook) ad accounts |
| `list_meta_ad_creatives` | ads | `adAccountId` | no | List creative assets (headlines, body text, CTAs, images) for Meta ads |
| `list_meta_campaigns` | ads | `adAccountId` | no | List Meta ad campaigns with optional status filter and pagination |
| `list_tiktok_ad_accounts` | ads | `credentialId` | no | List TikTok advertiser accounts for a connected credential |
| `list_tiktok_adgroups` | ads | `credentialId`, `adAccountId`, `campaignId` | no | List TikTok ad groups within a campaign |
| `list_tiktok_ads` | ads | `credentialId`, `adAccountId` | no | List TikTok ads, optionally narrowed to a single ad group. Returns creative details alongside each ad |
| `list_tiktok_campaigns` | ads | `credentialId`, `adAccountId` | no | List TikTok ad campaigns for an advertiser account |
| `create_chat` | agent-chat | — | no | Start a new agent conversation |
| `send_chat_message` | agent-chat | `threadId`, `message` | no | Send a message in an existing agent conversation |
| `analyze_performance` | analytics | — | no | Analyze recent content performance over the last 30 days. Returns engagement rates grouped by content type, platform, and posting time, plus top-performing posts. |
| `get_analytics` | analytics | — | no | Get analytics data for the user. Can specify a time range and metrics. |
| `get_content_analytics` | analytics | `contentId`, `contentType` | no | Get analytics for a specific piece of content (article, video, or image) |
| `get_linkedin_analytics` | analytics | `contentId` | no | Get analytics for LinkedIn posts including impressions, engagement rate, reactions, comments, and shares. Requires a content ID. |
| `get_linkedin_connection_status` | analytics | — | no | Check whether a LinkedIn account is connected for the current user. Returns connection status, handle, and avatar if connected. |
| `get_trends` | analytics | — | no | Get trending topics and content ideas based on current trends across social media and news. |
| `get_video_analytics` | analytics | `videoId` | no | Get detailed analytics for a specific video |
| `get_brand_completeness` | brand | `brandId` | no | Get the current brand context completeness score and a list of fields that still have gaps. Read-only, no credits charged. |
| `list_brand_publishing_readiness` | brand | `brandId` | no | List a brand connected publishing channels with credential ID, schedulability, health, and diagnostics. Read-only; check before scheduling. |
| `skip_brand_interview_question` | brand | `interviewId` | yes | Skip the current interview question (e.g. the user doesn't know or wants to skip). Returns the next question and updated progress. |
| `start_brand_interview` | brand | `brandId` | yes | Start a brand context interview for the given brand. Charges 10 credits once (idempotent — resuming an active session does not re-charge). Returns the first question to ask the user, plus progress and completeness info. |
| `submit_brand_interview_answer` | brand | `interviewId`, `answer` | yes | Submit the user's answer to the current interview question. Pass the interviewId from start_brand_interview. Returns the next question (if any) and updated progress. |
| `analyze_clip_project` | clips | `youtubeUrl` | yes | Analyze a YouTube video for viral highlights: downloads audio, transcribes, and LLM-detects segments (1 credit). Poll with get_clip_project or get_clip_highlights. |
| `create_clip_project_from_youtube` | clips | `youtubeUrl` | yes | Create a clip project from a YouTube URL and run the AI clip factory async (1 credit/clip). HeyGen/Argil need avatarId+voiceId; GenfeedAI needs a brand character reference. Poll get_clip_project. |
| `generate_clips` | clips | `projectId`, `selectedHighlightIds`, `editedHighlights` | yes | Generate clips from selected highlights (1 credit/clip). Avatar: avatarId+voiceId (HeyGen/Argil) or character ref (GenfeedAI); raw-cut: neither. |
| `get_clip_highlights` | clips | `projectId` | no | Get the detected highlights for a clip project after analysis. Returns the highlights array plus the project's current status. |
| `get_clip_project` | clips | `projectId` | no | Read a clip project by ID: status, progress, highlights, and generated clip results (with playable video URLs when ready). Poll this after analyze or generate. |
| `list_clip_projects` | clips | — | no | List clip projects in your organization, most recent first. Returns id, name, status, and progress for each. |
| `create_article` | content | `topic` | yes | Generate viral AI-powered articles with SEO optimization. Specify topic, tone, length, target audience, and keywords for maximum engagement. |
| `create_post` | content | — | yes | Create a post draft, or confirm direct publishing for an existing item via a confirmation card. |
| `fetch_x_post` | content | `postIdOrUrl` | no | Open one X post from a link or post id and return its text and stats. |
| `generate_content_batch` | content | `count`, `platforms` | yes | Generate a batch of content (images, videos, carousels) for a brand. Specify count, platforms, and date range. Use handle param to resolve @username to a credential. Returns a batch ID for tracking. Credits scale by item format and caption model tier — not a flat fee. |
| `generate_linkedin_content` | content | `topic` | no | Generate LinkedIn-optimized post text for a given topic or brief. Returns ready-to-publish text content with hook, body, CTA, and hashtags. |
| `get_article` | content | `articleId` | no | Get a specific article by ID |
| `get_content_calendar` | content | — | no | Get the content calendar for the coming week. Returns scheduled and draft posts with gap analysis showing days without content. |
| `list_posts` | content | — | no | List recent posts for the user. Can filter by target execution state (draft, scheduled, published). |
| `repurpose_post` | content | `postId`, `platform`, `mode` | no | Repurpose an existing post into a draft for another channel. Deterministic mode adapts the caption instantly through the channel capability catalog (length, hashtags, links, media compatibility); agent mode rewrites it with the content engine and lands the draft in the review queue. Never publishes or schedules anything. |
| `search_articles` | content | `query` | no | Search published articles by query, category, or tags. Filter and find content quickly. |
| `search_x_posts` | content | `query` | no | Search recent posts on X by topic. Returns posts with author, text, stats, and link. Explains clearly if the connected account cannot search. |
| `describe_tool` | core | `name` | no | Describe one tool by exact name, returning its full input schema, toolset, mutation policy, credit cost, and required role. Useful for a tool that was filtered out of tools/list by the connection toolsets. |
| `get_account_info` | core | — | no | Get current account info including user, organization, scopes, and active brand |
| `get_brand` | core | — | no | Get details of a selected brand. When an organization has more than one brand, pass brandId; the first brand is never chosen automatically. |
| `get_credits_balance` | core | — | no | Get available credits balance and usage information for your account |
| `get_job_status` | core | `jobId` | no | Check the status of a content generation job. Auto-detects content type. |
| `get_usage_stats` | core | — | no | Get detailed usage statistics including content created, credits used, and account activity |
| `list_brands` | core | — | no | List the user's brands with their names, descriptions, and tone profiles. |
| `list_toolsets` | core | — | no | List the toolsets available on this server, each with its description and tool count. Use this to see what a narrower ?toolsets= connection is missing. |
| `resolve_approval` | core | `approvalId`, `decision` | no | Approve or decline a pending MCP write action that was queued for human review, executing it on approval. Pass the approvalId returned by the original (pending) tool call. Superadmin-only. |
| `search_tools` | core | — | no | Search for tools by name/description substring and/or toolset. Provide at least one of query or toolset. Returns a summary per match — use describe_tool for the full schema of a specific tool. |
| `generate_image` | generation | `prompt` | no | Generate AI images with a custom prompt, style, and dimensions. |
| `generate_music` | generation | `prompt` | no | Generate music or audio using AI. Describe the desired music style, mood, instruments, and genre. Returns the audio URL. |
| `generate_video` | generation | `prompt` | no | Generate a video from a prompt. Add imageUrl+audioUrl for talking-avatar lip-sync. Returns the video URL. |
| `generate_voice` | generation | `text` | no | Generate speech audio from text using text-to-speech. If you do not already have a catalog or cloned voiceId, omit voiceId and call prepare_voice_clone instead so the user can pick a voice from the catalog. Do not ask the user to open Library → Voices. |
| `get_video_status` | generation | `videoId` | no | Check the status of a video creation job |
| `list_avatars` | generation | — | no | List all available avatars |
| `list_characters` | generation | — | no | List the current brand's active named characters (handle, label, description, whether a reference image exists). Tenant-scoped. |
| `list_images` | generation | — | no | List all generated images |
| `list_music` | generation | — | no | List all generated music tracks |
| `list_videos` | generation | — | no | List all videos in your organization |
| `reframe_image` | generation | `imageId` | no | Reframe an existing image to a new aspect ratio. Provide imageId and target aspect ratio. |
| `upscale_image` | generation | `imageUrl` | no | Upscale an existing image to higher resolution. Provide the image URL or asset ID. |
| `get_instagram_inspiration_detail` | inspiration | `username` | no | Fetch latest or top public posts from one Instagram account and return provenance plus abstract hook, format, pacing, and style signals. |
| `get_tiktok_top_performers` | inspiration | `credentialId`, `adAccountId` | no | Get top performing TikTok ads sorted by a specific metric (CTR, CPC, spend, etc.) |
| `list_instagram_inspiration` | inspiration | — | no | Discover public Instagram accounts and content patterns relevant to the selected brand niche. |
| `archive_knowledge_source` | knowledge | `sourceId` | no | Archive a Knowledge source so it never appears in retrieval again. Its receipts on past outputs are kept. |
| `assign_knowledge_purpose` | knowledge | `sourceId` | no | Change the purpose of a Knowledge source (Brand Truth, Inspiration, Research) and optionally hide it from retrieval. |
| `capture_knowledge` | knowledge | — | no | Save a page, document, feed, media or pasted text into the brand Knowledge library and start ingestion. Pass sourceId to refresh an existing URL or RSS source. Default purpose is INSPIRATION; pass BRAND_TRUTH only for material the brand owns and vouches for. |
| `list_knowledge_sources` | knowledge | — | no | List the brand Knowledge sources with their purpose, processing state and failure reason. |
| `read_knowledge_source` | knowledge | `sourceId` | no | Read one Knowledge source: metadata, current version state, provenance, a bounded text preview and the spaces it belongs to. |
| `retry_knowledge_ingestion` | knowledge | `sourceId` | no | Requeue ingestion for a Knowledge source whose last attempt failed. Never creates a duplicate. |
| `search_knowledge` | knowledge | `query` | no | Search the brand Knowledge library (saved pages, documents and notes) and return cited passages with their source, purpose and relevance. Use it before writing anything that must be accurate about the brand. |
| `connect_social_account` | onboarding | `platform` | no | Start a resumable social-account connection. Returns a connectionId and browser authorization URL. Poll get_connection_status until authorized. |
| `get_connection_status` | onboarding | — | no | Get connection status for a social platform or a durable connection request id. Safe to poll. |
| `initiate_oauth_connect` | onboarding | `platform` | no | Start connecting a social account and return a durable connection request plus a connect button. |
| `control_scheduled_release` | scheduler | `releaseId`, `action` | yes | Control a scheduled release lifecycle: cancel, pause, resume, or publish now. |
| `create_scheduled_release` | scheduler | `release` | yes | Create a multi-channel scheduled release. |
| `get_scheduled_release` | scheduler | `releaseId` | no | Get one scheduled release by ID: channel targets, validation/execution state, attachments, recurrence, and transition history. |
| `get_scheduler_capability` | scheduler | `platform` | no | Get one scheduler channel capability by platform: caption limits, media rules, publish modes, required settings, status. Read-only. |
| `list_scheduler_capabilities` | scheduler | — | no | List scheduler channel capabilities: platforms, caption limits, media rules, publish modes, required settings. Read-only. |
| `update_scheduled_release` | scheduler | `releaseId`, `scope`, `changes` | yes | Update a release or a target. |
| `validate_scheduler_target` | scheduler | `platform` | no | Validate a proposed target against the channel-capability contract; returns errors/warnings/validationState. Read-only. |
| `install_skills_pro_skill` | skills-pro | `receiptId`, `skillSlug` | yes | Install one entitled Skills Pro pack into the authenticated organization runtime after integrity verification. |
| `verify_skills_pro_entitlement` | skills-pro | `receiptId` | no | Verify a Skills Pro receipt for the authenticated organization and list the exact skill slugs it grants. |
| `approve_social_draft` | social-inbox | `conversationId`, `messageId` | yes | Approve a social inbox draft and publish it externally as a reply or DM. Requires approval before execution. |
| `assign_social_conversation` | social-inbox | `conversationId` | no | Assign or unassign a social inbox conversation. |
| `create_social_reply_draft` | social-inbox | `conversationId`, `text` | no | Create a draft reply or DM in the social inbox for later approval. This does not send externally. |
| `get_social_conversation` | social-inbox | `conversationId` | no | Get one social inbox conversation and, by default, its recent messages. |
| `list_social_conversations` | social-inbox | — | no | List social inbox conversations across connected YouTube and Instagram accounts, with filters for review state, assignee, tags, and platform. |
| `list_x_account_activity` | social-inbox | — | no | List recent posts from an X account. Uses the brand's connected account when no username is given. |
| `mark_social_conversation_resolved` | social-inbox | `conversationId` | no | Mark a social inbox conversation as resolved. |
| `post_social_reply` | social-inbox | `conversationId`, `text` | yes | Publish a reply in a social inbox conversation. Requires approval before execution. |
| `reject_social_draft` | social-inbox | `conversationId`, `messageId` | no | Reject a social inbox draft without publishing it externally. |
| `send_social_dm` | social-inbox | `conversationId`, `text` | yes | Send a direct message from a social inbox conversation. Requires approval before execution. |
| `tag_social_conversation` | social-inbox | `conversationId`, `tags` | no | Replace tags on a social inbox conversation. |
| `create_ad_remix_workflow` | workflows | `adId`, `source` | yes | Create a draft, review-only ad remix workflow from a selected public or connected ad. This never launches an ad. |
| `create_instagram_remix_workflow` | workflows | `username`, `shortcode` | yes | Create a draft, review-only Instagram remix workflow that adapts a public post pattern to the selected brand. This is prompt-based reinterpretation, not video style transfer. |
| `create_workflow` | workflows | `label` | no | Create a workflow: direct graph, a recurring scaffold, or natural-language generation. Editable in the Workflows app. |
| `duplicate_workflow` | workflows | `workflowId` | no | Duplicate a workflow into the current organization and brand scope so the copy can be edited or scheduled without mutating the source workflow. |
| `execute_workflow` | workflows | `workflowId` | no | Execute an existing workflow immediately. Select nodeIds to rerun edited steps while reusing locked outputs; pass required variables for full or partial execution. |
| `get_workflow_run` | workflows | `runId` | no | Inspect a single workflow run, including status, trigger, node results, progress, timing, errors, and metadata. |
| `get_workflow_status` | workflows | `workflowId` | no | Get the current status and progress of a workflow, including step completion details. |
| `inspect_workflow` | workflows | `workflowId` | no | Inspect one workflow, including schedule, lifecycle, inputs, graph summary, and immutable system-workflow metadata when present. |
| `install_system_workflow` | workflows | `canonicalId` | no | Install one system workflow catalog entry into the current organization as an editable, schedulable copy. Installing the same entry twice returns the existing workflow. |
| `list_system_workflow_catalog` | workflows | — | no | List the code-owned Genfeed system workflow catalog with per-organization install state. Use this to discover official automations before installing one. |
| `list_workflow_runs` | workflows | — | no | List workflow run history with optional workflow, status, trigger, limit, and offset filters. |
| `list_workflow_templates` | workflows | — | no | List available workflow templates that can be used to quickly create new workflows. |
| `list_workflows` | workflows | — | no | List all workflows in your organization with optional status filtering. |
| `set_workflow_schedule` | workflows | `workflowId`, `enabled` | no | Enable, disable, or update the schedule on an editable workflow duplicate. Disabling requires no new cron expression when the workflow already has one. |
