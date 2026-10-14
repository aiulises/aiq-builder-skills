#!/usr/bin/env python3
"""AIQ read-only context router. Stdlib only. Never reads secret files or fetches network."""
import argparse
import json
import pathlib
import sys

ROUTES = {
    "hairplan": {
        "markers": ("HairPlanPro",),
        "entry": ("CLAUDE.md", "docs/ARCHITECTURE_RULES.md", "docs/CONSTITUTION.md"),
        "skills": {"ui": "aiq-web-product-quality", "inventory": "aiq-universal-event-contract",
                   "auth": "aiq-universal-secret-scan"},
    },
    "lead-radar": {
        "markers": ("lead-radar",),
        "entry": ("AGENTS.md", "CLAUDE.md"),
        "skills": {"ui": "aiq-web-product-quality", "booking": "aiq-universal-event-contract",
                   "auth": "aiq-universal-secret-scan"},
    },
    "mrai": {
        "markers": ("MrAI-Private-Brain",),
        "entry": ("STATUS.md", "docs/CONTROL_LAYER.md", "docs/APPROVAL_MATRIX.md", "docs/BUSINESS_MODE.md"),
        "skills": {"backup": "restore-guard", "security": "aiq-universal-secret-scan",
                   "automation": "cost-guardian"},
    },
}
RISK = {"auth", "security", "backup", "infra", "payments", "database"}
ALIASES = {"hairplanpro": "hairplan", "mr.ai": "mrai", "mrai-private-brain": "mrai"}

def route(root, product, task):
    product = ALIASES.get(product.lower(), product.lower())
    if product not in ROUTES:
        raise ValueError("Unknown product; explicit product required")
    cfg = ROUTES[product]
    root = pathlib.Path(root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("Repository directory missing")
    if root.name.lower() not in tuple(x.lower() for x in cfg["markers"]):
        raise ValueError("Directory name does not match requested product")
    present = [p for p in cfg["entry"] if (root / p).is_file()]
    if product == "lead-radar":
        if not present:
            raise ValueError("Lead Radar agent entry missing on this branch")
    elif len(present) != len(cfg["entry"]):
        raise ValueError("Mandatory product entry file missing; stop before work")
    task = task.lower()
    matched = [key for key in cfg["skills"] if key in task]
    if len(matched) > 1:
        raise ValueError("Ambiguous task; select one primary skill")
    return {"status": "ROUTED_NOT_EXECUTED", "product": product,
            "root": str(root), "read_first": present,
            "suggested_skill": cfg["skills"][matched[0]] if matched else None,
            "risk_gate": "OWNER_GO_REQUIRED" if any(x in task for x in RISK) else "NORMAL_REVIEW",
            "next": "Read listed files, verify git state and product contracts; no automatic download or modification"}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", required=True, help="Existing local checkout path")
    p.add_argument("--product", required=True, choices=sorted(set(ROUTES) | set(ALIASES)))
    p.add_argument("--task", required=True, help="Task class, e.g. ui, inventory, booking, auth, backup")
    a = p.parse_args()
    try:
        print(json.dumps(route(a.repo, a.product, a.task), ensure_ascii=False, indent=2))
    except ValueError as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}), file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
