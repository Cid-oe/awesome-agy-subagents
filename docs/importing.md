# Importing & Maintenance

This document describes how the AGY ecosystem repository discovers, imports,
converts, deduplicates and validates subagents, and how to keep it up to date.

## Pipeline overview

```
discover ──► import ──► convert ──► dedupe ──► validate ──► report ──► export
   │            │           │           │           │           │          │
   │            │           │           │           │           │          └─ tools/, exports/
   │            │           │           │           │           └─ reports/*.md
   │            │           │           │           └─ metadata/validation_report.json
   │            │           │           └─ agents/ (canonical), metadata/agents.json
   │            │           └─ agents/ + metadata/agents.json (pre-dedupe)
   │            └─ imports/sources/<repo>/
   └─ metadata/discovered_repos.json
```

Run everything with `python3 scripts/run_all.py` (or stage-by-stage flags).

## Stage details

### 1. discover — `scripts/discover.py`

Queries the GitHub search API with agent-specific terms (subagents, claude
code, codex, gemini, path filters, topics) and a curated `KNOWN_REPOS` list,
then writes `metadata/discovered_repos.json` (full name, stars, license,
description, topics, clone URL).

### 2. import — `scripts/import.py`

Shallow-clones repositories whose metadata matches agent/skill keywords into
`imports/sources/<owner>--<repo>/`. This directory is **git-ignored**; the
importer re-clones on demand, so reruns are cheap and the repository stays
small.

### 3. convert — `scripts/convert.py`

Scans each cloned repo for agent definitions:

- **Formats** — Markdown frontmatter, Codex TOML, YAML, and JSON.
- **Locations** — `agents/`, `.claude/agents/`, `.gemini/agents/`,
  `.codex/agents/`, `.cursor/agents/`, `.agents/`, `.pi/agents/`,
  `plugins/*/agents/`, `subagents/`, and root-level persona files with
  agent-signal frontmatter.
- **Skips** — skills, commands, docs, tests, examples, templates, and memory
  files (these are not subagents).

For each agent it extracts `name`, `description`, model, tools, MCP servers,
and the system-prompt body, then maps foreign tool names onto canonical AGY
tools and computes a compatibility status.

### 4. dedupe — `scripts/dedupe.py`

- Merges **exact-duplicate** bodies (same prompt from different repos).
- Merges **same-name, same-category** agents (e.g. one agent ported across
  Claude Code / Codex / Gemini CLI), keeping the richest prompt and folding in
  every source for attribution.
- Merges **near-identical** agents (Jaccard ≥ 0.97, same category).
- Disambiguates any remaining name collisions.

No identical prompts are kept; every original source is preserved in
`agy.sources`.

### 5. validate — `scripts/validate.py`

Checks each agent against `docs/AGY-SPEC.md`: name/description/prompt
presence, name-slug legality, category membership. Failures are listed in
`reports/validation.md`.

### 6. report — `scripts/report.py`

Regenerates `metadata/summary.json` and the human-readable reports:
summary, categories, compatibility, tool usage, MCP dependencies, and
repository import report.

### 7. export — `scripts/export.py`

Writes the `tools/` catalog (core AGY tools + MCP integrations) and the
`exports/agents.json` / `exports/agents.csv` registries.

## Scheduled re-runs

The pipeline is idempotent and re-runnable. A CI job (e.g. a weekly GitHub
Action) can run `python3 scripts/run_all.py`, then open a pull request with any
new `agents/`, `metadata/`, `reports/`, and `tools/` changes. A ready-to-use
workflow is provided at `templates/import-workflow.yml` — copy it to
`.github/workflows/import.yml`. It:

1. Installs `pyyaml` and the `gh` CLI.
2. Runs `python3 scripts/run_all.py`.
3. Commits changes and opens a PR via `gh pr create`.

## Troubleshooting

- **`yaml` import error** — `pip install pyyaml`.
- **GitHub rate limits** — `discover.py` sleeps between queries; a PAT
  (already available via `gh`) raises the search limit.
- **Unsupported sources** — repositories that store agents as Python classes
  or TypeScript code (rather than frontmatter files) are recorded as
  `requires-manual-conversion` or left unimported; see
  `reports/compatibility.md`.
