# AIQ Cross-Repo Agent Quality Gates — V1

Owner: AIQ. This is an **orchestration overlay**, not a replacement for the 15 canonical V1 skills or target repository constitutions. Do not change canonical skill count or ownership. This document is a proposed standard on a draft PR until reviewed and merged.

## Read order / token discipline
1. Target repo `AGENTS.md` / `CLAUDE.md` and local constitution, architecture, status and approval rules FIRST. If absent, inspect README and relevant source.
2. This concise cross-repo index; select only the skill(s) needed for the task. Do not load every skills document.
3. Actual code paths, tests, manifests, migrations and CI workflows relevant to the requested vertical slice.
4. Git status/branch/HEAD and relevant remote/deployment evidence; record UNKNOWN rather than invent.
5. Timebox one 30–90-minute task, reserve 20–30% for tests and handoff, record actual token usage only if telemetry exists.

## Product ownership
- `aiq-builder-skills`: shared practices, proven reusable skills and templates; NOT runtime data.
- `HairPlanPro`: product source, architecture and salon tenant/client data. Its own architecture rules outrank this index.
- `lead-radar`: Lead Radar source, booking evidence, reports, provider integrations and CRM. `aiq-lead-radar` is a distinct repo; do not assume equivalence.
- `MrAI-Private-Brain`: owner control/approvals, status, health and cost guardian; its CONTROL_LAYER and APPROVAL_MATRIX outrank this index. Mr.AI does not become a second canonical product DB.
- `aiq-agent-system`: orchestration and commercial workflow; no duplicate product truths.

## Build order (across products)
P0. **Read-only inventory:** canonical repo and runtime, branch, code ownership, security and release status; classify ALREADY EXISTS/PARTIAL/MISSING/LEGACY/DO NOT REBUILD.
P1. **Safety baseline:** auth/session, tenant isolation, backend secrets, role checks, CI, security scans, backup/restore, approved scopes and negative tests.
P2. **Observability & IDs:** trace_id/request_id, tenant/user/customer/lead/job/run/provider-call IDs, sanitized Sentry, privacy-safe PostHog, release SHA and environment.
P3. **Product vertical slice:** UX design tokens → responsive frontend → authenticated API → DB persistence → error/retry states → unit/contract/E2E.
P4. **Button Truth:** inventory every control, verify actual action, persisted result, negative path and Playwright desktop/mobile emulation; physical Android/iOS testing separately.
P5. **Jobs/voice/MCP:** queue/cron heartbeat, idempotency, bounded retries, tool allowlists, confirmation for writes, cost caps; reuse existing controllers.
P6. **Billing/retention:** server-side entitlements, monthly/annual pricing, accurate discounts, API usage ledger separated by tenant/user/owner/internal, GDPR and store channel checks.
P7. **Release:** local SHA vs GitHub SHA vs Hetzner deployed SHA/image digest, staging smoke, rollback proof, human GO, production smoke and incident plan.
P8. **Learn:** proven failure → root cause → fix → regression test → reusable SKILL, update local CURRENT_STATE/STATUS and PR evidence.

## Shared mandatory gates
- **No dead buttons or fake metrics:** screenshots and green unit tests alone do not prove live features.
- **Privacy:** customer isolation enforced server-side and by RLS where relevant, not by UI filter; never log secrets, raw sensitive client notes or recordings to telemetry.
- **UI:** Apple HIG, Material 3, WCAG 2.2 AA as applicable; consistent product-specific branding, loading/empty/error states, keyboard/touch accessibility.
- **Voice/MCP:** authenticate and scope every tool; read-only by default; confirm side effects, constrain costs and external content.
- **Cron/repair:** Tier 0 monitor, Tier 1 bounded approved idempotent repair, Tier 2 draft fix PR, Tier 3 production/destructive changes only with explicit owner GO.
- **Subscriptions:** verified provider/store webhooks and entitlements, cancellation/deletion, price transparency, privacy and store review checks.
- **No unilateral writes to production, paid APIs, mass mail, merges, releases or store submission.**
- **Proof vocabulary:** PLANNED / BUILT / TESTED / DEPLOYED / PROVEN; label each separately.

## Agent task packet template
```
PRODUCT / REPO / BRANCH:
OBJECTIVE + USER VALUE:
CURRENT TRUTH (local SHA / GitHub SHA / Hetzner SHA):
RELEVANT FILES (max 10 initially):
AUTH + TENANT / COST / PRIVACY RISKS:
SCOPE + NON-GOALS:
ACCEPTANCE (success, error, unauthorized, mobile):
TEST COMMANDS + EVIDENCE:
BUDGET / STOP CONDITION:
OWNER GO REQUIRED FOR:
HANDOFF (files, commit, verified, unknown, next):
```

## Implementation and adoption
This file is the short canonical index, not a request to install every pictured tech. Per-repo adapters link to this index and preserve existing constitutions. Roll out in draft PRs and review each repo. Future global automation/CI/rulesets require a separate permissioned audit. No claim of Hetzner inspection, live tests or app-store approval is implied.

## Mandatory responsive UI/UX + data-truth gate (all AIQ products)
Applies to **every** new or changed page, modal, product grid, inventory view and workflow in HairPlan.PRO, Lead Radar and other AIQ apps. AI agents (Claude, Codex, Gemini and others) must audit and report evidence; writing this checklist does not mean it has been executed.

1. **Inventory before redesign:** identify actual route, component, data source, auth/tenant rules and live vs mocked behavior. Respect existing design system and user edits; do not duplicate an existing feature.
2. **Responsive coverage:** capture real browser screenshots at **360, 390, 768, 1024 and 1440 CSS px** using Playwright; include portrait/landscape where meaningful, and Android/iOS/iPad physical-device checks when available. Emulation alone is not proof of real-device compatibility. Check grid density (typically 1–2 mobile, 2–3 tablet, 4–5 desktop only where readable), overflow, truncated names, tap targets, safe areas, sticky headers, menus, forms, keyboard, zoom, screen-reader labels, contrast and loading/empty/error states. Choose columns based on content rather than hard-coded counts.
3. **Button Truth:** test every visible button, menu, sort, search, filter, upload, edit and close action end-to-end, including permission errors and persistence. No dead mockup actions, fake success toasts or invented values.
4. **Data Truth:** trace displayed numbers **database → API → component**. Each SKU/variant/location/tenant must have its own authoritative record. Suspicious identical stock percentages, grams or unopened-tube counts across shades must be investigated as possible defaults, copied fixtures, cache/query-key bugs or wrong joins, not assumed incorrect without evidence. Change one shade in an isolated test and prove other shades remain unchanged; verify reload, concurrency and negative cross-tenant access.
5. **Salon inventory terminology (HairPlan-specific, not universal labels):** **Farvelager** for color, toner, developer and bleach (grams/ml/tubes); **Videresalg** for take-home customer products (units); **Tester / Salonbrug** for open testers, wash-station liter bottles and salon-use masks (units plus remaining ml/g as applicable). Reuse one product/variant catalog with separate stock locations/uses and traceable transfers; avoid double counting. Do not introduce a POS/checkout merely to count resale stock.
6. **Evidence-based acceptance:** report PASS / FAIL / UNKNOWN by viewport and workflow, with screenshots, Playwright/test commands, affected files, actual source of truth, reproduction steps, root cause and residual risk. Do not call something responsive, secure, deployed or fixed without proof.
7. **Safety and change gate:** start READ-ONLY AUDIT; preserve the current release/demo freeze. No database migration, live inventory write, production change, merge or deploy without separate explicit founder GO. Security P1 findings outrank cosmetic improvements; proposed UI changes remain draft documentation until approved.

**Reusable agent instruction:** “Before declaring any AIQ UI/UX task complete, run the responsive UI/UX + data-truth gate in `playbooks/AIQ_CROSS_REPO_AGENT_QUALITY_GATES.md`, provide viewport screenshots and functional evidence, and state what was NOT verified.”
