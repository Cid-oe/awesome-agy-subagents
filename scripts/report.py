#!/usr/bin/env python3
"""Generate summary, compatibility, category, tool, MCP and repository reports."""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META_DIR = ROOT / "metadata"
REPORTS = ROOT / "reports"


def load(path: Path, default):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def main() -> None:
    agents = load(META_DIR / "agents.json", [])
    repos = load(META_DIR / "discovered_repos.json", [])
    cloned = load(META_DIR / "cloned_repos.json", {})
    dedupe = load(META_DIR / "dedupe_report.json", {})
    validation = load(META_DIR / "validation_report.json", {})

    # Derive scanned repositories from the filesystem if registry is stale.
    sources_dir = ROOT / "imports" / "sources"
    scanned_dirs = []
    if sources_dir.exists():
        scanned_dirs = sorted(d.name for d in sources_dir.iterdir() if d.is_dir())
    discovered_by_slug = {}
    for r in repos:
        discovered_by_slug[r["full_name"].replace("/", "--")] = r
    scanned = len(cloned) or len(scanned_dirs)
    if not cloned and scanned_dirs:
        cloned = {}
        for d in scanned_dirs:
            full_name = d.replace("--", "/")
            meta = discovered_by_slug.get(d, {})
            cloned[full_name] = {
                "full_name": full_name,
                "stars": meta.get("stars"),
                "license": meta.get("license"),
                "path": f"imports/sources/{d}",
            }
        (META_DIR / "cloned_repos.json").write_text(json.dumps(cloned, indent=2), encoding="utf-8")

    REPORTS.mkdir(parents=True, exist_ok=True)

    # Stats.
    n = len(agents)
    cat_counter = Counter(a.get("category", "general") for a in agents)
    status_counter = Counter(a.get("compatibility", "?") for a in agents)
    tool_counter = Counter()
    mcp_counter = Counter()
    license_counter = Counter()
    repo_counter = Counter()
    for a in agents:
        for t in a.get("tools", []):
            tool_counter[t] += 1
        for m in a.get("mcp_servers", []):
            mcp_counter[m] += 1
        for s in a.get("sources", []):
            repo_counter[s.get("repo", "?")] += 1
            lic = s.get("license", "")
            license_counter[lic or "unknown"] += 1

    score_sum = sum(
        {
            "fully-compatible": 100, "requires-mcp": 85, "needs-tool-mapping": 75,
            "requires-manual-conversion": 50, "unsupported": 0,
        }.get(a.get("compatibility", ""), 0)
        for a in agents
    )
    avg_score = round(score_sum / n, 1) if n else 0
    fully = status_counter.get("fully-compatible", 0)
    conv_rate = round(100 * fully / n, 1) if n else 0

    summary = {
        "generated_at": __import__("agy").now_iso(),
        "repositories_scanned": len(cloned),
        "repositories_discovered": len(repos),
        "agents_discovered": dedupe.get("total_before", n),
        "agents_converted": n,
        "agents_fully_compatible": fully,
        "agents_incompatible": n - fully,
        "duplicates_removed": dedupe.get("duplicates_removed", 0),
        "licenses_detected": len(license_counter),
        "conversion_success_rate": conv_rate,
        "average_compatibility_score": avg_score,
        "category_distribution": dict(cat_counter),
        "compatibility_distribution": dict(status_counter),
        "tool_usage": dict(tool_counter),
        "mcp_dependencies": dict(mcp_counter),
        "repositories_contributing": dict(repo_counter),
        "licenses": dict(license_counter),
    }
    (META_DIR / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # --- summary.md ---
    L = ["# AGY Ecosystem — Summary Report", "", f"_Generated {summary['generated_at']}_", ""]
    L += [
        "## Core metrics", "",
        "| Metric | Value |", "|---|---|",
        f"| Repositories discovered | {summary['repositories_discovered']} |",
        f"| Repositories scanned (cloned) | {summary['repositories_scanned']} |",
        f"| Agents discovered (pre-dedupe) | {summary['agents_discovered']} |",
        f"| Agents converted | {summary['agents_converted']} |",
        f"| Fully AGY-compatible | {summary['agents_fully_compatible']} |",
        f"| Incompatible (need work) | {summary['agents_incompatible']} |",
        f"| Duplicates removed | {summary['duplicates_removed']} |",
        f"| Licenses detected | {summary['licenses_detected']} |",
        f"| Conversion success rate | {summary['conversion_success_rate']}% |",
        f"| Average compatibility score | {summary['average_compatibility_score']} |",
        "",
    ]
    (REPORTS / "summary.md").write_text("\n".join(L), encoding="utf-8")

    # --- categories.md ---
    L = ["# Category Distribution", ""]
    L += ["| Category | Agents |", "|---|---|"]
    for cat, c in cat_counter.most_common():
        L.append(f"| {cat} | {c} |")
    L.append("")
    (REPORTS / "categories.md").write_text("\n".join(L), encoding="utf-8")

    # --- compatibility.md ---
    L = ["# Compatibility Report", "", "## Status distribution", ""]
    L += ["| Status | Count |", "|---|---|"]
    for st, c in status_counter.most_common():
        L.append(f"| {st} | {c} |")
    L.append("")
    L.append("## Per-agent compatibility")
    L.append("")
    L.append("| Agent | Category | Status | Score | Notes |")
    L.append("|---|---|---|---|---|")
    for a in sorted(agents, key=lambda x: x["name"]):
        score = {"fully-compatible": 100, "requires-mcp": 85, "needs-tool-mapping": 75,
                 "requires-manual-conversion": 50, "unsupported": 0}.get(a.get("compatibility", ""), 0)
        L.append(f"| {a['name']} | {a.get('category','?')} | {a.get('compatibility','?')} | {score} | {a.get('compatibility_notes','')} |")
    L.append("")
    (REPORTS / "compatibility.md").write_text("\n".join(L), encoding="utf-8")

    # --- tools.md ---
    L = ["# Tool Usage Statistics", ""]
    L += ["| Tool | Agents using it |", "|---|---|"]
    for t, c in tool_counter.most_common():
        L.append(f"| `{t}` | {c} |")
    L.append("")
    (REPORTS / "tools.md").write_text("\n".join(L), encoding="utf-8")

    # --- mcp.md ---
    L = ["# MCP Dependency Statistics", ""]
    L += ["| MCP Server | Agents requiring it |", "|---|---|"]
    for m, c in mcp_counter.most_common():
        L.append(f"| `{m}` | {c} |")
    if not mcp_counter:
        L.append("| _(none)_ | 0 |")
    L.append("")
    (REPORTS / "mcp.md").write_text("\n".join(L), encoding="utf-8")

    # --- repositories.md ---
    L = ["# Repository Import Report", ""]
    L.append("## Repositories contributing agents")
    L.append("")
    L += ["| Repository | Agents |", "|---|---|"]
    for r, c in repo_counter.most_common():
        L.append(f"| {r} | {c} |")
    L.append("")
    L.append("## All discovered repositories")
    L.append("")
    L += ["| Repository | Stars | License | Description |", "|---|---|---|---|"]
    for r in repos:
        L.append(f"| {r['full_name']} | {r.get('stars',0)} | {r.get('license') or '—'} | {(r.get('description') or '')[:70]} |")
    L.append("")
    (REPORTS / "repositories.md").write_text("\n".join(L), encoding="utf-8")

    print(f"Summary: {n} agents, {len(cloned)} repos scanned, {conv_rate}% conversion rate.")
    print("Reports written to reports/ and metadata/summary.json")


if __name__ == "__main__":
    main()
