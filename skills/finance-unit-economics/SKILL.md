---
name: finance-unit-economics
version: 1.0.0
owner: global-aiq
purpose: SaaS unit economics monitoring, gross margin governance, and per-subscriber AI model token cost caps.
---

# Finance & Unit Economics

## WHEN TO USE
- When modeling SaaS profitability, setting subscription pricing, or auditing infrastructure token expenditure.
- When reviewing financial telemetry inside the Executive Dashboard at `insights.aiq-labs.com`.

## WHEN NOT TO USE
- When resolving local CSS layout bugs or writing client components.

## REQUIRED INPUTS
- Active subscriber count.
- Monthly Recurring Revenue (MRR) from Stripe.
- Hosting & infrastructure fees (Hetzner / Cloudflare).
- Total LLM model token expenditure (Anthropic, OpenAI, Gemini).

## PROCESS
1. **Calculate Core Financial Metrics (`SRC-BESS-SAAS`):**
   - $MRR = \sum (\text{Active Subscribers} \times \text{Plan Rate})$
   - $ARR = MRR \times 12$
   - $ARPU = \frac{MRR}{\text{Active Subscribers}}$
   - $\text{Gross Margin \%} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} \times 100$
2. **Enforce AI Token Cost Cap:**
   - `[AIQ RULE]` AI model API spend must not exceed **15% of subscriber fee** (e.g. max $3.00/month for a $20/month subscriber).
   - If user crosses 80% of token budget, route simple tasks to cheap local/cloud models.
3. **Monitor Target Heuristics:**
   - `[HEURISTIC]` Target Gross Margin ≥ 75%.
   - `[HEURISTIC]` Target LTV:CAC ratio ≥ 3:1.
   - `[HEURISTIC]` Target Monthly Subscriber Churn < 4.0%.

## STRUCTURED OUTPUT
```text
FINANCIAL HEALTH SCORECARD:
  Current MRR: $4,200.00
  Active Subscribers: 210 (ARPU: $20.00)
  Gross Margin: 78.4% (PASS)
  Avg AI Token Cost / User: $1.92 / mo (9.6% of ARPU - PASS)
  Monthly Churn: 3.2% (HEURISTIC PASS)
  LTV:CAC Ratio: 3.8:1 (HEURISTIC PASS)
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[AIQ RULE] [BLOCKER]` Negative unit economics (AI model tokens + hosting costs exceed subscription revenue).
- `[AIQ RULE] [FAIL]` Individual user token consumption exceeds 20% of subscription fee without fair-use throttling.
- `[HEURISTIC] [WARNING ONLY]` Gross margin is 68% instead of 75%; LTV:CAC is 2.2:1 during initial launch. **(Heuristics never block a release).**

## APPROVAL LEVEL
- **RED**: Pricing adjustments or budget cap alterations require founder sign-off.

## VERIFICATION
- Test script: `bun test test/unit_economics.test.ts` calculating margins against simulated subscriber cohorts.

## DEPENDENCIES
- `universal-event-contract` (for billing and token telemetry).
- `pricing-offer-arch` (for plan tier prices).

## SOURCE REFERENCES
- `SRC-BESS-SAAS`: [Bessemer Venture Partners SaaS Framework](https://www.bvp.com/atlas/scaling-to-100m)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Monthly financial close.
