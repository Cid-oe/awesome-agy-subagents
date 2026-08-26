#!/usr/bin/env python3
"""Clone discovered repositories into imports/sources/ for scanning.

Uses metadata/discovered_repos.json as input. Only clones repositories that are
likely to contain agent definitions (have an agents/ directory, agent files, or
match agent-related topics/keywords).
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "imports" / "sources"
META_DIR = ROOT / "metadata"

KEYWORDS = [
    "agent", "subagent", "skill", "claude", "codex", "gemini", "cursor",
    "opencode", "plugin", "prompt", "ai ",
]


def slug_name(full_name: str) -> str:
    return full_name.replace("/", "--")


def main() -> None:
    repos_file = META_DIR / "discovered_repos.json"
    if not repos_file.exists():
        print("Run scripts/discover.py first.", file=sys.stderr)
        sys.exit(1)
    repos = json.loads(repos_file.read_text(encoding="utf-8"))

    SOURCES.mkdir(parents=True, exist_ok=True)
    cloned_file = META_DIR / "cloned_repos.json"
    cloned = {}
    if cloned_file.exists():
        cloned = json.loads(cloned_file.read_text(encoding="utf-8"))

    for repo in repos:
        full_name = repo["full_name"]
        text = f"{repo.get('description','')} {' '.join(repo.get('topics', []))} {full_name}".lower()
        if not any(kw in text for kw in KEYWORDS):
            continue
        dest = SOURCES / slug_name(full_name)
        if (dest / ".git").exists() or dest.exists():
            continue
        print(f"cloning {full_name} ...")
        r = subprocess.run(
            ["git", "clone", "--depth", "1", repo["clone_url"], str(dest)],
            capture_output=True, text=True, timeout=300,
        )
        if r.returncode != 0:
            print(f"  ! failed: {r.stderr.strip().splitlines()[-1] if r.stderr else '?'}")
            continue
        cloned[full_name] = {
            "full_name": full_name,
            "stars": repo.get("stars"),
            "license": repo.get("license"),
            "path": str(dest.relative_to(ROOT)),
        }
        cloned_file.write_text(json.dumps(cloned, indent=2), encoding="utf-8")

    print(f"\nCloned {len(cloned)} repos. Registry: {cloned_file.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
