#!/usr/bin/env python3
"""Discover public repositories containing AI agent definitions.

Queries the GitHub search API for repositories that host subagents/agents for
Claude Code, Codex, Gemini CLI, Cursor, OpenCode, Pi, Antigravity, etc., and
writes a normalized registry to metadata/discovered_repos.json.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META_DIR = ROOT / "metadata"
OUT = META_DIR / "discovered_repos.json"

# Canonical, known high-yield repositories (always included).
KNOWN_REPOS = [
    "wshobson/agents",
    "VoltAgent/awesome-claude-code-subagents",
    "VoltAgent/awesome-codex-subagents",
    "iannuttall/claude-agents",
    "lst97/claude-code-sub-agents",
    "0xfurai/claude-code-subagents",
    "tintinweb/pi-subagents",
    "HazAT/pi-interactive-subagents",
    "Doriandarko/maestro",
    "nicobailon/pi-subagents",
    "0xSteph/pentest-ai-agents",
    "zubair-trabzada/ai-marketing-claude",
    "data-goblin/power-bi-agentic-development",
    "ccplugins/awesome-claude-code-plugins",
    "disler/claude-code-subagents",
]

SEARCH_QUERIES = [
    # keyword / name / description / topic searches
    "subagents in:name,description,topic",
    "claude code subagents",
    "claude subagents",
    "codex subagents",
    "gemini subagents",
    "agent skills claude",
    "claude code plugins",
    "subagents in:readme",
    # filename-based searches
    "filename:AGENT.md",
    "filename:agent.md",
    "filename:*.agent.md",
    "filename:CLAUDE.md",
    "filename:SYSTEM.md",
    "filename:instructions.md",
    "filename:subagent.md",
    "filename:SUBAGENT.md",
    # path-based searches
    "path:.claude/agents",
    "path:.gemini/agents",
    "path:.codex/agents",
    "path:.cursor/agents",
    "path:.opencode/agents",
    "path:.agents",
    "path:agents",
    "path:subagents",
    # topic searches
    "topic:claude-code",
    "topic:subagents",
    "topic:gemini-cli",
    "topic:codex",
    "topic:cursor",
    "topic:opencode",
    "topic:aider",
    "topic:ai-agent",
    "topic:coding-agent",
    "topic:agent-skills",
    "topic:claude-skills",
    "topic:claude-agents",
    "topic:codex-agents",
    "topic:llm-agent",
    "topic:antigravity",
]


def gh_api(endpoint: str) -> dict | list:
    out = subprocess.run(
        ["gh", "api", endpoint],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[:500])
    return json.loads(out.stdout)


def search_repos(query: str, per_page: int = 30) -> list[dict]:
    from urllib.parse import quote
    endpoint = f"search/repositories?q={quote(query)}&sort=stars&order=desc&per_page={per_page}"
    try:
        data = gh_api(endpoint)
    except RuntimeError as e:
        print(f"  ! search failed ({query[:30]}): {e}", file=sys.stderr)
        return []
    items = data.get("items", []) if isinstance(data, dict) else []
    return items


def normalize(item: dict) -> dict:
    owner = (item.get("owner") or {}).get("login", "")
    lic = (item.get("license") or {})
    return {
        "full_name": item.get("full_name"),
        "owner": owner,
        "stars": item.get("stargazers_count", 0),
        "forks": item.get("forks_count", 0),
        "license": lic.get("spdx_id") if lic else None,
        "description": (item.get("description") or "").strip(),
        "default_branch": item.get("default_branch"),
        "html_url": item.get("html_url"),
        "clone_url": item.get("clone_url"),
        "topics": item.get("topics", []),
        "pushed_at": item.get("pushed_at"),
        "archived": item.get("archived", False),
    }


def main() -> None:
    discovered: dict[str, dict] = {}
    known_names = set()

    print("Fetching known canonical repos...")
    for full_name in KNOWN_REPOS:
        try:
            data = gh_api(f"repos/{full_name}")
            discovered[full_name] = normalize(data)
            known_names.add(full_name)
            print(f"  + {full_name} ({discovered[full_name]['stars']} stars)")
        except RuntimeError as e:
            print(f"  ! {full_name}: {e}", file=sys.stderr)

    print("Searching GitHub...")
    for q in SEARCH_QUERIES:
        print(f"  query: {q}")
        for item in search_repos(q):
            full_name = item.get("full_name")
            if not full_name or full_name in discovered:
                continue
            discovered[full_name] = normalize(item)
        time.sleep(3)  # be gentle with rate limits

    # Order by stars desc.
    repos = sorted(discovered.values(), key=lambda r: -r["stars"])
    META_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(repos, indent=2), encoding="utf-8")
    print(f"\nWrote {len(repos)} repos to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
