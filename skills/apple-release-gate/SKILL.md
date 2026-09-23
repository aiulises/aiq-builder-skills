---
name: apple-release-gate
version: 1.0.0
owner: global-aiq
purpose: Source-validated verification of Apple App Store Review Guidelines, HIG ergonomics, and privacy compliance.
---

# Apple Release Gate

## WHEN TO USE
- When preparing an iOS build (native Swift or Capacitor / WKWebView container) for App Store submission or TestFlight release.
- When reviewing authentication, account settings, in-app purchases, camera permissions, or AI data flows on iOS.

## WHEN NOT TO USE
- When building pure Android or desktop web applications (use `adaptive-experience` or `web-product-quality`).

## REQUIRED INPUTS
- iOS project directory (`ios/` or Capacitor bundle).
- `Info.plist` with permission descriptions.
- App Store Connect metadata & review credentials.
- Application route tree and account settings view.

## PROCESS
1. **Authentication Parity (Guideline 4.8):**
   - `[OFFICIAL REQUIREMENT]` If third-party social login (Google, Facebook, X) is offered, verify that an equivalent privacy-preserving login (e.g. Sign in with Apple) is implemented with equal prominence.
2. **In-App Account Deletion (Guideline 5.1.1(v)):**
   - `[OFFICIAL REQUIREMENT]` Verify in-app account deletion path exists in Profile/Settings. Confirm it purges personal records and invokes the Apple token revocation REST API if Sign in with Apple was used.
3. **Generative AI Data Consent (Guideline 5.1.2(i) - Nov 2025 Update):**
   - `[OFFICIAL REQUIREMENT]` Ensure explicit user consent is obtained before transmitting photos, text, or audio to third-party AI models (Gemini, Claude, OpenAI). Verify App Privacy nutrition labels match.
4. **Monetization & In-App Purchases (Guideline 3.1.1):**
   - `[OFFICIAL REQUIREMENT]` Confirm consumer digital unlocks and subscriptions route strictly through StoreKit 2. Zero external Stripe checkout links inside the iOS binary.
5. **App Completeness (Guideline 2.1):**
   - `[OFFICIAL REQUIREMENT]` Verify absence of dead buttons, placeholder text ("Coming soon"), broken links, or dummy images.
6. **Ergonomics & Touch Targets:**
   - `[PLATFORM GUIDANCE]` Verify interactive hit regions meet minimum 44x44 points (points, not pixels).
   - `[AIQ RULE]` Viewport height configured to `100dvh` with `env(safe-area-inset-*)` padding for Dynamic Island and home bar.

## STRUCTURED OUTPUT
```text
STATUS: PASS | WARNING | BLOCK RELEASE | NEEDS HUMAN REVIEW
CHECKLIST:
  [PASS] Guideline 4.8 (Login Services parity)
  [PASS] Guideline 5.1.1(v) (In-app deletion & Apple token revocation)
  [PASS] Guideline 5.1.2(i) (Third-party AI explicit consent modal)
  [PASS] Guideline 3.1.1 (StoreKit 2 implementation; no external checkout)
  [PASS] Guideline 2.1 (Zero placeholder controls or broken links)
  [PASS] HIG Touch Targets (Hit regions ≥ 44pt)
  [PASS] Info.plist strings (Specific human rationale provided)
```

## FAILURE CONDITIONS & BLOCKERS
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Missing in-app account deletion mechanism or temporary-disable-only option.
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Offering third-party social login without Sign in with Apple parity.
- `[OFFICIAL REQUIREMENT] [BLOCKER]` External web payment links for digital services within the iOS app binary.
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Placeholder UI, dead buttons (`href="#"`), or dummy "Coming soon" views.
- `[PLATFORM GUIDANCE] [WARNING]` Hit region is between 40pt and 43pt in non-critical secondary views.
- `[HEURISTIC] [WARNING]` Launch screen animation duration exceeding 2 seconds.

## APPROVAL LEVEL
- **RED**: App Store binary submission requires developer account holder approval.

## VERIFICATION
- Test script: `bun test test/apple_release_gate.test.ts` scanning routes for account deletion, Apple auth buttons, and Info.plist permission strings.

## DEPENDENCIES
- `server-entitlements` (for StoreKit 2 receipt validation).

## SOURCE REFERENCES
- `SRC-APPL-4.8`: [Apple Guideline 4.8 Login Services](https://developer.apple.com/app-store/review/guidelines/)
- `SRC-APPL-5.1.1v`: [Apple Guideline 5.1.1(v) Account Deletion](https://developer.apple.com/app-store/review/guidelines/)
- `SRC-APPL-5.1.2i`: [Apple Guideline 5.1.2(i) Third-Party AI Data Sharing](https://developer.apple.com/app-store/review/guidelines/)
- `SRC-APPL-3.1.1`: [Apple Guideline 3.1.1 In-App Purchase](https://developer.apple.com/app-store/review/guidelines/)
- `SRC-APPL-2.1`: [Apple Guideline 2.1 App Completeness](https://developer.apple.com/app-store/review/guidelines/)
- `SRC-APPL-HIG-TOUCH`: [Apple HIG Hit Regions](https://developer.apple.com/design/human-interface-guidelines/buttons)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** WWDC policy updates or receipt of an Apple Review rejection notice.
