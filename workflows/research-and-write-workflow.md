---
name: research-and-write
description: Deep-research a topic with the researcher agent, then hand the notes to a writer agent to produce a structured article.
steps:
  - agent: researcher
    category: research
    prompt: Gather and synthesize authoritative sources on <topic>.
  - agent: content-writer
    category: writing
    prompt: Turn the research notes into a structured, engaging article.
synthesis: Review the draft for accuracy and cite every claim back to the research notes.
---

# Research & Write Workflow

1. **Research** — delegate to the `researcher` subagent; it returns a
   source-linked brief.
2. **Write** — pass the brief to the `content-writer` subagent; it returns a
   draft with sections and a hook.
3. **Verify** — the parent agent checks every factual claim against the
   research notes before publishing.

> Both agents are imported under `agents/research/` and `agents/writing/`.
