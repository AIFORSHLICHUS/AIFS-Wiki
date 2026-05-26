---
type: tool
slug: video-tools
aliases: [CapCut, Descript, VideoLeap, Gling, Filmora, Pictory, Clipchamp, Captions AI]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Video Editing Tools

Reference page for the video-creation stack used by shluchim — mostly
for **extracting short social-media clips from longer shiur recordings**
and for adding subtitles.

## The lineup

| Tool | Strength | Notes |
| --- | --- | --- |
| **VideoLeap** | Camera-roll clip → Instagram reel. Rayi Stern: *"best I've seen."* [chat 2025-11-24] | Chinese origin; mobile-first. |
| **CapCut** | Free; AI auto-cut option; subtitles. [chat 2026-01-09, 2026-05-24] | Best for quick reels. |
| **Descript** | Video + audio editing with auto-captioning. [chat 2025-08-21, Elisha Pearl] | Subscription. |
| **Gling.ai** | AI video editing / shorts creation. | — |
| **Filmora** (Wondershare) | Full editor. | — |
| **Pictory.ai** | Shorts from long-form content. | — |
| **Clipchamp** | Microsoft's video editor. | Free, web-based. |
| **Opus Clip / Opus.pro** | Extract short clips from long videos; B-roll. [chat 2025-08-03] | Limited upload capacity. |
| **Kapwing** | Browser-based editing. | — |
| **Captions.AI** | Auto-subtitles, $11/mo, works for Hebrew. [chat 2025-11-27, +1 954-478-8015] | — |
| **Riverside.fm** | Recording + auto-subtitles for shiurim. [chat 2025-08-21] | Web-based. |
| **Synthesys AI VSL Studio** | AI video sales letters. [chat 2025-12-05, Rayi Stern] | Newer. |
| **YouTube Create** | YouTube's free editor. Alternative to CapCut. [chat 2026-01-09] | Mobile. |
| **Google Vids** | Workspace's video creator. [chat 2025-08-01] | — |

## Workflow: long shiur → short clips

[chat 2025-08-03, +27 65 944 5633] asked: *"I'd like to use AI to
extract short clips from video recordings of shiurim."*

Best stack the chat has converged on:

1. **Transcribe** with [[sofer-ai]] (Hebrew/Yiddish) or Whisper (English).
2. **Identify highlights** with [[claude]] or [[chatgpt]] — *"give me
   the 30-second clips with the strongest stand-alone teachings."*
3. **Cut** in Descript or CapCut.
4. **Subtitle** in CapCut / Captions.AI / Riverside.

## Avatar generation

Separate path — when you want a *talking-head* video without filming:

- **HeyGen** — text-to-speaking avatar. [chat 2025-12-04]
- **Synthesia** — AI avatars. [chat 2025-12-04]
- **D-ID** — Israeli alternative; possibly better.
  [chat 2025-12-04, +1 818-335-7103]
- **InVideo** — text-to-video with impressive audio.

## Animated video

- **Kling 3.0** — animated videos longer than 10 seconds.
  [chat 2026-02-16, Rabbi Zalman Abraham]
- **Veo (Google)** — emerging video gen.
- **[[sora]]** — for shorter clips with demographic-prompt caveats.
- **Grok** — replaced Sora for one user. [chat 2026-05-07]

## Hebrew subtitles

- **Captions.AI** confirmed works. [chat 2025-11-27]
- **Riverside.fm** for auto-subtitled recording.
- **berel.me/jemsubtitles** by Berel Marozov for shliach-specific
  workflows. [chat 2026-01-27]

## Open issue

[chat 2026-04-27, +1 310-666-2302]: *"Is there AI that I can upload
shorts or classes to and it automatically fills it with B-roll?"*
Captions.AI suggested but not confirmed end-to-end for B-roll
generation.

## Related

- [[../topics/transcription]]
- [[../topics/shiur-prep]]
- [[sora]]
- [[sofer-ai]]
