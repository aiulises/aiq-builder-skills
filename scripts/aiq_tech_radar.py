#!/usr/bin/env python3
"""Low-cost metadata-only AIQ radar. Python stdlib, no tokens, no secrets.
Usage: python3 scripts/aiq_tech_radar.py --output /tmp/aiq-radar.md
"""
import argparse
import datetime as dt
import json
import os
import urllib.error
import urllib.parse
import urllib.request

SOURCES = {
    "NVIDIA SkillSpector": "NVIDIA/SkillSpector",
    "NVIDIA garak": "NVIDIA/garak",
    "Trivy": "aquasecurity/trivy",
    "OSV Scanner": "google/osv-scanner",
    "Playwright": "microsoft/playwright",
    "Supabase": "supabase/supabase",
    "Hugging Face Transformers": "huggingface/transformers",
    "Hugging Face Hub": "huggingface/huggingface_hub",
    "Docker": "docker/cli",
    "OWASP ASVS": "OWASP/ASVS",
}
UA = "AIQ-Technology-Radar/0.1 (metadata-only)"
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json" if "api.github.com" in url else "application/json"})
    with urllib.request.urlopen(req, timeout=12) as response:
        return json.load(response)
def clean(x):
    return str(x or "").replace("|", "\\|").replace("\n", " ")[:220]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="aiq-radar-report.md")
    args = parser.parse_args()
    today = dt.datetime.now(dt.timezone.utc)
    lines = ["# AIQ Technology & Security Radar", "", "Generated UTC: " + today.isoformat(), "", "Discovery only. Metadata is NOT an installed-version or vulnerability-impact audit.", "", "## Official GitHub upstream releases", "", "| Source | Latest published release | Link | Status |", "|---|---|---|---|"]
    failures = 0
    for label, slug in SOURCES.items():
        try:
            x = get("https://api.github.com/repos/" + slug + "/releases/latest")
            lines.append("| " + clean(label) + " | " + clean(x.get("published_at")) + " — " + clean(x.get("tag_name")) + " | " + clean(x.get("html_url")) + " | DISCOVERED |")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, OSError) as e:
            failures += 1
            lines.append("| " + clean(label) + " | — | https://github.com/" + slug + " | UNKNOWN (" + type(e).__name__ + ") |")
    lines += ["", "## Hugging Face recently updated models (untrusted metadata)", "", "| Model | Updated | Link | Status |", "|---|---|---|---|"]
    try:
        params = urllib.parse.urlencode({"sort": "lastModified", "direction": "-1", "limit": "8"})
        data = get("https://huggingface.co/api/models?" + params)
        for x in data:
            mid = x.get("id", "")
            if not mid or "/" not in mid:
                continue
            lines.append("| " + clean(mid) + " | " + clean(x.get("lastModified")) + " | https://huggingface.co/" + urllib.parse.quote(mid, safe="/") + " | UNREVIEWED |")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, OSError) as e:
        failures += 1
        lines.append("Hugging Face: UNKNOWN (" + type(e).__name__ + ")")
    lines += ["", "## Human/agent review", "", "Classify each candidate by SECURITY / BACKEND / FRONTEND-UX / CREATIVE / MODEL / POLICY, then NOW / NEXT / LATER / IGNORE. Check affected package versions, licensing, source and cost before any action.", "", "## Coverage limits", "", "- Does not read X posts, CVEs, private repositories, installed package versions or app telemetry.", "- No installation, scanning of local files, deploy, model execution, or automatic notifications.", "- Network and GitHub rate limits may make results UNKNOWN.", "- Metadata and release dates alone cannot prove a change is new since last run.", "", f"Failed source lookups: {failures}."]
    output = args.output
    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("Report written:", output, "failures:", failures)
if __name__ == "__main__":
    main()
