# AGY Subagent Specification

AGY subagents are single Markdown files. The file **body** is the subagent's
system prompt; the **YAML frontmatter** carries its runtime configuration and
provenance metadata.

An AGY subagent can be dropped into an Antigravity CLI (`agy`) project under
`.gemini/agents/` (or a compatible harness that reads frontmatter subagents)
and invoked by name.

## File layout

```
---
name: security-auditor
description: Audits code for security vulnerabilities.
kind: local
model: inherit
temperature: 1.0
max_turns: 30
timeout_mins: 10
tools:
  - read_file
  - grep
  - run_shell_command
mcpServers: {}
agy:
  version: "1.0.0"
  category: security
  tags: [security, audit]
  compatibility:
    status: fully-compatible
    score: 100
    notes: Converted directly; no manual steps required.
  validation: passed
  imported: 2026-08-25T00:00:00+00:00
  sources:
    - repo: example/repo
      author: example
      license: MIT
      url: https://github.com/example/repo
      path: agents/security-auditor.md
      format: markdown-frontmatter
---

You are an expert security auditor...
```

## Runtime fields (top level)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Unique slug: lowercase letters, numbers, hyphens, underscores. |
| `description` | string | yes | Short summary the parent agent uses to decide when to invoke this subagent. |
| `kind` | string | no | `local` (default) or `remote`. |
| `model` | string | no | Model to use, or `inherit` (default) to use the parent session model. |
| `temperature` | number | no | Sampling temperature (0.0–2.0). Default 1.0. |
| `max_turns` | integer | no | Maximum conversation turns. Default 30. |
| `timeout_mins` | integer | no | Maximum execution time in minutes. Default 10. |
| `tools` | array | no | Tool allow-list. Supports `*` (all), `mcp_*`, `mcp_server_*`. Omitted ⇒ inherits parent tools. |
| `mcpServers` | object/array | no | Inline MCP server configuration isolated to this subagent. |

## Provenance & metadata (`agy.*`)

Every imported agent carries an `agy` block that records where it came from and
how it was converted. This is the machine-readable contract the importer and
validator maintain:

| Field | Description |
|---|---|
| `agy.version` | AGY schema version. |
| `agy.category` | One of the canonical categories (see `CATEGORIES` in `scripts/agy.py`). |
| `agy.tags` | Free-form tags. |
| `agy.compatibility.status` | `fully-compatible`, `requires-mcp`, `needs-tool-mapping`, `requires-manual-conversion`, or `unsupported`. |
| `agy.compatibility.score` | 0–100 compatibility score. |
| `agy.compatibility.notes` | Human-readable explanation of any conversion steps. |
| `agy.validation` | `passed` or `failed` (against this spec). |
| `agy.imported` | ISO-8601 import timestamp. |
| `agy.sources[]` | One entry per upstream source (repo, author, license, url, path, format). |

`agy.sources` is a **list**: when two upstream projects define the same agent,
the agent is merged once and both sources are preserved for attribution.

## Compatibility statuses

- **fully-compatible** (100) — frontmatter converted 1:1; no manual work.
- **requires-mcp** (85) — agent depends on one or more MCP servers listed in
  `mcpServers`; install those servers before use.
- **needs-tool-mapping** (75) — some source tools had no direct AGY equivalent
  and were dropped or approximated; review `tools`.
- **requires-manual-conversion** (50) — no frontmatter could be parsed; the
  prompt was extracted from raw text and needs a human to finish conversion.
- **unsupported** (0) — the source format could not be converted at all.

## Tool mapping

The importer maps foreign tool names onto the canonical AGY tool set. The
canonical names (see `tools/core/` for full documentation) include:

`read_file`, `write_file`, `edit_file`, `replace_file_content`, `view_file`,
`grep`, `grep_search`, `glob`, `list_dir`, `run_command`, `run_shell_command`,
`send_message`, `find_by_name`, `read_url_content`, `web_search`, `web_fetch`,
`schedule`, `todo`, `define_subagent`, `invoke_subagent`.

Foreign spellings (Claude Code `Read`/`Write`/`Edit`/`Bash`, Codex
`developer_instructions` TOML, etc.) are mapped automatically; unmapped tools
lower the agent's compatibility score to `needs-tool-mapping`.

## Validation

`scripts/validate.py` checks every agent against the invariants above:
presence of `name`, `description` and a non-empty prompt body; name-slug
legality; category membership. Results are written to
`reports/validation.md` and `metadata/validation_report.json`.
