# AIQ Product Engineering System

Read the relevant `skills/*/SKILL.md`, `project-skills/*/SKILL.md` and playbook for the requested task. The target product repository's current rules and the user's instructions take precedence.

Audit before building. Identify canonical checkout, branch, status, diff, architecture, owner and data source. Classify existing pieces as ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD. Reuse and connect first.

Keep one authoritative source per fact. Separate AI inference from persisted truth, test output from deployment, and deployment from user-visible proof. Preserve user edits and use isolated worktrees for simultaneous writers.

Do not commit, push, deploy, publish, send customer messages, spend money or change external automation without explicit authority for that action. Report the exact proof and remaining gap.

For cross-repository sequencing, quality and proof gates, consult [AIQ Cross-Repo Agent Quality Gates](playbooks/AIQ_CROSS_REPO_AGENT_QUALITY_GATES.md) **after** the target repo's own instructions. Do not load every skill or override canonical V1 skill ownership.
