---
name: deployment-production
description: Prepare and verify controlled releases.
---

# Deployment Production

Before deploy, identify exact commit/tree, reviewed diff, target environment, lease or governance mechanism, migration impact and rollback target. Use the project's documented deploy wrapper. Afterward verify served release identity, API/worker health, migrations and a real browser path. Distinguish dev from production and deployed from user-visible.
