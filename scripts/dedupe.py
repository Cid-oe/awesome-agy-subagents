#!/usr/bin/env python3
"""Detect and merge duplicate agents (re-runnable maintenance step).

Stage 1: exact-duplicate bodies and same-name variants are merged (idempotent).
Stage 2: near-identical cross-name agents (Jaccard >= 0.97, same category) are
         merged, preserving every source.
The canonical set of agent files is rewritten from the merged records.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agy import (  # noqa: E402
    AgentRecord,
    SourceInfo,
    dedupe_records,
    jaccard,
    merge_sources,
    render_agent_markdown,
    tokenize,
    validate_record,
    write_json,
)

ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"
META_DIR = ROOT / "metadata"

NEAR_DUP_THRESHOLD = 0.97


def load_records() -> list[AgentRecord]:
    raw = json.loads((META_DIR / "agents.json").read_text(encoding="utf-8"))
    recs = []
    for d in raw:
        recs.append(AgentRecord(
            name=d["name"], description=d["description"], body=d["body"],
            category=d.get("category", "general"), tags=d.get("tags", []),
            model=d.get("model", "inherit"), kind=d.get("kind", "local"),
            temperature=d.get("temperature"), max_turns=d.get("max_turns"),
            timeout_mins=d.get("timeout_mins"), tools=d.get("tools", []),
            required_tools=d.get("required_tools", []),
            optional_tools=d.get("optional_tools", []),
            mcp_servers=d.get("mcp_servers", []),
            examples=d.get("examples", []),
            sources=[SourceInfo(**s) for s in d.get("sources", [])],
            compatibility=d.get("compatibility", "fully-compatible"),
            compatibility_notes=d.get("compatibility_notes", ""),
            validation=d.get("validation", "pending"),
            imported=d.get("imported", ""),
        ))
    return recs


def main() -> None:
    recs = load_records()
    total_before = len(recs)

    # Stage 1: exact + same-name (idempotent).
    recs = dedupe_records(recs)
    after_name = len(recs)

    # Stage 2: near-identical cross-name merges.
    merged_out: list[AgentRecord] = []
    removed = 0
    for i, rec in enumerate(recs):
        absorbed = False
        for j, other in enumerate(merged_out):
            if rec.category != other.category:
                continue
            if len(rec.body) < 120 or len(other.body) < 120:
                continue
            if jaccard(tokenize(rec.body), tokenize(other.body)) >= NEAR_DUP_THRESHOLD:
                merge_sources(other, rec)
                removed += 1
                absorbed = True
                break
        if not absorbed:
            merged_out.append(rec)

    print(f"Loaded {total_before}; after exact/name dedupe {after_name}; "
          f"after near-dup merge {len(merged_out)} (removed {removed}).")

    # Rewrite canonical files.
    shutil.rmtree(AGENTS_DIR, ignore_errors=True)
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for rec in merged_out:
        rec.validation = "passed" if not validate_record(rec) else "failed"
        (AGENTS_DIR / rec.category).mkdir(exist_ok=True)
        (AGENTS_DIR / rec.category / f"{rec.name}.md").write_text(
            render_agent_markdown(rec), encoding="utf-8")

    write_json(META_DIR / "agents.json", [r.to_dict() for r in merged_out])
    write_json(META_DIR / "dedupe_report.json", {
        "total_before": total_before,
        "total_after": len(merged_out),
        "duplicates_removed": total_before - len(merged_out),
        "clusters": len(merged_out),
    })
    print("Registry, dedupe report, and agent files updated.")


if __name__ == "__main__":
    main()
