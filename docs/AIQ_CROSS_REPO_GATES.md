# AIQ Cross-Repo Decision Gates & Escalation
Status: DRAFT | 2026-10-14

## STOP conditions
- Wrong repo/worktree/branch, ambiguous target, missing owner or unclear data source.
- Security: secrets in logs/Git, tenant crossing, unsafe auth, unapproved customer-data access.
- Legal: unclear manufacturer content redistribution rights, customer marketing consent, external AI data transfer.
- Infrastructure: unverified deploy SHA, unknown backup/restore status, no rollback, non-isolated prod tests.
- Money: unapproved spend, subscription, paid API usage, unverified payment or refunds.
- Agents: two writers on same files, recursive model-to-model loop, root access or arbitrary production shell.

## Agent decision contract
`ALLOW`: narrow scope, verified authority, tests and evidence.
`REVIEW`: preserve reversible work, ask one concrete owner decision with options and estimated impact.
`BLOCK`: stop risky action, capture safe evidence, propose lawful/security-preserving alternatives.
`UNKNOWN`: unverified. Never call UNKNOWN green.

## Escalation format
- Project / operation / environment / owner
- What is known and source evidence
- What is unknown or conflicting
- Impact and severity (P0-P3)
- Safest reversible option A and alternative B
- Required approval (owner, CTO, DPO/counsel as appropriate)
- Next safe action, cost, rollback and verification

## Review model
One implementer, separate reviewer when useful; only owner can approve publication/deploy/spend. Reviewers share references/diffs, not secrets or entire chats. The agent coordinator cannot grant permissions absent from the underlying connector.

## Proof
A markdown gate is NOT a technical gate. Require tests/branch protection/CI, identity-scoped connector grants, real browser evidence and deploy manifest before claiming enforcement. Track proposed vs installed vs verified status.
