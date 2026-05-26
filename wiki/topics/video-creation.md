---
type: topic
slug: video-creation
aliases: [video, reels, shorts, social video, video editing]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Video Creation

Pulling video out of shiurim, generating short-form social content,
adding subtitles. A persistent chat topic — *"how do I make a reel
from this 90-minute class?"* — without a single clean answer.

## The standard workflow

1. **Record** the shiur (phone, Zoom, Riverside, lapel mic).
2. **Transcribe** with [[../tools/sofer-ai]] (Hebrew/Yiddish/English
   mix) or Whisper/Turboscribe (English).
3. **AI-pick the highlights.** Paste transcript into
   [[../tools/claude]]: *"Identify the 30-second clips most
   stand-alone-worthy."* Get timestamps.
4. **Cut clips** in [[../tools/video-tools]] (Descript / CapCut /
   VideoLeap).
5. **Add subtitles.** Captions.AI ($11/mo, works for Hebrew),
   Riverside.fm, or built-in CapCut.
6. **Post**.

## Generation paths (no source video)

- **[[../tools/sora]]** — short clips, demographic-prompt caveats.
- **Grok** — increasingly preferred when Sora refuses.
- **Kling 3.0** — animated, &gt;10 seconds.
- **Veo (Google)** — emerging.
- **InVideo** — text-to-video, decent audio.

## Avatar / talking-head paths

- **HeyGen** — text-to-speaking avatar.
- **Synthesia** — same category.
- **D-ID** — Israeli alternative; *"possibly better."*
- **NotebookLM Video Overview** — generates a host-and-guest podcast
  video from uploaded sources, with Nano-Banana-generated illustrations.

## Music for video

- **Suno** — custom songs.
- **Moises.app** — remove vocals from existing tracks.
- **AI Galaxy Acapella** — extract a cappella.

## The unresolved problems

- **B-roll generation** from a shiur transcript. No turnkey solution.
- **Hebrew subtitles** at production quality. Captions.AI works;
  others spotty.
- **Lip-sync language change** (English shiur → Hebrew with voice
  cloning). Asked [chat 2026-05-07]; no clean answer.

## Specific shliach use cases

- **Avraham Fried's AI Moshiach video** — `youtu.be/vrzCfLPTOcI` —
  cited as a quality bar.
- **Mivtzoim flyer-to-video** — turn a flyer into a short reel by
  generating supporting B-roll. Possible with Captions.AI; needs
  practice.

## Related

- [[../tools/video-tools]] — full tool roster.
- [[../tools/sora]]
- [[../tools/suno]]
- [[transcription]]
- [[shiur-prep]]
