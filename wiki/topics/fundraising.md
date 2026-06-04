---
type: topic
slug: fundraising
aliases: [grants, donor research, prospect research, campaigns]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# Fundraising

Where AI has produced some of the chat's most undeniable, time-measurable
wins.

## Grant writing

Pattern from [chat 2025-08-19]:

> *"It has been very inhibiting or time consuming at times to enter
> grant proposals. AI has been very helpful in filling out grant
> information."*

Workflow:

1. Paste the grant's parameters into the model.
2. Add: Chabad House description, mission, programs, financials,
   recent impact metrics.
3. Ask the model to draft answers to each grant question.
4. Edit; verify any numbers; submit.

[chat 2026-01-22] Comet (Perplexity's agentic browser, $200/mo)
auto-fills web grant forms. [chat 2025-08-19, +1 347-598-7098] tested
this for grant proposal form auto-filling.

## Fundraising letters

The Jeff Brooks technique, applied:

1. Write your own first draft (or have AI write one from notes).
2. Prompt: *"Rewrite this at a 6th-grade reading level while keeping my
   voice and main points."*
3. Direct mail at lower reading levels historically gets higher response.

[chat 2025-08-06, Mendy Cunin LA]. See [[letter-writing]].

## Donor research / prospect lookup

| Goal | Tool |
| --- | --- |
| Top Jewish philanthropists in a city (public info) | **Claude Cowork** — produced spreadsheet, [chat 2026-04-19, Shmulie Cunin] |
| Find emails for a known person | **Gemini `=AI(...)` formula in Google Sheets** — concatenate all known fields per row, drag the formula down. [chat 2026-03-19] |
| Background on a *baal habayis* | **Perplexity Spaces** with relevant uploads; **Hatch.ai** (Lubavitch-owned, paid). |
| Score names for likely Jewish | **Community gists** — see below. |
| CRM enrichment (lapsed donors, next-best-action) | Agents on **Attio** / **LGL** / **Hecher**. See [[crm-automation]]. |

> *"It goes through specific lists, researches and updates."*
> — [chat 2026-03-19], describing an Attio agent.

## Jewish-name detection prompts

Two community-maintained open gists [chat 2026-05-03]:

- **Agent**: `gist.github.com/jonazri/006e3b667dc309f8db4d9875ce8a51e1`
  Walks each name, researches online, scores Jewish likelihood with
  evidence.
- **Simple prompt**: `gist.github.com/jonazri/b353b67db66a902ba1bcf66c94d48b62`
  Single prompt; guesses from name alone, very effective.

Run on AI Studio, Vercel, OpenAI Console, or Anthropic Console with a
loop over your list. *"Use responsibly."*

Also see the community's full obituary + Jewish-score custom
GPT [chat 2025-09-03, +1 347-515-0835] — 2-sheet Excel workbook with
Jewish Score evidence, spouse cross-reference, source URLs.

## End-of-year &amp; matching campaigns

Use cases shipped:

- **Cypcampaign.lovable.app** — end-of-year volunteer + donor
  dashboard. [chat 2025-12-14]
- **Campaign page generation** in Claude → HTML in ChabadOne via the
  iframe trick. [[chabadone-integration]]
- **Donor thank-you letters at scale.** AI batches the names; you
  personalize one line each.

## Bookkeeping the donations

[chat 2026-05-19, +1 917-620-7220]:

> *"If you have a bunch of Zelle, PayPal, CashApp donations you
> received and you want to know how much was given by a given person
> over a span of time (assuming these emails aren't yet logged in your
> CRM) — you can connect Gemini to your Gmail and ask it point blank
> what you want to know."*

For real bookkeeping, **QuickBooks** is the default; **Kick.co** and
**Booking.ai** mentioned but unfavorably ([chat 2025-10-22] —
"underwhelming, similar to Mint.com"). AI for QuickBooks workflow
was mentioned [chat 2026-05-18] but details weren't shared.

## Maaser / tzedaka tools

Community projects in this space:

- **Tenpr.app** — *maaser* education tool, built in Google AI Studio.
  [chat 2026-01-15]
- **My Charity Box** — Emmanuel Mergui's offline pledge tracker.
  [chat 2026-04-28]
- **Berel.me/donatext** — quick donation link / payment snippet
  generator. [chat 2026-01-27]
- **Countomer** — Sefiras HaOmer with daily *Daf of Sotah* and tzeis
  notifications. [chat 2026-04-16]

## Open problems

- **Real-time campaign analytics** (donor velocity, segmentation, next
  best action) without paying Salesforce Einstein or Bloomerang prices.
- **Multi-CRM donor view** — pulling LGL + ChabadOne + bank statements
  into one queryable place.
- **Stewardship cadence automation** — voice note → CRM follow-up →
  scheduled phone call → templated email, all in one chain. Hecher
  has it; not yet shippable as a template.

## Related

- [[crm-automation]]
- [[letter-writing]]
- [[../tools/perplexity]]
- [[../tools/claude]]
