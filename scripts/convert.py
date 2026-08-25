#!/usr/bin/env python3
"""Scan cloned sources, extract agents, and convert them to canonical AGY format.

Outputs:
  agents/<category>/<name>.md   -- canonical AGY agent files
  metadata/agents.json           -- machine-readable registry of every record
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agy import (  # noqa: E402
    AgentRecord,
    SourceInfo,
    dedupe_records,
    extract_agent,
    iter_agent_files,
    render_agent_markdown,
    validate_record,
    write_json,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "imports" / "sources"
AGENTS_DIR = ROOT / "agents"
META_DIR = ROOT / "metadata"


_LICENSE_BY_REPO: dict[str, str] = {}


def _load_license_map() -> dict[str, str]:
    if _LICENSE_BY_REPO:
        return _LICENSE_BY_REPO
    reg = ROOT / "metadata" / "discovered_repos.json"
    if reg.exists():
        data = json.loads(reg.read_text(encoding="utf-8"))
        for r in data:
            lic = r.get("license")
            if lic:
                _LICENSE_BY_REPO[r["full_name"]] = lic
    return _LICENSE_BY_REPO


def source_info_for(repo_dir: Path, rel: Path) -> SourceInfo:
    repo_name = repo_dir.name.replace("--", "/")
    license_name = _load_license_map().get(repo_name, "")
    if not license_name:
        license_name = _sniff_license(repo_dir)
    return SourceInfo(
        repo=repo_name,
        author=repo_name.split("/")[0],
        license=license_name,
        url=f"https://github.com/{repo_name}",
        path=str(rel),
    )


def _sniff_license(repo_dir: Path) -> str:
    # Best-effort license detection from LICENSE file.
    license_name = ""
    for cand in ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "COPYING"]:
        p = repo_dir / cand
        if p.exists():
            head = p.read_text(encoding="utf-8", errors="replace")[:200].lower()
            if "mit" in head:
                license_name = "MIT"
            elif "apache" in head:
                license_name = "Apache-2.0"
            elif "gnu general public license" in head and "version 3" in head:
                license_name = "GPL-3.0"
            elif "gnu general public license" in head and "version 2" in head:
                license_name = "GPL-2.0"
            elif "bsd" in head:
                license_name = "BSD"
            elif "mozilla public license" in head:
                license_name = "MPL-2.0"
            elif "creative commons" in head:
                license_name = "CC"
            else:
                license_name = cand
            break
    return license_name


def main() -> None:
    if not SOURCES.exists():
        print("No sources. Run scripts/import.py first.", file=sys.stderr)
        sys.exit(1)

    raw_records: list[AgentRecord] = []
    total_files = 0

    for repo_dir in sorted(SOURCES.iterdir()):
        if not repo_dir.is_dir():
            continue
        count = 0
        for f in iter_agent_files(repo_dir):
            total_files += 1
            rel = f.relative_to(repo_dir)
            src = source_info_for(repo_dir, rel)
            rec = extract_agent(f, src, relpath=str(rel))
            if rec is None:
                continue
            # Reject files with no real prompt content.
            if len(rec.body) < 40:
                continue
            raw_records.append(rec)
            count += 1
        if count:
            print(f"  {repo_dir.name}: {count} agents")

    print(f"\nTotal files scanned: {total_files}")
    print(f"Agents extracted (pre-dedupe): {len(raw_records)}")

    records = dedupe_records(raw_records)
    print(f"Unique agents after dedupe: {len(records)}")

    # Write agent files.
    if AGENTS_DIR.exists():
        import shutil
        shutil.rmtree(AGENTS_DIR)
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)

    written = 0
    for rec in records:
        rec.validation = "passed" if not validate_record(rec) else "failed"
        cat_dir = AGENTS_DIR / rec.category
        cat_dir.mkdir(parents=True, exist_ok=True)
        out = cat_dir / f"{rec.name}.md"
        out.write_text(render_agent_markdown(rec), encoding="utf-8")
        written += 1

    print(f"Wrote {written} agents to agents/")

    # Write registry.
    registry = [r.to_dict() for r in records]
    write_json(META_DIR / "agents.json", registry)
    write_json(META_DIR / "dedupe_report.json", {
        "total_before": len(raw_records),
        "total_after": len(records),
        "duplicates_removed": len(raw_records) - len(records),
        "clusters": len(records),
    })
    print(f"Wrote registry to metadata/agents.json")


if __name__ == "__main__":
    main()
