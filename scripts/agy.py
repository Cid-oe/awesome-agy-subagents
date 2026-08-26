#!/usr/bin/env python3
"""
AGY ecosystem core library.

AGY is the Antigravity CLI (``agy``) subagent format: a Markdown file whose body
is the system prompt and whose YAML frontmatter carries the runtime
configuration (name, description, model, tools, mcpServers, ...).

This module implements discovery, scanning, parsing, conversion, categorization,
deduplication, validation and reporting for converting agents from other
harnesses (Claude Code, Codex, Cursor, Gemini CLI, Pi, OpenCode, ...) into the
canonical AGY format.
"""

from __future__ import annotations

import json
import re
import hashlib
import os
import sys
import datetime
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #

AGY_VERSION = "1.0.0"

CATEGORIES = [
    "backend",
    "frontend",
    "security",
    "devops",
    "infrastructure",
    "ai",
    "research",
    "writing",
    "data",
    "database",
    "testing",
    "architecture",
    "performance",
    "accessibility",
    "documentation",
    "productivity",
    "mobile",
    "game-development",
    "cloud",
    "networking",
    "ci-cd",
    "linux",
    "windows",
    "embedded",
    "machine-learning",
    "prompt-engineering",
    "general",
]

# AGY runtime frontmatter fields (top-level keys that map to the runtime).
RUNTIME_FIELDS = [
    "name",
    "description",
    "kind",
    "model",
    "temperature",
    "max_turns",
    "timeout_mins",
    "tools",
    "mcpServers",
]

# Tool mapping: canonical AGY tool name -> set of foreign spellings.
TOOL_MAP: dict[str, set[str]] = {
    "read_file": {"read", "readfile", "view_file", "viewfile", "cat", "read_file"},
    "write_file": {"write", "writefile", "save_file", "create_file", "write_file"},
    "edit_file": {"edit", "multiedit", "str_replace_editor", "replacetext",
                  "replace_in_file", "notebookedit", "edit_file", "apply_patch"},
    "grep": {"grep", "search_content", "searchcontent", "ripgrep", "rg", "content_search"},
    "glob": {"glob", "globtool", "search_file", "find_file", "list_files", "filesearch"},
    "list_dir": {"ls", "listdir", "list_directory", "list_dir", "read_dir"},
    "run_shell_command": {"bash", "shell", "run_command", "runcommand", "exec",
                          "terminal", "run_shell_command", "command"},
    "web_search": {"websearch", "web_search", "search_web", "brave_search", "tavily"},
    "web_fetch": {"webfetch", "web_fetch", "fetch_url", "read_url", "browse", "puppeteer"},
    "todo": {"todowrite", "todo_write", "todolist", "tasklist", "todo"},
    "mcp": {"mcp", "mcp__", "mcp_"},
}

# Tools that imply subagent recursion, which AGY subagents do not support.
# These are intentionally left unmapped so they surface as needs-tool-mapping.
UNSUPPORTED_TOOL_SPELLINGS = {"task", "agent", "subagent", "spawn", "delegate",
                              "task_agent", "launch_agent"}

# Reverse lookup: foreign tool -> canonical.
_FOREIGN_TO_CANON: dict[str, str] = {}
for _canon, _spellings in TOOL_MAP.items():
    for _s in _spellings:
        _FOREIGN_TO_CANON[_s.lower()] = _canon

# Compatibility statuses.
STATUS_FULLY = "fully-compatible"
STATUS_TOOLMAP = "needs-tool-mapping"
STATUS_MCP = "requires-mcp"
STATUS_MANUAL = "requires-manual-conversion"
STATUS_UNSUPPORTED = "unsupported"

# Directory patterns that indicate a file is an agent definition.
AGENT_PATH_PATTERNS = [
    r"(^|/)agents?/",            # agents/ or agent/
    r"\.claude/agents?/",
    r"\.gemini/agents?/",
    r"\.codex/agents?/",
    r"\.cursor/agents?/",
    r"\.opencode/agents?/",
    r"\.agents/",
    r"\.pi/agents?/",
    r"plugins/.*/agents?/",
    r"subagents?/",
    r"\.augment/agents?/",
]

# Patterns to skip entirely (skills/commands/references are not subagents).
SKIP_PATH_PATTERNS = [
    r"node_modules",
    r"\.git/",
    r"__pycache__",
    r"\.venv",
    r"vendor/",
    r"dist/",
    r"build/",
    r"\.next",
    r"site-packages",
    r"/skills/",
    r"/commands/",
    r"/references/",
    r"/examples/",
    r"/docs/",
    r"/doc/",
    r"/test/",
    r"/tests/",
    r"/templates/",
    r"/agent-memory/",
    r"/memory/",
    r"/tasks/",
    r"/rules/",
    r"/assets/",
    r"/playbooks/",
    r"/bench/",
    r"/adapters/",
    r"Testing Framework",
    r"Test Framework",
    r"/test-fixtures/",
    r"/fixtures/",
]

SKIP_FILENAMES = {
    "readme.md", "contributing.md", "license.md", "license", "licence",
    "licence.md", "copying", "changelog.md", "changelog", "skill.md",
    "memory.md", "claude.md", "agents.md", "security.md", "code_of_conduct.md",
    "index.md", "toc.md",
}

# Agent-signal frontmatter fields (beyond name/description) that indicate the
# file is an agent definition rather than a skill/command/doc.
AGENT_SIGNAL_FIELDS = {
    "tools", "model", "kind", "color", "emoji", "vibe", "temperature",
    "max_turns", "timeout_mins", "mcpServers", "mcp_servers", "system",
    "system_prompt", "agent", "personality", "role",
}


# --------------------------------------------------------------------------- #
# Utilities
# --------------------------------------------------------------------------- #

def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "agent"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def norm_body(text: str) -> str:
    """Normalize prompt body for exact-duplicate detection."""
    t = text.lower()
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def read_json(path: Path, default: Any) -> Any:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# --------------------------------------------------------------------------- #
# Data model
# --------------------------------------------------------------------------- #

@dataclass
class SourceInfo:
    repo: str
    author: str = ""
    license: str = ""
    url: str = ""
    path: str = ""
    format: str = "markdown-frontmatter"


@dataclass
class AgentRecord:
    name: str
    description: str
    body: str  # system prompt
    category: str = "general"
    tags: list[str] = field(default_factory=list)
    model: str = "inherit"
    kind: str = "local"
    temperature: Optional[float] = None
    max_turns: Optional[int] = None
    timeout_mins: Optional[int] = None
    tools: list[str] = field(default_factory=list)
    required_tools: list[str] = field(default_factory=list)
    optional_tools: list[str] = field(default_factory=list)
    mcp_servers: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)
    sources: list[SourceInfo] = field(default_factory=list)
    compatibility: str = STATUS_FULLY
    compatibility_notes: str = ""
    validation: str = "pending"
    imported: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        return d

    @property
    def body_hash(self) -> str:
        return sha256(norm_body(self.body))


# --------------------------------------------------------------------------- #
# Frontmatter parsing
# --------------------------------------------------------------------------- #

def _strip_yaml(value: Any) -> Any:
    return value


def parse_markdown_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return (frontmatter dict, body)."""
    # Some exporters indent the entire file (frontmatter included). Dedent.
    first_nonblank = next((ln for ln in text.split("\n") if ln.strip()), None)
    if first_nonblank is not None and first_nonblank.lstrip().startswith("---") \
            and first_nonblank != first_nonblank.lstrip():
        import textwrap
        text = textwrap.dedent(text)
    text = text.lstrip("\n")
    if not text.startswith("---"):
        return {}, text
    # Find closing fence.
    m = re.match(r"^---\s*\n", text)
    if not m:
        return {}, text
    rest = text[m.end():]
    end = re.search(r"^---\s*$", rest, re.MULTILINE)
    if not end:
        return {}, text
    fm_raw = rest[:end.start()]
    body = rest[end.end():].lstrip("\n")
    data: dict[str, Any] = {}
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(fm_raw) or {}
    except Exception:
        # Fallback: minimal key: value parser.
        for line in fm_raw.splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip()
    if not isinstance(data, dict):
        data = {}
    return data, body


def parse_toml(text: str) -> dict[str, Any]:
    import tomllib
    return tomllib.loads(text)


def parse_json(text: str) -> dict[str, Any]:
    return json.loads(text)


# --------------------------------------------------------------------------- #
# Tool mapping
# --------------------------------------------------------------------------- #

def map_tools(raw_tools: list[str]) -> tuple[list[str], list[str]]:
    """Return (mapped_tools, unmapped_tools)."""
    mapped: list[str] = []
    unmapped: list[str] = []
    for t in raw_tools:
        key = t.lower()
        if key in ("*", "all"):
            mapped.append("all")
            continue
        # MCP tool wildcards.
        if key.startswith("mcp__"):
            mapped.append(key)
            continue
        # Subagent-recursion tools are unsupported in AGY -> leave unmapped.
        if key in UNSUPPORTED_TOOL_SPELLINGS:
            unmapped.append(t)
            continue
        canon = _FOREIGN_TO_CANON.get(key)
        if canon:
            mapped.append(canon)
        else:
            unmapped.append(t)
    # de-dupe preserving order
    seen = set()
    out = [x for x in mapped if not (x in seen or seen.add(x))]
    return out, unmapped


# --------------------------------------------------------------------------- #
# Categorization
# --------------------------------------------------------------------------- #

_CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "backend": ["backend", "api", "server", "graphql", "rest", "microservice", "restful"],
    "frontend": ["frontend", "ui", "ux", "design", "react", "vue", "angular", "css",
                 "tailwind", "component", "web design", "front-end", "front end"],
    "security": ["security", "pentest", "vulnerab", "exploit", "audit", "threat",
                 "auth", "secops", "red team", "blue team", "cve", "sql injection",
                 "xss", "reverse engineering", "malware", "crypto"],
    "devops": ["devops", "sre", "incident", "monitoring", "observability", "on-call",
               "runbook", "reliability"],
    "infrastructure": ["infrastructure", "infra", "terraform", "iac", "platform",
                       "provisioning", "config management"],
    "ai": ["ai ", "llm", "agent", "gpt", "prompt", "rag", "chatbot", "nlp", "llmops",
           "orchestration", "copilot"],
    "research": ["research", "analysis", "analyst", "investigat", "survey", "literature"],
    "writing": ["writing", "writer", "copy", "content", "blog", "article", "editor",
                "proofread", "seo content", "marketing copy", "documentation",
                "story", "novel", "translate", "translation"],
    "data": ["data engineer", "data pipeline", "etl", "analytics", "big data",
             "spark", "databricks", "airflow", "data warehouse", "data scien"],
    "database": ["database", "postgres", "mysql", "sql", "nosql", "mongodb",
                 "redis", "dba", "migration", "schema"],
    "testing": ["test", "qa", "quality", "tdd", "cypress", "playwright", "unit test",
                "debug", "debugger"],
    "architecture": ["architecture", "architect", "design pattern", "c4", "uml",
                     "system design", "domain-driven", "ddd"],
    "performance": ["performance", "optimiz", "benchmark", "profiling", "latency",
                    "scaling", "load test"],
    "accessibility": ["accessibility", "a11y", "wcag", "screen reader", "inclusive"],
    "documentation": ["documentation", "docs", "readme", "technical writing"],
    "productivity": ["productivity", "workflow", "automation", "task", "todo",
                     "planning", "meeting", "notes"],
    "mobile": ["mobile", "android", "ios", "react native", "flutter", "swift",
               "kotlin", "expo"],
    "game-development": ["game", "unity", "unreal", "godot", "gameplay", "game dev"],
    "cloud": ["cloud", "aws", "azure", "gcp", "google cloud", "serverless", "lambda",
              "cloudformation"],
    "networking": ["network", "networking", "dns", "tcp", "firewall", "router",
                   "proxy", "load balancer"],
    "ci-cd": ["ci/cd", "ci-cd", "cicd", "pipeline", "jenkins", "github action",
              "gitlab", "deployment", "release", "circleci"],
    "linux": ["linux", "bash", "shell", "ubuntu", "debian", "systemd", "nix"],
    "windows": ["windows", "powershell", "dotnet", ".net", "c#", "active directory",
                "msbuild"],
    "embedded": ["embedded", "microcontroller", "arduino", "raspberry", "firmware",
                 "iot", "rtos", "arm", "cortex"],
    "machine-learning": ["machine learning", "ml ", "deep learning", "neural",
                         "pytorch", "tensorflow", "training", "finetune", "fine-tune",
                         "inference", "mlops"],
    "prompt-engineering": ["prompt engineering", "prompt engineer", "prompting",
                           "system prompt", "few-shot"],
    "general": [],
}


def categorize(name: str, description: str, body: str, tags: list[str]) -> str:
    text = f"{name} {description} {' '.join(tags)}".lower()
    scores: dict[str, int] = {}
    for cat, kws in _CATEGORY_KEYWORDS.items():
        score = 0
        for kw in kws:
            if kw in text:
                score += 1 + (3 if kw in name.lower() else 0)
        scores[cat] = score
    # Also scan body head for strong signals.
    body_head = body[:3000].lower()
    best = "general"
    best_score = 0
    for cat, score in scores.items():
        if score > best_score:
            best, best_score = cat, score
    if best_score == 0:
        # fall back to body scan
        for cat, kws in _CATEGORY_KEYWORDS.items():
            if any(kw in body_head for kw in kws):
                return cat
    return best


# --------------------------------------------------------------------------- #
# Scanning
# --------------------------------------------------------------------------- #

def iter_agent_files(root: Path):
    """Yield Path objects that look like agent definitions."""
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = str(p)
        if any(re.search(pat, rel) for pat in SKIP_PATH_PATTERNS):
            continue
        if p.name.lower() in SKIP_FILENAMES:
            continue
        if p.suffix.lower() not in (".md", ".markdown", ".toml", ".yaml", ".yml", ".json"):
            continue
        if p.suffix.lower() in (".yaml", ".yml", ".json") and not any(
            re.search(pat, rel) for pat in AGENT_PATH_PATTERNS
        ):
            # Only treat yaml/json as agents if under an agent dir.
            continue
        yield p


def is_agent_path(rel: str) -> bool:
    return any(re.search(pat, rel) for pat in AGENT_PATH_PATTERNS)


# --------------------------------------------------------------------------- #
# Conversion
# --------------------------------------------------------------------------- #

def extract_agent(path: Path, source: SourceInfo, relpath: str | None = None) -> Optional[AgentRecord]:
    """Parse a single file into an AgentRecord, or None if not an agent."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    if relpath is None:
        relpath = str(path)
    if not text.strip():
        return None

    suffix = path.suffix.lower()
    fm: dict[str, Any] = {}
    body = text

    if suffix in (".md", ".markdown"):
        fm, body = parse_markdown_frontmatter(text)
        source.format = "markdown-frontmatter"
    elif suffix == ".toml":
        try:
            fm = parse_toml(text)
        except Exception:
            return None
        source.format = "toml"
        body = fm.get("developer_instructions") or fm.get("prompt") or fm.get(
            "system_prompt") or fm.get("instructions") or ""
    elif suffix in (".yaml", ".yml"):
        try:
            import yaml
            fm = yaml.safe_load(text) or {}
        except Exception:
            return None
        source.format = "yaml"
        if isinstance(fm, dict):
            body = fm.get("prompt") or fm.get("system_prompt") or fm.get("instructions") or ""
    elif suffix == ".json":
        try:
            fm = json.loads(text)
        except Exception:
            return None
        source.format = "json"
        if isinstance(fm, dict):
            body = fm.get("prompt") or fm.get("system_prompt") or fm.get("instructions") or ""

    # Body from structured formats may be a non-string (int/bool/list).
    if not isinstance(body, str):
        body = str(body) if body is not None else ""

    if not isinstance(fm, dict):
        fm = {}

    # Some sources nest under "agent" or "config".
    for key in ("agent", "subagent", "config"):
        if isinstance(fm.get(key), dict) and "name" in fm.get(key, {}):
            fm = {**fm, **fm[key]}

    # ------------------------------------------------------------------ #
    # Agent-ness determination: reject skills/commands/docs/plain files.
    # ------------------------------------------------------------------ #
    under_agent_path = is_agent_path(relpath)
    signal = AGENT_SIGNAL_FIELDS & set(fm.keys())
    fm_name = str(fm.get("name") or "").strip()
    fm_desc = str(fm.get("description") or "").strip()
    if not under_agent_path:
        # Only import non-agent-path files that look like real agents.
        if not fm_name and not fm_desc:
            return None
        if not signal:
            return None
        if not fm_desc:
            return None

    name = fm_name or path.stem
    description = fm_desc
    if not description and body.strip():
        # Fallback to first non-heading paragraph.
        for line in body.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                description = line
                break

    if not body.strip() and not description:
        return None
    if not body.strip():
        # A description-only file is not a usable agent prompt.
        return None

    tools_raw = fm.get("tools") or []
    if isinstance(tools_raw, str):
        tools_raw = [x.strip() for x in tools_raw.replace(",", " ").split() if x.strip()]
    if not isinstance(tools_raw, list):
        tools_raw = []

    mapped_tools, unmapped = map_tools(list(tools_raw))

    mcp_servers = []
    mcp_cfg = fm.get("mcpServers") or fm.get("mcp_servers") or fm.get("mcp") or {}
    if isinstance(mcp_cfg, dict):
        mcp_servers = list(mcp_cfg.keys())
    elif isinstance(mcp_cfg, list):
        mcp_servers = [str(x) for x in mcp_cfg]

    # Detect MCP tool references in tools list.
    for t in list(tools_raw):
        if t.lower().startswith("mcp__"):
            srv = t[5:].split("__")[0]
            if srv and srv not in mcp_servers:
                mcp_servers.append(srv)

    # Compatibility.
    if not fm:
        status = STATUS_MANUAL
        note = "No frontmatter/metadata detected; prompt extracted from raw text."
    elif mcp_servers:
        status = STATUS_MCP
        note = f"Requires MCP servers: {', '.join(mcp_servers)}."
    elif unmapped:
        status = STATUS_TOOLMAP
        note = f"Unmapped tools: {', '.join(unmapped)}."
    else:
        status = STATUS_FULLY
        note = "Converted directly; no manual steps required."

    rec = AgentRecord(
        name=slugify(name),
        description=description,
        body=body.strip(),
        model=str(fm.get("model") or fm.get("modelName") or "inherit"),
        kind=str(fm.get("kind") or "local"),
        temperature=fm.get("temperature"),
        max_turns=fm.get("max_turns") or fm.get("maxTurns"),
        timeout_mins=fm.get("timeout_mins") or fm.get("timeoutMins"),
        tools=mapped_tools,
        required_tools=mapped_tools,
        optional_tools=[],
        mcp_servers=mcp_servers,
        sources=[source],
        compatibility=status,
        compatibility_notes=note,
        imported=now_iso(),
    )
    # Preserve original name (pre-slug) as a tag only if different.
    if name and slugify(name) != name:
        rec.tags.append(name)
    rec.category = categorize(rec.name, description, body, rec.tags)
    return rec


def extract_repo_records(repo_dir: Path, repo_name: str, license_name: str = "",
                         url: str | None = None) -> list[AgentRecord]:
    """Extract all usable AgentRecords from a cloned repository directory."""
    records: list[AgentRecord] = []
    url = url or f"https://github.com/{repo_name}"
    for f in iter_agent_files(repo_dir):
        rel = f.relative_to(repo_dir)
        src = SourceInfo(repo=repo_name, author=repo_name.split("/")[0],
                         license=license_name, url=url, path=str(rel))
        rec = extract_agent(f, src, relpath=str(rel))
        if rec is None:
            continue
        if len(rec.body) < 40:
            continue
        records.append(rec)
    return records


def render_agent_markdown(rec: AgentRecord) -> str:
    """Render an AgentRecord into canonical AGY markdown."""
    front = {
        "name": rec.name,
        "description": rec.description,
        "kind": rec.kind,
        "model": rec.model,
    }
    if rec.temperature is not None:
        front["temperature"] = rec.temperature
    if rec.max_turns is not None:
        front["max_turns"] = rec.max_turns
    if rec.timeout_mins is not None:
        front["timeout_mins"] = rec.timeout_mins
    if rec.tools:
        front["tools"] = rec.tools
    if rec.mcp_servers:
        front["mcpServers"] = rec.mcp_servers

    agy_meta = {
        "version": AGY_VERSION,
        "category": rec.category,
        "tags": rec.tags,
        "compatibility": {
            "status": rec.compatibility,
            "score": compatibility_score(rec),
            "notes": rec.compatibility_notes,
        },
        "validation": rec.validation,
        "imported": rec.imported,
        "sources": [asdict(s) for s in rec.sources],
    }
    front["agy"] = agy_meta

    import yaml
    lines = ["---"]
    lines.append(yaml.safe_dump(front, sort_keys=False, allow_unicode=True, width=1000).rstrip())
    lines.append("---")
    lines.append("")
    lines.append(rec.body.strip())
    lines.append("")
    return "\n".join(lines)


def compatibility_score(rec: AgentRecord) -> int:
    if rec.compatibility == STATUS_FULLY:
        return 100
    if rec.compatibility == STATUS_TOOLMAP:
        return 75
    if rec.compatibility == STATUS_MCP:
        return 85
    if rec.compatibility == STATUS_MANUAL:
        return 50
    return 0


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #

def validate_record(rec: AgentRecord) -> list[str]:
    errors: list[str] = []
    if not rec.name:
        errors.append("missing name")
    if not rec.description:
        errors.append("missing description")
    if not rec.body.strip():
        errors.append("missing prompt body")
    if not re.fullmatch(r"[a-z0-9-_]+", rec.name):
        errors.append(f"invalid name slug: {rec.name!r}")
    if rec.category not in CATEGORIES:
        errors.append(f"unknown category: {rec.category!r}")
    return errors


# --------------------------------------------------------------------------- #
# Deduplication
# --------------------------------------------------------------------------- #

def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def semantic_duplicate(rec_a: AgentRecord, rec_b: AgentRecord, threshold: float = 0.95) -> bool:
    if rec_a.body_hash == rec_b.body_hash:
        return True
    if len(rec_a.body) < 120 or len(rec_b.body) < 120:
        return False
    return jaccard(tokenize(rec_a.body), tokenize(rec_b.body)) >= threshold


def merge_sources(rec: AgentRecord, other: AgentRecord) -> None:
    for s in other.sources:
        if not any(s.url == cs.url and s.path == cs.path for cs in rec.sources):
            rec.sources.append(s)
    for t in other.tags:
        if t not in rec.tags:
            rec.tags.append(t)
    for t in other.tools:
        if t not in rec.tools:
            rec.tools.append(t)
    for m in other.mcp_servers:
        if m not in rec.mcp_servers:
            rec.mcp_servers.append(m)


def dedupe_records(records: list[AgentRecord]) -> list[AgentRecord]:
    """Merge duplicates and assign unique names.

    Stage 1: merge exact-duplicate bodies.
    Stage 2: merge same (name, category) agents, keeping the richest body.
    Stage 3: disambiguate any remaining name collisions.
    """
    # Stage 1: exact body duplicates.
    by_hash: dict[str, AgentRecord] = {}
    for rec in records:
        h = rec.body_hash
        if h in by_hash:
            merge_sources(by_hash[h], rec)
        else:
            by_hash[h] = rec
    exact_merged = list(by_hash.values())

    # Stage 2: same name + category.
    by_namecat: dict[tuple[str, str], AgentRecord] = {}
    variant_count: dict[tuple[str, str], int] = {}
    for rec in exact_merged:
        key = (rec.name, rec.category)
        if key in by_namecat:
            variant_count[key] = variant_count.get(key, 1) + 1
            existing = by_namecat[key]
            if len(rec.body) > len(existing.body):
                # New record is richer; make it canonical and fold in existing.
                merge_sources(rec, existing)
                by_namecat[key] = rec
            else:
                merge_sources(existing, rec)
        else:
            by_namecat[key] = rec

    merged = []
    for key, rec in by_namecat.items():
        n = variant_count.get(key, 1)
        if n > 1:
            note = f"Merged {n} same-name variants into one canonical agent."
            if rec.compatibility_notes:
                rec.compatibility_notes += " " + note
            else:
                rec.compatibility_notes = note
        merged.append(rec)

    # Stage 3: disambiguate remaining name collisions (across categories).
    seen_names: set[str] = set()
    for rec in merged:
        if rec.name in seen_names:
            rec.name = f"{rec.name}-{rec.category}"
            if rec.name in seen_names:
                i = 2
                while f"{rec.name}-{i}" in seen_names:
                    i += 1
                rec.name = f"{rec.name}-{i}"
        seen_names.add(rec.name)

    merged.sort(key=lambda r: (r.category, r.name))
    return merged
