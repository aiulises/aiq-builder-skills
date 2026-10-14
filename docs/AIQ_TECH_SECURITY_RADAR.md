# AIQ Tech & Security Radar
Status: PROPOSED / low-cost discovery agent | 2026-10-14

## Mission
Watch relevant **primary sources** for changes in agent security, dependency vulnerabilities, model releases, coding tools, frontend/backend UX, AI products, and policies. Triage for HairPlan.PRO, Lead Radar, Shopify/HairPlan.eu and Mr.AI separately. Never auto-install, publish, deploy, or execute third-party code.

## Two distinct operations
1. **Download Guard** (event-driven, not daily): inspect provenance, pinned SHA, permissions, scripts, licensing, malware/prompt injection, known vulnerabilities. NVIDIA SkillSpector for skills, Trivy/OSV for dependencies and containers. Review findings before installing.
2. **Innovation Radar** (weekly cheap metadata pass): collect release/update metadata from verified GitHub upstream repositories and Hugging Face Hub; categorize SECURITY / BACKEND / FRONTEND-UX / CREATIVE / MODEL / POLICY; filter for product relevance and produce human-readable recommendations.

## Source tiers
- Official: GitHub releases/security advisories of NVIDIA, Google, Microsoft, Apple, OpenAI, Hugging Face, OWASP, Playwright, Docker, Supabase, Shopify; vendor developer changelogs.
- Hugging Face: model/space/dataset metadata and cards are discovery signals, not proof of safety or quality. Review model license, gated terms, provenance, model card, files, code execution/trust_remote_code and benchmark reproducibility before any use.
- X: official verified accounts and employee posts are **signals**, not authoritative release documentation. Use only an authorized API or public official source; never bypass rate limits, login or anti-bot protections. Cross-check against vendor docs/GitHub.
- CVE: vendor security advisories, OSV, NVD/CISA KEV for impact verification; do not conflate a generic vulnerability with a confirmed impact on our exact versions.

## Minimal reporting contract
- date, upstream, URL, published_at, category, product impact, evidence strength, recommended NOW/NEXT/LATER/IGNORE, severity, verified installed version, expected cost, owner, decision.
- No unverified zero-days, fabricated urgency, or claims that every new model is an upgrade.
- No user/customer data or secrets in external searches.

## Runtime/cost
- Start with stdlib Python collector at scripts/aiq_tech_radar.py and GitHub Actions artifact-only weekly/manual workflow; no API keys or paid LLMs. If API limits/permissions fail, report UNKNOWN rather than fabricate coverage.
- Agent interpretation can be on-demand after report, not automatic on every feed entry. Add more sources only when proven useful.
- GitHub Action runs only after PR merge and Actions permission is enabled. No push-to-production or write access.
- Alert on critical *confirmed relevance* only after dependency inventory/version match, not on headlines.

## Device strategy
MacBook: approved terminal CLI for scans, browser dashboard for reports. Android Samsung S23 Ultra: GitHub app/browser notifications and report reading; no privileged phone scanner or device-wide interception. Hetzner: read-only CI artifacts and isolated scanners; no root agent.
