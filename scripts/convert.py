#!/usr/bin/env python3
"""Scan cloned sources and extract agents into raw records.

Outputs:
  metadata/raw_records.json -- raw (pre-dedupe) AgentRecord dicts for every
                               reusable agent found in imports/sources/.

When the cloned sources are absent (e.g. they were streamed & deleted by
scripts/process_all.py), this step is a no-op — the raw records will already
have been accumulated into metadata/raw_records.json by the streaming pipeline.
The deduped canonical set is produced by scripts/finalize.py.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agy import extract_repo_records, write_json  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "imports" / "sources"
META_DIR = ROOT / "metadata"
RAW_OUT = META_DIR / "raw_records.json"


def main() -> None:
    if not SOURCES.exists():
        print("No imports/sources. If process_all.py streamed records, "
              "raw_records.json is already populated; skipping scan.")
        return

    raw_records: list[dict] = []
    total_files = 0
    for repo_dir in sorted(SOURCES.iterdir()):
        if not repo_dir.is_dir():
            continue
        repo_name = repo_dir.name.replace("--", "/")
        recs = extract_repo_records(repo_dir, repo_name)
        raw_records.extend(r.to_dict() for r in recs)
        total_files += len(recs)
        if recs:
            print(f"  {repo_dir.name}: {len(recs)} agents")

    write_json(RAW_OUT, raw_records)
    print(f"\nExtracted {len(raw_records)} raw agents to {RAW_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
