#!/usr/bin/env python3
"""Run the full AGY import pipeline end-to-end.

    python3 scripts/run_all.py [--discover] [--clone] [--convert] [--dedupe]
                               [--validate] [--report] [--export]

Runs every stage in order by default. Use flags to run only specific stages
(for scheduled re-runs / maintenance).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGES = [
    ("discover", "scripts/discover.py"),
    ("process", "scripts/process_all.py"),
    ("convert", "scripts/convert.py"),
    ("finalize", "scripts/finalize.py"),
    ("classify", "scripts/classify.py"),
    ("validate", "scripts/validate.py"),
    ("report", "scripts/report.py"),
    ("export", "scripts/export.py"),
]


def main() -> None:
    args = sys.argv[1:]
    run_all = not any(a.startswith("--") for a in args)
    enabled = {name for name, _ in STAGES if run_all or f"--{name}" in args}

    for name, script in STAGES:
        if name not in enabled:
            print(f"[skip] {name}")
            continue
        print(f"\n===== {name} =====")
        r = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT)
        if r.returncode != 0:
            print(f"[fail] {name} exited with {r.returncode}", file=sys.stderr)
            sys.exit(r.returncode)
    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
