# AIQ Adoption — no big bang
Status: DRAFT | 2026-10-14

## 1. Global router
This PR adds a *supporting* router to aiq-builder-skills. It does not change the frozen canonical 15 skill list, the Mr.AI operating system, or any product's deployment permissions.

## 2. Product entrypoints
HairPlan.PRO: existing draft PR #39 adds Legal Shield, device/browser skills, progressive SaaS resilience, and a file-presence CI. Review/merge that PR separately. Do not misrepresent draft as live.
Lead Radar: inspect `lead-radar` working branch `feat/mrai-private-release` and active runtime before proposing a small AGENTS.md pointer to this router. Do not change app logic or production.
HairPlan.eu Shopify/cloud app: discovery-only; no migration or deployment changes. Verify code export, auth, storage, database, billing, domain and platform terms before portability claim.

## 3. Global-to-product distribution
No automated full file copies. Product AGENTS.md may link to this router and pin a reviewed commit SHA. Agents with network/connector access can read it. Offline agents must use a small checked-in, versioned summary with source URL/SHA and conflict rules. No tool can guarantee all agents read GitHub without startup configuration.

## 4. Implementation priority
P0 secure auth/tenant isolation/backups and working January 2027 demo flows.
P1 UI/browser regression tests, PR gates, three-truths release proof.
P2 monitoring, error/backup alerts and safe rollback.
P3 load tests/queue/scale only when metrics justify; do not buy new services or create speculative infrastructure.

## 5. Not yet done
No global enforcement, no active cross-repo runtime bridge, no scheduled audit, no production proof, no confirmation of the HairPlan.eu platform export route. This document is a proposed operating standard until adopted and verified.
