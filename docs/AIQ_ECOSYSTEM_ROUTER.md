# AIQ Ecosystem Router — canonical map, not a second source of truth
Status: DRAFT for review | 2026-10-14 | Maintainer: owner + CTO

## Why
Every coding agent, connector and approved workflow needs to resolve **which product**, **which source of truth**, **which permissions** and **which evidence gate** applies. This document is a discovery and routing contract, not an API that automatically grants access.

## Authority order
1. User's current explicit instructions and authorization.
2. Target product repo's checked-out AGENTS.md, CLAUDE.md, architecture/security/deployment rules.
3. AIQ cross-domain trust and model orchestration: [aiq-agent-system](https://github.com/aiulises/aiq-agent-system) (AGENTS.md, architecture/MRAI-OPERATING-SYSTEM.md, security/TRUST-COMPLIANCE-BOUNDARIES.md).
4. Reusable engineering patterns: this [aiq-builder-skills](https://github.com/aiulises/aiq-builder-skills) repo (canonical 15 portfolio, matching skill/project-skill).
5. Runtime, deployment and customer transaction truth must be observed from their own authoritative system, never inferred from repo docs or chat.

If rules conflict, STOP the affected action and surface the exact conflicting clauses. Do not quietly choose the most permissive interpretation.

## Product registry (routing, not live-state certification)
| project_id | Purpose | Repo / system | Canonical business data | Isolation |
| --- | --- | --- | --- | --- |
| prj_hairplan_pro | B2B salon consultations, color knowledge, AI support and salon workflows | https://github.com/aiulises/HairPlanPro | Product DB + verified manufacturer/salon knowledge layers; source repo for code | HairPlan production is highest-trust zone; no direct cross-product DB access |
| prj_lead_radar | B2B lead discovery, research, CRM/outreach and follow-up | https://github.com/aiulises/lead-radar | Lead Radar's own persisted CRM/events | No HairPlan data access |
| prj_hairplan_eu | Website/shop + cloud-hosted app (user-reported Shopify and Supabase-backed app) | Shopify/cloud service, exact repo and hosting not yet verified | Shopify for orders, app backend for its own data | Do not assume it shares HairPlan.PRO identity/data |
| prj_mrai_system | Agent coordination, roles, safe handoffs, commercial workflows | https://github.com/aiulises/aiq-agent-system | Governance docs + approved workflow traces | Sandbox no privileged production access |
| prj_aiq_skills | Reusable skill portfolio, guidance and project routing | https://github.com/aiulises/aiq-builder-skills | Canonical 15 skill registry and skill documents | No customer data |
| prj_aiq_lead_radar_placeholder | Empty repository, not a verified active runtime | https://github.com/aiulises/aiq-lead-radar | NONE VERIFIED | Do not deploy or mirror blindly |

Other repos exist (e.g. MrAI-Private-Brain, AIQ-LABS, Colorist), but are NOT automatically active production services. Inspect and classify before connecting.

## Resolve a request
- Identify target product and operation, not just keyword. If 'HairPlan' could mean .PRO vs .EU, check context and ask only when the difference affects the action.
- Read target repo's own AGENTS.md and current branch/worktree. Use `project-skills/hairplan-pro/SKILL.md`, `project-skills/lead-radar/SKILL.md` or `project-skills/shopify/SKILL.md` as applicable.
- Read only matching reusable skills, e.g. auth-security, testing-qa, deployment-production, apple-release-gate, web-product-quality. Do not load every skill into context.
- For legal/marketing/privacy and cross-platform UX, target repo's approved policy applies; HairPlan currently has a draft proposal in PR #39, not yet merged into main. Treat drafts as proposals, not active controls.
- Confirm project_id, operation_id, actor/owner, environment, data class, source refs, permitted tools, DoD, rollback and budget.
- Only then read live connector data with the connector's own authorization. Never pass raw tokens, customer images, personal data or private project records between models unless a specific lawful and authorized workflow requires it.

## Cross-product workflow (no shared database)
Discovery (Lead Radar) -> approved lead qualification -> consent/authorized outreach -> Shopify sales/checkout where appropriate -> fulfillment/activation in product -> product-owned telemetry -> aggregate business reporting.
Every arrow is a **contract**, not permission. Use explicit event/API adapter with version, purpose, minimal data, identity, authorization, trace_id, idempotency, retry/timeout, audit and revocation. Human review for risky writes. No integration is presumed implemented merely because it is drawn here.

## Handoff envelope for agents/connectors
```json
{
  "project_id": "prj_hairplan_pro",
  "operation_id": "op_example",
  "workflow_id": "wf_example",
  "run_id": "run_example",
  "trace_id": "trace_example",
  "environment": "DEV",
  "data_class": "INTERNAL",
  "owner": "one named implementation owner",
  "intent": "one bounded operation",
  "input_refs": [],
  "output_refs": [],
  "tool_allowlist": [],
  "cost_budget": "no extra paid services without approval",
  "policy_gate": "ALLOW|REVIEW|BLOCK",
  "definition_of_done": "tests + user-visible evidence",
  "rollback": "documented reversible path",
  "status": "PLANNED|RUNNING|DONE|BLOCKED|UNKNOWN"
}
```
The envelope is a documentation schema until implemented and tested; it is not a working event bus.

## Gates
G0 Discover: identify canonical repo/branch and active runtime, verify tools and source.
G1 Trust: privacy, IP, data classification, least privilege and legal uncertainty.
G2 Build: existing contracts, unit/integration tests, non-AI fallback, no unbounded loops.
G3 Experience: browser + responsive UI, controls, accessibility, user journey, actual screenshots with synthetic data; physical device tests where available.
G4 Release: local SHA, remote SHA, deployed artifact identity; CI, migrations, smoke tests, rollback, human authorization.
G5 Operate: low-cost deterministic health checks; alert on incidents, failed backups, error spikes, queues; no unrestricted autonomous repair.
G6 Learn: dated evidence-backed lessons promoted to correct owner repo; never duplicate a new canonical source.

## Frequency and token budget
- Every new agent session: short AGENTS.md/router preflight.
- Every code change: targeted lint/typecheck/unit tests; UI changes get browser evidence.
- Every PR: risk/contract review and CI.
- Every release: G0-G4 full targeted release gate and live deployment proof.
- Daily: cheap deterministic uptime/backup/CI status checks ONLY when configured; do not claim they run yet.
- Weekly: owner-readable digest of new incidents, high-risk changes and relevant rules; configure only if approved and costed.
- Quarterly or major change: human-led policy/source review.

## Source verification
The repo and document descriptions above were inspected on 2026-10-14; live production state, connector grants, Hetzner region and Shopify/Supabase portability were not independently verified.
