---
name: lead-radar
description: Apply Lead Radar's sales-loop, CRM truth, research provenance and analytics rules.
---

# Lead Radar

The product loop is Discover → Research → Qualify → Prepare → Contact → Objection → Outcome → Follow-up → Learn. Every change should strengthen a step or the connection between steps.

Audit the active repository and existing contracts before implementation. The canonical record of contact outcome, objection, next action and follow-up belongs in the existing CRM pipeline. A new UI producer should write to that contract and prove the values survive reload. Do not add a parallel CRM or analytics store.

Research is evidence: preserve the source, timestamp and status of each signal. `NOT_CHECKED` means the source was not queried; `NOT_FOUND` means it was queried without a match. Never imply an unchecked source was searched. Compare useful verified facts across 10–20 leads without replacing them with a generated essay.

Derive funnel metrics only from persisted events. Document formula, denominator and exclusions for discovered, qualified, contacted, responded, meeting, won/lost, follow-up completion and time to first contact where the schema supports them. Monetary ROI requires actual deal or revenue data. Do not use a fixed value per lead.

Keep future lead priority A/B/C separate from playbook approach A/B/C. Prepare customer messages as drafts until authorized to send. Verify a real journey from lead discovery through saved research, contact, outcome, follow-up, reload and KPI change before claiming the loop works.
