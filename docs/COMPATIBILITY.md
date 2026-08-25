# Compatibility Model

Every imported agent is assigned a compatibility status describing how much
work (if any) remains before it runs correctly in AGY.

| Status | Score | Meaning | Typical cause |
|---|---|---|---|
| `fully-compatible` | 100 | Ready to use as-is. | Standard frontmatter; tools mapped 1:1. |
| `requires-mcp` | 85 | Works, but needs one or more MCP servers installed. | `mcpServers` populated (e.g. `context7`, `sequential-thinking`). |
| `needs-tool-mapping` | 75 | Works after reviewing the tool allow-list. | Source used tools with no direct AGY equivalent (e.g. Claude `Task`). |
| `requires-manual-conversion` | 50 | Prompt extracted from raw text; needs a human to finalize. | No parseable frontmatter. |
| `unsupported` | 0 | Could not be converted. | Agents defined in executable code, not data files. |

The **average compatibility score** of the current corpus and the full
per-agent breakdown are in [`reports/compatibility.md`](../reports/compatibility.md).

## How statuses are computed

1. If no frontmatter/metadata can be parsed, the prompt is extracted from the
   raw text and the agent is marked `requires-manual-conversion`.
2. If the agent declares MCP servers, it is marked `requires-mcp`.
3. If some tools have no canonical AGY mapping, it is marked
   `needs-tool-mapping`.
4. Otherwise it is `fully-compatible`.

## Tool mapping reference

Foreign tool names are normalized onto the canonical AGY tool set:

| Canonical AGY tool | Claude Code | Codex / other |
|---|---|---|
| `read_file` | `Read` | `read_file`, `view_file` |
| `write_file` | `Write` | `write_file`, `create_file` |
| `edit_file` | `Edit`, `MultiEdit`, `NotebookEdit` | `edit_file`, `apply_patch` |
| `grep` | `Grep` | `search_content`, `ripgrep` |
| `glob` | `Glob` | `search_file`, `list_files` |
| `list_dir` | `LS` | `list_dir` |
| `run_shell_command` | `Bash` | `shell`, `run_command` |
| `web_search` | `WebSearch` | `web_search`, `brave_search` |
| `web_fetch` | `WebFetch` | `fetch_url`, `browse` |
| `todo` | `TodoWrite` | `todo` |

The full mapping table is in `scripts/agy.py` (`TOOL_MAP`).

## Unsupported sources

Some repositories define agents as executable code rather than data files
(e.g. orchestrators implemented in Python or TypeScript). These cannot be
converted losslessly by the importer. They are documented here so future
importers can add targeted extractors:

- `Doriandarko/maestro` — agents are Python orchestration code.
- `nicobailon/pi-subagents` / `tintinweb/pi-subagents` — subagents are
  implemented as Pi TypeScript extensions.
- `shinpr/sub-agents-mcp` — a runtime that defines agents procedurally.

These are recorded as analyzed-but-not-converted in
[`reports/repositories.md`](../reports/repositories.md).
