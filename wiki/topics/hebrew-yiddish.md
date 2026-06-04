---
type: topic
slug: hebrew-yiddish
aliases: [hebrew, yiddish, multilingual, translation, ksav yad, RTL]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Hebrew &amp; Yiddish

Three problems collapse into this topic: **translation**,
**right-to-left layout**, and **transcription / OCR**. Each has a
different best-tool answer.

## Translation

**Surprise winner for pure Hebrew/Yiddish translation: [Qwen](https://chat.qwen.ai/).**

After testing eight LLMs:
> *"Qwen doesn't just give the translation, he also provides the
> etymology, the root (shoresh), occurrences, and a word-by-word
> transliteration. It's very practical. He also gives the context of
> the verse."*
> — [chat 2026-04-16, +33 6 51 82 35 18]

Runners-up:
- **Claude** — best at *Yiddish*, which is hard for everyone (Yiddish OCR
  &gt; Hebrew OCR in difficulty). A bake-off was run [chat 2026-04-21]
  between Opus 4.7, Sonnet, Gemini 2.5 Pro and Flash for Yiddish OCR.
- **Gemini Pro** — strong on modern Hebrew, integrates with Workspace.

**For specifically translating a Yiddish or Hebrew shiur to English**:
[[../tools/sofer-ai]] for transcription, then any of the above for
translation. "sofer.ai" recommended specifically for
Yiddish/Hebrew audio. [chat 2026-02-01]

## Transcription

Best per language:

| Language | Tool | Notes |
| --- | --- | --- |
| Hebrew (modern) | [[../tools/sofer-ai]] | Built for shiurim; handles mixed Hebrew/English/Yiddish. |
| Hebrew (modern, free) | `transcribe.ivrit.ai` | Free Hebrew-only transcription. [chat 2025-12-02] |
| Yiddish | [[../tools/sofer-ai]] or Whisper | Whisper + Parakeet models with heavy lifting. ~6/10 quality per [chat 2025-11-05, Yossi Lipskier]. |
| English with Hebrew terms | Whisper, MacWhisper, Turboscribe | Handles the code-switching reasonably. |
| Ashkenazi Hebrew pronunciation | n/a | Trick: write the text in Hebrew with *nikkud* tuned for Ashkenazi sounds; ElevenLabs V3 then pronounces correctly. [chat 2025-11-21] |

See [[transcription]] for the full tool comparison.

## RTL &amp; image-text problems

Every image-gen model garbles Hebrew. The two reliable workarounds:

1. **Strip-and-replace.** Generate the visual, then ask the model to
   *remove Hebrew letters leaving placeholders, change nothing else*.
   Type the Hebrew in [[../tools/canva]] (or Affinity) where you
   control the font. [chat 2026-05-19, +44 7980-795936]
2. **Background-only.** Generate the visual background only;
   compose the Hebrew text on top in Canva.
   [chat 2025-11-20]

For *typeset* documents (magazines, source sheets):
- Use **LaTeX** or **Typst**, not DOCX. Claude knows LaTeX well.
  [chat 2026-03-09]
- Set a *golden rule* at the top of the chat: "Hebrew goes
  right-to-left." "Do not edit my Hebrew text." Claude needs
  reminding to keep sentence order intact.
  [chat 2026-05-19, +44 7980-795936]

## Hebrew OCR

This remains the rough edge:

- **Rashi script.** *"I'm trying to run a text through AI, but can't
  find anything to read Rashi script, is there any rashi script OCR?"*
  — [chat 2025-11-18, +1 758-718-1172]. **Unresolved as of 2026-05.**
- **Hebrew print (square letters).** Decent options exist:
  - **Google DocumentAI** ($300 free credit on Google Cloud).
    [chat 2025-09-11]
  - **Google Lens** / Google Drive → "Open in Google Docs."
  - **i2ocr.com** — free online Hebrew OCR, often better than LLMs for
    raw text extraction. [chat 2026-05-24]
- **Likkutei Sichos PDF (two-column, footnotes mixed in).**
  Direct ChatGPT upload "a disaster." Better path: use
  [[../tools/dach-dev]] or the Anash.org Likkutei Sichos app for plain
  text export, then translate. [chat 2025-11-04]
- **Hebrew handwriting (*ksav yad*).** `chabad.mekorotai.dicta.org.il`
  exists but as of [chat 2026-02-17, +1 415-634-7727]: "Nah" — not yet
  reliable.

## Text-to-speech in Hebrew / Yiddish

[[../tools/elevenlabs]] V3 is the leader for reliable *ches/chet*,
*ayin*, and *vav* distinctions. Trick: write input in *Ashkenazi
transliteration* or with strategic *nikkud* to force pronunciation
([chat 2025-11-21]).

**Suno** can produce Hebrew songs but mispronounces; trick is to write
"Khabad" instead of "Chabad", "samayakh" instead of "samayach".
[chat 2026-02-16, +1 520-703-7466]

## Pronunciation hacks

- Write `מחודש` with explicit *nikkud* matched to Ashkenazi vowels.
- Write `Khabad` not `Chabad` for English-speaking TTS engines.
- Write `samayakh` not `samayach` for Suno.

## Open questions

- Rashi script OCR (still open).
- Yiddish (vs. Hebrew) transcription quality.
- Custom dictionary for Gboard talk-to-text to learn *tefillin*,
  *tichel*, *Chabad* — [chat 2025-08-25, +1 415-634-7727]. No fix yet.

## Related

- [[../tools/sofer-ai]]
- [[../tools/elevenlabs]]
- [[../tools/notebooklm]]
- [[../tools/dach-dev]]
- [[../themes/ai-flyer-aesthetics]]
- [[transcription]]
