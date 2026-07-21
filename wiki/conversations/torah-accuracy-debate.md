---
type: conversation
slug: torah-accuracy-debate
aliases: [Torah AI debate, hallucination thread, 9 principles thread]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
participants: []
date_range: 2025-08-19 to 2026-05-25
---

# The Torah Accuracy Debate

Not a single conversation but a recurring through-line spanning the
whole chat: **what does it take to use AI for Torah without breaking
something sacred?** See [[../themes/ai-and-torah-accuracy]] for the
distilled positions; this page tracks the conversation as it
unfolded.

## Phase 1 — "Can I use AI to write a devar Torah?"

**2025-08-19.** Shared in chat: Menachem Posner's Chabad.org article
*Can I Use AI to Write a Devar Torah?* The thread's earliest framing:

- AI is fine for **brainstorming, editing, organizing.**
- AI-generated *Torah* is problematic. Posner: when we innovate in
  Torah, we become God's partners; "but can a computer create this
  Divine unity?"
- Ethical concern: ***geneivat daat*** if readers think it's the
  author's own thought.

The framing of *why* AI struggles: *"To understand why AI is cool
but limited, ask it to explain what happens when it computes
2+2=4."*

## Phase 2 — The hallucination drumbeat

**2025-08-06** onward. Recurring user complaint: ChatGPT cites
*Likkutei Sichos, vol. X, p. Y* — and the page doesn't exist, or the
sicha doesn't say that. By 2025-12-13 the diagnosis crystallizes:

> *"LLMs are 'word generators' not 'databases.' Without structured
> data — all of Igros indexed — this problem will persist for years.
> Unless OpenAI/Anthropic gives access to all texts and structures
> them, hallucinations for Torah references will continue."*
> — [chat 2025-12-13]

[chat 2025-12-13] reports ChatGPT inventing whole
*Rebbe answers* with fake citations to Igros and Likkutei Sichos.

## Phase 3 — Building substitutes

**Late 2025 onward.** The community starts building alternatives:

- **[[../tools/dicta-mekorotai]]** — purpose-built rabbinic AI;
  refuses what it can't cite. Demoed at
  [[kinus-ai-day-nov-2025]] but not yet shipping reliably.
- **[[../tools/notebooklm]] with the Rebbe's Torah** — 2026-02-06,
  shared notebook with Likkutei Sichos / Igros Kodesh / Toras
  Menachem / Maamarim. *"He starts telling me things and I'm like
  'the Rebbe said that?!' … It's actually accurate."*
- **[[../tools/dach-dev]]** — plain-text Chassidic corpus that you
  paste *into* the LLM rather than asking the LLM to recall.
- **[[../tools/maamorim-app]]** — curated maamorim with vetted
  summaries.
- **anash.org's Likkutei Sichos app**, **likuteysichos.com**, Sefaria.

## Phase 4 — The "9 Principles" document

**2026-02-23.** A community member announces they're drafting
plain-language rules for AI Torah citation:

> *"I'm working on a set of principles and detailed rules — written
> in plain language, not code — that you paste into whatever tool
> you already use. No downloads, no new apps. You paste it once and
> the tool should handle Torah texts more carefully. The rules cover
> search methods, citation formats, verification steps, and
> domain-specific instructions for different types of texts."*

Open Google Doc circulated for community feedback. As of 2026-05, the
document is still iterating — but it's referenced as the closest the
community has to a *system prompt for Torah honesty*.

## Phase 5 — The "Bina Melachutit" thread

**2026-02-13–14.** A member introduces the Chassidic
distinction: *bina* (understanding, processing) without *chochma*
(the divine spark / sudden insight). Another member writes a full
Shabbos-table drosha tying *Parshas Mishpatim's Eved Ivri* to AI's
nature — ironically written *by Gemini*. The thread tangles into
Hebrew terminology (*melachutit* vs. *melachit*); philosophical, not
action-oriented, but produces the chat's most-quoted hashkafic
framing of AI:

> *"The machine has the 'bina,' but we have the 'neshama.'"*

## Phase 6 — "Read primary sources, not English chabad.org"

**2026-02-24:**

> *"AI has very little access to actual Torah sources. It's skimming
> basic English sites … regurgitating chabad.org back at you."*
> — [chat 2026-02-24]

**2026-02-27:**

> *"Torah doesn't fit the shape that AI is expecting to read.
> Layered, subtle, nuanced. The process is lost on it."*
> — [chat 2026-02-27]

The hardening consensus by Q1 2026: even when the model "sounds right,"
it's regurgitating English translations of secondary commentary, not
reasoning from primary sources.

## Phase 7 — Magazine project lessons

**2026-03-18.** A member documents 10 lessons from a 10-page
Pesach magazine in Claude. The Torah-relevant ones:

- *Set golden rules at the start of the chat:* "don't edit my text",
  "Hebrew is RTL", "no hyphens."
- *Test Claude on a Maamor outline* — got the wrong sicha attribution
  until shown an image; even then unreliable. *"Don't just trust
  Claude."*
- *Cross-reference everything that names a source.*

## Phase 8 — Specialized translation

**2026-04-16.** A member tests eight LLMs for Hebrew
translation. **Qwen** wins for pure translation work — etymology,
*shoresh*, word-by-word transliteration. Adds a new tool to the
recommended stack for Torah work specifically.

## Phase 9 — Curricula and shiur prep

**2026-05-20** onward. The conversation shifts from "can AI
*translate* Torah?" to "can AI *organize* Torah?" — and the answer is
*yes, with vetted sources*. Claude becomes the default for 60-minute
shiur outlines with discussion questions, teacher guides, student
handouts. See [[../topics/shiur-prep]].

The catch: the input must be vetted text from
[[../tools/dach-dev]], [[../tools/notebooklm]], or a typed sicha.
Don't ask Claude to fetch the sicha from memory.

## Phase 10 — Bar-mitzvah maamar

**2026-05-25:**

> *"I uploaded the last maamar I learned (בלתי מוגה) to Claude and he
> beautifully extracted the *nekuda* of the maamar and presented it
> in a way that a 13-year-old can understand. It was the biggest
> nachas to see a boy from my community chazering a maamar at his
> bar mitzvah."*

The pattern works when you supply the maamar. AI extracts the *nekuda*;
the human verifies and teaches.

## The chat's working answer

By May 2026 the chat's working answer for AI-and-Torah:

1. **Curate the corpus.** Use [[../tools/dach-dev]], NotebookLM with
   vetted sources, [[../tools/maamorim-app]], Sefaria — never raw
   model memory.
2. **Match the model to the task.** Claude for *iyyun* and shiur
   structure. Gemini Pro / Qwen for translation. NotebookLM for
   citation-grounded Q&amp;A.
3. **Always cross-check citations.** *"Don't just trust Claude."*
4. **Buffer layers between AI and talmidim.** Curated apps
   (maamorim.app, mishna.me, megillah.app) instead of raw
   AI-generated content.
5. **Document principles** and share community prompts.
6. **Hashkafic framing**: AI provides *bina*; humans provide
   *chochma* and *neshama*. AI doesn't replace shluchim; it extends
   their reach.

## Related

- [[../themes/ai-and-torah-accuracy]]
- [[../topics/shiur-prep]]
- [[../topics/hebrew-yiddish]]
- [[../tools/dicta-mekorotai]]
- [[../tools/dach-dev]]
- [[../tools/notebooklm]]
- [[../tools/maamorim-app]]
- [[../resources/master-prompts]]
