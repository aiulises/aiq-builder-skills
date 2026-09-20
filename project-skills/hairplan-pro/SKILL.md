---
name: hairplan-pro
description: Apply HairPlan Pro's salon consultation, knowledge-layer and release-proof rules.
---

# HairPlan Pro

The product loop is consultation → observation → professional reasoning → recommendation → salon confirmation → follow-up. Preserve the stylist's professional authority and a calm, credible customer experience.

Read the target checkout's `CLAUDE.md` and `docs/ARCHITECTURE_RULES.md` before changing behavior. Reconcile the canonical checkout, branch, current diff and active release; old SHAs or paths are not live proof.

Keep three knowledge layers distinct: global brand-neutral professional knowledge, manufacturer-approved knowledge scoped to market and product line, and salon-private recipes, procedures and client data. A response must identify its source layer. Preserve tenant isolation across retrieval, embeddings, exports and analytics. The model may recommend, but authoritative safety, document approval, inventory and stylist-confirmation changes require typed tools, validation, permission and audit.

For a release, verify source SHA, governed deploy path, served bundle, API and worker, migrations, health, rollback target and the actual browser journey. Development proof is not production or authenticated microphone proof. Label any remaining device or user-path gap.
