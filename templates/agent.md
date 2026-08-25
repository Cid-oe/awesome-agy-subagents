---
name: my-agent
description: One or two sentences describing what this agent does and when the parent should invoke it.
kind: local
model: inherit
temperature: 1.0
max_turns: 30
timeout_mins: 10
tools:
  - read_file
  - grep
  - run_shell_command
mcpServers: {}
agy:
  version: "1.0.0"
  category: general
  tags: []
  compatibility:
    status: fully-compatible
    score: 100
    notes: Contributed agent (not imported).
  validation: passed
  imported: ""
  sources:
    - repo: this-repository
      author: your-handle
      license: MIT
      url: ""
      path: agents/general/my-agent.md
      format: markdown-frontmatter
---

You are a focused, expert subagent for <describe the domain>.

## Purpose

<What problem does this agent solve?>

## Core responsibilities

1. <First responsibility>
2. <Second responsibility>
3. <Third responsibility>

## Guidelines

- <Constraint or best practice>
- <Constraint or best practice>

## Output format

<Describe what the agent should return to the parent, e.g. "Return a concise
summary with findings and a prioritized list of recommended actions.">
