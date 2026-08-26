---
name: code-review
description: Orchestrates parallel review of a change set using the code-review, security-auditor, and performance-engineer subagents, then synthesizes findings.
steps:
  - agent: code-reviewer
    category: testing
    prompt: Review the staged changes for correctness, bugs, and maintainability.
  - agent: security-auditor
    category: security
    prompt: Audit the staged changes for vulnerabilities and unsafe patterns.
  - agent: performance-engineer
    category: performance
    prompt: Assess the staged changes for performance regressions and hotspots.
synthesis: Merge the three reports, deduplicate findings, and rank them by severity.
---

# Code Review Workflow

1. Run `code-reviewer`, `security-auditor`, and `performance-engineer` in
   parallel over the same change set.
2. Each returns a structured findings list.
3. A coordinator (the parent agent) merges the findings, removes duplicates,
   and ranks them: **blocker → warning → nit**.

> All three agents are imported in this repository under
> `agents/testing/`, `agents/security/`, and `agents/performance/`.
