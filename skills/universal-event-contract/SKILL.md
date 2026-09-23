---
name: universal-event-contract
version: 1.0.0
owner: global-aiq
purpose: Type-safe, PII-sanitized cross-product telemetry for PostHog and Sentry feeding insights.aiq-labs.com.
---

# Universal Event Contract

## WHEN TO USE
- When adding or modifying tracking, analytics, telemetry, or user event triggers in any AIQ application (`HairPlan.PRO`, `HairPlan Me`, `Lead Radar`).
- When sending business metrics (signups, activations, scans, checkout events) or system metrics (5xx errors, latencies, token consumption).

## WHEN NOT TO USE
- For internal database row updates or transaction logs within a single microservice.
- For raw, unstructured debugging logs (e.g. `console.log`).

## REQUIRED INPUTS
- `event_name` (snake_case, e.g. `photo_analysis_completed`, `subscription_created`).
- `category` (`product_analytics` vs `observability`).
- `product` (`hairplan_pro` | `hairplan_me` | `lead_radar` | `private_brain`).
- `environment` (`production` | `staging` | `development`).
- `user_id_hash` (one-way cryptographic hash of user ID; never raw email).
- `consent_analytics` (boolean flag).
- `properties` (structured JSON payload).

## PROCESS
1. Check `consent_analytics`: If `false` and category is `product_analytics`, drop or anonymize event.
2. Ensure strict categorization:
   - `[AIQ RULE]` Keep `product_analytics` (funnels, MRR, retention) strictly separate from `observability` (5xx errors, latencies, tokens).
3. Validate payload schema against `AiqEventEnvelope`:
   - `event_id`: UUIDv4.
   - `timestamp`: ISO-8601 UTC.
   - `pii_classification`: MUST BE `'none'`.
4. Run automated PII pre-filter:
   - `[SECURITY STANDARD]` Scan properties for emails, passwords, credit card numbers, or raw biometric photos. If detected, redact immediately before dispatch.
5. Transmit to designated engine:
   - `product_analytics` → PostHog API via batch client.
   - `observability` → Sentry Envelope API.

## STRUCTURED OUTPUT
```json
{
  "event_id": "c7a8b9d0-1234-5678-90ab-cdef12345678",
  "event_name": "scan_completed",
  "event_version": 1,
  "category": "product_analytics",
  "product": "hairplan_me",
  "environment": "production",
  "timestamp": "2026-09-23T14:30:00.000Z",
  "origin": "client",
  "user_id_hash": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
  "session_id": "sess_987654321",
  "consent_analytics": true,
  "pii_classification": "none",
  "properties": {
    "scan_type": "hair_level",
    "latency_ms": 320,
    "confidence_score": 0.94
  }
}
```

## FAILURE CONDITIONS & BLOCKERS
- `[SECURITY STANDARD] [BLOCKER]` Any plaintext PII (unhashed email, raw phone, token) in event properties.
- `[OFFICIAL REQUIREMENT] [BLOCKER]` Transmitting tracking events to third-party endpoints without verified user consent (GDPR / Apple Guideline 5.1.2(i)).
- `[ENGINEERING BEST PRACTICE] [FAIL]` Missing `event_version` or invalid ISO-8601 timestamp.
- `[HEURISTIC] [WARNING]` Event payload size exceeding 10KB (advisory warning to keep telemetry lightweight).

## APPROVAL LEVEL
- **GREEN**: Automated CI validation passes.

## VERIFICATION
- Test script: `bun test test/event_contract.test.ts` asserting 100% schema conformance.

## DEPENDENCIES
- Zod / TypeScript schema definitions.

## SOURCE REFERENCES
- `SRC-POSTHOG-EVT`: [PostHog Event Specification](https://posthog.com/docs/libraries/node)
- `SRC-SENTRY-EVT`: [Sentry Envelope Spec](https://develop.sentry.dev/sdk/envelopes/)
- `SRC-GDPR-17`: [EUR-Lex GDPR Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

## LAST VALIDATED & REVALIDATION TRIGGER
- **Last Validated:** 2026-09-23
- **Revalidation Trigger:** 90-day cycle or PostHog/Sentry SDK major version upgrade.
