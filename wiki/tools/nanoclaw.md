---
type: tool
slug: nanoclaw
aliases: [Nanoclaw, ClawdBot]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Nanoclaw

Security-focused AI agent framework. The chat's recommended *safer*
alternative to **ClawdBot** for agents that touch real systems.

## What it is

Founded by ex-JLI and ex-IDF 8200 engineers. Docker-sandboxed. The
*"Don't trust AI agents"* angle — agents run in isolated containers
so a compromised agent can't reach your filesystem, banking, or PII.

Forbes piece: *"Don't Trust AI Agents, Says Nanoclaw, Now Fully
Integrated with Docker"* — shared [chat 2026-03-13, Yonatan Azrielant].

## What the chat uses it for

- **CRM agents that work safely.** [[../people/didy-waks]]'s pattern
  with [[../tools/crm-tools]] (LGL). *"It's available free through
  Nanoclaw. Highly recommend learning more before getting another
  service."* [chat 2026-05-15]
- **Browser automation** without the security disasters of
  un-sandboxed Claude Cowork on banking sites.

## Why ClawdBot is the cautionary tale

[chat 2026-03-13, Yonatan Azrielant]: *"ClawdBot changed the world but
has major security flaws."* It's the chat's reference point for "an
agent that does too much with too few guardrails."

## Strengths

- Sandboxed execution.
- Self-learning across CRM features (Didy Waks reports).
- Free tier accessible.

## Weaknesses

- Less known than Manus.im or Claude Cowork.
- Setup overhead higher than browser-extension agents.

## Related

- [[manus]] — non-sandboxed alternative.
- [[claude]] — Dispatch/Cowork.
- [[../themes/vibe-coding]] — why agents need safety layers.
- [[../topics/crm-automation]]
- [[../people/didy-waks]]
- [[../people/yonatan-azrielant]]
