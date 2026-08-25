#!/usr/bin/env python3
"""Generate the tools/ catalog and export registries (JSON, CSV, markdown index).

tools/ contains:
  - core/     : documentation for AGY built-in tools
  - mcp/      : documentation for MCP servers (referenced by imported agents
                plus the standard reusable integrations)
Every tool doc includes name, description, parameters, examples, platforms,
related agents and compatibility information derived from the imported corpus.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META_DIR = ROOT / "metadata"
TOOLS_DIR = ROOT / "tools"
EXPORTS_DIR = ROOT / "exports"

# --------------------------------------------------------------------------- #
# Core AGY built-in tools (accurate, from the Antigravity CLI tool set)
# --------------------------------------------------------------------------- #

CORE_TOOLS = [
    {"name": "read_file", "platform": "filesystem", "description": "Read a file's contents, optionally with line ranges.", "example": 'read_file(path="src/main.py", limit=50)'},
    {"name": "write_file", "platform": "filesystem", "description": "Create or overwrite a file with full content.", "example": 'write_file(path="README.md", content="# Title\\n")'},
    {"name": "edit_file", "platform": "filesystem", "description": "Apply a targeted string replacement to a file.", "example": 'edit_file(path="app.js", old_text="var x = 1", new_text="const x = 1")'},
    {"name": "replace_file_content", "platform": "filesystem", "description": "Replace file content matching a pattern.", "example": 'replace_file_content(path="cfg.yaml", old="v1", new="v2")'},
    {"name": "view_file", "platform": "filesystem", "description": "View a file (read-only) with syntax awareness.", "example": 'view_file(path="src/main.py")'},
    {"name": "grep", "platform": "filesystem", "description": "Search file contents for a regular expression.", "example": 'grep(pattern="TODO", path="src/")'},
    {"name": "grep_search", "platform": "filesystem", "description": "Structured content search with context lines.", "example": 'grep_search(query="auth", path="src/", context=3)'},
    {"name": "glob", "platform": "filesystem", "description": "Find files matching a glob pattern.", "example": 'glob(pattern="**/*.test.ts")'},
    {"name": "list_dir", "platform": "filesystem", "description": "List a directory's contents.", "example": 'list_dir(path="src/components")'},
    {"name": "run_command", "platform": "shell", "description": "Execute a shell command in the environment.", "example": 'run_command(command="npm test")'},
    {"name": "run_shell_command", "platform": "shell", "description": "Execute a shell command with cwd/argument control.", "example": 'run_shell_command(command="git status", cwd=".")'},
    {"name": "send_message", "platform": "messaging", "description": "Send a message to the parent/user in the session.", "example": 'send_message(content="Refactor complete.")'},
    {"name": "find_by_name", "platform": "filesystem", "description": "Locate a file by name across the project.", "example": 'find_by_name(name="package.json")'},
    {"name": "read_url_content", "platform": "browser", "description": "Read the content of a URL as text/markdown.", "example": 'read_url_content(url="https://example.com")'},
    {"name": "web_search", "platform": "browser", "description": "Search the web and return ranked results.", "example": 'web_search(query="AGY subagent specification")'},
    {"name": "web_fetch", "platform": "browser", "description": "Fetch a URL and extract readable content.", "example": 'web_fetch(url="https://example.com/docs")'},
    {"name": "schedule", "platform": "productivity", "description": "Schedule a task or reminder for the session.", "example": 'schedule(at="+10m", task="re-run tests")'},
    {"name": "todo", "platform": "productivity", "description": "Maintain a structured task list.", "example": 'todo(items=[{"task": "Review PR", "status": "pending"}])'},
    {"name": "define_subagent", "platform": "orchestration", "description": "Define a transient subagent at runtime.", "example": 'define_subagent(name="echo", instructions="repeat input")'},
    {"name": "invoke_subagent", "platform": "orchestration", "description": "Invoke a defined subagent and await its result.", "example": 'invoke_subagent(name="echo", prompt="hello")'},
]

# Standard reusable MCP server integrations (accurate, well-known).
# (name, category, description, transport)
_MCP = [
    # Git / version control
    ("github", "github", "GitHub repos, issues, PRs, Actions, and code search.", "Streamable HTTP"),
    ("gitlab", "github", "GitLab repos, merge requests, CI, and issues.", "Streamable HTTP / stdio"),
    ("git", "github", "Read-only git inspection: log, diff, status, blame.", "stdio"),
    ("bitbucket", "github", "Bitbucket repos, PRs, and pipelines.", "Streamable HTTP"),
    ("azure-devops", "github", "Azure DevOps work items, repos, and pipelines.", "Streamable HTTP"),
    # Databases
    ("postgres", "database", "PostgreSQL queries, schema, and introspection.", "stdio"),
    ("mysql", "database", "MySQL/MariaDB queries and schema inspection.", "stdio"),
    ("sqlite", "database", "SQLite query and inspection.", "stdio"),
    ("redis", "database", "Redis data structures, keys, and commands.", "stdio"),
    ("mongodb", "database", "MongoDB queries and collection inspection.", "stdio"),
    ("supabase", "database", "Supabase database, auth, and storage.", "Streamable HTTP"),
    ("neo4j", "database", "Neo4j graph queries and traversal.", "stdio"),
    ("duckdb", "database", "In-process analytical SQL via DuckDB.", "stdio"),
    ("clickhouse", "database", "ClickHouse analytical queries.", "Streamable HTTP"),
    ("elasticsearch", "database", "Elasticsearch search and index operations.", "Streamable HTTP"),
    ("bigquery", "database", "Google BigQuery SQL and dataset inspection.", "Streamable HTTP"),
    ("snowflake", "database", "Snowflake data warehouse queries.", "Streamable HTTP"),
    # Cloud
    ("aws", "cloud", "AWS resource inspection and operations.", "Streamable HTTP / stdio"),
    ("aws-s3", "cloud", "Amazon S3 bucket and object management.", "stdio"),
    ("azure", "cloud", "Microsoft Azure resource management.", "Streamable HTTP"),
    ("gcp", "cloud", "Google Cloud resource inspection.", "Streamable HTTP"),
    ("terraform", "cloud", "Terraform plan/state inspection.", "stdio"),
    # Containers / orchestration
    ("docker", "docker", "Docker containers, images, and volumes.", "stdio"),
    ("kubernetes", "kubernetes", "Kubernetes pods, deployments, and clusters.", "stdio"),
    ("helm", "kubernetes", "Helm chart inspection and release management.", "stdio"),
    ("podman", "docker", "Podman container management.", "stdio"),
    # Browser / automation
    ("puppeteer", "browser", "Headless Chrome automation (navigate, click, screenshot).", "stdio"),
    ("playwright", "browser", "Cross-browser automation and testing.", "stdio"),
    ("browser-use", "browser", "Browser automation for agent-driven web tasks.", "stdio"),
    ("chrome-devtools", "browser", "Chrome DevTools Protocol debugging and inspection.", "stdio"),
    ("firecrawl", "browser", "Web scraping and crawling with markdown extraction.", "Streamable HTTP"),
    # Search
    ("brave-search", "search", "Brave-powered web search.", "stdio"),
    ("tavily", "search", "Real-time web search API.", "stdio"),
    ("exa", "search", "Semantic and neural web search.", "Streamable HTTP"),
    ("serper", "search", "Google SERP API search.", "Streamable HTTP"),
    ("perplexity", "search", "Perplexity answer-engine search.", "Streamable HTTP"),
    ("duckduckgo", "search", "DuckDuckGo search.", "stdio"),
    # Productivity / PM
    ("slack", "slack", "Slack channels, messages, and threads.", "Streamable HTTP"),
    ("notion", "productivity", "Notion pages, databases, and search.", "Streamable HTTP"),
    ("linear", "productivity", "Linear issues, projects, and cycles.", "Streamable HTTP"),
    ("jira", "productivity", "Jira issues, boards, and sprints.", "Streamable HTTP"),
    ("confluence", "productivity", "Confluence pages and spaces.", "Streamable HTTP"),
    ("asana", "productivity", "Asana tasks and projects.", "Streamable HTTP"),
    ("trello", "productivity", "Trello boards, lists, and cards.", "Streamable HTTP"),
    ("todoist", "productivity", "Todoist tasks and projects.", "Streamable HTTP"),
    # Files / notes / memory
    ("filesystem", "filesystem", "Path-scoped filesystem read/write/search.", "stdio"),
    ("memory", "memory", "Persistent knowledge-graph memory.", "stdio"),
    ("obsidian", "filesystem", "Obsidian vault notes and links.", "stdio"),
    ("markitdown", "filesystem", "Convert documents (PDF, DOCX, ...) to markdown.", "stdio"),
    # Observability
    ("sentry", "observability", "Sentry errors, issues, and release health.", "Streamable HTTP"),
    ("datadog", "observability", "Datadog metrics, logs, and traces.", "Streamable HTTP"),
    ("prometheus", "observability", "Prometheus metrics querying.", "Streamable HTTP"),
    ("grafana", "observability", "Grafana dashboards and queries.", "Streamable HTTP"),
    ("new-relic", "observability", "New Relic APM and telemetry.", "Streamable HTTP"),
    # Communication
    ("gmail", "communication", "Gmail send/search/read.", "Streamable HTTP"),
    ("google-workspace", "communication", "Google Drive, Docs, Sheets, and Calendar.", "Streamable HTTP"),
    ("telegram", "communication", "Telegram messaging and bots.", "stdio"),
    ("discord", "communication", "Discord channels and messages.", "stdio"),
    ("discord-webhook", "communication", "Discord webhook notifications.", "stdio"),
    # Docs / knowledge / reasoning
    ("fetch", "browser", "Fetch URLs and extract markdown.", "stdio"),
    ("context7", "knowledge", "Up-to-date library documentation lookup.", "Streamable HTTP"),
    ("sequential-thinking", "reasoning", "Structured multi-step reasoning.", "stdio"),
    ("time", "utility", "Current time and timezone conversion.", "stdio"),
    ("calendar", "productivity", "Calendar events and scheduling.", "Streamable HTTP"),
    # CRM / sales / support
    ("hubspot", "crm", "HubSpot contacts, deals, and tickets.", "Streamable HTTP"),
    ("salesforce", "crm", "Salesforce objects and records.", "Streamable HTTP"),
    ("stripe", "crm", "Stripe payments, customers, and invoices.", "Streamable HTTP"),
    ("zendesk", "crm", "Zendesk tickets and help center.", "Streamable HTTP"),
    ("intercom", "crm", "Intercom conversations and contacts.", "Streamable HTTP"),
    # AI / LLM
    ("openai", "ai", "OpenAI models for generation and embeddings.", "Streamable HTTP"),
    ("anthropic", "ai", "Anthropic Claude API access.", "Streamable HTTP"),
    ("google-gemini", "ai", "Google Gemini model access.", "Streamable HTTP"),
    ("ollama", "ai", "Local LLM inference via Ollama.", "stdio"),
    ("lmstudio", "ai", "Local LLM inference via LM Studio.", "stdio"),
    ("groq", "ai", "Groq fast LLM inference.", "Streamable HTTP"),
    ("mistral", "ai", "Mistral model access.", "Streamable HTTP"),
    ("cohere", "ai", "Cohere LLM and embeddings.", "Streamable HTTP"),
    ("huggingface", "ai", "Hugging Face models and datasets.", "Streamable HTTP"),
    ("replicate", "ai", "Replicate model inference.", "Streamable HTTP"),
    # Databases (extended)
    ("mariadb", "database", "MariaDB queries and schema inspection.", "stdio"),
    ("couchdb", "database", "CouchDB documents and views.", "Streamable HTTP"),
    ("influxdb", "database", "InfluxDB time-series queries.", "Streamable HTTP"),
    ("presto", "database", "Presto/Trino distributed SQL queries.", "Streamable HTTP"),
    ("scylladb", "database", "ScyllaDB NoSQL queries.", "stdio"),
    # Security / CI
    ("snyk", "security", "Snyk vulnerability scanning and remediation.", "Streamable HTTP"),
    ("semgrep", "security", "Semgrep static analysis for security.", "stdio"),
    ("jenkins", "ci-cd", "Jenkins builds, jobs, and logs.", "Streamable HTTP"),
    ("circleci", "ci-cd", "CircleCI pipelines and workflows.", "Streamable HTTP"),
    # Utility / misc
    ("math", "utility", "Symbolic and numeric math evaluation.", "stdio"),
    ("weather", "utility", "Current weather and forecasts by location.", "Streamable HTTP"),
    ("rss", "utility", "RSS feed reading and parsing.", "stdio"),
    ("hacker-news", "utility", "Hacker News stories and comments.", "stdio"),
    ("google-maps", "location", "Google Maps geocoding and places.", "Streamable HTTP"),
]

MCP_TOOLS = [
    {"name": n, "category": c, "description": d, "transport": t,
     "example": f"{n.replace('-', '_')}(...)",
     "platforms": ["All"] if t == "Streamable HTTP" else ["Linux", "macOS", "Windows"]}
    for n, c, d, t in _MCP
]


def load(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def main() -> None:
    agents = load(META_DIR / "agents.json", [])

    # Build tool -> related agents index.
    tool_agents: dict[str, list[str]] = {}
    for a in agents:
        for t in a.get("tools", []):
            tool_agents.setdefault(t, []).append(a["name"])

    mcp_agents: dict[str, list[str]] = {}
    mcp_used: Counter = Counter()
    for a in agents:
        for m in a.get("mcp_servers", []):
            mcp_used[m] += 1
            mcp_agents.setdefault(m, []).append(a["name"])

    TOOLS_DIR.mkdir(parents=True, exist_ok=True)

    # --- core tools ---
    core_dir = TOOLS_DIR / "core"
    core_dir.mkdir(exist_ok=True)
    for t in CORE_TOOLS:
        related = tool_agents.get(t["name"], [])
        body = f"""# {t['name']}

{t['description']}

## Platform
**{t['platform']}**

## Example

```
{t['example']}
```

## Related agents

{chr(10).join('- ' + r for r in related) if related else '_None in the current corpus._'}

## Compatibility

- AGY: built-in tool
- Claude Code mapping: `{t['name']}`
"""
        (core_dir / f"{t['name']}.md").write_text(body, encoding="utf-8")

    # --- mcp tools ---
    mcp_dir = TOOLS_DIR / "mcp"
    mcp_dir.mkdir(exist_ok=True)
    for t in MCP_TOOLS:
        related = mcp_agents.get(t["name"], [])
        in_corpus = mcp_used.get(t["name"], 0)
        body = f"""# {t['name']}

{ t['description'] }

## Category
**{t['category']}**

## Transport
{t['transport']}

## Usage

```
{ t['example'] }
```

## Platforms
{', '.join(t['platforms'])}

## Referenced by imported agents
{'Used by **' + str(in_corpus) + '** agent(s) in this corpus.' if in_corpus else 'Not yet referenced by any imported agent (standard integration).'}

{chr(10).join('- ' + r for r in related) if related else ''}

## Compatibility

- AGY: available via `mcpServers` frontmatter
- Claude Code: `mcp__{t['name']}__*` tools
"""
        (mcp_dir / f"{t['name']}.md").write_text(body, encoding="utf-8")

    # --- tools index ---
    idx = ["# Tools Catalog", ""]
    idx.append(f"Total documented tools: **{len(CORE_TOOLS) + len(MCP_TOOLS)}**")
    idx.append("")
    idx.append("## Core AGY built-in tools")
    idx.append("")
    for t in CORE_TOOLS:
        idx.append(f"- [`{t['name']}`](core/{t['name']}.md) — {t['description'][:80]}")
    idx.append("")
    idx.append("## MCP server integrations")
    idx.append("")
    for t in MCP_TOOLS:
        idx.append(f"- [`{t['name']}`](mcp/{t['name']}.md) — {t['description'][:80]}")
    idx.append("")
    (TOOLS_DIR / "README.md").write_text("\n".join(idx), encoding="utf-8")

    # --- exports ---
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (EXPORTS_DIR / "agents.json").write_text(json.dumps(agents, indent=2), encoding="utf-8")

    with open(EXPORTS_DIR / "agents.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "category", "description", "compatibility", "tools",
                    "mcp_servers", "repo", "license"])
        for a in agents:
            w.writerow([a["name"], a.get("category", ""), a.get("description", "")[:120],
                        a.get("compatibility", ""), "|".join(a.get("tools", [])),
                        "|".join(a.get("mcp_servers", [])),
                        ";".join(s["repo"] for s in a.get("sources", [])),
                        ";".join(s.get("license", "") for s in a.get("sources", []))])

    print(f"tools/ written: {len(CORE_TOOLS)} core + {len(MCP_TOOLS)} MCP = {len(CORE_TOOLS)+len(MCP_TOOLS)} tools.")
    print(f"exports/ written: agents.json, agents.csv")


if __name__ == "__main__":
    main()
