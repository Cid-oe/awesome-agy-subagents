# Importing & Maintenance

This document describes how the AGY ecosystem repository discovers, imports,
converts, deduplicates and validates subagents, and how to keep it up to date.

## Pipeline overview

```
discover ──► process ──► convert ──► finalize ──► classify ──► validate ──► report ──► export
   │            │            │           │             │            │           │          │
   │            │            │           │             │            │           │          └─ tools/, exports/
   │            │            │           │             │            │           └─ reports/*.md
   │            │            │           │             │            └─ metadata/validation_report.json
   │            │            │           │             └─ repo_status.json, reports/coverage.md, unsupported.md
   │            │            │           └─ agents/ (canonical), metadata/agents.json
   │            │            └─ metadata/raw_records.json (pre-dedupe)
   │            └─ clone → scan → classify → extract → delete (streamed)
   └─ metadata/discovered_repos.json
```

Run everything with `.venv/bin/python scripts/run_all.py` (or stage-by-stage
flags). Use a virtualenv because PyYAML is required (`python3 -m venv .venv &&
.venv/bin/pip install PyYAML`).

## Stage details

### 1. discover — `scripts/discover.py`

Queries the GitHub search API with a broad set of agent-specific terms —
keyword (`subagents`, `claude code subagents`, ...), `filename:` (`AGENT.md`,
`agent.md`, `*.agent.md`, `CLAUDE.md`, `SYSTEM.md`, `instructions.md`,
`subagent.md`), `path:` (`.claude/agents`, `.codex/agents`, `.gemini/agents`,
`.cursor/agents`, `.opencode/agents`, `agents`, `subagents`) and `topic:`
(`claude-code`, `subagents`, `gemini-cli`, `codex`, `cursor`, `opencode`,
`aider`, `ai-agent`, `coding-agent`, ...) — plus a curated `KNOWN_REPOS` list,
then writes `metadata/discovered_repos.json`.

### 2. process — `scripts/process_all.py`

For **every** discovered repository, in a resumable, disk-bounded stream:

1. Shallow-clones it into `imports/sources/<owner>--<repo>/` (git-ignored).
2. Recursively scans for candidate agent definitions across Markdown frontmatter,
   Codex TOML, YAML, and JSON, in `agents/`, `.claude/agents/`, `.gemini/agents/`,
   `.codex/agents/`, `.cursor/agents/`, `.agents/`, `.pi/agents/`,
   `plugins/*/agents/`, `subagents/`, and root-level persona files.
3. Extracts reusable agents (skipping skills, commands, docs, tests, examples,
   templates, memory files) and appends them to `metadata/raw_records.json`.
4. Classifies the repo, records it in `metadata/repo_scan.json`, and **deletes
   the clone** to bound disk usage.

### 3. convert — `scripts/convert.py`

Scans any source clones still present in `imports/sources/` into
`metadata/raw_records.json`. In the normal streamed flow this is a no-op
(records were already accumulated by `process_all.py`).

### 4. finalize — `scripts/finalize.py`

Deduplicates the raw records and writes the canonical AGY agent set:

- Merges **exact-duplicate** bodies (same prompt from different repos).
- Merges **same-name, same-category** agents (e.g. one agent ported across
  Claude Code / Codex / Gemini CLI), keeping the richest prompt and folding in
  every source for attribution.
- Merges **near-identical** agents (Jaccard ≥ 0.97, same category, guarded by a
  cheap body-length prefilter).
- Disambiguates any remaining name collisions.

No identical prompts are kept; every original source is preserved in
`agy.sources`. Outputs `agents/<category>/<name>.md` and
`metadata/agents.json`.

### 5. classify — `scripts/classify.py`

Assigns every repository one of six final statuses and emits the reports:

- **Imported** — contributed reusable agents.
- **Duplicate** — its content was fully subsumed by other repos during dedupe.
- **Unsupported** — agent-related content in a non-convertible format
  (runtime, framework, SDK, plugin collection, ...).
- **Empty** — agent structure but no usable prompt content.
- **Non-agent repository** — no reusable subagents (docs/knowledge/app).
- **Requires manual review** — clone/parse issues.

Writes `metadata/repo_status.json`, `reports/coverage.md` and
`reports/unsupported.md` (the latter explains why each unsupported repo cannot
be imported and what AGY compatibility would require).

### 6. validate — `scripts/validate.py`

Checks each agent against `docs/AGY-SPEC.md`: name/description/prompt
presence, name-slug legality, category membership. Failures are listed in
`reports/validation.md`.

### 7. report — `scripts/report.py`

Regenerates `metadata/summary.json` and the human-readable reports: summary
(including ecosystem coverage and repository classification), categories,
compatibility, tool usage, MCP dependencies, and repository report.

### 8. export — `scripts/export.py`

Writes the `tools/` catalog (20 core AGY tools + MCP integrations, including
MCP servers discovered in the corpus) and the `exports/agents.csv` registry.
`exports/agents.json` is a duplicate of `metadata/agents.json` and is
git-ignored.

## Scheduled re-runs

The pipeline is idempotent and re-runnable. A CI job (e.g. a weekly GitHub
Action) can run `.venv/bin/python scripts/run_all.py`, then open a pull request
with any new `agents/`, `metadata/`, `reports/`, and `tools/` changes. A
ready-to-use workflow is provided at `templates/import-workflow.yml` — copy it
to `.github/workflows/import.yml`. It:

1. Installs `pyyaml` and the `gh` CLI.
2. Runs `.venv/bin/python scripts/run_all.py`.
3. Commits changes and opens a PR via `gh pr create`.

## Troubleshooting

- **`yaml` import error** — `.venv/bin/pip install pyyaml` (or create the
  virtualenv first: `python3 -m venv .venv && .venv/bin/pip install PyYAML`).
- **`ModuleNotFoundError: yaml` on the system interpreter** — the environment
  is PEP-668 managed; always use the project virtualenv.
- **Disk pressure while processing** — `process_all.py` streams (clones are
  deleted after each repo is scanned), so `imports/sources/` stays small; the
  bulk intermediate `metadata/raw_records.json` is git-ignored.
- **GitHub rate limits** — `discover.py` sleeps between queries; a PAT
  (already available via `gh`) raises the search limit.
- **Unsupported sources** — repositories that store agents as Python classes
  or TypeScript code (rather than frontmatter files) are classified as
  `unsupported` (or `non-agent`) with an explanation in
  `reports/unsupported.md`.
