# NVIDIA SkillSpector + OpenShell: AIQ Security Adoption Runbook

Status: documentation and safe rollout plan, **not installed on Hetzner** and not verified on Grokbot. Product owner approval required for installation, live changes, new paid API calls, privileged access or network changes.

## Clarify the tools
- NVIDIA **SkillSpector**: static/optional LLM inspection of third-party agent skills before installation; can scan Git repos, URLs, ZIPs, directories and files. Detection is not a guarantee of safety.
  - https://github.com/NVIDIA/SkillSpector
  - https://docs.nvidia.com/skills/scanning-agent-skills
- NVIDIA **OpenShell**: runtime agent sandbox with filesystem/network/process/provider controls. It is not the same thing as pre-install scanning. Do not install on a live host until a separate Docker isolation/security assessment and resource review.
  - https://github.com/NVIDIA/OpenShell
  - https://docs.nvidia.com/openshell/home
- NVIDIA security-workflows: reusable GitHub scanning workflows and pinned pre-commit hooks; evaluate supply chain and compatibility before adopting, do not blindly add third-party workflow permissions.
  - https://github.com/NVIDIA/security-workflows

## First: read-only Hetzner discovery
Only via approved SSH from an environment with existing access, never paste keys/tokens in chat or logs.
1. Record host OS, Docker/Podman version, architecture, free disk/memory, services/ports, firewall, active agent processes, existing sandbox and scanner versions. Record commands and sanitized output.
2. Identify whether SkillSpector/OpenShell is already installed and by whom; inspect `command -v skillspector`, `command -v openshell`, package/venv locations, running containers, service files and logs. Do not assume absence.
3. Locate approved isolated staging directory/VM/container **outside HairPlan/Lead Radar/Mr.AI production volumes and networks**. Verify backup and recovery, host capacity and service ownership.
4. Record local/GitHub/Hetzner truth with SHA and change approvals; do not run external installers or clone arbitrary repos as a discovery step.

## Controlled staging installation (owner GO first)
1. Verify official upstream, license, release tag/commit, dependencies, lockfile and integrity/provenance; pin exact version and review install scripts before execution. Avoid `curl | sh` on production.
2. Prefer unprivileged dedicated user and disposable isolated venv/container, read-only mounts, no host Docker socket, no production secrets, no production network access, restricted egress, CPU/memory/time limits.
3. Scan a benign test skill and a deliberately suspicious fixture; record version, exit codes, findings and false positives. Do not allow a skill based on scanner PASS alone; human review and permissions still required.
4. Add CI as a separate, reviewed PR using pinned dependencies, read-only permissions, no privileged PR execution and artifact retention without secrets. Reject or quarantine untrusted skills; never automatically install.
5. If OpenShell is justified, separate security review: kernel support, Docker privileges, networking, provider credential injection, policy enforcement, audit/telemetry and rollback. Pilot on a non-production host or isolated staging, not shared HairPlan production.
6. Document incident rollback, scan coverage, cost, maintenance owner and update policy.

## Cross-agent live collaboration
- GitHub issue/task packet = single work unit; one owner per branch/worktree; no concurrent edits to same files.
- Claude Code implementation, Codex independent review/tests, Grokbot specialist scan/review, Mr.AI owner control and budget approval; agents exchange sanitized PR links, SHAs, test evidence, not raw credentials or customer data.
- Use least-privilege GitHub tokens/SSH keys and scoped MCP tool allowlists; protect main with checks and human merge gate.
- Evidence stages: PLANNED → BUILT → TESTED → DEPLOYED → PROVEN. No autonomous deployment or repairs beyond approved bounded Tier 1 actions.

## GDPR/EU privacy gate
- Identify controller/processor roles, data inventory, lawful basis, data processing agreements and international transfer assessment before sharing customer data with third-party model/scanner/cloud.
- Skills may contain prompts or secrets; scan locally with sanitized fixtures. Do not upload real customer notes, photos, voice, private repositories or access tokens to external scanning/LLM services without an approved privacy/security review.
- No production PII in Sentry/PostHog by default; pseudonymous correlation IDs and per-tenant RBAC. Log security scans minimally, with retention and access restrictions.
- Incident workflow includes suspected secret exposure, immediate containment and applicable breach notification assessment.

## Definition of done
- Read-only inventory and actual evidence.
- Approved isolated staging scan with verified version and safe sample findings.
- CI scanning gates proven in a test PR.
- Security and GDPR review completed.
- Explicit separate owner GO for production rollout.
- Hetzner actual running service, policy, health, trace, rollback and resource measurements verified before reporting installed/proven.
