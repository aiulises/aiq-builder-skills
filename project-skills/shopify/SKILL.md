---
name: shopify
description: Apply commerce source-of-truth and fulfillment rules to a verified Shopify project.
---

# Shopify

The product loop is product → cart → checkout → payment → fulfillment or access → analytics. Audit the actual store, theme, apps, product catalog, checkout configuration and order webhooks before recommending changes. Do not assume a store configuration from another project.

Keep price, tax, inventory, payment and order state in the authoritative commerce system. Reconcile webhook events idempotently, including retries and out-of-order arrival. Distinguish checkout started, payment authorized, paid, refunded and fulfilled. A receipt or client redirect alone does not prove access was delivered.

Test a sandbox or test-mode order through fulfillment and analytics before live commercial changes. Measure conversion from real events; do not invent sales, ROI or attribution. Any purchase, publication or customer message needs its own authority.
