# AIQ Agent Bootstrap v1 — Context Routing Contract

Status: PROPOSED / draft, not installed in agent runtimes. This contract extends existing playbooks/github-agent-workflow.md and the frozen 15-skill portfolio. Product repo instructions always win.

## Startup, every task
1. Identify repo, environment, user intent, read/write level, task risk. Unknown => stop and ask one specific question.
2. Read only target repo entry point (AGENTS.md, CLAUDE.md) and mandatory product constitution. For MrAI read STATUS.md then CONTROL_LAYER, APPROVAL_MATRIX, BUSINESS_MODE; for HairPlan read CLAUDE.md, ARCHITECTURE_RULES and CONSTITUTION as relevant.
3. Inspect git status, branch, diff and affected code. Read no more than 1 matching skill and 1 matching playbook initially. Escalate to additional files only on an explicit dependency.
4. Retrieve authoritative state from its owner: operational MrAI STATUS, product code/architecture from product repo, PM NEXT/BLOCKED/DONE from aiq-agent-system, reusable lessons from aiq-builder-skills. Never treat chat memory as live truth.
5. Produce short task packet: task, scope, source of truth, expected output, acceptance tests, risk, GO boundary. One agent writes; second reviews.
6. Follow canonical Golden Path: discover → verify → plan → build on owned branch → test → prove → owner GO for red zones/deploy → observe → learn.

## Routing matrix
| Intent | Mandatory project files | Skill/playbook selection | Gate |
|---|---|---|---|
| HairPlan UI | HairPlan CLAUDE.md + ARCHITECTURE_RULES; touched UI | web-product-quality or premium-product-gate | mobile/browser button truth |
| HairPlan salon inventory/mix | HairPlan architecture + affected domain/routes/db | universal-event-contract if events affected | tenant isolation, stock journal, tests |
| Lead Radar booking | Lead Radar branch AGENTS/CLAUDE + provider contract + active runtime | web-product-quality or universal-event-contract | evidence-based booking vendor detection |
| MrAI automation | MrAI STATUS, CONTROL_LAYER, APPROVAL_MATRIX, BUSINESS_MODE | existing cost/health/restore guards | owner-approved bounded autonomy |
| Auth / RLS / secrets | Target product rules + MrAI approvals | universal-secret-scan (MrAI owned) | RED ZONE; no unattended change |
| Hetzner / backup | MrAI approvals + verified runtime manifests | restore/storage/deployment-provenance guard | restore proof and GO |
| Pricing / subscriptions | Product rules + server entitlements contract | aiq-server-entitlements, pricing-offer-arch | backend entitlement negative tests |
| Shopify | Shopify target repo rules and theme instructions | commerce-payments if checkout affected | duplicate live theme; preview and owner GO |
| General discovery | Repo entry + actual code | none until justified | read-only |

## Context efficiency
- L0 typo: entry + touched file only.
- L1 component: entry + imports + test.
- L2 feature: entry + architecture + 1 skill + feature tests.
- L3 system: add ADR, contracts, integration proof.
- L4 security/incident: full affected trust boundary and independent reviewer.
Budgets in Golden Path are soft planning targets, not API-enforced quotas. No bulk ingestion of Drive, chat transcripts, or every skill.

## Skill and memory promotion
- A discovered issue is a task/incident, NOT automatically a new skill.
- Fix + reproducible regression + review => propose a lesson in an existing skill or playbook.
- Record source commit and observed tests; keep project status in owner repo, not global memory.
- Do not create Skill #16, auto-install external repositories, or sync private chat/PII/secrets.
- External skills: source provenance, pinned version, static scan (e.g. NVIDIA SkillSpector), manual review, sandbox trial, owner GO, then install in approved runtime. Scanner pass alone does not mean trusted.

## Readiness checks
1. Task router chooses the correct repo/mandatory files for each of 8 fixtures.
2. Wrong repo, missing entry, conflicting branches, missing mandatory rules => fail closed.
3. No secret values, no production write, no unapproved download.
4. One task packet per task, handoff under context budget, one writer per worktree.
5. Confirm agent-specific boot hooks for Claude Code, Codex, Antigravity, Grokbot; until verified mark UNKNOWN.
6. Record which file version/SHA was actually read. Do not claim read because link exists.

## Rollout
R0 documentation (this draft) → R1 deterministic local read-only router with fixture tests → R2 repo-specific entrypoint wiring in draft PRs → R3 real agent smoke tests → R4 approval-gated rollout. Never merge or deploy automatically.
