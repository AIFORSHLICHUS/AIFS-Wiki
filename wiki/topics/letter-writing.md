---
type: topic
slug: letter-writing
aliases: [writing, communications, email, drafts]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Letter Writing &amp; Communications

Drafting letters, emails, and short writing in a voice that sounds
*human* — and ideally like *you*. Foundational use case from the
chat's first weeks.

## What the group settled on

| Use case | Model |
| --- | --- |
| Pastoral / emotional / "knowing your *baalei batim*" | **Claude** |
| Personality / fun / casual tone | **Grok** |
| Default workhorse | **ChatGPT** |
| Style-matching past work (uploaded examples) | **Claude** with examples in the chat / a Project / a Custom GPT |

> *"Claude is better in my experience than ChatGPT. Provide a good
> outline of what you want the letter to say."*
> — [chat 2025-08-04]

> *"I find that Grok writes with more personality and a more genuine
> tone than ChatGPT."*
> — [chat 2025-08, +1 240-444-3345]

## The three workable patterns

### 1. Upload examples; let it copy your voice

Eulogy workflow [chat 2025-08-04]:
- Upload 20+ past eulogies you've written.
- Add a system message: *"Copy this style for future writing."*
- When a new eulogy is needed: take notes with the family, paste them
  into the same chat, get a draft that matches your prior style
  (similar openings, similar closings).

Generalizes to thank-you letters, sponsor letters, condolence notes,
press releases.

### 2. System-prompt rules

The most-shared writing prompt in the chat — an anti-AI
style sheet [chat 2025-08-04]. The key constraints:

- No em-dashes ever (use commas, semicolons, or two sentences).
- No "leverage", "synergy", "tapestry", "delve", "in conclusion".
- Active voice. Short paragraphs. Vary sentence length.
- Flesch reading score ≥ 80.
- Avoid adverbs. No clichés. Plain English.
- *Acknowledge with "Got it" and then respond to the actual request.*

See the full prompt in [[../resources/master-prompts]].

### 3. DIA Browser / writing-aware browser

[chat 2025-08-04]: DIA Browser has a built-in AI
assistant where you pre-load your writing style and sample authors
once — then everything you write gets ghostwritten in that voice
without re-prompting each time.

## Specific letter use cases

### Fundraising letters at a 6th-grade reading level

The Jeff Brooks technique, adapted [chat 2025-08-06, Mendy Cunin LA]:

1. Write your own draft.
2. Ask AI: *"Rewrite this at a 6th-grade reading level while keeping
   my voice and main points."*
3. The result is more accessible and historically gets higher response
   rates.

### Press releases

Generating press releases + media list customization is a [chat 2025-08,
+1 904-910-5676] specialty. Pattern: write one well-targeted release;
generate ten variations per outlet; check before sending.

### Grant proposals

[chat 2025-08-19]: paste the grant questions into AI with
your Chabad House context; AI fills out answers. Then you edit. Saves
hours.

### Eulogies / hespedim

The pattern above. Also use the AI to research
the deceased — names, dates, family members, public mentions — before
the family meeting.

### Condolence / yahrtzeit notes

Use the recipient's name and one specific memory; AI writes the
connective tissue. Don't trust AI to find the memory — that's *your*
job.

## "Sounds too AI" — fighting the tells

Common AI tells in letters:

- *Em-dashes everywhere.* Strip them.
- *"In today's world, ..." / "In conclusion, ..."* Cut these.
- *Triadic sentences.* "Faster, smarter, kinder." Three is the AI default.
- *Repeated framings*. "Not just X, but Y." "It's not about A — it's
  about B."
- *Verb-heavy openings.* "Imagine." "Picture." "Consider."

The 2026-04 TechCrunch article *"AI Writing: It's not just this, it's
that"* (shared [chat 2026-04-20, +1 415-634-7727]) catalogs the
patterns at length.

## Honest-feedback prompts

When the AI is sycophantic ("That's a great idea! You're brilliant!"):

> *"Be direct and brutally honest. Stress-test my ideas hard. If
> something is weak, say so plainly and explain why. Think from first
> principles, use logic over sentiment, and push until the argument is
> solid."*
> — [chat 2026-04-21, +1 847-452-8703]

> *"Recently I asked GPT to criticize my output and be 'merciless'
> about it. It worked."*
> — [chat 2026-04-21, +33 6 68 42 07 70]

> *"After AI response: 'Rate your response out of 10.' If not
> satisfied: give your own rating, e.g., 'I'd rate that a 6/10.' AI
> recalibrates understanding of what you need."*
> — [chat 2025-08-19]

## Pre-response clarification

> *"Ask me clarifying questions to make sure we're on the same page
> before responding or doing a task."*
> — [chat 2025-08-19]

A small prompt addition that prevents misinterpretations on
complicated writing tasks.

## ZeroGPT check

[chat 2025-08-05]: *"Always paste your text into
zerogpt.com or similar before posting to see if it's too much AI."*

## Related

- [[../resources/master-prompts]] — anti-AI style sheet and other prompts
- [[../tools/claude]]
- [[../tools/chatgpt]]
- [[../tools/grok]]
- [[fundraising]]
