# AIQ Secure Delivery Program — Roadmap & PM Gates (2026-10-08)

Status: **PROPOSED, documentation only**. Owner: Ulises. PM coordination: aiq-agent-system; operating truth: MrAI-Private-Brain/STATUS.md; product truth: HairPlanPro and lead-radar. No automatic jobs or installations are created by this document.

## Objective / Definition of Done
Make AIQ auditable by an external software/security reviewer: clear system inventory, traceable changes, verified backups, least-privilege credentials, tested tenant boundaries, automated CI gates, GDPR evidence, staged Hetzner security and a reversible cleanup. No claim of certification or absolute security.

## Source of truth and read order
1. Product repo local constitution / architecture / AGENTS or CLAUDE and live source.
2. MrAI CONTROL_LAYER + APPROVAL_MATRIX + STATUS (operations/permissions).
3. aiq-agent-system roles/project-manager.md, governance and security contracts (PM).
4. aiq-builder-skills AGENTS.md + only matching SKILL.md and this playbook.
5. Evidence from local/Drive/GitHub/Hetzner; unknown remains UNKNOWN.
Do not create a second status authority or a 16th canonical V1 skill.

## Dependency-based phases, estimated calendar (not scheduled automation)
Each phase starts only when its exit gate is proven; dates are **targets**, not promises. Critical findings may stop/reorder all work.

| Gate | Target | Owner | Execution / scope | Exit evidence |
|---|---|---|---|---|
| G0 Initiate | Day 1 | PM + owner | Define scope, repo ownership, risks, decision log, consent for read-only access, no write | Signed scope and authority matrix |
| G1 Discover | Days 1–3 | Codex/Claude read-only, PM consolidates | Local/Drive metadata/GitHub/Hetzner inventories, active runtimes, branches, data flows, access paths; classify EXISTS/PARTIAL/MISSING/LEGACY | Evidence-linked asset map and unknowns |
| G2 Contain | Days 3–5 | Security reviewer + owner | Address confirmed critical exposures with owner GO; MFA, key access, SSH least privilege, isolate dangerous agents; never rotate blindly | Access matrix, exposure/mitigation log, tested continuity |
| G3 Recover | Days 4–7 | Ops + owner | Inventory backups, alerts, encryption, offsite copy, retention, RPO/RTO; restore into isolated environment | Restore log + checksum/integrity + recovery owner; without proof = UNKNOWN |
| G4 Guard code | Days 6–10 | Codex implement, Claude review | Start HairPlan, then lead-radar, then MrAI; scoped draft PRs for secret scan, SAST/SCA, dependency, unit/contract/RLS tests, branch protection proposals | CI runs on actual PR, negative tests, human approval |
| G5 Runtime | Days 8–12 | Ops/Security | Hetzner read-only inspection, hardening plan, trace IDs, sanitized Sentry/PostHog, cron heartbeat, safe repairs, API budgets; stage NVIDIA SkillSpector and separately assess OpenShell | Stage evidence, rollback dry run, resource and isolation checks |
| G6 Privacy | Days 10–13 | Owner + DPO/legal reviewer | GDPR RoPA, data flows, legal bases, processors/DPAs, international transfers, retention, access/deletion and incident response; DPIA assessment where required | Gap register + reviewed documents, no false compliance claim |
| G7 Clean | Days 12–14 | PM + owner | KEEP/ARCHIVE/REVIEW/DELETE PROPOSED for local/Drive/repos; check consumers, backup and retention; owner GO before changes | Approved manifest, rollback path, post-cleanup smoke |
| G8 Verify & operate | Day 14 onward | PM + ops | Independent review, remediation backlog, regression evidence, 3-truth SHA checks and recurring reporting | Signed review findings, owners, due dates, tested controls |

## Runtime schedules — activate only after G1/G3 baseline and owner approval
| Job | Proposed cadence | Why | Failure action |
|---|---|---|---|
| Health + queue/cron heartbeat | Every 5–15 min if existing infrastructure supports; avoid duplicate polling | Catch failures quickly | Alert only; no blind restart |
| Backup job verification | Daily, after existing backup window | Missing/stale/failed backups | Critical alert; no false success |
| Secret/dependency scan | Each PR + weekly inventory | Prevent leaked keys and vulnerable packages | Block PR for validated critical finding; triage false positives |
| Restore rehearsal | Monthly isolated small sample, quarterly broader DR drill | Prove recoverability | Escalate failed restore, no cleanup |
| Access/SSH/MCP permissions review | Monthly and after personnel/agent changes | Least privilege | Revoke only with owner-approved impact check |
| Cost/usage and error review | Daily short digest, weekly trend | Detect loops, spikes, failing jobs | Budget alert; bounded repair only when preapproved |
| GDPR retention and processor review | Quarterly + when vendor/data flow changes | Privacy governance | Record gap and responsible reviewer |
| Drive/local cleanup | One-time approved wave, then quarterly review | Avoid accumulating risky copies | No unattended delete |
| Security incident tabletop | Quarterly | Practice response | Capture action items |
These are **proposals**. No task, cron or CI schedule should be created solely from this plan.

## Program work breakdown / dependencies
G0 → G1 → (G2 parallel with G3 when emergency) → G4 and G5 and G6 in controlled parallel → G7 only after G3 restore and G2 dependency review → G8.
Within G4: HairPlan authentication/tenant boundaries first → Lead Radar booking/provider evidence → MrAI control/agent boundary. Shared standards are linked, not duplicated.
One owner per branch/worktree. PM issues one task packet; implementer opens scoped PR; independent reviewer checks; owner approves merge/deploy.

## Task packet / memory discipline
Every task must include: issue ID, target repo, scope/non-goals, exact branch + SHA, source-of-truth links, preflight, security/tenant/privacy/cost impact, acceptance tests (happy/error/unauthorized/mobile), evidence paths, owner GO boundary, and handoff.
Memory layers:
- `aiq-builder-skills`: reusable **proven** lessons only; no ephemeral status or secret values.
- `aiq-agent-system`: program backlog, decisions, ownership, dependency gates and task packets.
- `MrAI-Private-Brain/STATUS.md`: actual operational status and blockages.
- Product repos: product-specific architecture, migrations, tests and release evidence.
At task close: update existing repo status only if verified, note what was actually run, capture reusable root-cause→fix→regression in the relevant existing skill after review. Never silently rewrite canonical skill portfolio.

## RACI / escalation
Owner: approves privileged changes, cost, cleanup, deploy and data handling.
PM (aiq-agent-system): sequencing, NEXT/BLOCKED/DONE, risks and dependencies.
Codex/Claude: one implementer, other independent reviewer; use least privilege.
MrAI: approved monitoring, cost/health and operational truth, no unapproved self-healing.
Grokbot: specialist research/scan under least privilege, not automatic installer.
DPO/legal professional: reviews GDPR gaps where required.

## Stop / release conditions
Stop for unexpected secret exposure, missing verified backup before cleanup, unknown live consumer, SSH host key mismatch, untested tenant isolation, missing rollback or unapproved production access. PLANNED ≠ BUILT ≠ TESTED ≠ DEPLOYED ≠ PROVEN.
