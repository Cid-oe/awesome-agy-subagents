#!/usr/bin/env python3
"""Assign final repo status and generate coverage + unsupported reports.

Reads metadata/repo_scan.json (produced by scripts/process_all.py) and, for
repos whose source is present in imports/sources/, re-scans them to compute
globally-unique agent body-hashes so that purely-duplicate repos are detected.

Writes:
  metadata/repo_status.json       -- final per-repo classification
  reports/coverage.md             -- discovery & coverage statistics
  reports/unsupported.md          -- why each repo cannot be imported
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agy import SourceInfo  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "imports" / "sources"
META_DIR = ROOT / "metadata"
REPORTS = ROOT / "reports"


def load(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default


def recompute_hashes() -> dict[str, set]:
    """Map each imported repo -> set of agent body-hashes it contributed.

    Derives the mapping from the persisted raw records (metadata/raw_records.json
    plus the per-repo record index metadata/repo_records.json) instead of
    re-scanning the (streamed/deleted) source clones.
    """
    scan = load(META_DIR / "repo_scan.json", {})
    raw = load(META_DIR / "raw_records.json", [])
    idx = load(META_DIR / "repo_records.json", {})
    out: dict[str, set] = {}
    for full, info in scan.items():
        if info.get("status") != "imported":
            continue
        indices = idx.get(full, [])
        hashes = set()
        for i in indices:
            rec = raw[i] if i < len(raw) else None
            if rec and isinstance(rec, dict) and rec.get("body"):
                hashes.add(sha256_of(rec["body"]))
        out[full] = hashes
    return out


def sha256_of(body: str) -> str:
    import hashlib
    t = body.lower()
    import re
    t = re.sub(r"\s+", " ", t).strip()
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def nature_explanation(status: str, nature: str, reason: str) -> str:
    base = reason
    return base


def agy_path_for(nature: str) -> str:
    """Describe what would be required for AGY compatibility given the nature."""
    if nature in ("runtime", "framework", "harness"):
        return ("This repository is a runtime/framework rather than a set of "
                "reusable agents. AGY compatibility would require extracting its "
                "built-in agent/skill definitions into individual AGY subagent "
                "markdown files (name/description frontmatter + system prompt body), "
                "decoupled from its execution engine.")
    if nature == "sdk":
        return ("This is an SDK. To be AGY-compatible, its agent-prompt templates "
                "would need to be lifted into standalone AGY subagent files that "
                "call the SDK via tools/MCP rather than embedding it.")
    if nature == "knowledge-base":
        return ("This is a knowledge base / learning resource. It contains "
                "information about agents but not reusable agent definitions. "
                "AGY compatibility would require authoring new subagents from the "
                "knowledge it documents.")
    if nature == "documentation":
        return ("This is documentation/curated-list content. No agent definitions "
                "are present. To contribute agents, the linked agent files would "
                "need to be imported (they live in other repositories).")
    if nature == "plugin-collection":
        return ("This is a plugin/skill collection. AGY can consume subagents, so "
                "plugins exposing .md frontmatter agents could be imported; "
                "non-frontmatter plugins (executable code) would need a thin "
                "AGY-subagent wrapper.")
    if nature == "application":
        return ("This is an end-user application. It may contain prompts internally, "
                "but they are not published as reusable subagents. AGY compatibility "
                "would require extracting its system prompts into standalone "
                "subagent files.")
    return ("The repository contains no parseable reusable agents in the current "
            "format. AGY compatibility requires converting its prompt definitions "
            "into standard AGY subagent markdown files.")


def main() -> None:
    scan = load(META_DIR / "repo_scan.json", {})
    discovered = load(META_DIR / "discovered_repos.json", [])
    by_name = {r["full_name"]: r for r in discovered}

    hashes = recompute_hashes()
    # Set of body-hashes that survive into the final deduped corpus. A repo is
    # "duplicate" only when none of its raw content survived deduplication (all
    # of it was subsumed by another repository's agent).
    final_agents = load(META_DIR / "agents.json", [])
    final_hashes = {sha256_of(a.get("body", "")) for a in final_agents
                    if a.get("body")}

    statuses: dict[str, dict] = {}
    for full, info in scan.items():
        status = info.get("status", "requires-manual-review")
        reason = info.get("reason", "")
        nature = info.get("nature", "")
        repo_meta = by_name.get(full, {})

        if status == "imported" and full in hashes:
            hs = hashes[full]
            if hs:
                survived = hs & final_hashes
                if not survived:
                    status = "duplicate"
                    reason = ("All extracted agent content was subsumed by "
                              "other repositories during deduplication; "
                              "nothing unique survived.")
                else:
                    reason = f"{len(survived)} unique reusable agent(s) contributed."
            else:
                status = "requires-manual-review"
                reason = "Imported marker but no agents re-derived on re-scan."

        statuses[full] = {
            "status": status,
            "reason": reason,
            "nature": nature,
            "stars": info.get("stars") or repo_meta.get("stars"),
            "license": info.get("license") or repo_meta.get("license"),
            "description": (info.get("description") or
                            (repo_meta.get("description") or "")[:200]),
            "html_url": repo_meta.get("html_url"),
            "clone_url": info.get("clone_url") or repo_meta.get("clone_url"),
        }

    (META_DIR / "repo_status.json").write_text(
        json.dumps(statuses, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    counts = Counter(v["status"] for v in statuses.values())
    n_disc = len(discovered)
    n_class = len(statuses)

    # ---- coverage.md ----
    L = ["# Ecosystem Coverage Report", "",
         f"_Generated {__import__('agy').now_iso()}_", "",
         "## Classification summary", "",
         "| Status | Repositories |", "|---|---|"]
    order = ["imported", "duplicate", "unsupported", "empty", "non-agent",
             "requires-manual-review"]
    for s in order:
        L.append(f"| {s} | {counts.get(s, 0)} |")
    L.append("")
    L.append("## Coverage")
    L.append("")
    L.append(f"- Repositories discovered: **{n_disc}**")
    L.append(f"- Repositories evaluated/classified: **{n_class}**")
    pct = round(100 * n_class / n_disc, 1) if n_disc else 0
    L.append(f"- Evaluation coverage: **{pct}%**")
    L.append(f"- Repositories importing agents: **{counts.get('imported', 0)}**")
    L.append(f"- Repositories remaining (not yet evaluated): **{n_disc - n_class}**")
    L.append("")
    L.append("## Per-status detail")
    L.append("")
    for s in order:
        rows = [(k, v) for k, v in statuses.items() if v["status"] == s]
        if not rows:
            continue
        L.append(f"### {s} ({len(rows)})")
        L.append("")
        L.append("| Repository | Stars | Nature | Reason |")
        L.append("|---|---|---|---|")
        for k, v in sorted(rows, key=lambda kv: -(kv[1].get("stars") or 0)):
            L.append(f"| {k} | {v.get('stars') or '—'} | {v.get('nature') or '—'} | "
                     f"{(v.get('reason') or '')[:90]} |")
        L.append("")
    (REPORTS / "coverage.md").write_text("\n".join(L), encoding="utf-8")

    # ---- unsupported.md ----
    L = ["# Unsupported Repositories", "",
         "Repositories that could not be imported into the AGY ecosystem, with "
         "an explanation of why and what would be required for AGY compatibility.",
         "",
         f"_Generated {__import__('agy').now_iso()}_", ""]
    rows = [(k, v) for k, v in statuses.items()
            if v["status"] in ("unsupported",)]
    L.append(f"Total unsupported: **{len(rows)}**")
    L.append("")
    for k, v in sorted(rows, key=lambda kv: -(kv[1].get("stars") or 0)):
        L.append(f"## {k}")
        L.append("")
        L.append(f"- **Stars:** {v.get('stars') or '—'}  ·  **License:** "
                 f"{v.get('license') or '—'}")
        L.append(f"- **Nature:** `{v.get('nature') or 'unknown'}`")
        L.append(f"- **Link:** {v.get('html_url') or v.get('clone_url') or ''}")
        L.append("")
        L.append(f"### Why it cannot be imported")
        L.append("")
        L.append(f"{v.get('reason') or 'No parseable reusable agents found.'}")
        L.append("")
        L.append("### What would be required for AGY compatibility")
        L.append("")
        L.append(agy_path_for(v.get("nature") or ""))
        L.append("")
    (REPORTS / "unsupported.md").write_text("\n".join(L), encoding="utf-8")

    print(f"Classified {n_class}/{n_disc} repos: {dict(counts)}")
    print("Wrote metadata/repo_status.json, reports/coverage.md, reports/unsupported.md")


if __name__ == "__main__":
    main()
