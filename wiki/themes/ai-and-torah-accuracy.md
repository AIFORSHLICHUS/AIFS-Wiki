---
type: theme
slug: ai-and-torah-accuracy
aliases: [hallucination, torah hallucination, bina melachutit]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# AI and Torah Accuracy

The single most charged technical topic in the chat. Every model the
group tests will, eventually, fabricate a Likkutei Sichos citation, blend
two acharonim into one ruling, or attribute an invented page number to
*Igros Kodesh*. The group has gone through several phases trying to
solve it.

## The problem, stated plainly

> *"Without structured data — all of Igros indexed — this problem will
> persist for years. Unless OpenAI/Anthropic gives access to all texts
> and structures them, hallucinations for Torah references will continue."*
> — [chat 2025-12-13]

> *"AI has very little access to actual Torah sources. It's skimming
> basic English sites … regurgitating chabad.org back at you."*
> — [chat 2026-02-24]

> *"Torah doesn't fit the shape that AI is expecting to read … layered,
> subtle, nuanced. The process is lost on it."*
> — [chat 2026-02-27]

LLMs are *word generators*, not *databases*. Hebrew sources are
under-represented in training data. Layered commentary collapses into a
flat "sounds plausible" output.

## Workarounds the group has found

### 1. Constrain sources

- Pull primary text from a trusted corpus (Sefaria, Chabad.org,
  HebrewBooks, [[../tools/dach-dev]]) and *paste it in*. Don't ask the
  model to fetch from memory.
- [[../tools/notebooklm]] indexed with the Rebbe's *Likkutei Sichos*,
  *Igros Kodesh*, *Toras Menachem*, *Maamarim* — see the shared
  notebook at `notebooklm.google.com/notebook/8fd6b863-…` [chat 2026-02-06, +1 520-703-7466]. Caveat: NotebookLM
  retrieves only ~12 sources per query.
- [[../tools/dicta-mekorotai]] (`chabad.mekorotai.dicta.org.il`),
  previewed at Kinus 2025-11-13, is purpose-built: claims-with-citation,
  rejects what it can't ground.

### 2. Use the right model for the right register

- **Claude** for *iyyun* / technical Torah, organized shiur structure.
  [[../topics/shiur-prep]]
- **Gemini Pro** for popular Chassidus and for *Hebrew translation
  with grammatical metadata* (when Qwen isn't available).
- **Qwen** for pure Hebrew/Yiddish translation with etymology and
  shoresh. [chat 2026-04-16, +33 6 51 82 35 18]
- **ChatGPT** — generally weakest on Torah specifics; strong as a
  writing partner once you've supplied sources.

### 3. "Plain-language rules" instead of code

[chat 2026-02-23] describes drafting a community document of **9
principles for AI Torah citation** — search methods, citation formats,
verification steps, domain-specific instructions for different text
types. Posted to Google Docs for community feedback. Not yet finalized,
but treated as one of the more important community efforts. See
[[../resources/master-prompts]].

### 4. Build buffer layers (don't expose AI raw to talmidim)

> *"Never release an AI-coded app with login functionality, financial
> transactions, or mission-critical email integrations."*
> — [chat 2026-03-13]

Tools like [[../tools/dach-dev]] and [[../tools/maamorim-app]] succeed
by curating the corpus and letting the LLM only re-present — not invent.

## Halachic / hashkafic threads

- **"Bina vs. Chochma"** ([chat 2026-02-13, +1 520-472-8840]):
  *Bina Melachutit* — artificial *understanding* — without *chochma*
  (the spark of insight). Generated a full Shabbos-table drosha (written
  by Gemini, ironically) tying the Eved Ivri to AI's nature. [chat 2026-02-13, +54 9 11 6164-2418]
- **"Can I use AI to write a Devar Torah?"** by Menachem Posner,
  Chabad.org — shared and debated [chat 2025-08-19]. Conclusion: AI as
  editing/brainstorming aid is fine; AI as the *source* of a devar
  Torah is *geneivat daat* and lacks the Divine unity created when a
  human is *mechadesh*.
- **AI agents running on Shabbos** [chat 2026-04-27, +39 340 359 5009;
  also Chabad.org *Can I Let My AI Agent Run on Shabbat*]. Rough
  consensus: backend-only OK; anything that triggers front-end
  notifications, sends customer-facing email, or transacts is
  problematic (incl. *maris ayin*).

## Open questions

- Will Mekorotai/Dicta ship to the public? (Promised "this year" as of
  Kinus 2025-11.) Status as of 2026-02-17: still not working well per
  [chat 2026-02-17, +1 415-634-7727].
- Is there a way to get AI to *read* Rashi script reliably?
  [chat 2025-11-18, +1 758-718-1172] — still no good answer.
- Hebrew handwriting / *ksav yad* OCR — [chat 2026-02-17, +972 54-239-9791]
  re Dicta's *chabad.mekorotai*: "Nah."

## Related

- [[../tools/dicta-mekorotai]]
- [[../tools/dach-dev]]
- [[../tools/notebooklm]]
- [[../tools/maamorim-app]]
- [[../tools/learningtanach-org]]
- [[../topics/hebrew-yiddish]]
- [[../topics/shiur-prep]]
