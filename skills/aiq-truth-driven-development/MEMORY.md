# AIQ Truth-Driven Development · MEMORY.md
**Purpose:** Portable, version-controlled engineering lessons for the supporting skill.
**Scope:** Public, generalized knowledge only. This is **not** ChatGPT account memory, an autonomous agent memory store, or proof that a workflow is active.

## How agents should use this file
1. Read `SKILL.md` and this file before relevant work.
2. Match lessons to the current task; do not blindly apply a rule to unrelated projects.
3. Separate **VERIFIED** lessons from **REPORTED / NOT INDEPENDENTLY VERIFIED** examples and **HYPOTHESES**.
4. Propose new lessons after reproduction and tests; append only with permission and source provenance.
5. Keep no credentials, customer details, private paths, proprietary architecture or confidential incident specifics.

## Lessons

### TDD-001 · Green tests may hide a permission mismatch
- **Status:** REPORTED / NOT INDEPENDENTLY VERIFIED in this repository
- **Observed pattern:** An authorization test matrix may pass while a route uses a read permission for a write operation.
- **Example:** A reported HairPlan P0-B review identified three treatment-zone mutation routes using a customer-record view permission. A previous report had shown 16 endpoints and 80 authorization checks passing.
- **Generalizable safeguard:** Build an action-to-permission matrix; distinguish GET/read from POST/PUT/DELETE/write; test the lowest-privilege role against every mutation; challenge whether tests reflect intended policy rather than just current code.
- **Verification needed:** Reproduce against the relevant code revision; confirm fix and regression tests before marking VERIFIED.
- **Source:** User-provided P0-B review narrative, 2026-10-15; not independently inspected here.

### TDD-002 · Separate local tests from production assurance
- **Status:** PRACTICE RULE
- **Rule:** Record whether evidence comes from mocks, real HTTP handlers, local PostgreSQL, staging or production. A local success cannot justify a production-safe claim.
- **Verification:** Cite exact command, environment, test scope and exit status.

### TDD-003 · Challenge the test itself
- **Status:** PRACTICE RULE
- **Rule:** For STRICT risk, ask what change would cause the test to fail. Consider property-based or mutation tests when they offer value and can run safely.
- **Limit:** Mutation testing is optional and must never intentionally weaken production code or touch live data.

## Candidate lesson template
```md
### TDD-XXX · Short lesson title
- Status: PROPOSED / REPRODUCED / VERIFIED / SUPERSEDED
- Problem:
- Evidence and reproduction (safe reference):
- Root cause:
- Fix and test:
- General rule:
- Applicability and limits:
- Source / date / reviewer:
```

## Maintenance rules
- Do not overwrite past lessons silently; mark SUPERSEDED with reason.
- Do not convert reported evidence into VERIFIED by rewriting a summary.
- New supporting skills do not become canonical V1 automatically.
- This file changes only through normal reviewed GitHub edits; it is not automatically updated by Friday Truth Audit.
