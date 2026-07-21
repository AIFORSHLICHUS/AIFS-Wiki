---
type: topic
slug: chabadone-integration
aliases: [chabadone, chabad.org platform, xhtml workaround]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# ChabadOne Integration

ChabadOne is the platform most Chabad Houses run their websites on. It
requires *XHTML 1.0* compliance, which collides head-on with the HTML5
+ inline-script habits of modern AI code generation. The chat has
documented several workable patterns.

## The XHTML compatibility wall

> *"If you want to embed AI-generated code, it has to be XHTML 1.0 to be
> fully compliant with ChabadOne and not get the XML error screen."*
> — [chat 2025-09-09]

## Pattern 1: Claude artifact + iframe

The workaround [chat 2025-09-09]:

1. Ask Claude to create a rich website with no limits/rules using
   HTML5.
2. Click *Publish* on the artifact (top right).
3. Click *Get embed code*, enter your domain, copy the embed
   `<iframe>` code.
4. Create a new web doc on ChabadOne; paste the `<iframe>` code.
5. Optional: in ChabadOne's advanced options, *expand body to full
   width* and *hide template* for a cleaner browsing experience.

**Warning:** the artifact is *public on Claude*. Don't use this for
anything sensitive.

## Pattern 2: Tell the AI about ChabadOne's constraints

Feed the AI ChabadOne's HTML help article + your design intent and
ask one model to write a *prompt* for another model that respects the
constraints. [chat 2025-11-28]:

> *"Feed the AI the ChabadOne help article with HTML guidelines (search
> 'HTML'). Ask one AI to create a prompt for another AI based on
> ChabadOne guidelines and your design ideas. Tell AI you need code
> that is 'xhtml 1.0' compatible."*

Then iterate: generate, test inside ChabadOne, ask AI to fix what
breaks. *"Have AI summarize what worked / didn't work. Create a brief
prompt with guidelines. Use going forward as parameters for building
other pages."* [chat 2025-08-29]

## Pattern 3: The Universal ChabadOne Page Builder prompt

[chat 2026-04-24] introduced a platform-agnostic
system prompt that works with Claude, ChatGPT, or Gemini:

- Paste contents to a fresh conversation.
- AI asks: CREATE NEW PAGE vs. MODERNIZE EXISTING PAGE.
- If modernizing, paste existing HTML; AI extracts content first, then
  only asks for what it can't figure out.
- **Content sourcing** hardcoded to orthodox sources: Chabad.org,
  Sefaria, Aish.com, OU, YU Torah, classical texts.
- Output: clean, mobile-responsive HTML for ChabadOne.

The prompt itself is on shluchimexchange.ai:
`https://www.shluchimexchange.ai/prompts/28cbafa6-f2e4-4c18-b072-7ccd8f5282f4`
([chat 2026-02-18]).

See [[../resources/master-prompts]] for a copy.

## Pattern 4: Minisites via Manus.im + ChabadOne articles

[chat 2026-02-22]:

1. Use AI to draft a prompt for Manus.im to scan Chabad.org for
   content (specify your audience + topic).
2. Take Manus's report back to your AI; add your event info; have it
   generate **HTML** for a one-page site (flyer placeholder + RSVP
   button).
3. Specify design preferences (colors, layout, nav bar) up front.
4. Paste into ChabadOne, adjust, done.
5. **Advanced:** multi-page minisite — each page a ChabadOne article;
   AI directs the nav bar to internal links.

Examples that worked:
- `jewishpedro.org/templates/articlecco_cdo/aid/7260228/jewish/Passover-Minisite.htm`
- `jewishpedro.org/templates/articlecco_cdo/aid/7260225/jewish/Purim-Minisite.htm`

## Pattern 5: Squarespace + ChabadBrand (alternative to ChabadOne)

For shluchim who give up on ChabadOne styling, the consensus alternative
is **Squarespace with ChabadBrand templates** — examples
`chabadfortwayne.com`, `jewishchagrinfalls.com` — and a Squarespace
account at $30/month, more design freedom, no XHTML constraint.
[chat 2025-08-18]

## What ChabadOne doesn't have (yet)

The group's recurring wishlist:

- **Native SMS RSVP.** [chat 2025-12-24] — most-voted
  missing feature. Workarounds via Lovable + Twilio.
- **Real dynamic CRM integration.** ChabadOne is on Salesforce, so MCP
  works — see [[crm-automation]].
- **AI agent to auto-update the site.** Periodically proposed.

## Related

- [[../tools/shluchimexchange-ai]] — has a ChabadOne CSS code agent.
- [[../resources/master-prompts]] — full universal page builder prompt.
- [[flyer-design]] — flyers eventually need to land here.
- [[crm-automation]] — Salesforce-backed CRM.
- [[../themes/vibe-coding]] — why some shluchim sidestep ChabadOne entirely.
