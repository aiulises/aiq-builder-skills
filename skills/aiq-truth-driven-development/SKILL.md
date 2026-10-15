---
name: aiq-truth-driven-development
description: Evidence-first AI-assisted software engineering. Audit existing code, implement minimal changes, independently challenge claims, verify real behavior, and promote proven lessons to reusable skills.
status: supporting-skill
version: 0.1.0
canonical_v1: false
---

# AIQ Truth-Driven Development
**AIQ Builder Skills · Build. Verify. Challenge. Learn.**

## Core rule
An AI agent's statement is a hypothesis, **not evidence**. A passing test proves only the behavior and environment actually exercised. Never report PASS, secure, production-ready, deployed or fixed without direct, reproducible proof. When evidence is missing, say UNKNOWN.

## Six-stage workflow
1. **AUDIT** — Inspect the actual repo, branch, git status, relevant code, architecture, data boundaries, existing tests and owner. Classify ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD. Read the target product's rules and roadmap. Avoid duplicate features.
2. **BUILD** — Propose the smallest change with scope, risk, rollback and acceptance criteria. Obtain explicit authorization before editing when required by repo policy. Use an isolated branch/worktree. Preserve user data and secrets.
3. **VERIFY** — Run type checks, unit/integration tests, authorization/negative tests and relevant end-to-end checks. Record exact commands, exit codes, environment and tested paths. Verify actual HTTP routing, database boundaries and UI interaction where applicable. Do not conflate mocked tests with live database or production validation.
4. **CHALLENGE** — Deliberately try to disprove the claimed success: inspect adjacent routes, role/permission boundaries, read-vs-write, cross-tenant IDs, malformed inputs, missing auth, service-worker identities, failure modes, regressions and whether test fixtures hide bugs. Prefer an independent reviewer or a separate adversarial pass; independence must not be invented.
5. **LEARN** — Record a reproducible issue -> root cause -> fix -> verification -> reusable rule. Only promote a lesson to shared skills when grounded in observed evidence. Avoid turning a one-off assumption into universal policy. Preserve source provenance and canonical V1 freeze.
6. **FOUNDER GO** — Summarize evidence, risks, and the exact proposed next action. Require distinct approval for commit, push, merge, deploy, destructive tests, production access, spending, or external communication. Documentation is not deployment permission.

## Truth labels
- **VERIFIED** — directly supported by reproducible evidence, with exact scope.
- **PARTIAL** — some checks pass; meaningful gaps remain.
- **FAILED** — a test or requirement is demonstrably not met.
- **UNKNOWN** — not tested or evidence unavailable.
- **BLOCKED** — cannot safely proceed until a dependency or approval is resolved.

Do not mark a feature GREEN because an agent wrote “16/16 PASS” if only a limited matrix was exercised. Say precisely *what* passed and *what* was not checked.

## Standard truth-audit report
- Goal and authorized scope
- Repo / branch / commit / dirty files
- Claims vs evidence table: CLAIM | OBSERVATION | TEST/FILE | VERDICT
- Tests run (exact command, environment, exit code)
- Adversarial checks, missing coverage and counterexamples
- Security: authn/authz, read/write roles, tenant isolation, workers, secrets, data safety, rollback
- Remaining risks and UNKNOWN items
- Recommended next action: GO / NO-GO with exact boundary
- Reusable lesson to capture, if verified

## Visual Architect teaching mode
Explain technical structures using familiar physical-business metaphors, then map them back to real files and security controls:
- `index.html` = front door; `src/` = workshop; `components/` = reusable workstations
- Database = records archive; authentication = identity check; authorization = which keys open which rooms
- Tenant isolation = different salons share the building but cannot access each other's customer files
- Tests = rehearsals, **not** proof of a real-world launch
Keep steps short and concrete. Never let the metaphor replace the technical requirement.

## Worked lesson: HairPlan P0-B (reported; not independently verified here)
A first local report said 16 endpoints passed five authorization scenarios (80 checks). A subsequent read-only review identified three treatment-zone POST handlers gated with `view_client_records`, which could let `apprentice` users mutate treatments. Correct expected design: GET retains view permission; zone start/check/end POST require a stylist-level write gate, followed by fresh negative/positive tests and regression checks. This is an example of **coverage blindness**, not proof that the AI deliberately lied or hallucinated. Treat this example as a reported finding until independently reproduced in the target repo.

## Commercial and governance boundaries
This is a **supporting** skill, not a new member of the frozen 15 canonical V1 skills. Respect `AGENTS.md`, the canonical portfolio, target repo instructions and explicit Founder GO. Do not leak private AIQ Builder OS instructions, customer data, credentials or proprietary product implementation details. No claim of formal certification, guaranteed security or registered trademark.

## Example invocation
“Apply AIQ Truth-Driven Development to this change. Audit first, list claims and evidence, challenge the tests and authorization boundaries, report VERIFIED/PARTIAL/FAILED/UNKNOWN, and ask before any commit or deployment.”
