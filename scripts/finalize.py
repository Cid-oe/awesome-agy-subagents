#!/usr/bin/env python3
"""Deduplicate raw records and write the canonical AGY agent set.

Reads metadata/raw_records.json (list of AgentRecord dicts), applies the same
deduplication used by the legacy convert.py (exact-body, same-name/category,
cross-name near-duplicate), then writes:

  agents/<category>/<name>.md  -- canonical AGY agent files
  metadata/agents.json          -- machine-readable registry
  metadata/dedupe_report.json   -- deduplication statistics
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
RAW = META_DIR / "raw_records.json"
NEAR_DUP_THRESHOLD = 0.97


def load_records() -> list[AgentRecord]:
    raw = json.loads(RAW.read_text(encoding="utf-8"))
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
    if not RAW.exists():
        print("No metadata/raw_records.json. Run scripts/process_all.py or "
              "scripts/convert.py first.", file=sys.stderr)
        sys.exit(1)

    recs = load_records()
    total_before = len(recs)

    # Stage 1: exact-body + same-name/category merge + name disambiguation.
    recs = dedupe_records(recs)
    after_name = len(recs)

    # Stage 2: near-identical cross-name merges. A cheap body-length prefilter
    # (integer compares) avoids tokenizing every pair, so only near-length
    # prompts pay for the expensive Jaccard computation.
    merged_out: list[AgentRecord] = []
    removed = 0
    for rec in recs:
        absorbed = False
        for other in merged_out:
            if rec.category != other.category:
                continue
            if len(rec.body) < 120 or len(other.body) < 120:
                continue
            if abs(len(rec.body) - len(other.body)) > max(40, len(other.body) * 0.05):
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

    shutil.rmtree(AGENTS_DIR, ignore_errors=True)
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for rec in merged_out:
        rec.validation = "passed" if not validate_record(rec) else "failed"
        (AGENTS_DIR / rec.category).mkdir(parents=True, exist_ok=True)
        (AGENTS_DIR / rec.category / f"{rec.name}.md").write_text(
            render_agent_markdown(rec), encoding="utf-8")

    write_json(META_DIR / "agents.json", [r.to_dict() for r in merged_out])
    write_json(META_DIR / "dedupe_report.json", {
        "total_before": total_before,
        "total_after": len(merged_out),
        "duplicates_removed": total_before - len(merged_out),
        "clusters": len(merged_out),
    })
    print(f"Wrote {len(merged_out)} agents to agents/ and metadata/agents.json")


if __name__ == "__main__":
    main()
