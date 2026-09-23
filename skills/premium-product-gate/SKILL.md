---
name: premium-product-gate
version: 1.0.0
owner: global-aiq
purpose: 9-stage quality ladder enforcing intentional, accessible, high-performance UI/UX and eliminating generic AI slop.
---

# AIQ Premium Product Gate

## WHEN TO USE
- Before marking any frontend screen, user interface, or client-side flow ready for production release.
- When evaluating UI hierarchy, touch target ergonomics, contrast ratios, skeleton loaders, or Core Web Vitals.

## WHEN NOT TO USE
- For pure backend service APIs without user-facing surfaces.

## REQUIRED INPUTS
- Target screen / component code.
- Rendered DOM tree and CSS stylesheets.
- Target platform identifier (`web` | `ios` | `android` | `pwa` | `extension`).

## PROCESS: THE 9-STAGE QUALITY LADDER
Ascend through all 9 stages sequentially:
1. **Functional:** `[ENGINEERING BEST PRACTICE]` 100% tests pass; all buttons, tabs, links, and form handlers are wired. Zero dead controls (`href="#"`).
2. **Secure:** `[SECURITY STANDARD]` Zero exposed secrets in client assets; strict tenant/user boundary enforcement.
3. **Platform Correct:** `[OFFICIAL REQUIREMENT]` Respect platform requirements (e.g. native back gestures on Android; safe area insets on iOS).
4. **AIQ Premium UX:** `[AIQ RULE]` Intentional spatial rhythm; one primary job per screen; progressive disclosure; zero generic purple gradients or random sparkle icons.
5. **Mobile Quality:** `[AIQ RULE]` Thumb-zone primary actions; safe area padding (`env(safe-area-inset-*)`); dynamic viewport height `100dvh`.
   - `[HEURISTIC]` Touch hit targets recommended ≥ 48px (44pt Apple, 48dp Android). Recommended max 5 items in bottom navigation.
6. **Accessibility:** `[SECURITY STANDARD]` WCAG 2.2 AA compliance: contrast ratio ≥ 4.5:1 for body text (3:1 for large text/icons); VoiceOver accessibility labels on icon buttons; keyboard focus rings (`:focus-visible`).
7. **Performance:** `[ENGINEERING BEST PRACTICE]` Core Web Vitals: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1. Layout-matching skeleton loaders mandatory to eliminate layout shift during data fetch.
8. **Analytics:** `[AIQ RULE]` Key user milestones emit typed events conforming to the Universal Event Contract.
9. **Release Ready:** `[ENGINEERING BEST PRACTICE]` Device smoke test executed; deployed Git SHA tagged.

## STRUCTURED OUTPUT
```text
AIQ QUALITY LADDER SCORECARD:
  1. Functional:       PASS
  2. Secure:           PASS
  3. Platform Correct: PASS
  4. Premium UX:       PASS
  5. Mobile Quality:   PASS (Heuristic: 4 bottom tabs, primary CTA in thumb zone)
  6. Accessibility:    PASS (Contrast 6.2:1, ARIA tree complete)
  7. Performance:      PASS (LCP 1.8s, CLS 0.02, Skeleton loaders verified)
  8. Analytics:        PASS (Event: scan_viewed emitted)
  9. Release Ready:    PASS (Smoke test verified on device)
OVERALL: PASS
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[SECURITY STANDARD] [BLOCKER]` Client bundle leaks secret keys; unauthenticated cross-tenant data visible.
- `[ENGINEERING BEST PRACTICE] [BLOCKER]` Dead buttons, broken routes, or uncaught JavaScript exceptions.
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Text contrast < 3:1 (illegible text); content obscured by device notches.
- `[AIQ RULE] [FAIL]` Bare spinner or blank white canvas on primary screen (skeleton loader missing).
- `[HEURISTIC] [WARNING ONLY]` Bottom navigation has 6 items instead of 5; primary button is outside bottom 40% thumb zone; LCP is 2.8s. **(Heuristics must NEVER block a release).**

## APPROVAL LEVEL
- **YELLOW**: Requires design / UX lead sign-off before public release.

## VERIFICATION
- Test script: `bun test test/premium_quality_gate.test.ts` scanning DOM for dead links, missing aria labels, and contrast ratios.

## DEPENDENCIES
- `universal-event-contract` (for stage 8).
- `brand-intelligence` (for stage 4 aesthetics).

## SOURCE REFERENCES
- `SRC-APPL-HIG-TOUCH`: [Apple HIG Hit Regions](https://developer.apple.com/design/human-interface-guidelines/buttons)
- `SRC-M3-TOUCH`: [Material 3 Accessibility](https://m3.material.io/foundations/accessible-design/accessibility-basics)
- `SRC-W3C-WCAG`: [WCAG 2.2 Level AA](https://www.w3.org/WAI/WCAG22/quickref/)
- `SRC-W3C-CWV`: [web.dev Core Web Vitals](https://web.dev/articles/vitals)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Major W3C accessibility revision or updated mobile OS design guidelines.
