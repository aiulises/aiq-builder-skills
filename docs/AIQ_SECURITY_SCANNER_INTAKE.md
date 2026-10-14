# AIQ Security Scanner Intake — NVIDIA SkillSpector and trusted tools
Status: PROPOSED, NOT INSTALLED | 2026-10-14

## Priority
1. NVIDIA SkillSpector for new third-party agent skills and MCP bundles: https://github.com/NVIDIA/SkillSpector
2. Aqua Security Trivy for project lockfiles, secrets, Docker images and IaC: https://github.com/aquasecurity/trivy
3. Google OSV-Scanner for vulnerable dependencies: https://github.com/google/osv-scanner
4. GitHub Dependabot/CodeQL/secret protection subject to repo plan and feature availability: https://docs.github.com/en/code-security
5. CrowdSec only after non-disruptive Hetzner ingress/firewall review; blocking can lock out the owner: https://github.com/crowdsecurity/crowdsec
6. NVIDIA garak for *controlled* AI red-team tests, not daily production probing: https://github.com/NVIDIA/garak

## MacBook operator setup (not executed)
Check Xcode/CLI tools, `git`, `uv`, and source authenticity first. Install SkillSpector isolated:
```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
skillspector scan /path/to/untrusted-skill --no-llm
```
Prefer pinning reviewed commit/tag and verifying release provenance for automation. The command above is a vendor-documented convenience example, not a pinned reproducible install.
Install Trivy only if absent, using official package/release, e.g. `brew install trivy`. Scan `trivy fs --scanners vuln,secret,misconfig /path/to/project` after reviewing output handling. Keep scan reports private: findings can reveal paths/secrets.

## Hetzner setup (not executed)
- First inventory existing security tools, operating system, SSH/VPN rules, Docker access, backup and rollback. Confirm which server is production and which is VPN; user reports Finland VPN and Germany backup but roles unverified.
- Run SkillSpector in unprivileged, isolated environment against a read-only copy of selected skills. Avoid host mounts, SSH secrets, root, Docker socket or broad filesystem access.
- Use Trivy in CI to scan images before deployment; no privileged daemon on production needed for first phase.
- Avoid enabling automatic IP bans/CrowdSec until network and emergency SSH access are tested.
- Do not expose SkillSpector MCP over unauthenticated network; prefer local stdio or localhost with authentication. MCP registration must be per-agent.
- Scan static-only by default: `--no-llm` prevents source file content being sent to model provider, but dependency coordinates may be sent to OSV.dev.

## Gate before accepting new skills
Source identity and repo owner verified -> pin version/commit -> inspect permissions and scripts -> static SkillSpector scan -> review findings -> sandbox smoke test -> explicit approval -> install with least privilege -> monitor and record SHA.
HIGH/CRITICAL = BLOCK pending review. LOW != safe by proof; scanner is not sandbox and can miss attacks. Maintain provenance, not blanket trust based on vendor brand.

## Cost and frequency
Scan before each new third-party skill/MCP installation and when its version changes. Re-scan changed first-party skills in CI if tooling is available. Run dependency scans on PRs and scheduled weekly when configured. Do not run expensive LLM security scans on every startup.

## Adoption
This is a guidance document only. No remote MacBook/Hetzner install, no agent MCP registration, no GitHub Actions security scan, no scheduled check and no production access has been performed.
