# AIQ Product Engineering System

A portable set of product engineering skills for Codex and Claude Code. Ulises Garcia — AI Product & Systems Architect.

Use `AGENTS.md` as the shared entry point, then choose a playbook, general skills, and a product-specific skill only if it matches the actual project. This repository stores guidance, not project source code or secrets.

Example task: “Read AGENTS.md and the relevant AIQ Builder Skills. Audit this repository first. Classify ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD. Propose the smallest implementation and its verification. Do not deploy without explicit approval.”

`skills/` holds reusable decisions. `project-skills/` holds product context. `playbooks/` gives task sequences. Current product repositories remain authoritative for their implementation and deployment rules.

## Canonical V1 Skills

AIQ has exactly **15 frozen canonical V1 skills**.

13 are physically owned by `aiq-builder-skills`:
- `aiq-universal-event-contract`
- `aiq-server-entitlements`
- `aiq-apple-release-gate`
- `aiq-premium-product-gate`
- `aiq-brand-intelligence`
- `aiq-adaptive-experience`
- `aiq-revenue-activation`
- `aiq-pricing-offer-arch`
- `aiq-commerce-payments`
- `aiq-web-product-quality`
- `aiq-launch-readiness`
- `aiq-growth-marketing`
- `aiq-finance-unit-economics`

The remaining 2 canonical skills are owned by `MrAI-Private-Brain`:
- `aiq-universal-secret-scan`
- `aiq-technology-radar`

**Important Governance Rules:**
- Other directories under `skills/` are support/internal engineering capabilities and are **NOT automatically canonical**.
- Directory existence alone does not grant canonical status.
- Agents must use `AIQ_CANONICAL_15_CORE_PORTFOLIO.md` as the authoritative portfolio definition.
- No new canonical skill may be created implicitly.

Canonical Golden Path for agents: [`playbooks/github-agent-workflow.md`](playbooks/github-agent-workflow.md).

The Claude Code ↔ ChatGPT handoff is currently a documented workflow in `CLAUDE.md`; this repository does not yet contain a working chat bridge.
