---
type: topic
slug: route-optimization
aliases: [delivery routes, route planning, mishloach manos routing]
status: draft
sources: [chat.txt]
updated: 2026-05-25
---

# Route Optimization

For mivtzoim deliveries, mishloach manos, car-menorah parades, and
Pesach matzah distribution. Standard request: *"Here are 200 addresses
and 6 drivers — optimize."*

## The paid path

- **OptimoRoute** — nonprofit discount; good for real-time route
  planning.
- **Circuit** (`circuit.app`) — app for organizing delivery routes;
  free trial + 50% nonprofit discount. [chat 2026-02-22]
- **Spoke** — same category; free trial + 50% nonprofit discount.
- **Badger** — *"extremely good app for route planning; 14 days free;
  makes addresses into optimized routes."*
  [chat 2026-02-22]

## The free / DIY path

[chat 2026-02-24]: free tools that work if you can plan ahead:

- **Nominatim** (OpenStreetMaps) — geocoding. Free. Generous rate limit.
- **Valhalla** or **OSRM** — routing engines. Free.
- Wire it together with [[../tools/claude]] Code:
  - Build a PRD: input (addresses + drivers), output (per-driver
    routes).
  - Have Claude write the script.
  - Test, refine.

> *"If you have time to plan ahead, no reason to pay."*

## What doesn't work

- **Plain ChatGPT** asking *"plan a route through these 200 addresses"*
  — refuses, hallucinates, or returns nonsense. The Google Routes API
  caps at 25 addresses per request, which prompts often confuse with
  capability.
- **AI for route planning *without* a routing engine** — LLMs aren't
  spatial reasoners.

## Specific deliverable: matzah distribution

**ConnectYid.org** — turnkey: maps, volunteer delegation, live
tracking. $60/season or $18/month. [chat 2026-03 week review]

## Related

- [[../topics/crm-automation]] — for getting the addresses out of your CRM.
- [[../themes/vibe-coding]] — Claude Code as the glue.
