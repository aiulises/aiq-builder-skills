# AIQ Premium Experience Standard — shared UI, UX, copy and layout playbook
Date: 2026-10-15 | Status: SUPPORT PLAYBOOK (not canonical Skill #16) | Applies to: AIQ apps when adopted by the product repository

## Philosophy
Human before technology. Premium = fewer decisions, clear next action, credible data, beautiful restraint and reliable behavior. Learn from competitors' workflows without copying copyrighted assets, layouts, source code or brand identity. Audit what exists before redesign. Preserve each product's own tokens and brand system. HairPlan-specific reference: `HairPlanPro/docs/product/SMART_MIX_COMPETITOR_UX_BENCHMARK_2026-10-15.md` on its documentation branch.

## 1. UI — visual consistency
- Design tokens for typography, colors, spacing, radii, shadows, focus, semantic states and motion; reuse existing components, never invent parallel systems.
- Clear hierarchy: one page goal, one dominant primary action, subordinate secondary actions; consistent alignment, padding and whitespace; avoid noisy card grids and fake luxury.
- Strong contrast and legibility in daylight, especially for numeric/measurement screens; do not communicate meaning with color alone.
- Responsive from narrow Android/iPhone to foldables, tablet/iPad and desktop/browser; account for safe areas, on-screen keyboard, zoom and touch.
- Use real product data or clearly labeled test fixtures. Never show fabricated activity, metrics, trust badges or Bluetooth status as live.

## 2. UX — interaction and complete flows
- Start from user task, context and time pressure. Progressive disclosure: show the next action, not every setting.
- Every visible control must have a real action or be clearly disabled with explanation. No dead buttons, fake confirmations or misleading mockups.
- Define loading, empty, success, validation, offline, denied, retry, timeout and error states. Preserve user work on navigation and interrupted sessions.
- Support accessible keyboard and screen-reader navigation, logical focus order, sufficiently large targets, reduced motion and visible feedback.
- Prefer minimum taps, safe defaults and undo where feasible. Do not make high-risk actions one-tap without review.
- Security UX: display which agent/tool acts, what data is involved and why; require human approval only at meaningful risk gates, never pretend that local/EU residency or compliance is verified.

## 3. Copy — words and content structure
- Danish-first plain professional language, short headings, specific verbs, labels matching the action and consistent terminology across screens.
- Screen pattern: **What is this? → What is happening? → What can I do next?** Help text only where needed. Explain failures and recovery in human language.
- Distinguish fact, estimate, AI suggestion and human-approved result. Measurements show units and source (live scale vs manual); timestamps and data provenance when relevant.
- No generic AI hype, unsupported superlatives, invented performance claims or faux urgency. Localization must preserve professional meaning and numeric conventions.
- Brand language is product-specific; HairPlan: 'More than a visit. A relationship.' / 'People · Hair · Intelligence.'

## 4. Layout and components
- Use a predictable page structure: context/header → essential status → main task/action → relevant details → secondary navigation.
- Stable placement for save, cancel, back, retry and destructive actions; do not hide critical controls in ambiguous ellipses.
- Cards should group related information; tables for comparisons; forms for real inputs; prominent figures for live measurements.
- Component states and semantics documented once, reused everywhere. No arbitrary pixel-perfect copying from competitors.

## 5. Agent review checklist: collect missing pieces first
For each page and flow produce a compact gap register with columns:
`Page/flow | User goal | UI | UX | Copy | Layout | Data/backend | Accessibility | Mobile/tablet/browser | Evidence | Status | Priority | Proposed minimal fix | Test`.
Use status **VERIFIED / PARTIAL / MISSING / UNKNOWN / LEGACY / DO NOT REBUILD**. Capture screenshots with consent and remove personal information. Review existing design system and route graph before suggesting new components. Rank security/data-integrity blockers ahead of cosmetics. Do not redesign every page at once.

## 6. Definition of done
- Every primary task is demonstrated end-to-end with real or explicitly marked synthetic data; API/auth/tenant checks included.
- All controls and error states are exercised, with reload/back/retry; unit/integration/device tests where applicable.
- Visual checks at mobile, tablet and desktop sizes, accessibility and language review, no overflow or clipped labels.
- Actual implementation evidence, not just screenshots/mockups; record before/after, defects, remaining limitations and owner approval.
- Follow target repo `AGENTS.md`, architecture rules and canonical Golden Path. No autonomous deployment or production changes.

## HairPlan addendum
Guided Smart Mix: client/service → formula → bowl → live/manual grams → Mix More → reweigh → measured/estimated consumption → journal → inventory. Differentiate mixed, remaining, removed from bowl, applied and waste; do not present ingredient-level applied quantities as directly measured if allocated proportionally. Keep COLOR / RESALE / TESTER-SALONBRUG inventory separate. Read HairPlan's detailed competitor benchmark before changing these screens.

## Governance
This is a reusable **support playbook**, not a new canonical skill. It does not supersede the 15-skill freeze, project rules or security P0. Update after validated lessons with explicit authorization; do not turn competitor observations into automatic BUILD instructions.
