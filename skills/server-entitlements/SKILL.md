---
name: server-entitlements
version: 1.0.0
owner: global-aiq
purpose: Authoritative server-side feature access control, webhook idempotency, and subscription lifecycle management.
---

# Server-Side Entitlements

## WHEN TO USE
- When controlling user access to paid SaaS features, plan tiers (FREE, TRIAL, PREMIUM), quotas, or seat limits.
- When processing Stripe, Apple StoreKit, or Google Play subscription webhooks.
- When designing gates in frontend or backend code where user permissions are verified.

## WHEN NOT TO USE
- For basic user identity authentication (login/password/sessions — use `auth-security`).
- For styling paywall UI elements (use `pricing-offer-arch` or `premium-product-gate`).

## REQUIRED INPUTS
- `userId` / `tenantId`.
- `featureKey` (string identifier, e.g. `unlimited_scans`, `formula_history`).
- Provider webhook payload and signature headers (`Stripe-Signature`).
- Database client with `tenant_entitlements` and `processed_webhook_events` tables.

## PROCESS
1. **Decoupled 4-Tier Model:**
   - `[AIQ RULE]` Maintain strict boundary: `Payment Provider State → Server Entitlement State → Authorized Feature Access → Client UI`.
   - Never trust client-sent boolean flags or local storage claims for feature access.
2. **Webhook Verification & Idempotency:**
   - `[SECURITY STANDARD]` Cryptographically verify webhook signature using raw body buffer and 5-minute (300s) replay tolerance.
   - `[ENGINEERING BEST PRACTICE]` Deduplicate incoming events using provider `event.id` stored in unique constraint table before processing.
3. **Entitlement State Evaluation:**
   - Check `canAccessFeature(userId, featureKey)` against authoritative server database records.
   - Handle plan statuses: `active`, `trialing`, `past_due` (with grace period), `canceled`, `unpaid`.
4. **Outage Fallback:**
   - `[ENGINEERING BEST PRACTICE]` In case of third-party payment provider downtime, serve cached entitlements from database/Redis; do not lock out paying users.

## STRUCTURED OUTPUT
```typescript
interface EntitlementDecision {
  allowed: boolean;
  planTier: 'free' | 'trial' | 'premium';
  reason?: 'NO_ACTIVE_PLAN' | 'PAST_DUE_EXPIRED' | 'QUOTA_EXCEEDED' | 'FEATURE_NOT_IN_PLAN';
  gracePeriodActive: boolean;
  expiresAt?: string; // ISO-8601
}
```

## FAILURE CONDITIONS & BLOCKERS
- `[SECURITY STANDARD] [BLOCKER]` Unprotected server route returning paid data based on client-asserted headers or unverified session claims (OWASP A01).
- `[SECURITY STANDARD] [BLOCKER]` Processing webhooks without cryptographic signature verification or using parsed JSON instead of raw buffer.
- `[ENGINEERING BEST PRACTICE] [FAIL]` Webhook handler crashes on duplicate event delivery (missing idempotency).
- `[HEURISTIC] [WARNING]` Grace period duration set outside 3–14 day window (7 days recommended).

## APPROVAL LEVEL
- **YELLOW**: Lead developer review required for entitlement schema or webhook changes.

## VERIFICATION
- Test script: `bun test test/entitlements_guard.test.ts` verifying rejection of client spoofing and webhook replay attacks.

## DEPENDENCIES
- `universal-event-contract` (for billing telemetry).
- Database migration with `processed_webhook_events`.

## SOURCE REFERENCES
- `SRC-OWASP-A01`: [OWASP Top 10 Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
- `SRC-STRP-SIG`: [Stripe Webhook Signatures](https://docs.stripe.com/webhooks/signatures)
- `SRC-STRP-IDEM`: [Stripe Idempotent Requests](https://docs.stripe.com/api/idempotent_requests)
- `SRC-APPL-3.1.1`: [Apple App Store Review Guideline 3.1.1 (In-App Purchase)](https://developer.apple.com/app-store/review/guidelines/)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Stripe API version upgrades or modification of paid pricing tiers.
