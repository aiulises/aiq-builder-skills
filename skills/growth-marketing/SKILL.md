---
name: growth-marketing
version: 1.0.0
owner: global-aiq
purpose: Acquisition funnels, 5-second landing page clarity, onboarding aha-moments, and retention loops.
---

# Growth & Marketing

## WHEN TO USE
- When designing landing page layouts, value propositions, hero sections, and CTA placement.
- When creating user signup flows, onboarding questionnaires, or re-engagement email triggers.

## WHEN NOT TO USE
- When executing raw database migrations or server clustering.

## REQUIRED INPUTS
- Target persona definition.
- Primary value proposition statement.
- Landing page copy and hero imagery.
- Funnel milestone definitions.

## PROCESS: THE 7-STAGE GROWTH ENGINE
1. **Acquisition:** Identify traffic origin (organic SEO, direct outreach, social proof).
2. **Landing Page Conversion:**
   - `[AIQ RULE]` Enforce the 5-Second Rule: A new visitor must comprehend the product, audience, and core benefit within 5 seconds.
   - Clean hero section with single primary high-contrast CTA (hitbox height ≥ 52px).
3. **Zero-Friction Signup:**
   - `[AIQ RULE]` Never ask for phone number, address, or credit card before proving initial value. Offer 1-click Google/Apple login or magic link.
4. **Onboarding & "Aha Moment":**
   - `[HEURISTIC]` Guide user to their first high-value result in ≤ 90 seconds (e.g. first instant formula or scan).
5. **Contextual Paywall:** Trigger paid upgrade modal at the exact moment of highest perceived value.
6. **Retention Loop:** Event-driven re-engagement (e.g. "Client toner touch-up due in 3 days").
7. **Referral Incentive:** In-app word-of-mouth loop ("Invite a salon colleague, get 1 month free").

## STRUCTURED OUTPUT
```text
GROWTH FUNNEL AUDIT:
  Landing Page Clarity: PASS (5-second test satisfied)
  Signup Friction: Minimal (1-click Google/Apple auth)
  Time-to-First-Value: 75 seconds (PASS)
  Paywall Timing: Contextual on formula unlock
  Referral Hook: Configured
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[AIQ RULE] [FAIL]` Landing page contains multiple competing primary CTAs with different goals.
- `[AIQ RULE] [FAIL]` Requiring a credit card before a user can see any sample analysis or basic value.
- `[HEURISTIC] [WARNING ONLY]` Time-to-first-value is 110s instead of 90s. **(Heuristics do not block release).**

## APPROVAL LEVEL
- **YELLOW**: Significant funnel or landing page copy rewrites require growth lead review.

## VERIFICATION
- Test script: `bun test test/growth_events.test.ts` verifying all funnel stage event emissions in DOM.

## DEPENDENCIES
- `universal-event-contract` (for funnel telemetry).
- `pricing-offer-arch` (for landing page pricing tables).

## SOURCE REFERENCES
- `SRC-POSTHOG-EVT`: [PostHog Event Tracking](https://posthog.com/docs/libraries/node)
- `SRC-W3C-CWV`: [web.dev Performance Impact](https://web.dev/articles/vitals)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Quarterly growth review.
