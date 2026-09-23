---
name: launch-readiness
version: 1.0.0
owner: global-aiq
purpose: 10-point commercial pre-flight flight check, live transaction verification, and instant rollback governance.
---

# Launch Readiness

## WHEN TO USE
- 24 to 48 hours prior to exposing any AIQ product to public traffic, switching DNS, or kicking off a marketing campaign.
- Before tagging a production release or promoting a development head to Last Known Good (LKG).

## WHEN NOT TO USE
- During early prototype construction or local feature development.

## REQUIRED INPUTS
- Production target domain.
- Deployed Git commit SHA.
- Live payment test card.
- Transactional email credentials.
- Rollback command definition.

## PROCESS: THE 10-POINT LAUNCH FLIGHT CHECK
1. **Domain, DNS & SSL:** Verify Cloudflare proxy active, SSL/TLS set to Full (Strict), and apex redirects properly.
2. **Live Payment Verification:** `[SECURITY STANDARD]` Execute real $1.00 transaction in live mode; verify webhook unlock; refund immediately.
3. **Real Device Smoke Test:** Verify cold start on physical Samsung Galaxy Android and iPhone Safari.
4. **Transactional Email Delivery:** Verify welcome and password reset emails arrive within 15 seconds.
5. **Telemetry Ingestion:** `[AIQ RULE]` Confirm Universal Event Contract events appear in live PostHog stream.
6. **Sentry Observability:** Sentry release tagged with exact Git commit SHA; zero unhandled exceptions.
7. **SEO & Social Graph:** Single `<h1>`, meta description (150–160 chars), OpenGraph preview image (1200x630px).
8. **Legal & Compliance:** `[OFFICIAL REQUIREMENT]` Public Terms of Service, Privacy Policy, and in-app account deletion verified.
9. **System Health Probe:** `/health` endpoint returns 200 OK with DB latency < 30ms.
10. **Verified Rollback Path (LKG):** `[AIQ RULE]` Previous Last Known Good commit SHA recorded; instant rollback command verified.

## STRUCTURED OUTPUT
```text
LAUNCH READINESS FLIGHT CHECK:
  [PASS] 1. Domain, DNS & SSL (TLS 1.3 Strict)
  [PASS] 2. Live Payment Test ($1.00 charge & refund verified)
  [PASS] 3. Real Device Smoke Test (Samsung & iPhone clean)
  [PASS] 4. Transactional Emails (Delivered in 8s)
  [PASS] 5. Telemetry Ingestion (PostHog receiving events)
  [PASS] 6. Sentry Observability (Git SHA tagged)
  [PASS] 7. SEO & OpenGraph (1200x630 image verified)
  [PASS] 8. Legal & Compliance (TOS/Privacy live)
  [PASS] 9. System Health (/health 200 OK, DB 14ms)
  [PASS] 10. Rollback Provenance (LKG commit 190d7b5 locked)
OVERALL: READY FOR PRODUCTION CUTOVER
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[SECURITY STANDARD] [BLOCKER]` Live payment failure or missing webhook secret in production environment.
- `[AIQ RULE] [BLOCKER]` Missing rollback plan or undefined LKG commit SHA.
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Missing in-app account deletion route.
- `[HEURISTIC] [WARNING ONLY]` OpenGraph image dimensions slightly non-standard (e.g. 1080x608px).

## APPROVAL LEVEL
- **RED**: Final production cutover requires founder sign-off.

## VERIFICATION
- Test script: `bun test test/launch_smoke.test.ts` running synthetic pre-flight checks.

## DEPENDENCIES
- `commerce-payments` (for payment test).
- `universal-event-contract` (for telemetry check).

## SOURCE REFERENCES
- `SRC-STRP-SIG`: [Stripe Signatures](https://docs.stripe.com/webhooks/signatures)
- `SRC-W3C-CWV`: [web.dev Core Web Vitals](https://web.dev/articles/vitals)
- `SRC-OWASP-SECR`: [OWASP Secret Management](https://github.com/OWASP/ASVS)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Prior to every public version release.
