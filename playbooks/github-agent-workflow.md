# GitHub Agent Playbook — Canonical Golden Path

**Audience:** Claude Code, Codex, Cursor, Antigravity, and AIQ Marcus Workers.  
**Status:** CANONICAL WORKFLOW SPECIFICATION  
**Governing Principle:** *"Minimum sufficient context. Maximum required evidence. Zero unearned autonomy."*

---

## 1. The Universal Agent Lifecycle

Every agent task across the AIQ ecosystem must execute the following sequential golden path:

```text
1. IDENTIFY
   └── Locate product/repo/environment.
2. DISCOVER
   └── Read existing code (GitHub + Drive context).
3. VERIFY
   └── Determine source of truth and what is already built.
4. PLAN
   └── Formulate the minimum bounded change.
5. BUILD
   └── Coding agent implements on an isolated branch.
6. TEST
   └── Run local unit tests + security + regression.
7. PROVE
   └── Produce evidence of functionality.
8. STAGING / DEVICE
   └── Human Test (Xcode/Browser) for real user experience.
🔴 STOP
   └── "Ready for production. GO?"
9. ULISES GO
   └── Final human approval for risky/irreversible actions.
10. DEPLOY
   └── Push verified changes to production.
11. VERIFY PRODUCTION
   └── Confirm health, auth, and release status live.
12. MEASURE
   └── Analyze real behavior (PostHog / Sentry).
13. LEARN
   └── capture reusable lesson → propose/update existing skill or playbook where appropriate → otherwise register as V2 candidate → never silently create Skill #16 or alter governance.
```

---

## 2. Context & Model Router (Token Budgeting)

To eliminate hallucinations and token waste, agents MUST operate within their assigned context budget:

| Tier | Token Budget | Scope | Appropriate Model |
|---|---|---|---|
| **Level 0: Direct** | < 2.000 tokens | Single CSS token, typo, padding, attribute tweak. | Fast / Small |
| **Level 1: Local** | < 8.000 tokens | 1 component + direct imports + 1 unit test file. | Fast / Standard |
| **Level 2: Feature** | < 20.000 tokens | Feature slice + 1 relevant skill (e.g. `mobile-first-ux`). | Standard |
| **Level 3: System** | < 50.000 tokens | Service manifest + ADR + integration test + schema. | Frontier Reasoning |
| **Level 4: Architecture** | Deep / Multi-Turn | Security boundary, tech radar, migration, incident review. | Frontier Reasoning |

---

## 3. The Four Mandatory RED ZONES

The following four domains are strictly protected. An agent is **FORBIDDEN** from applying autonomous changes to these areas:

1. 🔴 **Database / RLS** — PostgreSQL migrations, schema alterations, Row-Level Security policies.
2. 🔴 **Authentication** — JWT signing, password hashing, session tokens, OAuth flows.
3. 🔴 **Payments / Entitlements** — Stripe integrations, subscription status, trial/tier unlocks.
4. 🔴 **Secrets / Infrastructure** — API keys, credentials, Docker/Hetzner server configs, CI security pipelines.

### Red Zone Modification Protocol
When an agent determines a task requires touching a Red Zone, it MUST halt and follow this exact sequence:
```text
READ ──► DIAGNOSE ──► PROPOSE ──► BACKUP ──► HUMAN APPROVAL ──► CHANGE ──► VERIFY ──► ROLLBACK READY
```
1. **READ & DIAGNOSE:** Analyze the issue without modifying code.
2. **PROPOSE:** Present exact diff, rationale, and risks to the human operator.
3. **BACKUP:** Ensure database snapshot or config backup exists before execution.
4. **HUMAN APPROVAL:** Await explicit human confirmation.
5. **CHANGE & VERIFY:** Execute change, run tests, and probe health endpoints.
6. **ROLLBACK READY:** Ensure immediate revert mechanism (`rollback.sh`) is primed and tested.

---

## 4. Fundamental Rules of Engagement

- **Zero Blind Force-Push:** Never execute `git push --force`. Use lease verification if rebasing feature branches.
- **Zero Blind Branch Deletion:** Never delete branches without documented classification and reconciliation evidence.
- **Distinguish Operational Truths:**
  - `DEVELOPMENT HEAD` = Latest commit on active dev branch.
  - `DEPLOYED SHA` = Commit currently active in runtime directory.
  - `VERIFIED` = Release that has passed automated health checks.
  - `LKG (Last Known Good)` = Release approved by human operator.
- **Never Assume GitHub SHA = Deployed SHA:** Always verify runtime status via server symlink or `/health` telemetry.
- **Preserve Unrelated Work:** Never overwrite, clean, or stash uncommitted user edits without consent.
- **Load Task-Relevant Skills Only:** Never ingest the entire skill repository into context.
- **Secret Scan Before Commit:** Codebases must pass `secret-exposure-scan.mjs` with 0 exposed keys before commits.
- **Produce Evidence, Not Claims:** "Unit tests pass" is unacceptable. Show the exact test command and terminal output.
- **Anti-Self-Tampering:** Agents must NEVER modify governance rules, deploy scripts, or security scans to make a task succeed.
- **Scope Discipline:** Do not create new skills (No "Skill #16"). Do not touch unrelated products or repositories.
