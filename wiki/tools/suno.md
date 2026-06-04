---
type: tool
slug: suno
aliases: [Suno, Suno.com]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Suno

AI music generation — from lyrics and a hummed melody to a full
produced song. Free tier; ~$8 for a polished song.

## What the chat uses it for

- **Custom Purim songs** with your year's theme, town, even guests'
  names. [chat 2026-02-16, +1 520-703-7466]
- **Niggun production from a voice recording.** Sing into the phone;
  Suno turns it into a full arrangement. *"Rivals Tzama quality."*
  [chat 2025-11-26]
- **Sefira-period a-cappella.** *"If you want some sefira entertainment
  you can turn any song into acapella with Suno."*
  [chat 2026-04-12]
- **Chanukkah event theme songs.** [chat 2026-02-16]

## Workflow

1. **Lyrics**: have ChatGPT/Gemini write Purim/Chanukah/event-themed
   lyrics including local color (town name, year, theme).
2. **Music**: paste lyrics + style cue into Suno.
3. **Cover existing tunes**: hit *"cover"* in Suno instead of generating
   a new song; produces a version of *your* tune with new vocals/
   production.
4. **Pronunciation fix** for Hebrew/Yiddish: write transliteration as
   `Khabad` / `samayakh`, not `Chabad` / `samayach`.
   [chat 2026-02-16, +1 520-703-7466]

## Strengths

- Free now (used to be paid).
- Voice → full production is uncanny.
- Cover mode preserves an existing tune.

## Weaknesses

- Mispronounces Hebrew/Yiddish unless you transliterate manually.
- Style consistency across multiple songs is hit-or-miss.

## Related toolkit

- **BasicPitch** (Spotify, free) — audio → MIDI.
- **MuseScore** (free) — MIDI → formal sheet music.
- **Remusic.ai** — AI sheet music generator.
- **Moises.app** — voice removal / a cappella extraction. Free.
- **AI Galaxy Acapella** — `aigalaxy.app/acapella`.
- **NovelEffect** — sound effects with voice recognition (children's
  books). [chat 2026-02-20]

The full "free sheet music" pipeline [chat 2025-11-28]:

> *Step 1: Convert audio → MIDI using BasicPitch (free, super accurate
> for melody). basicpitch.spotify.com.*
>
> *Step 2: Open the MIDI in MuseScore (also free). musescore.org. It
> auto-converts MIDI notes → formal sheet music. Clean up timing
> (quantize to quarter/eighth notes). Add lyrics/chords if needed.
> Export to PDF, MusicXML, or PNG.*

## Related

- [[../topics/hebrew-yiddish]] — pronunciation tricks.
- [[../resources/master-prompts]] — lyrics-writing prompts.
- [[elevenlabs]] — TTS counterpart for spoken Hebrew.
