---
name: brand-intelligence
version: 1.0.0
owner: global-aiq
purpose: Machine-readable taste engine, visual memory, and aesthetic critique system enforcing Nordic minimalism and automotive-grade tactile clarity.
---

# AIQ Brand Intelligence

## WHEN TO USE
- When designing new screens, UI components, landing pages, marketing collateral, or brand copy.
- When evaluating whether a proposed layout feels authentic to its product identity or has degraded into generic "AI slop".
- When parameterizing regional design adaptations (Nordic/EU vs US/NA).

## WHEN NOT TO USE
- For testing network API latency or database transaction consistency.

## REQUIRED INPUTS
- Target brand identifier (`hairplan` | `lead_radar` | `aiq_labs`).
- Proposed visual tokens, color choices, and layout mockup.
- Regional context (`nordic_eu` | `us_na`).

## PROCESS: THE 5-STAGE BRAND CRITIQUE LOOP
1. **UNDERSTAND:** Ingest product purpose, audience, device form factor, and brand archetype.
2. **APPLY:** Enforce the curated brand design tokens:
   - `hairplan`: Nordic warm minimalism (deep slate `#0D1117`, surface `#161B22`, organic green accent `#38A169`, soft off-white text `#F0F6FC`).
   - `lead_radar`: Automotive cockpit HUD (obsidian `#08090C`, cyan accent `#00E5FF`, high contrast, glanceable).
3. **COMPARE:** Compare against the core principles:
   - `[AIQ RULE]` Automotive/industrial design discipline: Very little noise, strong hierarchy, tactile material feeling, controlled motion, large clean surfaces, coherent brand identity from phone to large screen.
4. **CRITIQUE:** Actively search for and eliminate anti-patterns:
   - `[AIQ RULE]` Banned: Generic purple gradients, gratuitous glassmorphism, random sparkle icons (✨), dashboard chart overload, fake futuristic UI.
5. **OUTPUT:** Produce precise design tokens, component styling guidelines, and copy tone direction.

## STRUCTURED OUTPUT
```yaml
brand_decision:
  brand: hairplan
  feeling: calm, precise, tactile, human
  aesthetic_pass: true
  banned_patterns_detected: 0
  copy_tone: understated expert colorist peer
  tokens:
    surface_border: "rgba(255, 255, 255, 0.08)"
    accent: "#38A169"
```

## FAILURE CONDITIONS & HEURISTIC INVARIANTS
- `[AIQ RULE] [FAIL]` Using generic purple/violet gradients or overused AI sparkle icons.
- `[AIQ RULE] [FAIL]` Hardcoding un-tokenized ad-hoc colors outside the brand palette.
- `[HEURISTIC] [WARNING]` Copy tone reads slightly too energetic or American SaaS-like for a Nordic brand. **(Advisory warning; does not block release).**

## APPROVAL LEVEL
- **RED**: Altering core brand profiles or primary palette tokens requires founder approval.

## VERIFICATION
- Test script: `bun test test/brand_lint.test.ts` verifying zero banned CSS classes and 100% token usage.

## DEPENDENCIES
- None. Provides foundations for `premium-product-gate`.

## SOURCE REFERENCES
- AIQ Brand Architecture Baseline (`AIQ_BRAND_INTELLIGENCE_SPEC.md`).

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** Bi-annual brand review.
