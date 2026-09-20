# AIQ Product Engineering System

A portable set of product engineering skills for Codex and Claude Code. Ulises Garcia — AI Product & Systems Architect.

Use `AGENTS.md` as the shared entry point, then choose a playbook, general skills, and a product-specific skill only if it matches the actual project. This repository stores guidance, not project source code or secrets.

Example task: “Read AGENTS.md and the relevant AIQ Builder Skills. Audit this repository first. Classify ALREADY EXISTS / PARTIAL / MISSING / LEGACY / DO NOT REBUILD. Propose the smallest implementation and its verification. Do not deploy without explicit approval.”

`skills/` holds reusable decisions. `project-skills/` holds product context. `playbooks/` gives task sequences. Current product repositories remain authoritative for their implementation and deployment rules.

The Claude Code ↔ ChatGPT handoff is currently a documented workflow in `CLAUDE.md`; this repository does not yet contain a working chat bridge.
