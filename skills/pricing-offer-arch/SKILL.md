---
name: pricing-offer-arch
version: 1.0.0
owner: global-aiq
purpose: Transparent SaaS and e-commerce pricing models, dynamic mathematical savings calculation, and EU Omnibus compliance.
---

# Pricing & Offer Architecture

## WHEN TO USE
- When creating or modifying pricing tables, checkout comparison toggles, annual discount badges, or bundle offers.
- When configuring plan tiers and promotional discounts in UI or database schemas.

## WHEN NOT TO USE
- When executing the live credit card transaction (use `commerce-payments`).

## REQUIRED INPUTS
- Monthly base rate ($).
- Proposed annual billing total ($).
- Plan feature list.

## PROCESS
1. **Compute Legitimate Mathematical Savings:**
   - `annualizedMonthly = monthlyRate * 12`
   - `savingsAmount = annualizedMonthly - annualTotal`
   - `savingsPercentage = Math.round((savingsAmount / annualizedMonthly) * 100)`
   - `effectiveMonthly = Math.round((annualTotal / 12) * 100) / 100`
2. **Enforce Truth in Advertising:**
   - `[OFFICIAL REQUIREMENT]` EU Omnibus Directive (Directive (EU) 2019/2161 Art. 6a) & FTC 16 CFR Part 233: Advertised savings must reflect genuine mathematical comparisons. Never hardcode fake discount percentages (e.g. claiming "Save 40%" when real math is 30%).
3. **Transparent Auto-Renewal:**
   - Clearly state renewal terms: *"Billed annually at $168/year ($14/month). Cancel anytime in 1 click."*

## STRUCTURED OUTPUT
```json
{
  "monthlyRate": 20.00,
  "annualTotal": 168.00,
  "annualizedMonthly": 240.00,
  "savingsAmount": 72.00,
  "savingsPercentage": 30,
  "effectiveMonthly": 14.00,
  "uiBadge": "Save $72 / year (30%)"
}
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Hardcoding promotional discount percentages that do not match verified mathematical calculation (EU Omnibus violation).
- `[AIQ RULE] [FAIL]` Claiming savings on an annual plan when annual cost is greater than or equal to 12x monthly cost.
- `[HEURISTIC] [WARNING ONLY]` Annual discount incentive is under 15% (weak incentive to convert to annual billing).

## APPROVAL LEVEL
- **RED**: Base price changes require founder sign-off.

## VERIFICATION
- Test script: `bun test test/pricing_math.test.ts` asserting exact percentage rounding across all tier configurations.

## DEPENDENCIES
- Feeds into `commerce-payments` and `growth-marketing`.

## SOURCE REFERENCES
- `SRC-FTC-PRICE`: [EU Omnibus Directive 2019/2161 Art. 6a & FTC 16 CFR Part 233](https://eur-lex.europa.eu/eli/reg/2019/2161/oj)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Bi-annual commercial pricing review.
