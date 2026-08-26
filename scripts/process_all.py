#!/usr/bin/env python3
"""Clone, scan and classify EVERY discovered repository (resumable).

This is the ecosystem-coverage workhorse. For each repository in
metadata/discovered_repos.json it:

  1. Shallow-clones it into imports/sources/<owner>--<repo>/ (git-ignored).
  2. Scans recursively for candidate agent definitions (all supported formats
     and locations, using the same logic as convert.py).
  3. Extracts/parses them to determine how many are real, reusable agents.
  4. Records per-repo stats and assigns a coarse classification.

Every repository ends up classified as one of:

    Imported                 -- contains reusable agents that were converted
    Duplicate                -- agent content entirely duplicates existing agents
    Unsupported              -- agent-related content in a non-convertible format
    Empty                    -- agent structure but no usable prompt content
    Non-agent repository     -- no reusable subagents (docs/framework/app/etc.)
    Requires manual review   -- could not be auto-classified (clone/parse issues)

Progress is persisted to metadata/repo_scan.json so the run is resumable; a
follow-up pass (scripts/classify.py) assigns the final status.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agy import (  # noqa: E402
    SourceInfo,
    extract_agent,
    extract_repo_records,
    iter_agent_files,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "imports" / "sources"
META_DIR = ROOT / "metadata"
SCAN_OUT = META_DIR / "repo_scan.json"
CLONED_OUT = META_DIR / "cloned_repos.json"
RAW_OUT = META_DIR / "raw_records.json"


def slug_name(full_name: str) -> str:
    return full_name.replace("/", "--")


def load(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default


def gh_clone(repo: dict, dest: Path) -> tuple[bool, str]:
    """Shallow clone; returns (ok, error_message)."""
    try:
        r = subprocess.run(
            ["git", "clone", "--depth", "1", repo["clone_url"], str(dest)],
            capture_output=True, text=True, timeout=300,
        )
    except subprocess.TimeoutExpired:
        return False, "clone-timeout"
    if r.returncode != 0:
        err = (r.stderr or r.stdout or "").strip().splitlines()
        return False, (err[-1] if err else "clone-failed")[:200]
    return True, ""


def write_atomic(path: Path, data: dict) -> None:
    """Write JSON atomically so a crash never leaves a corrupt file."""
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)


def repo_nature(repo: dict) -> str:
    """Infer repository nature from description/topics for non-agent repos."""
    text = " ".join([
        repo.get("description") or "",
        " ".join(repo.get("topics", [])),
        repo.get("full_name", ""),
    ]).lower()
    rules = [
        ("runtime", ["runtime", "agent harness", "meta-harness", "orchestration", "framework", "sdk", "sdk ", "cli tool", "harness"]),
        ("framework", ["framework", "agent framework", "build your own", "sdk"]),
        ("knowledge-base", ["knowledge base", "wiki", "kb ", "notes", "notebook", "book ", "learn ", "tutorial", "course", "guide", "how-to"]),
        ("documentation", ["documentation", "docs", "reference", "cheat sheet", "blog", "awesome list", "curated list", "resources", "collection"]),
        ("plugin-collection", ["plugin", "plugin collection", "plugins", "extension", "marketplace", "registry", "package"]),
        ("application", ["app", "application", "tool", "desktop", "webapp", "dashboard", "website"]),
        ("model", ["llm", "model", "weights", "dataset", "fine-tune", "training"]),
    ]
    for name, kws in rules:
        if any(k in text for k in kws):
            return name
    return "unknown"


def classify_candidates(repo: dict, candidates, extracted, empty, parse_fail) -> tuple[str, str]:
    """Return (status, reason)."""
    if extracted > 0:
        return "imported", f"{extracted} reusable agent(s) extracted"
    if empty > 0:
        return "empty", f"{empty} agent shell(s) found but no usable prompt content"
    if parse_fail > 0:
        return "unsupported", f"{parse_fail} candidate(s) present but none parse into agents"
    if candidates > 0:
        return "unsupported", f"{candidates} candidate file(s) present but none are reusable agents"
    nature = repo_nature(repo)
    return "non-agent", f"no reusable agents; nature: {nature}"


def main() -> None:
    limit = 0  # 0 = all
    args = sys.argv[1:]
    if args and args[0].isdigit():
        limit = int(args[0])

    repos = load(META_DIR / "discovered_repos.json", [])
    scan = load(SCAN_OUT, {})
    cloned = load(CLONED_OUT, {})
    raw_records = load(RAW_OUT, [])
    if not isinstance(raw_records, list):
        raw_records = []
    SOURCES.mkdir(parents=True, exist_ok=True)
    # Track repo -> list of raw record indices contributed, for duplicate logic.
    repo_record_idx: dict[str, list[int]] = load(
        META_DIR / "repo_records.json", {})

    # Which repos still need work?
    pending = []
    for repo in repos:
        full = repo["full_name"]
        if full in scan:
            continue
        pending.append(repo)
    if limit:
        pending = pending[:limit]

    print(f"Discovered: {len(repos)}  Already scanned: {len(scan)}  "
          f"Pending: {len(pending)}  Processing this run: {min(limit, len(pending)) if limit else len(pending)}")

    t_start = time.time()
    ok = fail = 0
    for repo in pending:
        full = repo["full_name"]
        slug = slug_name(full)
        dest = SOURCES / slug

        # 1. clone
        if not (dest / ".git").exists():
            cloned_ok, err = gh_clone(repo, dest)
            if not cloned_ok:
                scan[full] = {
                    "status": "requires-manual-review",
                    "reason": err,
                    "candidate_files": 0, "extracted": 0,
                    "empty": 0, "parse_fail": 0,
                    "nature": repo_nature(repo),
                }
                fail += 1
                continue
            cloned[full] = {
                "full_name": full,
                "stars": repo.get("stars"),
                "license": repo.get("license"),
                "path": str(dest.relative_to(ROOT)),
            }
            CLONED_OUT.write_text(json.dumps(cloned, indent=2), encoding="utf-8")

        # 2. scan
        candidates = []
        try:
            candidates = list(iter_agent_files(dest))
        except Exception as e:
            scan[full] = {"status": "requires-manual-review", "reason": f"scan-error: {e}",
                          "candidate_files": 0, "extracted": 0, "empty": 0,
                          "parse_fail": 0, "nature": repo_nature(repo)}
            fail += 1
            continue

        extracted = empty = parse_fail = 0
        license_name = repo.get("license") or ""
        for f in candidates:
            rel = f.relative_to(dest)
            src = SourceInfo(repo=full, author=full.split("/")[0],
                             license=license_name, url=f"https://github.com/{full}",
                             path=str(rel))
            try:
                rec = extract_agent(f, src, relpath=str(rel))
            except Exception:
                parse_fail += 1
                continue
            if rec is None:
                parse_fail += 1
                continue
            if len(rec.body) < 40:
                empty += 1
            else:
                extracted += 1

        status, reason = classify_candidates(
            repo, len(candidates), extracted, empty, parse_fail)
        scan[full] = {
            "status": status, "reason": reason,
            "candidate_files": len(candidates), "extracted": extracted,
            "empty": empty, "parse_fail": parse_fail,
            "nature": repo_nature(repo),
            "stars": repo.get("stars"),
            "license": license_name,
            "description": (repo.get("description") or "")[:200],
            "clone_url": repo.get("clone_url"),
        }
        # Convert imported repos to raw records now (keeps disk bounded).
        start_idx = len(raw_records)
        if status == "imported" and (dest / ".git").exists():
            for rec in extract_repo_records(dest, full, license_name):
                raw_records.append(rec.to_dict())
            repo_record_idx[full] = list(range(start_idx, len(raw_records)))
            ok += 1
        else:
            fail += 1
        print(f"  [{status}] {full}  cand={len(candidates)} ext={extracted} "
              f"empty={empty} parse_fail={parse_fail}")
        # Stream: always drop the clone after scanning (records are persisted).
        if (dest / ".git").exists():
            try:
                shutil.rmtree(dest, ignore_errors=True)
            except Exception:
                pass
            if full in cloned:
                del cloned[full]
        if len(scan) % 5 == 0:
            write_atomic(SCAN_OUT, scan)
            write_atomic(RAW_OUT, raw_records)
            write_atomic(META_DIR / "repo_records.json", repo_record_idx)
            CLONED_OUT.write_text(json.dumps(cloned, indent=2), encoding="utf-8")
            elapsed = time.time() - t_start
            rate = len(scan) / max(elapsed, 0.001)
            print(f"  ... checkpoint {len(scan)} scanned, {elapsed:.0f}s, "
                  f"{rate:.2f} repos/s, raw={len(raw_records)}")

    write_atomic(SCAN_OUT, scan)
    write_atomic(RAW_OUT, raw_records)
    write_atomic(META_DIR / "repo_records.json", repo_record_idx)
    CLONED_OUT.write_text(json.dumps(cloned, indent=2), encoding="utf-8")
    print(f"\nDone. Scanned {len(scan)}/{len(repos)} repos "
          f"(imported-ish {sum(1 for v in scan.values() if v['status']=='imported')}).")


if __name__ == "__main__":
    main()
