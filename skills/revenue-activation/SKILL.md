---
name: revenue-activation
version: 1.0.0
owner: global-aiq
purpose: Signature business gate enforcing the shortest path to the first paying customer and halting premature feature creep.
---

# Revenue Activation (The Business Gate)

## WHEN TO USE
- Before commencing work on any new feature milestone on an unmonetized product.
- When an agent or developer proposes adding complex secondary features while zero paying users exist.
- When preparing an MVP or pilot release for commercial launch.

## WHEN NOT TO USE
- When refactoring mature, established products with proven ARR.

## REQUIRED INPUTS
- Target buyer persona description.
- Core value proposition.
- Current payment integration status (Stripe / StoreKit live check).
- Estimated time-to-first-value (minutes).

## PROCESS: THE 10-STEP REVENUE PATHWAY
1. **Identify Target Buyer:** Clearly identify who specifically pulls out a credit card (e.g. Salon Owner vs Consumer).
2. **Isolate Core Value Driver:** Pinpoint the single transformation they pay for (e.g. "Save a color client disaster").
3. **Define Smallest Paid Offer:** Package minimum viable utility into a simple price point ($20/month or $49 one-off).
4. **Verify Payment Path:** `[SECURITY STANDARD]` Check if a working checkout button is operational. If missing → **HALT OTHER DEVELOPMENT**.
5. **Measure Time-to-First-Value:**
   - `[HEURISTIC]` Target time from signup to first core value is ≤ 90 seconds. If > 5 minutes → simplify onboarding immediately.
6. **Secure First 5 Paying Users:** Focus 100% of effort on direct outreach or waitlist conversion.
7. **Measure Repeat Usage:** Verify that users return within 7 days.
8. **Gather Conversion Feedback:** Identify friction points.
9. **Unblock Secondary Features:** Only AFTER payment and repeat use are proven may secondary features be developed.
10. **Activate Retention & Upsell:** Introduce annual plans and advanced tiers.

## STRUCTURED DIRECTIVES
```text
REVENUE ACTIVATION EVALUATION:
  Directives:
    ❌ HALT FEATURE 'COMMUNITY FORUM': Product has 0 paying users.
    ⚠️ PAYMENT GATEWAY MISSING: Connect Stripe checkout to core analysis first.
    ⚠️ FIRST-VALUE TOO SLOW (6 min): Reduce intake questionnaire to 3 questions.
    ✅ ACTION: Launch $20/month pilot offer to first 10 salons immediately.
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[AIQ RULE] [BLOCKER]` Developing secondary expansion features when zero paying users exist and the payment checkout path is broken or unbuilt.
- `[AIQ RULE] [FAIL]` Product requires manual administrator database intervention to grant access to a paid user.
- `[HEURISTIC] [WARNING ONLY]` Time-to-first-value is 120 seconds instead of 90 seconds. **(Does not block release; triggers simplification advisory).**

## APPROVAL LEVEL
- **RED**: Overriding a revenue activation halt requires founder sign-off.

## VERIFICATION
- Test script: `bun test test/revenue_flow.test.ts` verifying unauthenticated user can hit paywall and trigger checkout in < 3 clicks.

## DEPENDENCIES
- `pricing-offer-arch` (for offer structuring).
- `commerce-payments` (for payment execution).

## SOURCE REFERENCES
- AIQ Commercial Architecture Baseline (`P1_06_REVENUE_ACTIVATION_SPEC.md`).

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Product roadmap review milestones.
