---
name: incident-response
description: Triage a production incident using the incident-responder agent, then follow up with a postmortem written by the postmortem-writer agent.
steps:
  - agent: incident-responder
    category: devops
    prompt: Triage the incident, identify the blast radius, and propose mitigations.
  - agent: postmortem-writer
    category: writing
    prompt: Draft a blameless postmortem from the triage notes and timeline.
synthesis: Confirm the timeline, assign owners for follow-ups, and file the postmortem.
---

# Incident Response Workflow

1. **Triage** — the `incident-responder` subagent (in `agents/devops/`)
   produces a severity assessment, timeline, and mitigation plan.
2. **Remediate** — the parent agent executes the mitigations.
3. **Postmortem** — a `postmortem-writer` subagent drafts the blameless
   postmortem; the parent agent reviews and files it.

> MCP note: pair `incident-responder` with an observability MCP server
> (`datadog`, `prometheus`, or `sentry`) for live telemetry — see `tools/mcp/`.
