---
type: resource
slug: master-prompts
aliases: [prompt library, golden prompts]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Master Prompt Library

The most-cited prompts in the chat, organized by use case. The
big-ticket *flyer designer* prompt has its own page —
[[designer-prompt]]. This file collects the rest.

---

## Writing &amp; voice

### Anti-AI writing-style sheet

[chat 2025-08-04]. The most-quoted writing-style prompt in the chat.

> *"Keep your writing style simple and concise. Use clear,
> straightforward language, short, impactful sentences. Organize ideas
> with bullet points. Active voice; avoid passive. Focus on practical,
> actionable insights. Engage readers by posing thought-provoking
> questions and addressing them directly using 'you' and 'your.'
> Avoid clichés, metaphors, broad generalizations. Skip 'in
> conclusion' / 'in summary.' Eliminate warnings, hashtags,
> semicolons, emojis, asterisks. Avoid excess adjectives and
> adverbs."*
>
> Banned words include: *accordingly, additionally, arguably,
> certainly, consequently, hence, however, indeed, moreover,
> nevertheless, nonetheless, thus, undoubtedly, adept, commendable,
> dynamic, efficient, ever-evolving, exemplary, innovative,
> invaluable, robust, seamless, synergistic, transformative, utmost,
> vibrant, vital, efficiency, integration, implementation, landscape,
> optimization, realm, tapestry, transformation, aligns, augment,
> delve, embark, facilitate, maximize, underscores, utilize,
> "a testament to…," "in conclusion…," "in summary…," "it's important
> to note/consider…"*
>
> **Style rules**:
> - Do not use em-dashes (—) EVER. Use a comma, semicolon, or split
>   the sentence.
> - Avoid hyphens unless part of a standard compound word.
> - Write in clear, conversational English. Vary sentence length;
>   short paragraphs.
> - Cut empty phrases like "in today's world," "leverage," "unlock
>   the power."
> - Use numbers or bullets; never em-dashes for list items.
> - Before sending, review and remove any em-dashes or extra hyphens.
> - Acknowledge with "Got it" and then respond.
>
> Plus: Flesch reading score ≥ 80, active voice, plain English,
> jargon only when needed, no salesy or overly enthusiastic tone —
> calm confidence.

Use case: drop into Claude / ChatGPT as a system message before any
serious letter or email writing.

---

### Honest-feedback prompt

[chat 2026-04-21, +1 847-452-8703]:

> *"Be direct and brutally honest. Stress-test my ideas hard. If
> something is weak, say so plainly and explain why. Think from
> first principles, use logic over sentiment, and push until the
> argument is solid."*

Simple version, [chat 2026-04-21, +33 6 68 42 07 70]:

> *"Criticize my output and be merciless about it."*

---

### Pre-response clarification

[chat 2025-08-19]:

> *"Ask me clarifying questions to make sure we're on the same page
> before responding or doing a task."*

---

### Rate-your-response

[chat 2025-08-19]:

> *"Rate your response out of 10."*
>
> Then if dissatisfied: *"I'd rate that a 6/10."* The model
> recalibrates.

---

## Multi-step / debugging

### The "Golden Prompt" — one step at a time

[chat 2025-11-14, +972 53-338-6770]:

> *"When I ask how to do something, work with me step by step — ONE
> step at a time. DON'T give me all the steps at once. Instead:
> Start with a SHORT explanation of what we're going to do. Then
> give me ONLY the first step. Wait for me to confirm it worked or
> show you the results. Then move to step 2. If there are different
> ways to solve something, first tell me briefly what the options
> are. Let me choose which approach I want, and THEN we'll go through
> it step by step."*

Why: when something goes wrong, you can point at *that step* without
the model relitigating the whole plan.

---

### Meta-prompting

[chat 2026-02-11]:

> *"Help me write a great prompt for [tool] for [task]. Ask me
> clarifying questions until you have what you need to make the
> prompt maximally effective. Keep it concise and to the point. When
> you're done, audit the prompt and suggest areas for refining. Then
> implement those."*

Generalization: ask AI how to ask AI. It's surprisingly good at this.

---

## Hebrew / Yiddish

### Ashkenazi TTS pronunciation trick

[chat 2025-11-21]:

> *"Tell it to write in Hebrew with nikkud such that a TTS will
> pronounce in Ashkenazis."*

Concrete tactic: write `מחודש` with vowels tuned to Ashkenazi sounds;
ElevenLabs V3 then says it correctly. Or transliterate as `khabad` /
`samayakh` instead of `chabad` / `samayach`.

---

## ChabadOne page builder

[chat 2026-04-24]:

> *"This is a platform-agnostic system prompt for building modern,
> clean, mobile-responsive HTML pages that render correctly inside
> ChabadOne. Works with Claude, ChatGPT, Gemini, or any capable LLM.
>
> How to use: paste this entire prompt as your first message in a
> fresh conversation. The AI will ask: CREATE A NEW PAGE or MODERNIZE
> AN EXISTING PAGE.
>
> - If creating new: AI interviews you, then produces an HTML page.
> - If modernizing: paste existing HTML; AI extracts content first,
>   then only asks for what it can't figure out.
>
> Content sourcing: hardcoded to orthodox sources — Chabad.org,
> Sefaria, Aish.com, OU, YU Torah, classical texts."*

Full version on shluchimexchange.ai at
`/prompts/28cbafa6-f2e4-4c18-b072-7ccd8f5282f4`. See
[[../topics/chabadone-integration]].

---

## Sora prompt (avoiding demographic refusals)

[chat 2025-11-20].

Avoid: *"Jewish women," "Caucasian," "Jewish-looking."*

Use: *"Women wearing modern modest dresses, hair visible, celebrating
at a Shabbat dinner table."* / *"Women in contemporary casual clothing,
smiling and talking while lighting Chanukah candles."* / *"A group of
friends wearing smart casual party outfits at a festive Jewish event."*

Why: describes attire, actions, and scene — not protected attributes.

---

## Shiur creation

### From a Hebrew sicha

[chat 2025-09-22]:

> *"Create structured, detailed and comprehensive speech notes based
> on this talk. It should follow a logical structure. I'm not looking
> for a verbatim speech script, only content notes. Include all
> stories and anecdotes in full."*

### 60-minute shiur format

[chat 2026-05-20, +1 520-472-8840]:

> *"Organize into a 60-minute shiur with discussion questions,
> summaries, and follow-along printout — teacher's guide and student
> handout."*

### Roast my drosho

[chat 2025-09-07, +1 347-515-0835]:

> *"Roast this!"* — paste your speech first.

---

## Jewish-name detection

Two community gists:

- **Research agent** (full online lookup): `gist.github.com/jonazri/006e3b667dc309f8db4d9875ce8a51e1`
- **Single-prompt scorer** (name-only): `gist.github.com/jonazri/b353b67db66a902ba1bcf66c94d48b62`

*Use responsibly.* See [[../topics/fundraising]] for context.

---

## Data extraction

### WhatsApp chat → summary

[chat 2025-12-04, +1 203-887-6044]:

> *"Condense this entire chat into a clear, organized summary. Remove
> timestamps, system data, and speaker labels. Keep only the actual
> ideas and information, in clean sections."*

### Excel script generation

[chat 2026-05-19, +1 737-786-5770]:

> *"Ask ChatGPT to write you a script to use in Excel. You can ask
> it to make a sophisticated script that will ask you before it
> deletes anything etc. The advantage of a script is that it's a
> program that is tied to your data and not an AI that will
> hallucinate."*

---

## Productivity

[chat 2026-02-25, +44 7980-795936]:

> *"Adopt the role of a productivity expert tasked with establishing a
> sustainable workload management system… Begin by analyzing the
> current workload and tasks. Then, develop a prioritization system
> based on urgency and importance. Next, estimate time requirements
> for each task. Finally, create a balanced schedule that allows for
> breaks and personal time.
>
> #INFORMATION ABOUT ME:
> My current tasks: [LIST YOUR CURRENT TASKS]
> My available work hours per day: [INSERT AVAILABLE WORK HOURS]
> My work environment: [DESCRIBE YOUR WORK ENVIRONMENT]
> My energy levels throughout the day: [DESCRIBE YOUR ENERGY PATTERNS]
> My long-term career goals: [INSERT YOUR CAREER GOALS]
>
> Present your workload management system in a markdown table with
> three columns: [CURRENT TASKS], [ESTIMATED TIME], [PRIORITY LEVEL].
> Below the table, list additional recommendations for maintaining
> work-life balance and preventing burnout."*

---

## Related

- [[designer-prompt]] — the flyer system prompt has its own page.
- [[nonprofit-discounts]] — the other persistent reference.
- [[../topics/letter-writing]]
- [[../topics/shiur-prep]]
- [[../topics/chabadone-integration]]
