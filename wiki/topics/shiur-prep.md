---
type: topic
slug: shiur-prep
aliases: [shiur preparation, lesson prep, curriculum building, drosho]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Shiur &amp; Curriculum Preparation

Using AI to turn a *sicha*, a *maamar*, a Gemara *sugya*, or an article
into a polished shiur or curriculum.

## Where the consensus has landed

**Claude wins this category.** Repeatedly tested against ChatGPT and
Gemini for organizing sichos into 60-minute shiurim with discussion
questions, teacher guides, and student handouts. The pattern:

> *"I tell it to organize into a 60-minute shiur with discussion
> questions, summaries, and follow-along printout — teacher's guide and
> student handout. Does an amazing job."*
> — [chat 2026-05-20]

> *"I tried with ChatGPT and Gemini, and what they came up with was
> very poor in comparison. Claude was beautifully formatted."*
> — [chat 2026-05-14] (testing Gemara)

> *"Claude beautifully extracted the *nekuda* of the maamar and
> presented it in a way that a 13-year-old can understand. It was the
> biggest nachas to see a boy from my community chazering a maamar at
> his bar mitzvah."*
> — [chat 2026-05-25]

## The pattern

1. **Source the text.** Pull plain text from a vetted corpus:
   [[../tools/dach-dev]], [[../tools/notebooklm]] (for Rebbe's
   *Likkutei Sichos*, *Igros Kodesh*, etc.), Sefaria, or upload your
   own PDFs.
2. **Hand the whole thing to Claude.** Don't ask it to *fetch* the
   sicha; that's where hallucination starts. *Paste* the sicha.
3. **Specify the format.**
   > *"Create structured, detailed and comprehensive speech notes
   > based on this talk. It should follow a logical structure. I'm not
   > looking for a verbatim speech script, only content notes. Include
   > all stories and anecdotes in full."*
   > — [chat 2025-09-22]
4. **Add the audience and use-case.** *"60-minute shiur, mixed-level
   adult class, English with Hebrew terms transliterated."*
5. **Request the artifacts explicitly.** Teacher's guide, student
   handout, discussion questions, exit-ticket questions, a printable
   PDF (Claude can use [`pptx`](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) and HTML→PDF skills).
6. **Add Q&amp;A and stories.** Claude will, if asked, embed niglah /
   nigleh stories with proper context.
7. **Verify.** Cross-check any cited mareh-mekomos against the source.
   The model *will* fabricate them otherwise.

## Audio-first workflow

You recorded the shiur instead of writing it:

1. Transcribe with [[../tools/sofer-ai]] (Hebrew/Yiddish/English mix)
   or Turboscribe (English) or Whisper. See [[transcription]].
2. Paste transcript to Claude.
3. *"Summarize this shiur and produce a one-page printable PDF."*
   — pattern from [chat 2026-05-20] on Sofer.ai →
   Claude for *פת הבאה בכסנין*.
4. Iterate: longer version, shorter version, focus on specific points.

## NotebookLM as a corpus tool

Special-purpose use of [[../tools/notebooklm]]: upload an entire shas
or all of Likkutei Sichos as the *sources*. NotebookLM will cite
chapter and verse — but it caps at ~12 sources per query, so structure
prompts to demand specificity:

> *"I just searched for 100 insights into the yomtov of Pesach and it
> provided from 109 different sources."*
> — [chat 2026-03-24]

Shared notebook of the Rebbe's Torah (Likkutei Sichos, Igros Kodesh,
Toras Menachem, Maamarim): `notebooklm.google.com/notebook/8fd6b863-…`
[chat 2026-02-06].

## Audio Overview &amp; podcasted shiurim

NotebookLM's *Audio Overview* generates a podcast-style two-host
discussion from any uploaded sources — one community example: a
Schnei Shneor Ashkenazi sicha converted into a structured Rosh Hashanah speech
[chat 2025-09-22]. Then *Interrupt* lets you join the
conversation as a third voice.

## Drosho-specific tips

- **"Roast this!"** [chat 2025-09-07] — after pasting
  your speech, ask the model to critique mercilessly. Surprisingly
  useful.
- **Read it aloud.** [[../tools/elevenlabs]] V3 handles Hebrew with
  ches/chet pronunciation if you write Ashkenazi-style with *nikkud*.
- **Cross-language.** AI can take a Yiddish sicha and produce an
  English shiur, *if* you give it the text — see [[hebrew-yiddish]].

## Custom GPTs / Gems for repeated use

Some shluchim build custom GPTs / Gems with their preferences baked
in (preferred opening prayer, recurring stories, brand voice). See
[[chabadone-integration]] for analogous patterns on the website side.
[chat 2026-02-11]: "Hard-code your preferences,
flyer styles you like, past examples, brand colors — you'll get more
consistent results."

## Open questions

- Reverse *mafteach inyanim*: given a page of a sefer, list every
  inyan discussed. [chat 2026-05-20] — "Gemini failed
  miserably." Best path: have AI write a Python script over indexed
  data, not run inference each time.
- AI lecturer that reliably handles 5+ acharonim without flattening
  them — open question across [[../themes/ai-and-torah-accuracy]].

## Related

- [[../themes/ai-and-torah-accuracy]]
- [[../tools/claude]]
- [[../tools/notebooklm]]
- [[../tools/dach-dev]]
- [[../tools/sofer-ai]]
- [[transcription]]
