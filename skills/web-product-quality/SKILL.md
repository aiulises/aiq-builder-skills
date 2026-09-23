---
name: web-product-quality
version: 1.0.0
owner: global-aiq
purpose: Cross-browser web app quality, responsive ergonomics, cookie hygiene, PWA resilience, and Core Web Vitals compliance.
---

# Web Product Quality

## WHEN TO USE
- When developing, testing, or releasing web applications, browser-based SaaS platforms, or PWAs (`HairPlan.PRO`, `HairPlan Me`, `Lead Radar`).
- When configuring cookies, client storage, dynamic viewports, or performance optimization.

## WHEN NOT TO USE
- When building Chrome/Edge browser extensions (use `aiq-browser-extension-eng`).

## REQUIRED INPUTS
- Web application codebase (`src/`).
- Build configuration (`vite.config.ts`, `wrangler.jsonc`).
- Web App Manifest (`manifest.json` / `manifest.webmanifest`).

## PROCESS
1. **Dynamic Mobile Viewport:**
   - `[AIQ RULE]` Configure full-height mobile views to `100dvh` to avoid Safari navigation bar clipping.
2. **Cookie & Storage Hygiene:**
   - `[SECURITY STANDARD]` Session tokens must be stored strictly in `HttpOnly`, `Secure`, `SameSite=Lax` cookies.
   - `[SECURITY STANDARD]` Sensitive secrets must never be placed in unencrypted `localStorage`.
3. **PWA Offline Resilience:**
   - `[ENGINEERING BEST PRACTICE]` Service worker cache strategy: Cache-First for static assets, Network-First for API data with IndexedDB fallback.
4. **Core Web Vitals Optimization:**
   - `[HEURISTIC]` Largest Contentful Paint (LCP) target ≤ 2.5s; Cumulative Layout Shift (CLS) target ≤ 0.1; Interaction to Next Paint (INP) target ≤ 200ms.

## STRUCTURED OUTPUT
```text
WEB PRODUCT QUALITY AUDIT:
  Cross-Browser Compatibility: Safari, Chrome, Firefox, Edge PASS
  Dynamic Viewport: 100dvh configured
  Cookie Security: HttpOnly, Secure, SameSite=Lax confirmed
  PWA Offline Fallback: Operational
  Core Web Vitals: LCP 1.9s, CLS 0.03, INP 110ms (PASS)
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[SECURITY STANDARD] [BLOCKER]` Storing session JWTs or API keys in plaintext `localStorage`.
- `[ENGINEERING BEST PRACTICE] [FAIL]` Layout shifts (CLS > 0.1) due to missing image aspect ratios or missing skeleton loaders.
- `[HEURISTIC] [WARNING ONLY]` LCP is between 2.5s and 3.5s on mobile networks. **(Triggers performance optimization warning; does not block release).**

## APPROVAL LEVEL
- **GREEN**: Automated Lighthouse CI and Vitest pass.

## VERIFICATION
- Test script: `bun test test/web_quality.test.ts` & Lighthouse CI CLI (`lhci autorun`).

## DEPENDENCIES
- `premium-product-gate` (for visual quality ladder).

## SOURCE REFERENCES
- `SRC-W3C-CWV`: [web.dev Core Web Vitals](https://web.dev/articles/vitals)
- `SRC-W3C-WCAG`: [W3C WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Major browser engine releases (Safari WebKit, Chromium).
