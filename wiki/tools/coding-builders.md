---
type: tool
slug: coding-builders
aliases: [Claude Code, Cursor, GitHub Copilot, Google Jules, cto.new, Kiro, Base44, Bolt, Replit, app builders]
status: maintained
sources: [chat.txt]
updated: 2026-05-25
---

# AI Coding &amp; App Builders

Reference page for the **coding-tool stack** beyond [[lovable]].
The canonical comparison is from [chat 2026-02-22]:

| Tool | Price | Best for | Caveat |
| --- | --- | --- | --- |
| **Claude Code** | Free with Claude Pro | Real engineering, GitHub integration, multi-file refactors | Skill curve. Add MCP for power. |
| **GitHub Copilot** | $10/mo | Inline AI in your IDE; best value | Less holistic than Claude Code |
| **Cursor** | $20–$500/mo at heavy use | Power tool with whole-codebase context | Expensive — $300–500/mo at heavy use reported |
| **Google Jules** | Free | Phone-based prompting from GitHub | New; works but rough edges |
| **cto.new** | Free | Browser-based, GitHub sign-in | Quick experiments |
| **Kiro.dev** | Free preview | Desktop-app style | Beta |
| **OpenAI Codex (for OSS)** | Free 6 mo Pro | Open-source devs | Form-based application |
| **Lovable** | Credits, ~$25/mo | Single-page apps, prototypes | Can't import existing repos |
| **Base44** | Cheap | Database-backed Chabad apps | Less polished UI than Lovable |
| **Bolt** | Cheap | Similar to Lovable | Less community usage in chat |
| **Replit** | Tiered | Browser IDE; deploy + share apps | Used for AIFS workflows app |

## Claude Code

The chat's recommendation for *serious* vibe coding. [chat 2026-04-27]:

> *"Go to Settings &gt; Connectors &gt; GitHub. Add the connection — your
> Claude will now have access to all your repos. Then select the repo
> and start prompting."*

[chat 2026-01-08]: cheaper than Lovable for serious work; no need for
WordPress / Elementor anymore. Build forms that beat JotForm / Typeform.

## Base44

[chat 2026-01-11, Shaul Wasserman]:

> *"Built an advanced web app with 10 API integrations using Base44.
> Found better results than Lovable. WhatsApp integration."*

[chat 2026-02-24]: The **Rebbe's Global Footprint**
website was built in 15 minutes on Base44.

## When to use what

- **Quickest prototype** → [[lovable]].
- **Database-heavy** → Base44.
- **Real engineering** → Claude Code.
- **Already in an IDE all day** → GitHub Copilot.
- **Free tinkering on phone** → Google Jules.
- **You have budget and a complex codebase** → Cursor.

See [[../themes/vibe-coding]] for what to *not* build with any of these.

## Related

- [[lovable]]
- [[claude]]
- [[../themes/vibe-coding]]
- [[megillah-app]] — Claude Code success story.
- [[berel-me]] — Claude (Opus 4.5) portfolio.
