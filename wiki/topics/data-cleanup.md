---
type: topic
slug: data-cleanup
aliases: [spreadsheets, Excel cleanup, contact lists, dedupe]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Data Cleanup &amp; Spreadsheets

Cleaning mailing lists, deduplicating contacts, standardizing
addresses, fixing dates. A recurring request; no clean turnkey
answer.

## The principle

> *"Don't ask AI to directly process the data. Ask AI to write a
> script that processes the data."*

Why: AI hallucinates and reassures. A script runs deterministically
and you can read it.

[chat 2026-05-19, +1 737-786-5770]:

> *"Ask ChatGPT to write you a script to use in Excel. You can ask it
> to make a sophisticated script that will ask you before it deletes
> anything etc."*

## What tools handle directly

- **Gemini `=AI(...)` Sheets formula** — at scale, ~2-3k formula
  calls/day on paid Workspace tier. Best for enrichment passes
  (find emails, infer attributes, standardize entries) where each
  cell is independent.
- **ChatGPT Pro connectors** — connect Gmail; "find all RSVPs in my
  email and make a table." [chat 2025-08-31]
- **Microsoft Copilot for Excel** — improving rapidly.
  [chat 2026-05-20]
- **Rows.com** — for extracting text from images into spreadsheets.
  *"Amazing for this specific task."* [chat 2025-12-05]
- **Datablist** — non-AI data cleaning / duplicate detection.

## The chunking rule

[chat 2025-08-19]:

> *"When collecting large datasets (e.g., 100+ records), break into
> ~20-record chunks. Large datasets cause AI to 'lose data it worked
> on' or fill with placeholders. Download file after each task."*

## Specific use cases that worked

- **Cleaning Excel sheets** (capitalization, zip codes, date formats)
  with ChatGPT Plus uploads. [chat 2025-08-06]
- **Phone-number formatting** — *"asked to add + and country code
  only where necessary (based on country field) and flag too long or
  too short numbers for me to review."* [chat 2025-12-04]
- **Email-finding via Sheets formula.** Concatenate everything known
  about a person → drag down. Retry failures.

## Specific use cases that didn't work

- **AI infers Jewish names without disclosing how** — legal limits.
  [chat 2025-09-12]
- **Mass de-dupe with confidence per change** — Datablist gets close;
  no AI does this with the "review each change" UI shluchim want.
  [chat 2025-09-17]
- **Direct AI processing of large datasets** — the failure mode Mendy
  Mann warned about.

## PDF → spreadsheet

- **Google DocumentAI** — $300 credit; good for structured PDFs.
- **Gemini CLI** for OCR.
- **Direct PDF upload to ChatGPT** — "a disaster" for multi-column /
  Hebrew. [chat 2025-11-04]

## Related

- [[../topics/fundraising]] — donor-list enrichment.
- [[../topics/crm-automation]] — pre-feed cleanup.
- [[../tools/gemini]] — Sheets formula.
