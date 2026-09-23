---
name: adaptive-experience
version: 1.0.0
owner: global-aiq
purpose: Multi-device ergonomic adaptation across Phone, Tablet/Foldable, Desktop, and Large Screen Tizen displays.
---

# Adaptive Multi-Device Experience

## WHEN TO USE
- When designing responsive layouts across multiple device form factors (mobile phones, iPads/tablets, foldables, desktop web, smart displays).
- When implementing navigation structures (bottom navigation bar vs navigation rail vs permanent drawer vs spatial focus).

## WHEN NOT TO USE
- When configuring backend database pooling or server clustering.

## REQUIRED INPUTS
- Target screen resolution and viewport width range.
- Primary input modality (touch/tap, mouse/keyboard, spatial remote control D-pad).
- Screen role (focused consumer app, dense pro dashboard, passive glanceable mirror display).

## PROCESS: 4-TIER ERGONOMIC ADAPTATION
1. **Phone (Compact < 600px):**
   - `[AIQ RULE]` Dynamic mobile viewport `100dvh` with `env(safe-area-inset-*)` padding.
   - `[HEURISTIC]` Single-column layout; primary actions in bottom 40% thumb zone; recommended 3 to 5 bottom navigation items.
2. **Tablet & Foldable (Medium 600–1024px):**
   - `[AIQ RULE]` Never simply stretch a single phone column across a 10-inch screen.
   - `[AIQ RULE]` Implement Master-Detail layout (list on left, detail on right) or collapsible vertical Navigation Rail.
3. **Desktop (Expanded > 1024px):**
   - `[AIQ RULE]` Multi-panel horizontal workspaces with persistent sidebar.
   - `[ENGINEERING BEST PRACTICE]` Keyboard shortcut support (`Cmd+K` command palette, `Esc` dismiss) and visible focus rings.
4. **Large Screen / Smart Display / Samsung Tizen (10-Foot UI):**
   - *Activated strictly when targeting TV/salon displays; not required for standard web apps.*
   - `[PLATFORM GUIDANCE]` Spatial D-pad focus engine (`outline: 4px solid var(--accent); transform: scale(1.04);`).
   - `[HEURISTIC]` Typography scaled for 2–3 meter distance (body text ≥ 24px, headers 48px+).

## STRUCTURED OUTPUT
```text
DEVICE ERGONOMIC AUDIT:
  Viewport: 820x1180 (Tablet)
  Layout Mode: Master-Detail Split
  Navigation: Vertical Navigation Rail (Left)
  Touch Clearance: 48dp minimum
  Keyboard Accelerators: Configured
  Status: PASS
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[AIQ RULE] [FAIL]` Tablet layout is merely a stretched mobile view with 400px of empty margins on either side.
- `[ENGINEERING BEST PRACTICE] [FAIL]` Desktop layout lacks keyboard accessibility or produces horizontal overflow.
- `[HEURISTIC] [WARNING ONLY]` Bottom nav on phone has 6 items; thumb zone action is slightly higher than 40%. **(Heuristics do not block release).**

## APPROVAL LEVEL
- **YELLOW**: Layout shifts across breakpoints require UX lead review.

## VERIFICATION
- Test script: `bun test test/viewport_matrix.test.ts` testing DOM rendering at 390px, 820px, and 1440px.

## DEPENDENCIES
- `premium-product-gate` (for quality ladder verification).

## SOURCE REFERENCES
- `SRC-APPL-HIG-TOUCH`: [Apple HIG Touch Targets](https://developer.apple.com/design/human-interface-guidelines/buttons)
- `SRC-M3-NAV`: [Material 3 Navigation Rails & Drawers](https://m3.material.io/components/navigation-bar/overview)
- `SRC-M3-TOUCH`: [Material 3 Target Sizing](https://m3.material.io/foundations/accessible-design/accessibility-basics)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Major OS device form-factor announcements.
