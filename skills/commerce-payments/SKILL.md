---
name: commerce-payments
version: 1.0.0
owner: global-aiq
purpose: Stripe subscription engine, checkout session generation, webhook idempotency, proration, and dunning recovery.
---

# Commerce & Payments

## WHEN TO USE
- When creating Stripe checkout sessions, customer portals, or subscription webhook handlers.
- When managing upgrade/downgrade proration, cancellation surveys, or failed payment recovery.

## WHEN NOT TO USE
- When managing physical e-commerce store inventory (use `shopify-commerce`).

## REQUIRED INPUTS
- `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` (server environment only).
- Stripe Price IDs.
- Customer identifier.

## PROCESS
1. **Checkout Session Creation:**
   - Call `stripe.checkout.sessions.create` with `mode: 'subscription'`.
   - Provide explicit `success_url` and `cancel_url`.
2. **Webhook Cryptographic Processing:**
   - `[SECURITY STANDARD]` Verify `Stripe-Signature` using raw body buffer and 5-minute replay tolerance.
   - `[ENGINEERING BEST PRACTICE]` Deduplicate incoming `evt_...` identifiers using unique database constraint.
3. **Lifecycle Handling:**
   - `checkout.session.completed` → link Stripe customer ID to user record.
   - `invoice.payment_succeeded` → confirm active entitlement.
   - `invoice.payment_failed` → transition tenant to `past_due` with 7-day grace period; trigger dunning email.
   - `customer.subscription.updated` → handle proration and tier shifts.
   - `customer.subscription.deleted` → downgrade to FREE tier at period end.

## STRUCTURED OUTPUT
```json
{
  "checkout_url": "https://checkout.stripe.com/c/pay/cs_live_...",
  "session_id": "cs_live_1234567890",
  "status": "ready"
}
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[SECURITY STANDARD] [BLOCKER]` Exposing `STRIPE_SECRET_KEY` in client-side code or public repositories.
- `[SECURITY STANDARD] [BLOCKER]` Processing webhooks without signature verification or relying on parsed JSON.
- `[ENGINEERING BEST PRACTICE] [FAIL]` Webhook handler crashes on duplicate event delivery.
- `[HEURISTIC] [WARNING ONLY]` Failed payment retry schedule exceeds 4 attempts over 3 weeks.

## APPROVAL LEVEL
- **RED**: Modifying live Stripe webhook endpoints or payout settings requires founder approval.

## VERIFICATION
- Test script: `bun test test/stripe_webhook.test.ts` testing signature verification and duplicate event rejection.

## DEPENDENCIES
- `server-entitlements` (for authoritative feature unlocking).
- `pricing-offer-arch` (for validated price configurations).

## SOURCE REFERENCES
- `SRC-STRP-SIG`: [Stripe Webhook Signatures](https://docs.stripe.com/webhooks/signatures)
- `SRC-STRP-IDEM`: [Stripe Idempotency](https://docs.stripe.com/api/idempotent_requests)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Stripe API version upgrade.
