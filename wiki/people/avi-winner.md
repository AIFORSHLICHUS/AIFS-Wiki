---
type: person
slug: avi-winner
aliases: [Avi Winner]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Avi Winner

Lovable-era app builder; the chat's "no-code lateral thinker." Many
quick-shipped tools and spreadsheet-as-app patterns.

## Things he's built

- **cypcampaign.lovable.app** — end-of-year volunteer + donor dashboard.
  [chat 2025-12-14]
- **preview--sms-invite-joy.lovable.app** — SMS invitation tool.
  [chat 2025-12-25]
- **chabadvocate.lovable.app** — early Chabad-advocacy concept.

## Editorial contributions

- **"Act like an expert" prompt pattern** for graphic-design feedback
  [chat 2025-08-19]:
  > *"Create the flyer yourself. Paste into ChatGPT with prompt: 'Act
  > like an expert graphic designer and tell me what's wrong with my
  > design, why, and what I can do to fix it.' Edit yourself based on
  > feedback, don't have AI do it."*
- **WhatsApp message-link spreadsheet formula** [chat 2026-03-06]:
  ```
  =HYPERLINK("https://wa.me/" & REGEXREPLACE(I2,"[^0-9]","")
    & "?text=Hey%20" & B2 & "%2C%20…", "Send WhatsApp")
  ```
  Principle: *"If you can't do it in a spreadsheet, don't do it in
  an app."*

## Editorial positions

- **AI flyer skepticism** — identifies font inconsistency, lack of
  structure/spacing as the persistent AI tells.
- **Sound advice on event tools** — recurring voice when shluchim
  ask for SMS RSVP / event registration that combines email + SMS +
  tickets + QR (the chat's most-requested missing tool).
- **megillah.app universal appeal** — *"It is universally appealing,
  applies to non-shluchim and even non-Chabad."* [chat 2026-02-20]

## Style

Practical and ironic. Frequently the *"have you tried a spreadsheet?"*
voice when the chat over-engineers.

## Related

- [[../tools/lovable]]
- [[../tools/chabad-apps]]
- [[../themes/ai-flyer-aesthetics]]
- [[../topics/letter-writing]]
- [[../topics/fundraising]]
