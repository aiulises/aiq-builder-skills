# AIQ Business Agent OS — Idea Vault / Brainstorm (2026-10-08)

**Status: BRAINSTORM ONLY — PARKED. NOT APPROVED TO BUILD.** This is a durable product idea capture, not an implementation instruction, deployment authorization, new canonical skill, or claim that APIs work. Owner: Ulises. Revisit only when explicitly prioritized by owner/PM.

## Vision
Turn Grokbot / Mr.AI-inspired agent capabilities into a tenant-isolated SaaS product where each business gets a configurable AI teammate. Voice-first, minimal typing, human-guided actions, proactive ideas, evidence-based decisions, and safe scaling. Models remain replaceable; no single model gets privileged production access.

## Customer jobs / channels
- Google Business Profile review triage and drafted replies; platform permissions and allowed publishing must be checked.
- Trustpilot review monitoring/draft responses; verify commercial API terms and business access.
- Unified inbox: website chat, WhatsApp, Instagram/Facebook DM, SMS, email, with channel-specific official adapters and consent.
- Voice assistant on phone/mobile/web; speech-to-text, text-to-speech, push-to-talk, readback/confirmation for consequential actions.
- Optional telephony: inbound voice agent, callback and human handoff, lawful recording notices and retention.
- Camera/photo-first: invoice/product extraction, anomaly detection, human confirmation before inventory/accounting changes.
- Salon pilot: booking vendor discovery (Planway/BookSalon/Fresha etc.), reviews and customer service; no cross-product data access by default.

## Agent behaviour
- Suggest innovative, prioritized business improvements, each with evidence, expected benefit, cost and reversible experiment.
- Ask short Q&A when uncertain; never fabricate booking, review, customer identity or API success.
- Detect stale feeds, broken integrations, failed scheduled jobs, duplicate events, corrupted/trash data, missing links in a workflow.
- Separate observation → diagnosis → proposal → safe test → approval → action → verification → learning.
- Human handoff on complaints, refunds, cancellations, identity ambiguity, sensitive data and low confidence.
- Never self-modify production or autonomously merge/deploy. Safe self-repair only for explicitly approved bounded operations.

## Architecture hypothesis
1. Web/mobile/voice UI + channels.
2. Identity, tenant_id, entitlements, consent, RBAC, rate limits.
3. Model-agnostic agent orchestration, versioned prompts/tools, per-tenant knowledge with citations and retention.
4. Typed tools / workflow engine, durable queue, idempotency keys, dead-letter queue, approvals, trace IDs.
5. PostgreSQL with RLS, object storage, audit trail, observability, per-tenant model/token/voice cost ledger.
6. Scale via load tests, SLOs, concurrency quotas, queue backpressure, horizontal workers, circuit breakers and rollback.
7. Playwright for deterministic UI/browser testing and allowed supervised browser flows; prefer official channel APIs.
8. Strict trust separation: HairPlan production, Lead Radar, MrAI sandbox, commerce and future SaaS tenant data.

## UX principles
- Voice first, text always available; accessible captions and correction/undo.
- Single daily brief: what happened, what needs approval, what is broken, what agent suggests.
- Three interaction states: DONE with proof / NEEDS YOUR ANSWER / BLOCKED with reason.
- Never show a simulated integration as live.
- Ask one concise clarification at a time, with proposed safe default where applicable.

## Discovery questions before any build
- Target customer: salon-first vs broader local business?
- First paid use case and expected willingness to pay?
- Provider APIs, permissions, quotas, terms and geographic coverage?
- GDPR lawful bases, processors, call recording, cross-border transfers and deletion?
- Per-tenant unit economics and failure budgets?
- How to evaluate quality, safety and human handoff?
- Should product be inside MrAI, Lead Radar, or separate SaaS repo? Decide after repo/runtime audit, not by creating another duplicate.

## Proposed later stages (NOT scheduled)
D0 evidence and user interviews → D1 PRD, architecture/ADR, threat model and pricing → D2 isolated tenant MVP → D3 reviews + voice draft flow → D4 messaging/phone adapters → D5 proactive QA, load tests, scale → D6 controlled pilots → D7 paid rollout.

## Success criteria for future proposal
At least one validated customer workflow; official provider access; isolated tenant negative tests; audit/consent/retention; voice latency and accessibility targets; approved human-in-loop actions; measurable cost per tenant; successful backup/restore; owner GO.

## Ownership and memory
Store this as an idea, not operational STATUS, active PM NEXT, or canonical SKILL. If approved later, PM creates scoped task packets in aiq-agent-system; product repo owns implementation; verified reusable engineering lessons may be promoted to an existing skill after review.

**DO NOT BUILD NOW. DO NOT DOWNLOAD TOOLS, PROVISION SERVICES, CONNECT CUSTOMER CHANNELS, SCHEDULE JOBS OR SPEND MONEY BASED ON THIS FILE.**
