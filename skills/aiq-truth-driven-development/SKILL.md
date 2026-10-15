---
name: aiq-truth-driven-development
description: Risk-adaptive, evidence-first AI software engineering. Audit existing work, model risks, test first, build minimally, verify, challenge claims, learn from reproduced errors, and require human release approval.
status: supporting-skill
version: 0.2.0
canonical_v1: false
---

# AIQ Truth-Driven Development · V2
**Build smarter. Learn visually. Ship safely.**
**Core principle:** An agent's claim is not evidence. A green test only proves the specific behavior exercised in its actual environment. Never invent PASS, deployment, security guarantees or independent verification.

## When to activate
Use for any AI-assisted implementation, refactor, security change, bug fix or release review. Scale verification by risk rather than forcing expensive checks on every change.

### Risk gate — FAST vs STRICT
- **FAST**: copy, styling, low-impact isolated UI. Require scoped audit, minimal diff, appropriate checks and human approval where repo policy requires it.
- **STRICT**: authentication, authorization, tenant data, database, payments, secrets, background workers, destructive changes, infrastructure, migrations and deployments. Require explicit threat scenarios, tests first when feasible, negative/positive coverage, independent challenge and rollback.
- **UNKNOWN risk**: classify STRICT until understood.
- The target repo's more restrictive rules always win. A FAST classification does not bypass Founder GO.

## Seven gates (test-first V2)
1. **AUDIT** — Confirm actual repo, branch, HEAD, status, rules, roadmap, affected files and data flow. Classify ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD. Establish a baseline and list unknowns.
2. **THREAT & TEST FIRST** — State expected behavior and misuse cases *before* implementation. For STRICT changes, define a small threat model: assets, actors, trust boundaries, entry points, abuse cases and mitigations. Write focused failing tests when feasible; if not feasible, state why and design a verifiable alternative. Do not manufacture a red test.
3. **BUILD** — Propose and implement the smallest authorized change in an isolated branch/worktree; preserve data, secrets and user edits. Explain how to revert. No unapproved scope expansion.
4. **VERIFY** — Run relevant type checks, lint, unit, integration, real-route and database tests, device checks where appropriate. Capture exact commands, environment, exit codes, assertions and test data isolation. Distinguish mocked, local, staging and production evidence.
5. **CHALLENGE** — Try to disprove the result: permission vs operation, read/write, ID tampering, tenant boundaries, workers, error paths, concurrency, regressions and test blind spots. Use independent review where available; a second pass by the same agent is not independent. For high-value critical tests, consider property-based testing or mutation testing **in a safe isolated environment**, never production. Record any surviving mutants and what they imply.
6. **LEARN** — For reproducible failures, record observed issue -> reproduction -> root cause -> fix -> verification -> generalized lesson -> limits. Update MEMORY.md only with evidence; do not claim a proposed fix is verified. Promote to reusable skills only after review and with provenance.
7. **FOUNDER GO** — Report scope-limited VERIFIED / PARTIAL / FAILED / UNKNOWN / BLOCKED, remaining risks, and exact next action. Distinct explicit approvals for edit, commit, push, merge, deploy, spending, destructive tests and external communications as required by project policy.

## Acceptance matrix (especially STRICT)
| Check | Expected evidence |
| --- | --- |
| Correct role | Authorized action succeeds with real permission context |
| Wrong role | 403 or appropriate denial, not just a mocked helper |
| No login | 401 at actual route boundary |
| Cross-tenant | No read, write, enumeration or ID leakage across tenants |
| Read vs write | Read privilege alone cannot mutate records |
| Malformed/tampered ID | Fail closed with no data disclosure |
| Worker/service identity | Background jobs keep functioning under correct non-human permissions |
| Regression | Previously working legitimate flows still pass |
| Data safety | Test isolation, safe migrations, restore and rollback where applicable |

Check the implementation AND whether the tests would fail if the security control were absent. Passing a limited matrix never means the entire product is secure.

## Reporting contract
Report:
1. Goal, risk mode, authorized scope and repo/branch/HEAD/diff
2. Claims vs observations vs direct evidence, with paths and exact test commands
3. Negative cases and attempted counterexamples
4. What is mocked, untested, unverified or blocked
5. Verdict for each claim: **VERIFIED, PARTIAL, FAILED, UNKNOWN, BLOCKED**
6. GO/NO-GO recommendation, explicit approval boundary and rollback
7. MEMORY.md lesson candidate with evidence status

Never confuse a documentation commit with activation of an agent workflow.

## Visual Architect teaching
Explain in short Danish-first steps, with real business metaphors AND real technical mapping: `index.html` = front door; `src/` = workshop; `components/` = reusable workstations; database = customer archive; authentication = identity; authorization = keys; tenant isolation = separate salons. Show file names, actual control, and how to verify it. Metaphors do not replace technical proof.

## Case lesson — reported HairPlan P0-B
An initial report said 16 endpoints passed 80 authorization checks. A subsequent read-only review reported three treatment-zone POST handlers gated by `view_client_records`, allowing an apprentice role with read permission to mutate treatment data. Expected policy: GET retains read access; zone start/check/end POST require an appropriate stylist-level write gate, with negative and positive tests. **This is a reported coverage gap, not independently reproduced by this public skill and not proof of intentional AI deception.** Do not label fixed until the change and tests are verified.

## Safe skill memory
Read adjacent `MEMORY.md` for reviewed lessons and open hypotheses. MEMORY is a versioned project knowledge file, not a claim that the model's internal memory or all agents update automatically. Append only non-sensitive, generalized facts with status and provenance. Do not copy secrets, client data or private implementation details to this public repository.

## Governance
Supporting skill only; does **not** change the frozen 15 canonical V1 portfolio. Follow `AGENTS.md`, product repo instructions and Founder GO. Do not claim formal security certification, guaranteed bug detection, automatic tool integration or trademark registration.

## Agent invocation
“Use AIQ Truth-Driven Development V2. Audit before building, choose FAST/STRICT, define risks and tests first, implement only authorized scope, verify with exact evidence, challenge your own success claims, propose a MEMORY.md lesson, and ask for GO before any commit or deploy.”
