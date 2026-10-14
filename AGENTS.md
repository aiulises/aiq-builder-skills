# AIQ Product Engineering System

Read the relevant `skills/*/SKILL.md`, `project-skills/*/SKILL.md` and playbook for the requested task. The target product repository's current rules and the user's instructions take precedence.

Audit before building. Identify canonical checkout, branch, status, diff, architecture, owner and data source. Classify existing pieces as ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD. Reuse and connect first.

Keep one authoritative source per fact. Separate AI inference from persisted truth, test output from deployment, and deployment from user-visible proof. Preserve user edits and use isolated worktrees for simultaneous writers.

Do not commit, push, deploy, publish, send customer messages, spend money or change external automation without explicit authority for that action. Report the exact proof and remaining gap.

## Cross-product routing (read when a task spans repos or connectors)
Read `docs/AIQ_ECOSYSTEM_ROUTER.md` and `docs/AIQ_CROSS_REPO_GATES.md` before connecting products, models, APIs, automations or release evidence. They route to existing canonical documents; they do not replace the frozen canonical 15 skills or product-specific rules. Read only the relevant sections to conserve tokens. If the target product, permissions, live state or cross-domain data boundary is unclear, stop the risky action and report UNKNOWN.
