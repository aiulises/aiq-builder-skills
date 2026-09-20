---
name: product-architecture
description: Audit an existing product before designing or building a feature.
---

# Product Architecture

1. Inventory the canonical checkout, owners, current components, consumers, contracts, data sources, costs, and deployment path. Classify each as ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD.
2. Do not create a second source of truth. Connect before rebuilding. Prefer deterministic logic for authoritative decisions; AI inference is not database truth.
3. Do not put fabricated demo data in production. Measure real behavior before expanding the surface. Treat mobile as a first-class product surface.
4. Map the proposed change to the product's core loop and identify the smallest useful slice. Passing tests does not authorize deploy.
