#!/usr/bin/env python3
"""Validate every converted agent against the AGY specification.

Checks frontmatter completeness, name-slug validity, category membership, and
prompt presence. Writes metadata/validation_report.json and a human-readable
markdown report to reports/validation.md.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agy import validate_record, write_json  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
META_DIR = ROOT / "metadata"
REPORTS = ROOT / "reports"


def main() -> None:
    raw = json.loads((META_DIR / "agents.json").read_text(encoding="utf-8"))
    results = []
    for d in raw:
        # Reconstruct minimal record for validation.
        from agy import AgentRecord
        rec = AgentRecord(
            name=d["name"], description=d.get("description", ""),
            body=d.get("body", ""), category=d.get("category", "general"),
        )
        errors = validate_record(rec)
        results.append({"name": d["name"], "category": rec.category,
                        "errors": errors, "valid": not errors})

    valid = [r for r in results if r["valid"]]
    invalid = [r for r in results if not r["valid"]]
    error_counts = Counter(e for r in results for e in r["errors"])

    write_json(META_DIR / "validation_report.json", {
        "total": len(results),
        "valid": len(valid),
        "invalid": len(invalid),
        "error_counts": dict(error_counts),
        "failures": invalid,
    })

    REPORTS.mkdir(parents=True, exist_ok=True)
    lines = ["# AGY Validation Report", ""]
    lines.append(f"- Total agents validated: **{len(results)}**")
    lines.append(f"- Valid: **{len(valid)}**")
    lines.append(f"- Invalid: **{len(invalid)}**")
    lines.append("")
    if error_counts:
        lines.append("## Error distribution")
        lines.append("")
        for e, c in error_counts.most_common():
            lines.append(f"- `{e}`: {c}")
        lines.append("")
    if invalid:
        lines.append("## Invalid agents")
        lines.append("")
        lines.append("| Agent | Category | Errors |")
        lines.append("|---|---|---|")
        for r in invalid:
            lines.append(f"| {r['name']} | {r['category']} | {', '.join(r['errors'])} |")
        lines.append("")
    (REPORTS / "validation.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Validated {len(results)} agents ({len(valid)} valid, {len(invalid)} invalid).")
    print(f"Reports: metadata/validation_report.json, reports/validation.md")


if __name__ == "__main__":
    main()
