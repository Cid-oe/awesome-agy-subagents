# Compatibility Report

## Status distribution

| Status | Count |
|---|---|
| fully-compatible | 3024 |
| needs-tool-mapping | 594 |
| requires-manual-conversion | 347 |
| requires-mcp | 285 |

## Per-agent compatibility

| Agent | Category | Status | Score | Notes |
|---|---|---|---|---|
| 1-ceo-quality-control-agent | ai | needs-tool-mapping | 75 | Unmapped tools: "*". |
| 1-problem-solver-specialist | research | needs-tool-mapping | 75 | Unmapped tools: "*". |
| 2026-08-18-docs-governance-and-spec-workflow | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-18-docs-governance-and-spec-workflow-zh | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-19-phase-0b-doc-audit-outcomes | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-19-phase-0b-doc-audit-outcomes-zh | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-25-batch-composition | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-25-executable-harness-foundations | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-25-files-service-seam | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-25-layered-agent-governance | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-25-openai-entry-controllers | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-26-ide-token-and-device-history-normalization | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-26-linux-secret-tool-availability | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-26-proxy-session-and-routing-hardening | networking | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 2026-08-26-security-boundary-hardening | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| 3d-scene-developer | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| a11y | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| a11y-architect | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| a11y-enforcer | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| a11y-guardian | accessibility | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| a2a | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| a2a-protocol-manager | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ab-test-analysis | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| abraham-lincoln | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| abstract-bilingual-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| academic-papers | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| academic-research-synthesizer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| academic-research-uses-structured-extraction-with-cross-source-synthesis | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| academic-researcher | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. Merged 2 same-name variants into one canonical agent. |
| acceptance-test-generator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| accessibility-auditor | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| accessibility-expert | accessibility | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']. Merged 3 same-name variants into one canonical agent. |
| accessibility-reviewer | accessibility | needs-tool-mapping | 75 | Unmapped tools: Agent. Merged 2 same-name variants into one canonical agent. |
| accessibility-runtime-tester | accessibility | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'openSimpleBrowser']. |
| accessibility-specialist | accessibility | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, google_web_search, write_todos, read_many_files, ask_user]. Merged 5 same-name variants into one canonical agent. |
| accessibility-tester | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| accessibility-tester-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| account-strategist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| accounting-controls-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| accounts-payable-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| action-planning-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| action-planning-agent-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| activation-system | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| actix-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ad-attacker | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ad-creative-strategist | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| ad-security-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| ada-lovelace | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| adapt-the-four-phase-processing-pipeline-to-domain-specific-throughput-needs | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| adaptive-coordinator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| adaptive-coordinator-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| adr-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| adr-generator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ads-strategist | research | needs-tool-mapping | 75 | Unmapped tools: [Read, WebFetch]. |
| adversarial-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| advisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| advisor-backend | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| advocate | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| aegis | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| aem-front-end-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'web/fetch', 'githubRepo', 'figma-dev-mode-mcp-server']. |
| aeo-foundations-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| ag2-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| ag2-prompt-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ag2-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-communication-protocol | ai | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| agent-creator | ai | needs-tool-mapping | 75 | Unmapped tools: ["Write", "Read"]. |
| agent-environment-simulator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-evaluator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-evolution-system | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-governance-reviewer | ai | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'terminalCommand']. |
| agent-installer | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. Merged 5 same-name variants into one canonical agent. |
| agent-name | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-notes-externalize-navigation-intuition-that-search-cannot-discover-and-traversal-cannot-reconstruct | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-orchestration-context-manager | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-organizer | ai | needs-tool-mapping | 75 | Unmapped tools: Task. Merged 6 same-name variants into one canonical agent. |
| agent-sdk-capabilities | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| agent-sdk-verifier-py | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-sdk-verifier-ts | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-self-memory-should-be-architecturally-separate-from-user-knowledge-systems | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-session-boundaries-create-natural-automation-checkpoints-that-human-operated-systems-lack | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agent-system | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| agent-test-report | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| agent-thread-architect | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| agent-tree-spec | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| agent-workflow-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| agentdb-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agentic-identity-trust-architect | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agentic-payments | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agentic-search-optimizer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| agentic-workflows | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agentica-agent | ai | needs-tool-mapping | 75 | Unmapped tools: [Bash, Grep]. |
| agents-are-simultaneously-methodology-executors-and-subjects-creating-a-unique-trust-asymmetry | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agents-orchestrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| agents-reference | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| aging-parent-care-companion | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| agy-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-citation-strategist | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| ai-content-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-data-remediation-engineer | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-dev-jobs-search | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-engineer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 9 same-name variants into one canonical agent. |
| ai-engineer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-engineer-machine-learning | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-ethics-governance-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-feature-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-generated-code-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-governance-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-hygiene-auditor | security | needs-tool-mapping | 75 | Unmapped tools: [Bash, Read]. |
| ai-ml-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| ai-observability-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-programmer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-readiness-reporter | ai | needs-tool-mapping | 75 | Unmapped tools: ['execute', 'read', 'search', 'search/codebase', 'editFiles']. |
| ai-recon | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-safety-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-shifts-knowledge-systems-from-externalizing-memory-to-externalizing-attention | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-team-dev | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-team-producer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-team-qa | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-writing-auditor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ai-writing-auditor-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| aidefence-guardian | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| albert-einstein | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| alert-analyzer | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| alert-analyzer-general | general | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| alexander | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| alexander-the-great | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| algorithm-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| algorithm-expert-ai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| algorithm-expert-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| algorithm-reviewer | performance | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| alkhwarizmi | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| allpurpose-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| alpine | backend | requires-mcp | 85 | Requires MCP servers: laravel-boost. |
| altshuller | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| am-channel | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| am-delegate | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ambient-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| amplitude-experiment-implementation | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| analysis-agent | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| analytics | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| analytics-advisor | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| analytics-engineer | data | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, google_web_search, write_todos, read_many_files, ask_user]. Merged 5 same-name variants into one canonical agent. |
| analytics-implementation-specialist | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| analytics-reporter | data | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| android-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| angelos-symbo | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| angular-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| angular-expert | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 2 same-name variants into one canonical agent. |
| angular-pro | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| angularjs-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| animation-choreographer | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| anna | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| anomaly-detector | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| anomaly-detector-database | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| ansible-expert | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| anthropic-provider-proposal | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| anthropologist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-arbiter | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-depth-prober | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-execharness-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-feature-coordinator | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-framework-generator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-framework-validator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-fresh-verifier | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-goal-checker | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-implementer | testing | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-intake | security | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-janitor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-juror | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-manager | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-preflight-probe | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-re-anchor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-scope-coordinator | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-scoper | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-scribe | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-sweep-coordinator | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| ap-sweeper | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-synthesizer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ap-verifier | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| apex | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| api | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| api-builder | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-contract-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-design-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-designer | backend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, read_many_files, ask_user, google_web_search, web_fetch]. Merged 10 same-name variants into one canonical agent. |
| api-docs | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| api-documentation | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| api-documenter | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 13 same-name variants into one canonical agent. |
| api-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-gateway-engineer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| api-integration-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-platform-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-reviewer | backend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| api-scaffolding-backend-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-scaffolding-django-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-scaffolding-fastapi-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-scaffolding-graphql-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-security-audit | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| api-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| api-tester-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| api-testing-observability-api-documenter | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| apify-integration-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| app-store-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| application-performance-frontend-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| application-performance-observability-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| application-performance-performance-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| application-security-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| apply | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| arbiter | testing | needs-tool-mapping | 75 | Unmapped tools: [Bash, Grep]. Merged 2 same-name variants into one canonical agent. |
| arbitrage-bot | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| arch-linux-expert | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'terminalCommand', 'runCommands', 'edit/editFiles']. |
| archaeologist | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| archimedes | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| architect | architecture | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 19 same-name variants into one canonical agent. |
| architect-review | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| architect-reviewer | architecture | requires-mcp | 85 | Requires MCP servers: sequential-thinking, context7. Merged 6 same-name variants into one canonical agent. |
| architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| architecture-advisor | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| architecture-analyzer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| architecture-critic | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| architecture-explainer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| architecture-reviewer | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. Merged 2 same-name variants into one canonical agent. |
| archivist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| archon-engine-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| archon-expert | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| archon-expert-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-aws-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-aws-research-reader | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "TodoWrite", "mcp__plugin_arckit_aws-knowledge__aws___search_documentation", "mcp__plugin_arckit_aws-knowledge__aws___read_documentation", "mcp__plugin_arckit_aws-knowledge__aws___recommend", "mcp__plugin_arckit_aws-knowledge__aws___get_regional_availability", "mcp__plugin_arckit_aws-knowledge__aws___list_regions"]. |
| arckit-azure-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-azure-research-reader | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "TodoWrite", "mcp__plugin_arckit_microsoft-learn__microsoft_docs_search", "mcp__plugin_arckit_microsoft-learn__microsoft_docs_fetch", "mcp__plugin_arckit_microsoft-learn__microsoft_code_sample_search"]. |
| arckit-cloud-research-writer | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Write", "Edit"]. |
| arckit-competitors-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Write", "Edit"]. |
| arckit-datascout | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Write", "Bash", "TodoWrite", "WebSearch", "WebFetch"]. |
| arckit-datascout-reader | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "WebSearch", "WebFetch", "TodoWrite", "mcp__plugin_arckit_govreposcrape__search_uk_gov_code", "mcp__plugin_arckit_datacommons-mcp__search_indicators", "mcp__plugin_arckit_datacommons-mcp__get_observations"]. |
| arckit-datascout-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit"]. |
| arckit-framework | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Write", "Bash", "TodoWrite"]. |
| arckit-gcp-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-gcp-research-reader | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "TodoWrite", "mcp__plugin_arckit_google-developer-knowledge__search_documents", "mcp__plugin_arckit_google-developer-knowledge__get_document", "mcp__plugin_arckit_google-developer-knowledge__batch_get_documents"]. |
| arckit-gov-code-search | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-gov-code-search-reader | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "WebFetch", "TodoWrite", "mcp__plugin_arckit_govreposcrape__search_uk_gov_code"]. |
| arckit-gov-code-search-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Write", "Edit"]. |
| arckit-gov-landscape | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-gov-landscape-reader | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "WebFetch", "TodoWrite", "mcp__plugin_arckit_govreposcrape__search_uk_gov_code", "mcp__plugin_arckit_govreposcrape__vulnerability_exposure"]. |
| arckit-gov-landscape-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Write", "Edit"]. |
| arckit-gov-reuse | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| arckit-gov-reuse-reader | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "WebFetch", "TodoWrite", "mcp__plugin_arckit_govreposcrape__search_uk_gov_code", "mcp__plugin_arckit_govreposcrape__dependency_compare"]. |
| arckit-gov-reuse-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit"]. |
| arckit-grants | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Write", "Bash", "TodoWrite", "WebSearch", "WebFetch"]. |
| arckit-grants-reader | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "WebSearch", "WebFetch", "TodoWrite"]. |
| arckit-grants-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit"]. |
| arckit-research | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Write", "Bash", "TodoWrite", "WebSearch", "WebFetch"]. |
| arckit-research-reader | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "WebSearch", "WebFetch", "TodoWrite"]. |
| arckit-research-writer | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Write", "Edit"]. |
| arckit-tenders-reader | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "TodoWrite", "mcp__plugin_arckit_uk-tenders__search_tenders", "mcp__plugin_arckit_uk-tenders__top_suppliers", "mcp__plugin_arckit_uk-tenders__awarded_value_by_buyer", "mcp__plugin_arckit_uk-tenders__aggregate_tenders", "mcp__plugin_arckit_uk-tenders__awards_over_time", "mcp__plugin_arckit_uk-tenders__get_tender", "mcp__plugin_arckit_uk-tenders__get_status"]. |
| arckit-tenders-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Write", "Edit"]. |
| arendt | security | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| argument-builder-agent | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| aris-reviewer-claude-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| aristotle | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| aristotle-frontend | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| arm-cortex-expert | embedded | needs-tool-mapping | 75 | Unmapped tools: []. |
| arm-migration-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| art-director | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| article-analyzer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| article-illustrator | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| artifact-architect | architecture | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| ascii-ui-mockup-generator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| aspect-oriented-programming-solved-the-same-cross-cutting-concern-problem-that-hooks-solve | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| aspnet-core-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| assemble-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| asset-import | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 7 same-name variants into one canonical agent. |
| assignment-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| associative-ontologies-beat-hierarchical-taxonomies-because-heterarchy-adapts-while-hierarchy-brittles | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| assumption-mapping | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| assumption-validation | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| astro-expert | frontend | requires-mcp | 85 | Requires MCP servers: context7, astro-docs, exa, sequential-thinking, shadcn, gemini-design, fuse-browser. Merged 2 same-name variants into one canonical agent. |
| async-pattern-fixer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| atlas | testing | needs-tool-mapping | 75 | Unmapped tools: [Bash, Grep]. Merged 2 same-name variants into one canonical agent. |
| atlas-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| atlassian-requirements-to-jira | frontend | needs-tool-mapping | 75 | Unmapped tools: ['atlassian']. |
| attack-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| attention-residue-may-have-a-minimum-granularity-that-cannot-be-subdivided | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| audience-segmentation | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| audience-seo-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| audio-director | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| audio-mixer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| audio-quality-controller | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| audit | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| audit-evidence-organizer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| auditor | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. Merged 2 same-name variants into one canonical agent. |
| auth-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| auth0-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| auto-commit-hooks-eliminate-prospective-memory-failures-by-converting-remember-to-act-into-guaranteed-execution | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| auto-detection-engine | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| auto-handoff-threshold-focus | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| automated-detection-is-always-safe-because-it-only-reads-state-while-automated-remediation-risks-content-corruption | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| automation-governance-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| automation-should-be-retired-when-its-false-positive-rate-exceeds-its-true-positive-rate-or-it-catches-zero-issues | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| autonomous | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| autonomous-optimization-architect | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| autopilot-coordinator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| autoprompt-models-schema | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| autoresearch-agent | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| autoresearcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ava-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| avm-owner-triage | ai | needs-tool-mapping | 75 | Unmapped tools: [vscode, execute, agent, search, web, browser, 'github/*', 'microsoft.docs.mcp/*', 'terraform.mcp/*', todo]. |
| awaiter | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| aws-cloud-expert | cloud | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'edit/editFiles', 'web/fetch', 'runCommands', 'terminalLastCommand', 'problems']. |
| aws-cost-saver | cloud | requires-mcp | 85 | Requires MCP servers: awslabs-aws-api. |
| aws-incident-triage | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| aws-principal-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [execute/getTerminalOutput, execute/runTask, execute/createAndRunTask, execute/runInTerminal, execute/runTests, execute/testFailure, read/problems, read/readFile, read/terminalSelection, read/terminalLastCommand, read/getTaskOutput, edit/editFiles, search, web/fetch, web/githubRepo]. |
| aws-serverless-architect | cloud | needs-tool-mapping | 75 | Unmapped tools: [execute/getTerminalOutput, execute/runTask, execute/createAndRunTask, execute/runInTerminal, execute/runTests, execute/testFailure, read/problems, read/readFile, read/terminalSelection, read/terminalLastCommand, read/getTaskOutput, edit/editFiles, search, web/fetch, web/githubRepo]. |
| aws-specialist | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| axe | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| azure-avm-bicep-mode | cloud | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]. |
| azure-avm-terraform-mode | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]. |
| azure-db-developer | cloud | requires-mcp | 85 | Requires MCP servers: azure_databases. |
| azure-engineer | cloud | requires-mcp | 85 | Requires MCP servers: azure_services, azure, microsoft_learn. |
| azure-iac-exporter | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ['read', 'edit', 'search', 'web', 'execute', 'todo', 'runSubagent', 'azure-mcp/*', 'ms-azuretools.vscode-azure-github-copilot/azure_query_azure_resource_graph']. |
| azure-iac-generator | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'agent', 'azure-mcp/azureterraformbestpractices', 'azure-mcp/bicepschema', 'azure-mcp/search', 'pulumi-mcp/get-type', 'runSubagent']. |
| azure-infra-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| azure-logic-apps-expert-mode | cloud | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "changes", "edit/editFiles", "search", "runCommands", "microsoft.docs.mcp", "azure_get_code_gen_best_practices", "azure_query_learn"]. |
| azure-policy-analyzer | cloud | needs-tool-mapping | 75 | Unmapped tools: [read, search, execute, web, azure-mcp/*, ms-azuretools.vscode-azure-github-copilot/azure_query_azure_resource_graph]. |
| azure-principal-architect-mode-instructions | architecture | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_design_architecture", "azure_get_code_gen_best_practices", "azure_get_deployment_best_practices", "azure_get_swa_best_practices", "azure_query_learn"]. |
| azure-saas-architect-mode-instructions | architecture | needs-tool-mapping | 75 | Unmapped tools: ["changes", "search/codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "search/searchResults", "runCommands/terminalLastCommand", "runCommands/terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_design_architecture", "azure_get_code_gen_best_practices", "azure_get_deployment_best_practices", "azure_get_swa_best_practices", "azure_query_learn"]. |
| azure-smart-city-iot-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: ['search', 'search/codebase', 'edit/editFiles', 'fetch', 'runCommands', 'runTasks']. |
| azure-terraform-iac-implementation-specialist | infrastructure | needs-tool-mapping | 75 | Unmapped tools: [execute/getTerminalOutput, execute/awaitTerminal, execute/runInTerminal, read/problems, read/readFile, read/terminalSelection, read/terminalLastCommand, agent, edit/createDirectory, edit/createFile, edit/editFiles, search, web/fetch, 'azure-mcp/*', todo]. |
| azure-terraform-infrastructure-planning | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ["edit/editFiles", "fetch", "todos", "azureterraformbestpractices", "cloudarchitect", "documentation", "get_bestpractices", "microsoft-docs"]. |
| backend-api-security-backend-security-coder | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 9 same-name variants into one canonical agent. |
| backend-architect-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-build | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| backend-dev | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| backend-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| backend-development-performance-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-development-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-development-tdd-orchestrator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-development-test-automator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-domain-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| backend-fix | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| backend-implement | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| backend-reviewer | backend | needs-tool-mapping | 75 | Unmapped tools: Agent. Merged 2 same-name variants into one canonical agent. |
| backend-typescript-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| background-tasks | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| backlinks-implicitly-define-notes-by-revealing-usage-context | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| backlog-grooming | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| backlog-grooming-writing | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| backstage-specialist | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| backtest-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| backward-maintenance-asks-what-would-be-different-if-written-today | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| baidu-seo-specialist | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| balance-onboarding-enforcement-and-questions-to-prevent-premature-complexity | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| base-template-generator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bash-expert | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| bash-pro | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| basic-level-categorization-determines-optimal-moc-granularity | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| batch-scheduler | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| batching-by-context-similarity-reduces-switching-costs-in-agent-processing | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| bateson | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| bead-dependency-mapper | ai | requires-mcp | 85 | Requires MCP servers: dolt-mcp-vcs. |
| bead-epic-auditor | security | requires-mcp | 85 | Requires MCP servers: dolt-mcp-vcs. |
| bead-recovery-specialist | backend | needs-tool-mapping | 75 | Unmapped tools: Bash(bd, export:*), Bash(bd, version:*), Bash(bd, dolt, show:*), Bash(bd, dolt, status:*), Bash(bd, config, get:*), Bash(bd, config, list:*), Bash(bd, --help:*), Bash(bd, dolt, --help:*), Bash(dolt, status:*), Bash(curl:*), Bash(bash, ${CLAUDE_PLUGIN_ROOT}/scripts/server-health.sh:*), Bash(bash, ${CLAUDE_PLUGIN_ROOT}/scripts/dolt-idle-reaper.sh:*). |
| beads-guru | security | needs-tool-mapping | 75 | Unmapped tools: Bash(bd, list:*), Bash(bd, show:*), Bash(bd, ready:*), Bash(bd, memories:*), Bash(bd, search:*), Bash(bd, stats:*), Bash(bd-sync, status:*), Bash(git, status:*), Bash(git, log:*). |
| beads-warden | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| beer | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| behavioral-anti-patterns-matter-more-than-tool-selection | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| behavioral-nudge-engine | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bench | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| bench-matcher | ai | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| benchmark-reviewer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| benchmark-suite | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| benchmarking-specialist | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| betweenness-centrality-identifies-bridge-notes-connecting-disparate-knowledge-domains | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| bibliography-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| bicep-planning | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| bicep-specialist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| bilibili-content-strategist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| billing-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| bim-gis-specialist | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| bind | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bizlogic-hunter | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| blast-radius-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| blender-add-on-engineer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| bloat-auditor | security | needs-tool-mapping | 75 | Unmapped tools: [Bash, Write]. |
| blockchain-developer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| blockchain-developer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| blockchain-developer-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| blockchain-developer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| blockchain-developer-security | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| blockchain-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| blue | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| blueprint-mode | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| blueprints-that-teach-construction-outperform-downloads-that-provide-pre-built-code-for-platform-dependent-modules | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bm25-retrieval-fails-on-full-length-descriptions-because-query-term-dilution-reduces-match-scores | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| book-co-author | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| book-distiller | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| book-metadata-packaging-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| booked-schema | database | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| bookkeeper-controller | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| bootstrap | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| bootstrap-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bootstrap-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| bootstrap-orchestrator | ai | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master. |
| bootstrapping-principle-enables-self-improving-systems | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| borg | ai | needs-tool-mapping | 75 | Unmapped tools: Task, Skill. |
| borges | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| bot-deploy-verifier | backend | needs-tool-mapping | 75 | Unmapped tools: ["Bash"]. |
| boyd | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| bpa-expression-helper | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob"]. |
| brace | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| brag-spotter | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| brain | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| brain-router | networking | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| brainstorming | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking. |
| braintree-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| braintrust-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| branch-summary | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| branch-summary-context | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| branch-summary-preamble | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| brand-guardian | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| brand-guardian-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| brand-keeper | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| braudel | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| breadth-keeper | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| breaking-news-reporter | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bridge-monitor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| brief | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| browser-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| browser-debugger | testing | requires-mcp | 85 | Requires MCP servers: chrome_devtools. |
| browser-extension-developer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| browser-use | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| browser-use-writing | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| bruner | writing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| budget | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| budget-calculator | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| budget-justification-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| budget-sentinel | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| budget-variance-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| bug-bounty | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| bug-clusterer | devops | needs-tool-mapping | 75 | Unmapped tools: "Read, triage:fetch_mentions, triage:search_recent, triage:fetch_conversation". |
| bug-hunting-tango | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| build-automatic-memory-through-cognitive-offloading-and-session-handoffs | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| build-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| build-error-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| build-fix-prompt | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| build-fixer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| build-logger | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| build-release-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| builder | frontend | requires-mcp | 85 | Requires MCP servers: serena. |
| builtin-types | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| bullmq-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| bun-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| bus-messaging | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| business-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| business-boss | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-cynic | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-department | ai | needs-tool-mapping | 75 | Unmapped tools: ["filesystem", "database", "email", "creator-mcp"]. |
| business-expert | research | needs-tool-mapping | 75 | Unmapped tools: find, fetch_content, fetch_content_cloak, get_search_content. |
| business-intelligence-developer | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-pusher | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-rookie | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-rules-extractor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-transformation-master | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| business-watcher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| buzz | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| byzantine-coordinator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| c-developer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| c-expert | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| c-expert-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runNotebooks', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'microsoft.docs.mcp']. Merged 2 same-name variants into one canonical agent. |
| c-mcp-server-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| c-net-janitor | windows | needs-tool-mapping | 75 | Unmapped tools: [vscode/extensions, vscode/getProjectSetupInfo, vscode/installExtension, vscode/newWorkspace, vscode/runCommand, vscode/vscodeAPI, execute/getTerminalOutput, execute/runTask, execute/createAndRunTask, execute/runTests, execute/runInTerminal, execute/testFailure, read/terminalSelection, read/terminalLastCommand, read/getTaskOutput, read/problems, read/readFile, 'github/*', 'microsoft.docs.mcp/*', edit/editFiles, search, web]. |
| c-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| c2-evasion-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| c2-operator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| c4-code | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| c4-component | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| c4-container | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| c4-context | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| cache | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| calendar | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| calendar-coordinator-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| capture-the-reaction-to-content-not-just-the-content-itself | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| carnot | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| carousel-growth-engine | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cartographer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cartography-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cassandra-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| cast | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cast-imaging-impact-analysis-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cast-imaging-software-discovery-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cast-imaging-structural-quality-advisor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| catalog | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| cavecrew-builder | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cavecrew-investigator | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cavecrew-reviewer | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| caveman-mode | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| celery-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| centinela-qa | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| centos-linux-expert | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'terminalCommand', 'runCommands', 'edit/editFiles']. |
| chain | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| challenger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| challenger-backend | backend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. |
| champollion | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| change | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| change-management-consultant | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| changelog-generator | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| changelog-watcher | devops | requires-mcp | 85 | Requires MCP servers: exa, sequential-thinking, fuse-browser. |
| channel-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chaos | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chaos-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| chaos-engineer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chaos-engineer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| chaos-engineer-research | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| character-psychologist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| charles-darwin | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chat-engineering-gaps | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| chat-storage-design | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| chat-ui-craftsman | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| chief-executive-officer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| chief-financial-officer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chief-marketing-officer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chief-of-staff | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chief-of-staff-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| chief-operating-officer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chief-product-officer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chief-reviewer | productivity | needs-tool-mapping | 75 | Unmapped tools: find. |
| chief-technology-officer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| china-e-commerce-operator | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| china-market-localization-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| chinese-tech | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| choreography-engine | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| chronicler | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| ci-cd-expert | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-agent | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-automation-cloud-architect | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-automation-deployment-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-automation-devops-troubleshooter | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-automation-kubernetes-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-automation-terraform-specialist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-manager | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-pipeline-engineer | ci-cd | requires-mcp | 85 | Requires MCP servers: github, basic-memory. Merged 2 same-name variants into one canonical agent. |
| cicd-redteam | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| cicd-steward | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| circleci-expert | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| circular-dep-untangler | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| citation-compliance-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| citation-integrity-checker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| citation-keeper | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| cite | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| civil-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claim-auditor | security | needs-tool-mapping | 75 | Unmapped tools: ["Read"]. |
| claim-ref-alignment-audit-agent | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| claim-verifier | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| claims-authorizer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| claims-must-be-specific-enough-to-be-wrong | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-code | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-code-guide | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-code-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-code-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-ecom | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-md-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-persona | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claude-security | security | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion, Workflow, Workflow(claude-security:scan), TaskCreate, TaskGet, TaskUpdate, TaskOutput, TaskStop, Agent(claude-security:scan-inventory, claude-security:scan-researcher, claude-security:scan-verifier, claude-security:patch-generator, claude-security:patch-verifier, claude-security:explore). |
| claudehut-brainstormer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-contract-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-db-reviewer | database | requires-mcp | 85 | Requires MCP servers: postgres, mysql. |
| claudehut-explorer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-implementer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-learner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-observability-reviewer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-perf-reviewer | frontend | requires-mcp | 85 | Requires MCP servers: postgres, mysql, kafka. |
| claudehut-plan-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-planner | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-reuse-scanner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| claudehut-security-auditor | security | requires-mcp | 85 | Requires MCP servers: postgres, mysql, kafka. |
| claudehut-test-runner | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| clause | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| clean | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| clean-code-reviewer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| clean-code-reviewer-ai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| clean-code-reviewer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| clean-code-reviewer-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| cleopatra-vii | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| cli-developer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-discuss-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cli-execution-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cli-explore-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cli-for-beginners-content-sync | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-lite-planning-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-lite-planning-agent-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-planning-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-planning-agent-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| cli-roadmap-plan-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cli-ux-tester | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| client-ops-monitor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| clinical-evidence-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| clojure-developer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| clojure-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| clojure-interactive-programming | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| closure-rituals-create-clean-breaks-that-prevent-attention-residue-bleed | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cloud-and-saas-outage-triage | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| cloud-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| cloud-architect-cloud | cloud | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 9 same-name variants into one canonical agent. |
| cloud-infrastructure-deployment-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| cloud-infrastructure-network-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| cloud-security | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| cloud-security-architect | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| cms-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| coach | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| coach-writing | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Edit]. |
| coaching-program-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| coase | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| cobol-engineer | writing | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, read_many_files, ask_user, google_web_search]. Merged 2 same-name variants into one canonical agent. |
| cochrane | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| cockroachdb-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-analyzer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-archaeologist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-archaeologist-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-archaeologist-time-traveler | writing | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| code-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| code-assist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-commentator | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| code-commentator-ai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| code-commentator-documentation | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| code-commenter | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-developer-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-documentation-code-reviewer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-documentation-docs-architect | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-documentation-tutorial-engineer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-executor | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| code-explainer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-explorer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| code-generator | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| code-goal-planner | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-mapper | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-quality-pr-reviewer | testing | needs-tool-mapping | 75 | Unmapped tools: BashOutput. |
| code-reader | research | needs-tool-mapping | 75 | Unmapped tools: skill. |
| code-refactorer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-refactoring-legacy-modernizer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-refiner | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| code-review | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-review-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-review-mode | backend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| code-review-preshipment | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-review-swarm | embedded | requires-mcp | 85 | Requires MCP servers: claude-flow. Merged 4 same-name variants into one canonical agent. |
| code-review-waltz | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 21 same-name variants into one canonical agent. |
| code-reviewer-ai | ai | needs-tool-mapping | 75 | Unmapped tools: BashOutput. Merged 3 same-name variants into one canonical agent. |
| code-reviewer-architecture | architecture | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 3 same-name variants into one canonical agent. |
| code-reviewer-backend | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. Merged 6 same-name variants into one canonical agent. |
| code-reviewer-database | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-reviewer-frontend | frontend | requires-mcp | 85 | Requires MCP servers: github, basic-memory, zen. Merged 7 same-name variants into one canonical agent. |
| code-reviewer-pro | security | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 2 same-name variants into one canonical agent. |
| code-reviewer-windows | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-searcher | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-searcher-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-simplifier | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| code-simplifier-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-standards-enforcer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| code-verifier | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| code-verifier-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-analyzer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-analyzer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-archaeologist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-cleanup-test-automator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-deep-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-documenter | productivity | requires-mcp | 85 | Requires MCP servers: ide. |
| codebase-explorer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| codebase-explorer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-info | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| codebase-locator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-mapper | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-onboarding-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-orchestrator | ai | needs-tool-mapping | 75 | Unmapped tools: airis-mcp-gateway, context-manager, error-coordinator, pied-piper, subagent-catalog:search, subagent-catalog:fetch. |
| codebase-orchestrator-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-pattern-finder | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| codebase-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| codemap | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| codeowner-update | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| coder | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| coder-backend | backend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, activate_skill, read_many_files, ask_user]. Merged 2 same-name variants into one canonical agent. |
| coder-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| coder-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-artist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-cli | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-coordinator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-docs-maintainer | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-exec | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-exec-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-implementer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-implementer-writing | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-judge | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-onboarder | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-reviewer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-second-opinion | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| codex-worker | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| cognitive-offloading-is-the-architectural-foundation-for-vault-design | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| cognitive-outsourcing-risk-in-agent-operated-systems | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| coherence-maintains-consistency-despite-inconsistent-inputs | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| coherent-architecture-emerges-from-wiki-links-spreading-activation-and-small-world-topology | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| cohort-analysis | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| collaboration | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| collaboration-depth-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| collective-intelligence-coordinator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| collective-intelligence-coordinator-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| comet-opik | ai | needs-tool-mapping | 75 | Unmapped tools: ['read', 'search', 'edit', 'shell', 'opik/*']. |
| command-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| command-runner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| comment-analyzer | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| comment-analyzer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| comment-pruner | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| commit | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| commit-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| commit-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| commit-ci-cd | ci-cd | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| commit-detector | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| committer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| common-mistakes | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| comms-scanner | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| communication-excellence-coach | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| community-detection-algorithms-can-inform-when-mocs-should-split-or-merge | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| community-manager | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| compaction-short-summary | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| compaction-summary | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| compaction-summary-context | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| compaction-turn-prefix | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| compaction-update-summary | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| compat | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| competitive-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| complete-navigation-requires-four-complementary-types-that-no-single-mechanism-provides | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| complex-systems-evolve-from-simple-working-systems | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| compliance-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| compliance-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| compliance-automation-specialist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| compliance-checker | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| compliance-mapper | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| compliance-reviewer | security | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| compliance-reviewer-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, google_web_search, read_many_files, ask_user]. Merged 2 same-name variants into one canonical agent. |
| compliance-reviewer-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| compliance-validator | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| components | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| composable-knowledge-architecture-builds-systems-from-independent-toggleable-modules-not-monolithic-templates | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| compose-multi-domain-systems-through-separate-templates-and-shared-graph | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| composition | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| comprehensive-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| comprehensive-review-architect-review | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| comprehensive-review-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| computer-use | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| computer-use-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| computer-vision-engineer | machine-learning | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| computer-vision-specialist | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| concept-orientation-beats-source-orientation-for-cross-domain-connections | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| conceptual-planning-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| conceptual-planning-agent-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| concretizer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| conductor-geepers | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| conductor-orchestrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| conductor-validator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| confidence-thresholds-gate-automated-action-between-the-mechanical-and-judgment-zones | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| config-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| configuration-dimensions-interact-so-choices-in-one-create-pressure-on-others | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| configuration-paralysis-emerges-when-derivation-surfaces-too-many-decisions | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| confucius | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| connection-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| connector-discovery | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| consensus-coordinator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| consensus-reviewer | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| constitutional-validator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| contacts | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| contacts-general | general | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| container-breakout | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| container-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| content-creator | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 4 same-name variants into one canonical agent. |
| content-department | writing | needs-tool-mapping | 75 | Unmapped tools: ["filesystem", "database", "browser", "website", "email"]. |
| content-marketer | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| content-polisher | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| content-quality-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| content-seo | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| content-strategist | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| content-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| context | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| context-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: ['search/codebase', 'search/usages', 'read/problems', 'read/readFile', 'edit/editFiles', 'execute/runInTerminal', 'execute/getTerminalOutput', 'web/fetch']. |
| context-aware-activator | backend | requires-mcp | 85 | Requires MCP servers: basic-memory, github. |
| context-engineer | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Bash"]. |
| context-engineer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| context-files-function-as-agent-operating-systems-through-self-referential-self-extension | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| context-loader | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| context-management-enhancement | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| context-manager | ai | requires-mcp | 85 | Requires MCP servers: context7. Merged 4 same-name variants into one canonical agent. |
| context-manager-performance | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| context-manager-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| context-mode | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| context-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| context-phrase-clarity-determines-how-deep-a-navigation-hierarchy-can-scale | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| context-query-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| context-search-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| context-window-truncated-output | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| context7-docs-fetcher | documentation | requires-mcp | 85 | Requires MCP servers: ide. |
| context7-expert | writing | needs-tool-mapping | 75 | Unmapped tools: ['read', 'search', 'web', 'context7/*', 'agent/runSubagent']. |
| continuation-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| continuity-guardian | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| continuous-small-batch-processing-eliminates-review-dread | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| contract-review-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| contrarian | cloud | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| contrib | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| controlled-disorder-engineers-serendipity-through-semantic-rather-than-topical-linking | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| convention-checker | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| conversation-analyzer | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep"]. Merged 2 same-name variants into one canonical agent. |
| conversation-director | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| conversion-funnel | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| convex-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| copilot-workshops-content-sync | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| copy | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| copy-desk-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| copy-writer | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| copywriter | writing | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, read_many_files, ask_user]. Merged 4 same-name variants into one canonical agent. |
| corporate-training-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| correction-sweep | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cortex | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cost-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| council-ada | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-aristotle | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-aurelius | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-feynman | testing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-kahneman | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-karpathy | machine-learning | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-lao-tzu | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-machiavelli | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-meadows | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-munger | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-musashi | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-rams | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-socrates | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-sun-tzu | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-sutskever | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-taleb | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-torvalds | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| council-watts | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "WebSearch", "WebFetch"]. |
| counterpoint-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| coverage-analyst | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cpp-build-doctor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cpp-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cpp-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| cpp-expert | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| cpp-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cpp-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cpp-pro-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cpp-reviewer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| craft-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| craft-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| crdt-synchronizer | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| create-adk-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| create-prd-chat-mode | frontend | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "edit/editFiles", "fetch", "findTestFiles", "list_issues", "githubRepo", "search", "add_issue_comment", "create_issue", "update_issue", "get_issue", "search_issues"]. |
| creation-engine | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| creative-director | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| creative-writing-uses-worldbuilding-consistency-with-character-tracking | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| creator | writing | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| creator-economy-master | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| credential-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| crest | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| critic | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| critic-backend | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| critic-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| critic-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| critical-thinking-mode-instructions | ai | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'problems', 'search', 'searchResults', 'usages']. |
| cross-border-e-commerce-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| cross-linker | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| cross-links-between-moc-territories-indicate-creative-leaps-and-integration-depth | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| crypto-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| crypto-analyzer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| crypto-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| crypto-risk-manager | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| crypto-trader | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| crypto-trading-desk | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| cs-aeo | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| cs-agent-deployer | ai | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| cs-agent-grader | ai | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| cs-agent-interviewer | ai | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| cs-agent-launcher-orchestrator | ai | needs-tool-mapping | 75 | Unmapped tools: Skill, AskUserQuestion. |
| cs-agile-product-owner | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-ai-act-compliance | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-aims-iso42001 | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-andreessen | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-arquiteto | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-backend-engineer | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-bizops-orchestrator | frontend | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| cs-book-to-skill | database | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-caio-advisor | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-capture | productivity | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-caveman-mode | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cco-advisor | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cdo-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-ceo-advisor | testing | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cfo-advisor | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-chief-of-staff | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-chro-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-ciso-advisor | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-ciso-iso27001 | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-claude-coach | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cs-cmo-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-commercial-orchestrator | frontend | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| cs-compliance-officer | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-content-creator | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| cs-coo-advisor | performance | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cpo-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cqm-iso13485 | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cro-advisor | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-cto-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-deep-research | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Task]. |
| cs-deep-work | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-demand-gen-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| cs-dossier | devops | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| cs-dpo-gdpr | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-engineering-lead | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-fda-qsr-auditor | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-financial-analyst | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-frontend-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-fullstack-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-general-counsel-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-grants | research | needs-tool-mapping | 75 | Unmapped tools: [Read, WebFetch]. |
| cs-grill-master | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-grill-with-docs | documentation | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-growth-strategist | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-handoff-author | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| cs-human-gate | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-inbox-setup | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| cs-inbox-triage | research | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| cs-karpathy-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-landing | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-linkedin-editor | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Edit]. |
| cs-linkedin-orchestrator | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Edit]. |
| cs-litreview | research | needs-tool-mapping | 75 | Unmapped tools: [Read, WebFetch]. |
| cs-markdown-html-orchestrator | frontend | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| cs-meeting-discipline | productivity | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-memory-engineer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| cs-notebooklm | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-patent | security | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| cs-pm-orchestrator | frontend | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| cs-product-analyst | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-product-manager | productivity | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-product-orchestrator | frontend | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| cs-product-strategist | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-project-manager | productivity | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-pulse | infrastructure | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| cs-quality-regulatory | testing | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-reflect | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read]. |
| cs-research | research | needs-tool-mapping | 75 | Unmapped tools: [Read, WebFetch]. |
| cs-research-ops-orchestrator | research | needs-tool-mapping | 75 | Unmapped tools: Skill. |
| cs-roast-judge | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Task, WebSearch]. |
| cs-scraping-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cs-senior-engineer | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-skill-author | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-skill-doctor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cs-soc2-auditor | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-syllabus | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-ux-researcher | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-vpe-advisor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-webinar-marketer | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| cs-weekly-review | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| cs-wiki-ingestor | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-wiki-librarian | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-wiki-linter | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-workflow-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| cs-workspace-admin | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| csharp-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| csharp-developer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| csharp-developer-windows | windows | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| csharp-dotnet-pro | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| csharp-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| csharp-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| csharp-reviewer | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| css | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| css-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ctf-solver | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| cultural-intelligence-strategist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| curator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| curie | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| cursor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| cursor-agent-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| custdev | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| custom-agent-foundry | ai | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'agent', 'github/*', 'todo']. |
| customer-communications-specialist | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| customer-diagnostics-engineer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| customer-service | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| customer-success | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| customer-success-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| customer-success-manager-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| customer-success-manager-devops | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| customer-support | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| customer-support-documentation | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| cut | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| cypress-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| daa-specialist | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| daemon-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| daily-briefing-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| dangling-links-reveal-which-notes-want-to-exist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| dart-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dart-expert | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| darwin | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| dashboard-operator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 7 same-name variants into one canonical agent. |
| data-collector | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-consolidation-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-engineer | data | fully-compatible | 100 | Converted directly; no manual steps required. Merged 13 same-name variants into one canonical agent. |
| data-engineer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-engineer-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-engineer-infrastructure | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-exfiltrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-exit-velocity-measures-how-quickly-content-escapes-vendor-lock-in | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-generator | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-ml-reviewer | machine-learning | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| data-models | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| data-platform-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-privacy-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-privacy-officer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| data-scientist | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| data-scientist-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| data-scientist-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-scientist-data | data | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 2 same-name variants into one canonical agent. |
| data-scientist-database | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| data-scientist-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| data-steward | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| data-visualization | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| data-visualization-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| data-viz | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| data-viz-engineer | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| database | database | requires-mcp | 85 | Requires MCP servers: laravel-boost. |
| database-admin | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| database-administrator | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| database-architect | database | requires-mcp | 85 | Requires MCP servers: basic-memory, sequential-thinking. |
| database-attacker | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-cloud-optimization-database-architect | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-cloud-optimization-database-optimizer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-designer | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| database-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-modeler | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-optimization | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-optimization-reviewer | database | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| database-optimizer | database | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 6 same-name variants into one canonical agent. |
| database-optimizer-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| database-performance-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-reliability-engineer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| database-reviewer | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| database-specialist | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| db-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| db-inspector | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| db2-dba | database | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, google_web_search, read_many_files, write_todos, ask_user, web_fetch]. Merged 2 same-name variants into one canonical agent. |
| dba | database | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| ddd-domain-expert | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| dead-code-hunter | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deal | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deal-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deapi-media | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| debate-moderator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| debian-linux-expert | linux | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'terminalCommand', 'runCommands', 'edit/editFiles']. |
| debt-collector | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| debug-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| debug-explore-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| debug-mode-instructions | testing | needs-tool-mapping | 75 | Unmapped tools: ['edit/editFiles', 'search/codebase', 'search/usages', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'read/problems', 'execute/testFailure', 'web/fetch', 'execute/runTests']. |
| debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 27 same-name variants into one canonical agent. |
| debugging-toolkit-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| debugging-toolkit-dx-optimizer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| debunk-auditor | security | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| decisions | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| deck-qa | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| deck-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| declarative-agents-architect | ai | needs-tool-mapping | 75 | Unmapped tools: ['codebase']. |
| decontextualization-risk-means-atomicity-may-strip-meaning-that-cannot-be-recovered | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deep-executor | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| deep-fiction-master | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| deep-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| deepseek-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| default | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| defender-scout-kql | performance | needs-tool-mapping | 75 | Unmapped tools: ['read', 'search']. |
| defensive-code-cleaner | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| defi-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| delegate | ai | needs-tool-mapping | 75 | Unmapped tools: find, contact_supervisor. |
| delphi-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deming | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| demo-generator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| demonstrate-understanding-mode-instructions | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'web/fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']. |
| deneb-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob"]. |
| deno-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| dense-interlinked-research-claims-enable-derivation-while-sparse-references-only-enable-templating | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependencies | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| dependency-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependency-maintenance-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependency-manager | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| dependency-manager-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependency-resolution-through-topological-sort-makes-module-composition-transparent-and-verifiable | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependency-updater | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependency-updater-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dependency-upgrader | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deploy | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| deploy-engineer | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| deploy-with-verification | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| deployment-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. Merged 9 same-name variants into one canonical agent. |
| deployment-specialist | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| derivation-generates-knowledge-systems-from-composable-research-claims-not-template-customization | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| derivatives-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| derived-systems-follow-a-seed-evolve-reseed-lifecycle | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| description-quality-for-humans-diverges-from-description-quality-for-keyword-search | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| descriptions-are-retrieval-filters-not-summaries | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| design | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 3 same-name variants into one canonical agent. |
| design-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-boss | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-brand-guardian | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-bridge | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| design-cynic | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-department | frontend | needs-tool-mapping | 75 | Unmapped tools: ["filesystem", "database", "browser", "creator-mcp"]. |
| design-expert | frontend | requires-mcp | 85 | Requires MCP servers: magic, shadcn, gemini-design, fuse-browser. |
| design-frontend-assistant | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-image-prompt-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-inclusive-visuals-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-mocs-as-attention-management-devices-with-lifecycle-governance | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-pusher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-review | frontend | requires-mcp | 85 | Requires MCP servers: playwright, chrome-devtools. |
| design-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-rookie | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-sync | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-system-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| design-system-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, activate_skill, read_many_files, ask_user]. Merged 3 same-name variants into one canonical agent. |
| design-token-guardian | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-ui-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-ux-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-ux-researcher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-v2-review-findings | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| design-visual-storyteller | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-watcher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| design-whimsy-injector | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| desktop-app-dev | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| desktop-app-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| desktop-pilot | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Write]. |
| detailed-design | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| detection-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| dev-boss | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| dev-cynic | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dev-department | backend | needs-tool-mapping | 75 | Unmapped tools: ["filesystem", "database", "browser", "website-mcp"]. |
| dev-orchestrator | ai | requires-mcp | 85 | Requires MCP servers: agentmemory, gitnexus. |
| dev-pusher | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dev-rookie | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| dev-watcher | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| developer-advocate | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| developer-experience-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| developer-experience-optimizer | performance | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| developer-portal | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| developer-tooling-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| development-workflows-research-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| developmental-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| developmental-manuscript-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| device-coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| devils-advocate | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| devils-advocate-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| devils-advocate-reviewer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| devils-advocate-testing | testing | needs-tool-mapping | 75 | Unmapped tools: ['read', 'search', 'web']. |
| devops | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| devops-automator | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| devops-engineer | devops | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 11 same-name variants into one canonical agent. |
| devops-expert | devops | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo', 'runCommands', 'runTasks']. |
| devops-incident-responder | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| devops-platform-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| devops-reviewer | devops | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| devops-sre | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| devops-troubleshooter | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| devsecops-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| devtools-regression-investigator | research | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'openSimpleBrowser']. |
| dexter | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| dgx-spark-ops-engineer | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| diagnostic-pipeline | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| dialectician | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| diffbluecover | testing | needs-tool-mapping | 75 | Unmapped tools: [, 'DiffblueCover/*', ]. |
| digital-mutability-enables-note-evolution-that-physical-permanence-forbids | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dijkstra | testing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| directus-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| discourse-scanner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| discovery-coach | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| discovery-lead | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| discovery-reliability-reviewer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| discovery-scanner | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| discovery-threat-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| discussion-based-planning | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| distinctiveness-scoring-treats-description-quality-as-measurable | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| distributed-debugging-error-detective | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| distribution | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| django-api-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| django-backend-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| django-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| django-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| django-developer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| django-expert | backend | requires-mcp | 85 | Requires MCP servers: context7, basic-memory. Merged 2 same-name variants into one canonical agent. |
| django-orm-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| django-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| dna-claude-analysis | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| doc-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| doc-generator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| doc-scribe | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| doc-updater | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| doc-verifier | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| doc-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| docker-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| docker-expert-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| docker-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| docs | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 3 same-name variants into one canonical agent. |
| docs-drift-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| docs-lookup | documentation | requires-mcp | 85 | Requires MCP servers: context7. |
| docs-maintain | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| docs-maintainer | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| docs-researcher | documentation | requires-mcp | 85 | Requires MCP servers: openaiDeveloperDocs. Merged 2 same-name variants into one canonical agent. |
| docs-reviewer | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| docs-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| docs-writer-documentation | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| doctor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| doctor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| document-generator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| document-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| document-specialist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| documentation-analyst-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| documentation-engineer | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| documentation-expert | writing | requires-mcp | 85 | Requires MCP servers: context7. Merged 2 same-name variants into one canonical agent. |
| documentation-generator | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| documentation-mode | writing | needs-tool-mapping | 75 | Unmapped tools: Task. |
| documentation-specialist | writing | requires-mcp | 85 | Requires MCP servers: context7, basic-memory, zen. |
| documentation-specialist-documentation | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| documentation-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| docusaurus-expert | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| does-agent-processing-recover-what-fast-capture-loses | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| dolt-sync-advisor | backend | needs-tool-mapping | 75 | Unmapped tools: Bash(bd, dolt, show:*), Bash(bd, dolt, remote, list:*), Bash(bd, dolt, status:*), Bash(bd, dolt, --help:*), Bash(bd, init, --help:*), Bash(bd, backup, --help:*), Bash(dolt, remote, -v:*), Bash(curl:*), Bash(bash, ${CLAUDE_PLUGIN_ROOT}/scripts/server-health.sh:*), Bash(bash, ${CLAUDE_PLUGIN_ROOT}/scripts/dolt-idle-reaper.sh:*). |
| domain-analyzer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| domain-modeler | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| domain-reviewer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| dossier-investigator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| dotnet-architect | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| dotnet-core-expert | windows | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| dotnet-framework-4-8-expert | windows | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| dotnet-fullstack-mentor | windows | needs-tool-mapping | 75 | Unmapped tools: [execute/testFailure, execute/getTerminalOutput, execute/runTask, execute/createAndRunTask, execute/runInTerminal, read/problems, read/readFile, read/terminalSelection, read/terminalLastCommand, read/getTaskOutput, edit/editFiles, search]. |
| doublecheck | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| douyin-strategist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| draft | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| draft-writer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| drift | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| drift-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| droid | frontend | needs-tool-mapping | 75 | Unmapped tools: ["read", "search", "edit", "shell"]. |
| drone-reality-mapping-specialist | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| drupal-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| drupal-expert | architecture | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'terminalCommand', 'edit/editFiles', 'web/fetch', 'githubRepo', 'runTests', 'problems']. |
| drupal-performance-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| drupal-shopping-cart-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| dry-deduplicator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ds-flash | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| ds-pro | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| ds-pro-testing | testing | requires-mcp | 85 | Requires MCP servers: dsh-crew. |
| dual-coding-with-visual-elements-could-enhance-agent-traversal | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| dual-orchestrator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| duplicate-pr | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| duplicate-resource-detector | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| dx-optimizer | performance | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 8 same-name variants into one canonical agent. |
| dynamodb-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| dynatrace-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| e-commerce-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| e2e-runner | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| e2e-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| each-module-must-be-describable-in-one-sentence-under-200-characters-or-it-does-too-many-things | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| each-new-note-compounds-value-by-creating-traversal-paths | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| echo | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| echo-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| eco | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| economy-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| edge | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| edit-diff-learner | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| editor-in-chief-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| editor-review | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| editorial-synthesizer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| education-tech | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| efficiency-reviewer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| eic-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| eight-configuration-dimensions-parameterize-the-space-of-possible-knowledge-systems | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| einstein | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| ekman | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| elaborative-encoding-is-the-quality-gate-for-new-notes | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| elasticsearch-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| elasticsearch-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| electron-code-review-mode-instructions | frontend | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "editFiles", "fetch", "problems", "runCommands", "search", "searchResults", "terminalLastCommand", "git", "git_diff", "git_log", "git_show", "git_status"]. |
| electron-desktop-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| electron-developer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| electron-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| electron-pro | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| electron-pro-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 3 same-name variants into one canonical agent. |
| electron-pro-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| elixir-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| elixir-expert-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| elixir-expert-linux | linux | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. Merged 2 same-name variants into one canonical agent. |
| elixir-expert-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| elixir-pro | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| elk-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| email-calendar-supervisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| email-deliverability-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| email-intelligence-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| email-marketing-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| embed | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| embedded-firmware-engineer | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| embedded-systems | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| embedded-systems-engineer | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| ember | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| emergency-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| empathy-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| empty-state-storyteller | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| enforce-schema-with-graduated-strictness-across-capture-processing-and-query-zones | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| enforcing-atomicity-can-create-paralysis-when-ideas-resist-decomposition | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| engagement-planner | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| engelbart | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| engine-programmer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineer-architecture | architecture | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| engineering-ai-data-remediation-engineer | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-ai-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-autonomous-optimization-architect | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-backend-architect | backend | requires-mcp | 85 | Requires MCP servers: vue-docs, nuxt-ui-remote, nuxt-remote. |
| engineering-cms-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-code-reviewer | security | requires-mcp | 85 | Requires MCP servers: vue-docs, nuxt-ui-remote, nuxt-remote. |
| engineering-codebase-onboarding-engineer | backend | requires-mcp | 85 | Requires MCP servers: vue-docs, nuxt-ui-remote, nuxt-remote. |
| engineering-data-engineer | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-database-optimizer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-devops-automator | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-email-intelligence-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-frontend-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-git-workflow-master | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-incident-response-commander | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-manager | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| engineering-minimal-change-engineer | backend | requires-mcp | 85 | Requires MCP servers: vue-docs, nuxt-ui-remote, nuxt-remote. |
| engineering-mobile-app-builder | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-rapid-prototyper | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-security-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-senior-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-software-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-sre | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-technical-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-threat-detection-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-uses-technical-decision-tracking-with-architectural-memory | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| engineering-voice-ai-integration-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| enhanced-agent-organizer | ai | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master. |
| enhanced-agent-template | ai | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| enterprise-integration-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| enterprise-onboarding-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| enterprise-security-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| episode-orchestrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| equity-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| erdos | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| erlang | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| erlang-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| erlang-expert-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| error-coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| error-coordinator-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| error-detective | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| error-detective-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| error-detective-research | research | requires-mcp | 85 | Requires MCP servers: basic-memory, sequential-thinking, zen. Merged 4 same-name variants into one canonical agent. |
| error-recovery-designer | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| error-whisperer | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| escalation-support-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| esg-sustainability-officer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ethics-review-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| etl-specialist | data | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| euler | infrastructure | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| eval | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| eval-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob"]. |
| eval-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| eval-judge | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| eval-orchestrator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| evals | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| evaluator | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| evasion-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| evasion-specialist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| event-driven-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| event-sourcing-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| every-knowledge-domain-shares-a-four-phase-processing-skeleton-that-diverges-only-in-the-process-step | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| evidence-collector | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| evidence-retriever | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| evolution-observations-provide-actionable-signals-for-system-adaptation | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| example-generator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| example-generator-ai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| executive-summary-generator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| executor | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| executor-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| executor-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| experience-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| experiment-runner | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| experiment-runner-frontend | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| experiment-tracker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| experiment-tracker-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| expert-embedded-c-engineer | embedded | needs-tool-mapping | 75 | Unmapped tools: ['edit/editFiles', 'search/codebase', 'search/usages', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'read/problems', 'web/fetch']. |
| expert-net-software-engineer-mode-instructions | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runNotebooks", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp"]. |
| expert-nuxt-developer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]. |
| expert-react-frontend-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp"]. |
| expert-vue-js-frontend-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["search/changes", "search/codebase", "edit/editFiles", "vscode/extensions", "web/fetch", "web/githubRepo", "vscode/getProjectSetupInfo", "vscode/installExtension", "vscode/newWorkspace", "vscode/runCommand", "read/problems", "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection", "execute/createAndRunTask", "search/searchResults", "execute/testFailure", "search/usages", "vscode/vscodeAPI"]. |
| exploit-chainer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| exploit-guide | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| exploration-planner | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| explore | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| explore-codebase | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| explore-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| explorer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| explorer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| explorer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| explorer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| expo-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| expo-react-native-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| exponential-planner | mobile | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master, sequential-thinking, zen. |
| express-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| external-memory-shapes-cognition-more-than-base-model | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| extractor | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| faceted-classification-treats-notes-as-multi-dimensional-objects-rather-than-folder-contents | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| fact-checker | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| fact-checker-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| fact-checking-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| fairdb-automation-agent | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| fairdb-incident-responder | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| fairdb-ops-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| fairdb-setup-wizard | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| false-universalism-applies-same-processing-logic-regardless-of-domain | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| fantasy-sci-fi-master | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| faq-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| fastapi-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| fastapi-expert | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 2 same-name variants into one canonical agent. |
| fastapi-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| fastify-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| fastify-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| feat | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| feature-development-dance | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| feature-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| federated-wiki-pattern-enables-multi-agent-divergence-as-feature-not-bug | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| federation-coordinator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| fedora-linux-expert | linux | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'terminalCommand', 'runCommands', 'edit/editFiles']. |
| fedramp-rmf-compliance-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| feedback-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| feedback-synthesizer | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| feinstein | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| feishu-integration-developer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| fermi | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| feynman | security | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| fiber-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| fiber-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| fiction-development-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| field-analyst-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| filament | frontend | requires-mcp | 85 | Requires MCP servers: laravel-boost. |
| filament-optimization-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| file-analyzer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| file-operations | machine-learning | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| finance-lead | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| finance-tracker | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| finance-tracker-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| financial-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| financial-model-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| financial-modeling-agent | ai | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| finding-adjudicator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| finop | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| finops-engineer | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| fintech-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| fintech-engineer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| fintech-engineer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| firebase-operations-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| firestore-security-agent | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| firmware-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| first-principles-thinking | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| fisher | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| fit | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| fix | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| fix-verifier | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| flashloan-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| flask-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| flat-files-break-at-retrieval-scale | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| fleet-manager | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| fleming | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| flex-search | database | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| flight-schema | database | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| flow-coordinator | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| flow-nexus-app-store | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-auth | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-challenges | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-neural | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-payments | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-sandbox | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-swarm | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-user-tools | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| flow-nexus-workflow | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| flutter-dev | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| flutter-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| flutter-pro | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| flutter-reviewer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| flux | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| flyway-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| focus-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| folk | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| forced-engagement-produces-weak-connections | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| forensics-analyst | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| forge | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| forja-dev | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| forkmind-debugger | testing | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| form | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| form-liberator | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| formatter-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| foucault | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| four-abstraction-layers-separate-platform-agnostic-from-platform-dependent-knowledge-system-features | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| fp-a-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| frame | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| frankx-content-creator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| frankx-website-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| french-consulting-market-navigator | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| fresh-context-per-task-preserves-quality-better-than-chaining-phases | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| friction-driven-module-adoption-prevents-configuration-debt-by-adding-complexity-only-at-pain-points | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| friction-reveals-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| frida-kahlo | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| friedrich-nietzsche | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| frontend-architect | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| frontend-build | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| frontend-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| frontend-dev | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| frontend-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 13 same-name variants into one canonical agent. |
| frontend-engineer | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 2 same-name variants into one canonical agent. |
| frontend-experience-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| frontend-fix | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| frontend-implement | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| frontend-mobile-development-mobile-developer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| frontend-performance-investigator | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'fetch', 'findTestFiles', 'problems', 'runCommands', 'runTasks', 'runTests', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'openSimpleBrowser']. |
| frontend-review | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| frontend-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| frontend-security-coder | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| frontmatter | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| fsdp-engine-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| fsdp-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| fsharp-reviewer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| full-stack-developer | frontend | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking, magic. Merged 2 same-name variants into one canonical agent. |
| full-stack-developer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| fullstack-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| fullstack-developer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| fullstack-engineer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| fullstack-engineer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| futurist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| gadamer | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| gaia-benchmark-runner | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| gaia-submission-coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| galileo | mobile | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| galileo-galilei | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gallery-researcher | research | requires-mcp | 85 | Requires MCP servers: meigen. Merged 2 same-name variants into one canonical agent. |
| game-audio-engineer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| game-designer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| game-designer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| game-developer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| gameplay-programmer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| gan-evaluator | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gan-generator | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gan-planner | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gaps | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| garden-curator | productivity | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| gardening-cycle-implements-tend-prune-fertilize-operations | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gate | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gate-checker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gate-fixer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gates | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 8 same-name variants into one canonical agent. |
| gaussdb-expert-engineer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| gcp-starter-kit-expert | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| gdpr-ccpa-compliance | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gdpr-ccpa-compliance-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-a11y | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-api | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-business-plan | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-caddy | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-caddy-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-canary | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-canary-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-citations | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-citations-writing | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-code-checker | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-code-checker-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-corpus | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-corpus-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-corpus-ux | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-critic | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-dashboard | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-data | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-data-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-db | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-deps | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-design | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-diag | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-diag-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-docs | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-flask | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-flask-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-fullstack-dev | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-game | game-development | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-gamedev | game-development | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-godot | game-development | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-intern-pool | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-intern-pool-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-janitor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-janitor-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-links | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-links-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-checkpoint | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-checkpoint-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-corpus | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-corpus-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-deploy | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-orchestrator-fullstack | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-orchestrator-games | game-development | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-orchestrator-product | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-orchestrator-python | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-python-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-orchestrator-quality | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-orchestrator-research | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-orchestrator-web | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-perf | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-prd | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-pycli | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-react | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-repo | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-repo-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-scalpel | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-scalpel-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-scout | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-services | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-services-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-snippets | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-snippets-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-status | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-status-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-swarm-research | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-system-diag | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-system-help | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-system-help-documentation | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-system-onboard | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| geepers-validator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| geepers-validator-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| geertz | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| gem-browser-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-code-simplifier | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-devops | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-documentation-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-implementer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-mobile-tester | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-orchestrator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-planner | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-reviewer | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| gem-skill-creator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-1-pro-preview-edit-file | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-1-pro-preview-read-file | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-1-pro-preview-write-file | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-flash-preview-edit-file | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-flash-preview-read-file | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-flash-preview-run-shell | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-3-flash-preview-write-file | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-agent | ai | needs-tool-mapping | 75 | Unmapped tools: ["Bash", "Glob", "Read"]. |
| gemini-gpt-hybrid | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| gemini-gpt-hybrid-hard | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| genai-logs-schema | database | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| general-purpose | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| general-web | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| generated-image-output | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| generation | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| generation-effect-gate-blocks-processing-without-transformation | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| generic | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| generic-openai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| genghis-khan | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| genkit-flow-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| genome | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| geoai-ml-engineer | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| geographer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geolocation-chronolocation-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| geoprocessing-specialist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| george-washington | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| geospatial-engineer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| get-current-datetime | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| get-unpublished-changes | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| gh-actions-gcp-expert | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| gh-scraper | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gilfoyle-code-review-mode | research | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'codebase', 'web/fetch', 'findTestFiles', 'githubRepo', 'openSimpleBrowser', 'problems', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'usages', 'vscodeAPI']. |
| gin-expert | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 2 same-name variants into one canonical agent. |
| ginzburg | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| gis-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| gis-qa-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| git | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| git-expert | backend | requires-mcp | 85 | Requires MCP servers: github, basic-memory, zen. |
| git-historian | security | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| git-master | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| git-specialist | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| git-workflow-assistant | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| git-workflow-manager | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| git-workflow-master | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| git-workspace-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| github-actions-expert | security | needs-tool-mapping | 75 | Unmapped tools: ['github/*', 'search/codebase', 'edit/editFiles', 'execute/runInTerminal', 'read/readFile', 'search/fileSearch']. |
| github-actions-expert-ci-cd | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| github-actions-node-runtime-upgrade | ci-cd | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search']. |
| github-actions-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| github-actions-windows-arm64-wheel-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| github-debug | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| github-modes | backend | requires-mcp | 85 | Requires MCP servers: claude-flow. |
| github-workflow | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| gitlab-ci-expert | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| gitmoji-setup | security | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'editFiles', 'runCommands']. |
| global-podcast-strategist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| glyph | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| go-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| go-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| go-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| go-expert-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. |
| go-mcp-server-development-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| go-pro | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| go-resilience-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| go-reviewer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| go-zap-logging | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| goal-driven-memory-orchestration-enables-autonomous-domain-learning-through-directed-compute-allocation | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| goal-integration | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| goal-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| goal-planner-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| goal-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: find. |
| godel | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| godmode-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| godmode-explorer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| godmode-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| godmode-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| godmode-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| godmode-reviewer-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| godmode-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| godmode-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| godot-csharp-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| godot-gameplay-scripter | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| godot-gdextension-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| godot-gdscript-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| godot-multiplayer-engineer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| godot-shader-developer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| godot-shader-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| godot-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| golang-developer | testing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| golang-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| golang-pro | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| golang-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| golang-pro-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 2 same-name variants into one canonical agent. |
| golang-pro-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| golden-path-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| good-descriptions-layer-heuristic-then-mechanism-then-implication | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| gossip-coordinator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| government-digital-presales-consultant | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| grade-verifier | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| grader | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| grafana-expert | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| grand-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: Task. |
| grant-opportunity-scout | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| grant-reporting-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| grant-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| graph-navigator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| graph-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| graphify | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| graphql-architect | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 9 same-name variants into one canonical agent. |
| graphql-architect-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| graphql-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| grid | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| grok-implementer | frontend | needs-tool-mapping | 75 | Unmapped tools: Bash(lane-ctl, start:*), Bash(lane-ctl, status:*), Bash(lane-ctl, tail:*), Bash(lane-ctl, events:*), Bash(lane-ctl, cancel:*), Bash(lane-ctl, retry:*), Bash(lane-ctl, fallback:*), Bash(lane-ctl, verify:*), Bash(lane-ctl, accept:*). |
| growth-engineer | data | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| growth-hacker | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 3 same-name variants into one canonical agent. |
| growth-loops | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| growth-marketer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| grpc-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-advisor-researcher | research | requires-mcp | 85 | Requires MCP servers: context7. |
| gsd-ai-researcher | research | requires-mcp | 85 | Requires MCP servers: context7. |
| gsd-assumptions-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-code-fixer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-code-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-codebase-mapper | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-debug-session-manager | testing | needs-tool-mapping | 75 | Unmapped tools: Agent, AskUserQuestion. Merged 2 same-name variants into one canonical agent. |
| gsd-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-doc-classifier | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-doc-synthesizer | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-doc-verifier | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-doc-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-domain-researcher | research | requires-mcp | 85 | Requires MCP servers: context7. |
| gsd-eval-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-eval-planner | frontend | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| gsd-executor | backend | requires-mcp | 85 | Requires MCP servers: context7. Merged 2 same-name variants into one canonical agent. |
| gsd-framework-selector | ai | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| gsd-integration-checker | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| gsd-intel-updater | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-nyquist-auditor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| gsd-pattern-mapper | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-phase-researcher | research | requires-mcp | 85 | Requires MCP servers: context7, firecrawl, exa. Merged 3 same-name variants into one canonical agent. |
| gsd-plan-checker | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-planner | research | requires-mcp | 85 | Requires MCP servers: context7. Merged 2 same-name variants into one canonical agent. |
| gsd-project-researcher | research | requires-mcp | 85 | Requires MCP servers: context7, firecrawl, exa. Merged 2 same-name variants into one canonical agent. |
| gsd-research-synthesizer | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-roadmapper | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-ui-auditor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| gsd-ui-checker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gsd-ui-researcher | frontend | requires-mcp | 85 | Requires MCP servers: context7, firecrawl, exa. Merged 2 same-name variants into one canonical agent. |
| gsd-user-profiler | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| gsd-verifier | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| guard | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| guardrail | database | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| guide | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| guided-notes-might-outperform-post-hoc-structuring-for-high-volume-capture | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| gus | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| hackathon-ai-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hacker | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| haiku-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hallucination-investigator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| hamilton | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| handoff-document | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| handoff-summary-context | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| harden-orchestrator | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Task, Skill]. |
| harmonyos-app-resolver | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| harness-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| harness-runner | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| harriet-tubman | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| harsh-critic | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| hart | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| haskell-developer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| haskell-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| haskell-pro | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| health-wellness-uses-symptom-trigger-correlation-with-multi-dimensional-tracking | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| healthcare-admin | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| healthcare-compliance-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| healthcare-customer-service | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| healthcare-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| healthcare-innovation-strategist | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| healthcare-marketing-compliance-specialist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| healthcare-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| heartbeat | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| helm | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| herald | ci-cd | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| hierarchical-coordinator | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| high-level-big-picture-architect-hlbpa | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| hipaa-compliance | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| hipaa-compliance-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| historian | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| historian-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| hlasm-assembler-specialist | writing | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, read_many_files, ask_user, google_web_search]. Merged 2 same-name variants into one canonical agent. |
| holism-strategist | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| homelab-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| hook-composition-creates-emergent-methodology-from-independent-single-concern-components | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hook-driven-learning-loops-create-self-improving-methodology-through-observation-accumulation | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hook-enforcement-guarantees-quality-while-instruction-enforcement-merely-suggests-it | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hookbug-d5wz2f-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hookbug-d5wz2f-planner-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hookbug-d5wz2f-reviewer-1 | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hookbug-dispatch-log | devops | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hookbug-kydihy-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hookbug-kydihy-planner-1 | performance | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hookbug-kydihy-reviewer-1 | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-261745-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-261745-reviewer-1 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-288ewn-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-288ewn-planner-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-288ewn-reviewer-1 | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-2d99d1-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-2d99d1-planner-1 | infrastructure | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-2d99d1-reviewer-1 | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-77eri8-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-77eri8-planner-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-77eri8-reviewer-1 | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-80usvr-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-80usvr-planner-1 | linux | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-80usvr-reviewer-1 | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-8v56dp-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-8v56dp-reviewer-1 | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-ah4y1j-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-ah4y1j-reviewer-1 | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-dispatch-log | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-j6lzi1-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-j6lzi1-reviewer-1 | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-ki3aim-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-ki3aim-reviewer-1 | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-kt3ucx-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-kt3ucx-executor-2 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-kt3ucx-planner-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-kt3ucx-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-nnj6gt-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-nnj6gt-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-oln59n-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-oln59n-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-pwv7yj-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-pwv7yj-reviewer-1 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-px9k89-executor-1 | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-px9k89-executor-3 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-px9k89-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-px9k89-reviewer-3 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-r0qoai-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-r0qoai-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-r783op-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-r783op-planner-1 | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-r783op-reviewer-1 | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-u48cb6-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-u48cb6-executor-2 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-u48cb6-planner-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-u48cb6-planner-2 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-u48cb6-reviewer-1 | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-u48cb6-reviewer-2 | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-unkjkl-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-unkjkl-planner-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-unkjkl-reviewer-1 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-w56sog-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hooklog-w56sog-reviewer-1 | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooklog-xb6c47-reviewer-1 | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooks-are-the-agent-habit-system-that-replaces-the-missing-basal-ganglia | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooks-cannot-replace-genuine-cognitive-engagement-yet-more-automation-is-always-tempting | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hooks-enable-context-window-efficiency-by-delegating-deterministic-checks-to-external-processes | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hopper | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| horizon-tracker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| hospitality-guest-services | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| host-app-context | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| hr-onboarding | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| hr-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| html-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| html-exporter | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| hub-coordinator | ai | needs-tool-mapping | 75 | Unmapped tools: Agent, Bash(git, worktree, *), Bash(git, branch, *), Bash(git, checkout, *), Bash(git, merge, *), Bash(git, log, *), Bash(git, diff, *), Bash(git, status, *), Bash(python, *), Bash(mkdir, *), Bash(ls, *), Bash(cat, *). |
| hue | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| humanizer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| hunt | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| hybrid-cloud-architect | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| hypatia | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| hyperledger-fabric-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| hypotheses-manager | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| i18n-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, read_many_files, ask_user]. Merged 2 same-name variants into one canonical agent. |
| i18n-strategist | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| ibis-framework-maps-claim-based-architecture-to-structured-argumentation | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| ibm-i-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, read_many_files, ask_user, google_web_search]. Merged 2 same-name variants into one canonical agent. |
| ibn-khaldun | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ibnalhaytham | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| ibnkhaldun | testing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| icon-curator | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| idea-generator | backend | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'codebase', 'web/fetch', 'githubRepo', 'openSimpleBrowser', 'problems', 'search', 'searchResults', 'usages', 'microsoft.docs.mcp', 'websearch']. |
| idea-generator-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| idea-honing | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| idea-validator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ideator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| idempotent-maintenance-operations-are-safe-to-automate-because-running-them-twice-produces-the-same-result-as-running-them-once | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| identity-access-engineer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| identity-graph-operator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| idp-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| image-generator | backend | requires-mcp | 85 | Requires MCP servers: meigen. Merged 2 same-name variants into one canonical agent. |
| image-prompt-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| immanuel-kant | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| impact-assessment-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| impeccable-asset-producer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| impeccable-documenter | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| impeccable-finish-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| impeccable-manual-edit-applier | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| implement | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| implement-condition-based-maintenance-triggers-for-derived-systems | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| implementation-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| implementation-executor | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| implementation-finisher | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| implementation-plan-generation-mode | frontend | needs-tool-mapping | 75 | Unmapped tools: ["search/codebase", "search/usages", "vscode/vscodeAPI", "read/problems", "execute/testFailure", "read/terminalSelection", "read/terminalLastCommand", "vscode/openSimpleBrowser", "web/fetch", "vscode/extensions", "edit/editFiles", "vscode/getProjectSetupInfo", "vscode/installExtension", "vscode/newWorkspace", "vscode/runCommand", "execute/getTerminalOutput", "execute/runInTerminal", "execute/createAndRunTask", "execute/getTaskOutput", "execute/runTask"]. |
| implementation-reviewer | testing | needs-tool-mapping | 75 | Unmapped tools: BashOutput. |
| implementer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["mcp__magic-codex__spawn", "mcp__magic-codex__status", "mcp__magic-codex__result", "mcp__magic-codex__merge", "mcp__magic-codex__discard"]. |
| implementer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| implementer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| implementer-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| implicit-dependencies-create-distributed-monoliths-that-fail-silently-across-configurations | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| implicit-knowledge-emerges-from-traversal | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| incident-commander | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| incident-responder | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 11 same-name variants into one canonical agent. |
| incident-response-code-reviewer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| incident-response-commander | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| incident-response-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| incident-response-error-detective | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| incident-response-test-automator | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| inclusive-visuals-specialist | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| incremental-formalization-happens-through-repeated-touching-of-old-notes | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| incremental-reading-enables-cross-source-connection-finding | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| index-curator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| indexing-coordinator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| information-architect | architecture | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| infra-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| infra-monitor | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| infra-troubleshooter | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| infrastructure-maintainer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| init | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| injection-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ink | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| inline-links-carry-richer-relationship-data-than-metadata-fields | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| insight-accretion-differs-from-productivity-in-knowledge-systems | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| insight-engine | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| insights-advisor | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| instagram-curator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| instagram-curator-infrastructure | infrastructure | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| install-with-codex | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| intake-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| integration-boundaries | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| integration-engineer | backend | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, activate_skill, read_many_files, ask_user, google_web_search]. Merged 2 same-name variants into one canonical agent. |
| integration-operator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| integration-test-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| integrity-guard | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| integrity-verification-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| intelligence-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| intelligent-agent-selector | ai | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| interfaces | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| intermediate-packets-enable-assembly-over-creation | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| intermediate-representation-pattern-enables-reliable-vault-operations-beyond-regex | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| internationalization-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| interview-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| interview-prep | frontend | needs-tool-mapping | 75 | Unmapped tools: ["read", "search", "web/fetch"]. |
| investigator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| investment-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| invoice-reconciliation-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ios | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| ios-developer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| ios-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| iot-engineer | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| iot-fleet-engineer | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| iot-pentester | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| iris | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| isaac-newton | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| issue-manager | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| issue-plan-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| issue-queue-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| issue-tracker | frontend | requires-mcp | 85 | Requires MCP servers: claude-flow. |
| issue-tracker-devops | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| issue-triager | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| issues | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| issues-backend | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| it-ops-orchestrator | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| it-ops-orchestrator-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| it-service-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| jane-austen | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| jasmine-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| java-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| java-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| java-developer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| java-expert | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| java-mcp-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| java-pro | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| java-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| java-reviewer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| javascript-developer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| javascript-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| javascript-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| javascript-pro-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| javascript-pro-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| jenkins-expert | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| jest-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| jfrog-security-agent | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| jira-workflow-steward | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| jobs | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| johann-sebastian-bach | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| john-locke | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| joker | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| journal-submission-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| journey-mapper | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| jquery-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| jr-context-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| jsapi | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| judge | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| judge-ai | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| judge-security | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| julia-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| julius-caesar | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| justification-chains-enable-forward-backward-and-evolution-reasoning-about-configuration-decisions | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| jwt-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| k8s-operator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| kafka-expert | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| kaggle-miner | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| kahneman | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| karl-marx | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kauffman | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| kay | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| keel | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| keep | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kegg-bioinformatics | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kekule | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| keycloak-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| knex-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-base-author | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-build | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-graph-guide | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-graph-manager | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| knowledge-guide | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-librarian | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. |
| knowledge-navigator | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| knowledge-synthesizer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| knowledge-synthesizer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-synthesizer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| knowledge-system-architecture-is-parameterized-by-platform-capabilities-not-fixed-by-methodology | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-systems-become-communication-partners-through-complexity-and-memory-humans-cannot-sustain | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| knowledge-systems-share-universal-operations-and-structural-components-across-all-methodology-traditions | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| knuth | performance | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| korean-business-navigator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| kotlin-android-pro | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| kotlin-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| kotlin-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| kotlin-mcp-server-development-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kotlin-reviewer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| kotlin-specialist | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| kr62ia-dispatch-log | windows | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| kr62ia-io43px-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| kr62ia-io43px-reviewer-1 | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| kr62ia-kr62ia-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| kr62ia-kr62ia-planner-1 | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| kr62ia-kr62ia-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| kraken | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| kuaishou-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubb-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| kube | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubernetes-expert | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubernetes-expert-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubernetes-operator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubernetes-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubernetes-specialist-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubernetes-specialist-backend | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| kubernetes-specialist-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| kubestellar-console | ai | needs-tool-mapping | 75 | Unmapped tools: [codebase, terminalLastCommand, fetch]. |
| kubestellar-console-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| kusto-assistant | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| lamport | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| landing-page-copywriter | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| lane-supervisor | writing | needs-tool-mapping | 75 | Unmapped tools: Bash(lane-ctl, start:*), Bash(lane-ctl, status:*), Bash(lane-ctl, tail:*), Bash(lane-ctl, events:*), Bash(lane-ctl, cancel:*), Bash(lane-ctl, retry:*), Bash(lane-ctl, fallback:*), Bash(lane-ctl, verify:*), Bash(lane-ctl, accept:*). |
| langchain-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| language-translator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| laozi | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| laplace | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| laravel-backend-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-eloquent-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-expert-agent | ai | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'terminalCommand', 'edit/editFiles', 'web/fetch', 'githubRepo', 'runTests', 'problems', 'search']. |
| laravel-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| laravel-expert-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. |
| laravel-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-specialist-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-specialist-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| laravel-vue-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| lateral-movement | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| latex-engineer | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| launch-tracker-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| launchdarkly-flag-cleanup | ai | needs-tool-mapping | 75 | Unmapped tools: ['*']. |
| launcher-expert | machine-learning | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| launcher-expert-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| launcher-scheduler-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| lavoisier | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| lazycodex-clone-fidelity-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| lazycodex-code-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| lazycodex-gate-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| lazycodex-qa-executor | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| lazycodex-worker-high | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| lead-programmer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| leaf-node-detector | backend | requires-mcp | 85 | Requires MCP servers: basic-memory, sequential-thinking, zen. |
| lean-startup-advisor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| learn-process | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| learning-hub-updater | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| learning-system | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| learnings | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| legacy-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| legacy-code-remover | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legacy-modernization-specialist | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory, zen. |
| legacy-modernizer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legacy-modernizer-ai | ai | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 2 same-name variants into one canonical agent. |
| legacy-modernizer-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| legacy-modernizer-database | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| legal-advisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| legal-advisor-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-advisor-writing | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| legal-billing-time-tracking | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-case-management-uses-precedent-chains-with-regulatory-change-propagation | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-clauses | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-client-intake | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-compliance | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-compliance-checker | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-compliance-checker-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-counsel | research | needs-tool-mapping | 75 | Unmapped tools: find, fetch_content, fetch_content_cloak, get_search_content. |
| legal-document-review | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-obligations | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-ops-coordinator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-recommendations | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-research-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| legal-risks | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| legislative-tracker | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| leguin | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| lem | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| lens | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| leo-tolstoy | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| leonardo-da-vinci | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| lessons-compactor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| level-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| lexi | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| liaison | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| librarian | backend | needs-tool-mapping | 75 | Unmapped tools: lsp, ast_grep. |
| librarian-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| license-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| license-engineer-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| life-boss | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| life-cynic | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| life-pusher | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| life-rookie | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| life-watcher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| light-impressionist | productivity | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| lightcms | ai | needs-tool-mapping | 75 | Unmapped tools: Task. |
| line-copy-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| line-editor-voice-alchemist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| lingo-dev-localization-i18n-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| linkedin-content-creator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| linkedin-post-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "fetch"]. |
| linting-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| liquibase-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| liskov | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| literature-reviewer | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Grep", "Glob", "WebSearch", "WebFetch", "TodoWrite". Merged 3 same-name variants into one canonical agent. |
| literature-strategist-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| litestar-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| live-index-via-periodic-regeneration-keeps-discovery-current | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| live-ops-designer | frontend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| livestream-commerce-coach | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| livewire | frontend | requires-mcp | 85 | Requires MCP servers: laravel-boost. |
| llm-architect | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| llm-architect-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| llm-attention-degrades-as-context-fills | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-client | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| llm-finetuning-architect | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-finetuning-eval-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-finetuning-training-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-integration-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-integration-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-post-training-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-providers | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| llm-redteam | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llm-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| llms-maintainer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| load-balancing-coordinator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| load-testing-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| loadergen-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| loan-officer-assistant | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| local-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| local-first-file-formats-are-inherently-agent-native | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| localization-engineer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| localization-lead | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| localization-specialist | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| lodge | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| logging-concepts-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| logic-column-pattern-separates-reasoning-from-procedure | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| logic-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| loki-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| loop-operator | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| loop-worker-coordinator | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| lsp-index-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| lua-developer | game-development | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| lua-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| ludwig-van-beethoven | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| lumen | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| lyra | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| m-a-integration-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| m2close-dispatch-log | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| m2close-ot0edu-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| m2close-ot0edu-executor-2 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| m2close-ot0edu-reviewer-1 | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| m2close-ot0edu-reviewer-2 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| m2close-zekqgl-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| m2close-zekqgl-reviewer-1 | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| m365-admin | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| machine-learning-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| machine-learning-engineer-ci-cd | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| machine-learning-engineer-machine-learning | machine-learning | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 2 same-name variants into one canonical agent. |
| macos-spatial-metal-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| macro-economist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| maestro | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Task]. Merged 2 same-name variants into one canonical agent. |
| maf-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-alpine-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-api-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-cache-analyst | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-catalog-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-code-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-configuration-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-cronjob-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-css-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-deployment-engineer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-environment-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-feature-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-frontend-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-hyva-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-index-analyst | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-issue-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-knockout-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-local-environment-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-luma-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-magewire-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-model-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-module-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-order-analyst | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-performance-analyst | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-php-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-requirejs-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-security-analyst | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-theme-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-ui-component-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-upgrade-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| magento-xml-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| mahatma-gandhi | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mail-triage | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| mail-triage-frontend | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| maintenance-operations-are-more-universal-than-creative-pipelines-because-structural-health-is-domain-invariant | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| maintenance-scheduling-frequency-should-match-consequence-speed-not-detection-capability | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| maintenance-targeting-should-prioritize-mechanism-and-theory-notes | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| maisie | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| make-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| malware-analyst | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| manager | ai | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| mandelbrot | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| marcus-aurelius | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| margulis | mobile | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| mariadb-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| marie-curie | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mark | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| markdown-accessibility-assistant | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| markdown-plus-yaml-plus-ripgrep-implements-a-queryable-graph-database-without-infrastructure | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| markdown-syntax-formatter | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| market-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| market-competitive | research | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| market-content | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| market-conversion | performance | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| market-research-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| market-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| market-strategy | performance | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| market-technical | infrastructure | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| marketing-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| marketing-analyst | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| marketing-department | frontend | needs-tool-mapping | 75 | Unmapped tools: ["filesystem", "database", "browser", "website", "email"]. |
| marketing-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| mary-wollstonecraft | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| master-story-architect | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| matrix-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| maturity-field-enables-agent-context-prioritization | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| maui-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| maxwell | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| mcclintock | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| mckinsey-slide-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-deployment-orchestrator | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-developer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| mcp-developer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| mcp-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-m365-agent-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-registry-navigator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-security-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-server-advisor | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-server-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mcp-testing-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| meadows | ai | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| media-recorder | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Write]. |
| media-streaming | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| medical-billing-coding-specialist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| meeting-notes-specialist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| meeting-scribe | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| megatron-engine-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| megatron-expert | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| megatron-expert-ci-cd | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-bank-synchronizer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-bridge | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-extractor | frontend | needs-tool-mapping | 75 | Unmapped tools: [Bash, Read]. |
| memory-extractor-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-loader | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-specialist-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| memory-writer | writing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex. |
| mempool-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| mendeleev | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| mentor-mode | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'web/fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']. |
| mermaid-diagram-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mermaid-expert | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| mesh | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| mesh-coordinator | networking | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| message-handoff-probe | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| meta-acos-router | networking | needs-tool-mapping | 75 | Unmapped tools: Task. |
| meta-agent-quality-auditor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-agentic-jujutsu | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-agentic-project-scaffold | ai | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "readCellOutput", "runCommands", "runNotebooks", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "updateUserPreferences", "usages", "vscodeAPI", "activePullRequest", "copilotCodingAgent"]. |
| meta-analysis-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-eod | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-handover | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-memory-guardian | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-safety-guard | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-sync-repos | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| meta-verification-loop | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| metacognitive | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| metacognitive-confidence-can-diverge-from-retrieval-capability | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| metadata-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| metadata-reduces-entropy-enabling-precision-over-recall | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| metaharness-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| methodology-development-should-follow-the-trajectory-from-documentation-to-skill-to-hook-as-understanding-hardens | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| methodology-reviewer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| methodology-traditions-are-named-points-in-a-shared-configuration-space-not-competing-paradigms | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| metis | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| michelangelo | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| micro-frontend-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| microservices-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| microservices-architect-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| microsoft-learn-contributor | writing | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'search/codebase', 'edit/editFiles', 'new', 'openSimpleBrowser', 'problems', 'search', 'search/searchResults', 'microsoft.docs.mcp']. |
| microsoft-study-and-learn | frontend | needs-tool-mapping | 75 | Unmapped tools: ['microsoft_docs_search', 'microsoft_docs_fetch']. |
| midgley | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| migration-engineer | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| migration-pilot | database | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| migration-planner | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| migration-reviewer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| migration-specialist | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| migration-summary | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| mill | ai | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| minecraft-bukkit-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| minimal | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| minimal-change-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mint | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| misinformation-risk-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ml-developer | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| ml-developer-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| ml-engineer | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| ml-engineer-ci-cd | ci-cd | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| ml-engineer-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 3 same-name variants into one canonical agent. |
| ml-engineer-infrastructure | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| mle-reviewer | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| mlops | machine-learning | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| mlops-engineer | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. Merged 11 same-name variants into one canonical agent. |
| mnemonic-medium-embeds-verification-into-navigation | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| mobile | mobile | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| mobile-app-builder | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| mobile-app-developer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| mobile-dev | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| mobile-developer | mobile | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 11 same-name variants into one canonical agent. |
| mobile-engineer | mobile | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, activate_skill, read_many_files, ask_user, google_web_search]. Merged 2 same-name variants into one canonical agent. |
| mobile-pentester | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| mobile-release-engineer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| mobile-security-coder | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| mobile-ux-optimizer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| moc-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| moc-construction-forces-synthesis-that-automated-generation-from-metadata-cannot-replicate | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| moc-maintenance-investment-compounds-because-orientation-savings-multiply-across-every-future-session | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mocha-expert | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| mock | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mocs-are-attention-management-devices-not-just-organizational-tools | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| modal-craftsman | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| model-context-protocol-mcp-expert | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| model-qa-specialist | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| model-risk-manager | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| model-selector | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| model-switcher-stylist | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| modernization-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| modes | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 8 same-name variants into one canonical agent. |
| module-communication-through-shared-yaml-fields-creates-loose-coupling-without-direct-dependencies | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| module-deactivation-must-account-for-structural-artifacts-that-survive-the-toggle | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| moment-strategist | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| momus | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| monday-bug-context-fixer | frontend | needs-tool-mapping | 75 | Unmapped tools: ['*']. |
| mongodb-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| mongodb-performance-advisor | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| mongoose-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| monitor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| monitoring-agent | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| monitoring-observability-specialist | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| monorepo-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. Merged 2 same-name variants into one canonical agent. |
| monorepo-manager | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| monorepo-tooling | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| motion | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| move | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mqtt-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ms-sql-database-administrator | database | needs-tool-mapping | 75 | Unmapped tools: ["search/codebase", "edit/editFiles", "githubRepo", "extensions", "runCommands", "database", "mssql_connect", "mssql_query", "mssql_listServers", "mssql_listDatabases", "mssql_disconnect", "mssql_visualizeSchema"]. |
| mssql-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| multi | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| multi-agent-coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| multi-agent-orchestrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| multi-agent-systems-architect | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| multi-domain-systems-compose-through-separate-templates-and-shared-graph | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| multi-platform-publisher | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| multi-repo-swarm | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| multi-window | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| multimodal-director | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| music-producer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| music-producer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| mutation-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| mysql-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| n8n-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| n8n-workflow-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nagarjuna | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| naming | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| nano-banana-image-creator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| napoleon-bonaparte | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| narrative-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| narrative-director | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| narratologist | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| narrow-folksonomy-optimizes-for-single-operator-retrieval-unlike-broad-consensus-tagging | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| nats-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| navigation-infrastructure-passes-through-distinct-scaling-regimes-that-require-qualitative-strategy-shifts | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| navigational-vertigo-emerges-in-pure-association-systems-without-local-hierarchy | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| nelson-mandela | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| neo4j-docker-client-generator | ai | needs-tool-mapping | 75 | Unmapped tools: ['read', 'edit', 'search', 'shell', 'neo4j-local/neo4j-local-get_neo4j_schema', 'neo4j-local/neo4j-local-read_neo4j_cypher', 'neo4j-local/neo4j-local-write_neo4j_cypher']. |
| neo4j-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| neon-migration-specialist | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| neon-performance-analyzer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-leaf | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-queen | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-queen-leaf | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-queen-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-queen-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| nested-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nestjs-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| net-self-learning-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [vscode/getProjectSetupInfo, vscode/installExtension, vscode/newWorkspace, vscode/runCommand, execute/getTerminalOutput, execute/runTask, execute/createAndRunTask, execute/runInTerminal, read/terminalSelection, read/terminalLastCommand, read/getTaskOutput, read/problems, read/readFile, agent, edit/editFiles, search, web, vscode.mermaid-chat-features/renderMermaidDiagram, github.vscode-pull-request-github/issue_fetch, github.vscode-pull-request-github/labels_fetch, github.vscode-pull-request-github/notification_fetch, github.vscode-pull-request-github/doSearch, github.vscode-pull-request-github/activePullRequest, github.vscode-pull-request-github/pullRequestStatusChecks, github.vscode-pull-request-github/openPullRequest, ms-azuretools.vscode-azureresourcegroups/azureActivityLog, ms-azuretools.vscode-containers/containerToolsConfig, ms-python.python/getPythonEnvironmentInfo, ms-python.python/getPythonExecutableCommand, ms-python.python/installPythonPackage, ms-python.python/configurePythonEnvironment]. |
| net-upgrade | windows | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search', 'runCommands', 'runTasks', 'runTests', 'problems', 'changes', 'usages', 'findTestFiles', 'testFailure', 'terminalLastCommand', 'terminalSelection', 'web/fetch', 'microsoft.docs.mcp']. |
| network-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| network-attacker | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| network-config-reviewer | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| network-engineer | networking | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| network-programmer | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| network-troubleshooter | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| new-relic-incident-response-agent | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| news-fact-checker | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| newton | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| next-js-expert | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runNotebooks", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "figma-dev-mode-mcp-server"]. |
| nextjs-app-router-developer | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-dev | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| nextjs-developer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-developer-networking | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-diagnostics-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-expert | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| nextjs-expert-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, shadcn, gemini-design, fuse-browser. |
| nextjs-pro | performance | requires-mcp | 85 | Requires MCP servers: context7, magic. Merged 2 same-name variants into one canonical agent. |
| nextjs-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nextjs-vercel-deployment | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| nhs-mcp-search | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| night-reviewer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| nikola-tesla | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| nim-developer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| nlp-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| nlp-llm-integration-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| node-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| nodejs-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| nodejs-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: basic-memory, context7. |
| noether | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| nonfiction-manuscript-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| nosql-agent | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| note-titles-should-function-as-apis-enabling-sentence-transclusion | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| notes-are-skills-curated-knowledge-injected-when-relevant | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| notes-function-as-cognitive-anchors-that-stabilize-attention-during-complex-tasks | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| notfair | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| notification-director | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| novel-domains-derive-by-mapping-knowledge-type-to-closest-reference-domain-then-adapting | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| nudge-theory-explains-graduated-hook-enforcement-as-choice-architecture-for-agents | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| numpy-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| oauth-oidc-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| observability-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| observability-incident-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| observation-and-tension-logs-function-as-dead-letter-queues-for-failed-automation | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| obsidian | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ocaml-developer | machine-learning | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| ocaml-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| ocr-grammar-fixer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ocr-quality-assurance | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| octopus-release-notes-with-mcp | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| offer-lead-gen-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| omarchy-plugin-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| omarchy-submission-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| omega-memory | backend | requires-mcp | 85 | Requires MCP servers: omega-memory. |
| omomomo | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| onboard | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| onboard-backend | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| onboarder | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| onboarding-director | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| onboarding-sherpa | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| one-shot-feature-issue-planner | ai | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "githubRepo", "search", "usages", "web/fetch", "findTestFiles"]. |
| onomastophes | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ontologist | research | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| ontology-analyst | research | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| openai-api-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| openapi-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| openapi-to-application-generator | backend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search/codebase']. |
| opening-tournament | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| opensearch-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| opensource-forker | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| opensource-packager | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| opensource-sanitizer | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| opentelemetry-expert | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| operational-memory-and-knowledge-memory-serve-different-functions-in-agent-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| operational-wisdom-requires-contextual-observation | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| operations-manager | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| opsec-anonymizer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| opus-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| oracle | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, WebSearch]. Merged 2 same-name variants into one canonical agent. |
| oracle-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: find. |
| oracle-to-postgresql-migration-expert | database | needs-tool-mapping | 75 | Unmapped tools: [vscode/memory, vscode/runCommand, vscode/askQuestions, execute, search, todo]. |
| orchestrate | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| orchestrated-vault-creation-transforms-arscontexta-from-tool-to-autonomous-knowledge-factory | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| orchestration-analyst | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| orchestrator | architecture | needs-tool-mapping | 75 | Unmapped tools: Task. Merged 2 same-name variants into one canonical agent. |
| orchestrator-ai | ai | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 3 same-name variants into one canonical agent. |
| orchestrator-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| orchestrator-frontend | frontend | requires-mcp | 85 | Requires MCP servers: task-master, basic-memory, sequential-thinking, zen. Merged 2 same-name variants into one canonical agent. |
| orchestrator-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| organic-emergence-versus-active-curation-creates-a-fundamental-vault-governance-tension | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| organizational-psychologist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| orgscript-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| orm-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| orphan-notes-are-seeds-not-failures | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| osint-collector | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| osint-research-lead | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ospo-contributors-report | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ospo-organization-health-report | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ospo-stale-repository-report | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| oss-release-compliance-checker | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| ostrom | security | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| outbound-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| outline-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| over-automation-corrupts-quality-when-hooks-encode-judgment-rather-than-verification | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| overloop-cli | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| overnight-dev-coach | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| overview | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| owasp-top10-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| owner-router | networking | needs-tool-mapping | 75 | Unmapped tools: "Read, triage:lookup_service_owner, triage:lookup_oncall, triage:parse_codeowners, triage:lookup_recent_assignees, triage:lookup_recent_committers". |
| pablo-picasso | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pagerank-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pagerduty-incident-responder | devops | needs-tool-mapping | 75 | Unmapped tools: ["read", "search", "edit", "github/search_code", "github/search_commits", "github/get_commit", "github/list_commits", "github/list_pull_requests", "github/get_pull_request", "github/get_file_contents", "github/create_pull_request", "github/create_issue", "github/list_repository_contributors", "github/create_or_update_file", "github/get_repository", "github/list_branches", "github/create_branch", "pagerduty/*"]. |
| paid-media-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| paid-social-strategist | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| palace-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| pandas-expert | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| panini | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| paper-analysis | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| paper-miner | ai | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Bash", "Grep", "Glob"]. |
| paper-watch | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| paper-writer | writing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| parallel-coordinator | backend | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master, sequential-thinking, zen. |
| password-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| patch | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| patch-generator | frontend | needs-tool-mapping | 75 | Unmapped tools: Agent(claude-security:explore). |
| patch-verifier | testing | needs-tool-mapping | 75 | Unmapped tools: Agent(claude-security:explore). |
| patent-analyst | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| pathfinder | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| pave | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| payload-crafter | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| payment-integration | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| payment-integration-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| payment-integration-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 2 same-name variants into one canonical agent. |
| payment-integration-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| payments-billing-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pbip-validator | database | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash", "Edit"]. |
| pearl | machine-learning | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| peer-review-prep-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| peer-reviewer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| peirce | machine-learning | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| penetration-tester | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| penetration-tester-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| people-profiler | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| people-relationships-uses-dunbar-layered-graphs-with-interaction-tracking | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-code-paths | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-investigation-logger | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-orchestrator | research | needs-tool-mapping | 75 | Unmapped tools: Task, Bash(git:*), Bash(npm:*), Bash(pnpm:*), Bash(yarn:*), Bash(cargo:*), Bash(go:*), Bash(pytest:*), Bash(python:*), Bash(mvn:*), Bash(gradle:*), Bash(node:*). |
| perf-profiler | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| perf-theory-gatherer | writing | needs-tool-mapping | 75 | Unmapped tools: Bash(git:*), Bash(node:*), Bash(npm:*), Bash(pnpm:*), Bash(yarn:*), Bash(cargo:*), Bash(go:*), Bash(pytest:*), Bash(python:*), Bash(mvn:*), Bash(gradle:*). |
| perf-theory-tester | testing | needs-tool-mapping | 75 | Unmapped tools: Bash(git:*), Bash(npm:*), Bash(pnpm:*), Bash(yarn:*), Bash(cargo:*), Bash(go:*), Bash(pytest:*), Bash(python:*), Bash(mvn:*), Bash(gradle:*), Bash(node:*). |
| performance-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| performance-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| performance-analyzer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| performance-benchmarker | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| performance-enforcer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| performance-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 13 same-name variants into one canonical agent. |
| performance-guardian | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| performance-investigator | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| performance-monitor | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 7 same-name variants into one canonical agent. |
| performance-optimizer | performance | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 13 same-name variants into one canonical agent. |
| performance-pr-reviewer | performance | needs-tool-mapping | 75 | Unmapped tools: BashOutput. |
| performance-profiler | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| performance-prophet | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| performance-review | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| performance-reviewer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| performance-tester | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| perl-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| permission-analyst | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Bash"]. |
| permission-escalator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| permissions-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| persistence-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| persona-architect | architecture | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| persona-walkthrough-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| personal-assistant-uses-life-area-management-with-review-automation | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| personal-growth-mentor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| personality-engine | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| perspective-reviewer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| perspectivist | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| pest | testing | requires-mcp | 85 | Requires MCP servers: laravel-boost. |
| phase-1-schema-analysis | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| phase-2-field-utilization | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| phase-3-impact-assessment | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| phase-4-verification | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| phase-5-recommendations | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| phish | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| phishing-operator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| phoenix | linux | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| phoenix-expert | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| php-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| php-developer-backend | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| php-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| php-expert-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. |
| php-mcp-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| php-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| php-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| php-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| pii-detector | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| pimcore-expert | backend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'terminalCommand', 'edit/editFiles', 'web/fetch', 'githubRepo', 'runTests', 'problems']. |
| pipeline-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| pipeline-orchestrator-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| pitch | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| pkm-failure-follows-a-predictable-cycle | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| plan | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| plan-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| plan-backend | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| plan-compliance-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| plan-design | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| plan-factcheck-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| plan-mode-strategic-planning-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| plan-prompt | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| plan-research | research | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| plan-reviewer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| plan-scope | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| plan-standards-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| planner | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| planner-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| planner-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| planner-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| planner-machine-learning | machine-learning | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| planner-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| planner-research | research | needs-tool-mapping | 75 | Unmapped tools: find, fetch_content, fetch_content_cloak, get_search_content. |
| planner-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| planning-mode-instructions | productivity | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "fetch", "findTestFiles", "githubRepo", "search", "usages"]. |
| planning-prd-agent | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| plannotator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| platform-adapter-translation-is-semantic-not-mechanical-because-hook-event-meanings-differ | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| platform-admin | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| platform-capability-tiers-determine-which-knowledge-system-features-can-be-implemented | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| platform-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| platform-fragmentation-means-identical-conceptual-operations-require-different-implementations-across-agent-environments | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| platform-product-manager | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| platform-sre-for-kubernetes | devops | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| plato | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| playbooks | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| playwright | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| playwright-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| playwright-tester-mode | testing | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "fetch", "findTestFiles", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "playwright"]. |
| plinth-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-business-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-java-coder | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-java-micronaut-coder | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-java-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-java-quarkus-coder | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-java-spring-boot-coder | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-no-java | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| plinth-tech-lead | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| plot | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| plugin-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| plugin-validator | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash"]. |
| plugin-validator-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pm | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| pm-writing | writing | needs-tool-mapping | 75 | Unmapped tools: find, fetch_content, fetch_content_cloak, get_search_content. |
| poc-validator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| podcast-content-analyzer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| podcast-metadata-specialist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| podcast-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| podcast-transcriber | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| podcast-trend-scout | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| poincare | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| policy | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| policy-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| policy-enforcer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| policy-guardrail-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| polish | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| polya | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| polymath-bridger | productivity | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| popper | testing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| port | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| portfolio-manager | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| position-engine | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| posix-shell-pro | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| postgres-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| postgres-pro | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| postgresql-database-administrator | database | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "edit/editFiles", "githubRepo", "extensions", "runCommands", "database", "pgsql_bulkLoadCsv", "pgsql_connect", "pgsql_describeCsv", "pgsql_disconnect", "pgsql_listDatabases", "pgsql_listServers", "pgsql_modifyDatabase", "pgsql_open_script", "pgsql_query", "pgsql_visualizeSchema"]. |
| postgresql-pglite-pro | database | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 2 same-name variants into one canonical agent. |
| power-bi-data-modeling-expert-mode | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "search/codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "search/searchResults", "runCommands/terminalLastCommand", "runCommands/terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp"]. |
| power-bi-dax-expert-mode | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "search/codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "search/searchResults", "runCommands/terminalLastCommand", "runCommands/terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp"]. |
| power-bi-performance-expert-mode | performance | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp"]. |
| power-bi-visualization-expert-mode | frontend | needs-tool-mapping | 75 | Unmapped tools: ["changes", "search/codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "search/searchResults", "runCommands/terminalLastCommand", "runCommands/terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp"]. |
| power-platform-expert | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| power-platform-mcp-integration-expert | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| powershell-5-1-expert | windows | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| powershell-7-expert | windows | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| powershell-module-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| powershell-security-hardening | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| powershell-security-hardening-windows | windows | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| powershell-ui-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| ppc-campaign-strategist | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| pptx-deck-creation-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pr-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| pr-communications-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pr-description-composer | frontend | requires-mcp | 85 | Requires MCP servers: github, basic-memory. |
| pr-duplicate-check | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| pr-ghostwriter | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| pr-manager | ai | requires-mcp | 85 | Requires MCP servers: claude-flow. |
| pr-manager-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| pr-review | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pr-reviewer-specialist | ai | requires-mcp | 85 | Requires MCP servers: github, basic-memory, zen. |
| pr-test-analyzer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| pr44-verify-report | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| prd-creator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| prd-specialist | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| prd-writer | writing | needs-tool-mapping | 75 | Unmapped tools: Task. |
| pre-publish-review | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| predictive-orchestrator | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master. |
| preflight-prp | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| premature-complexity-is-the-most-common-derivation-failure-mode | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| presentation-claude-code | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| presentation-claude-gemini | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| presentation-vibe-coding | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prevent-domain-specific-failure-modes-through-the-vulnerability-matrix | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| pricing | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pricing-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| pricing-packaging-strategist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| primitives-and-tools | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| principal-software-engineer | frontend | needs-tool-mapping | 75 | Unmapped tools: ['agent', 'edit', 'execute', 'github/*', 'read', 'search', 'todo', 'vscode', 'web/fetch']. |
| prism | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| prisma-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| prisma-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| privacy-compliance-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| privacy-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| privacy-engineer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| private-domain-operator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| privesc-advisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| probe-mock-patterns | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| processing-effort-should-follow-retrieval-demand | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| procurement-compliance-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| prod-logs-health-check | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| producer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-behavioral-nudge-engine | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-boss | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-cynic | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-discovery-strategist | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-feedback-synthesizer | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-management-uses-feedback-pipelines-with-experiment-tracking | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| product-manager-ai | ai | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 3 same-name variants into one canonical agent. |
| product-manager-backend | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. Merged 2 same-name variants into one canonical agent. |
| product-manager-database | database | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| product-manager-research | research | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, google_web_search, read_many_files, ask_user]. Merged 4 same-name variants into one canonical agent. |
| product-org-os | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-pusher | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-rookie | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-sales-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-sprint-prioritizer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-strategist | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. Merged 2 same-name variants into one canonical agent. |
| product-trend-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| product-watcher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| production-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| production-validator | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| productivity-coach | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| productivity-porn-risk-in-meta-system-building | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| professor | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| profile | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| profile-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| profile-general | general | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| profile-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| profiler | performance | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| programmable-notes-could-enable-property-triggered-workflows | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| programmatic-display-buyer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| progress | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| progressive-disclosure-means-reading-right-not-reading-less | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| progressive-schema-validates-only-what-active-modules-require-not-the-full-system-schema | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| project-analyst | research | requires-mcp | 85 | Requires MCP servers: task-master, basic-memory, zen. Merged 2 same-name variants into one canonical agent. |
| project-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| project-architecture-planner | architecture | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'web/fetch', 'edit/editFiles', 'new', 'renderMermaidDiagram', 'openSimpleBrowser', 'runCommands', 'problems', 'usages', 'todo']. |
| project-board-sync | backend | requires-mcp | 85 | Requires MCP servers: claude-flow. |
| project-board-sync-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-coordinator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-curator | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-documenter | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-explorer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-idea-validator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| project-implementer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-management-experiment-tracker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-management-jira-workflow-steward | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-management-project-shepherd | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-management-studio-operations | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-management-studio-producer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-management-uses-decision-tracking-with-stakeholder-context | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-manager | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-manager-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-manager-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| project-manager-senior | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-memory | ai | needs-tool-mapping | 75 | Unmapped tools: []. |
| project-onboarder | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-replace-cli | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| project-scanner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-scanner-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-shepherd | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-shipper | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| project-structure-validator | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-supervisor-orchestrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| project-task-planner | productivity | needs-tool-mapping | 75 | Unmapped tools: Task, ExitPlanMode. |
| prometeo-pm | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| prometheus-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-architect | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| prompt-builder | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'web/fetch', 'githubRepo', 'problems', 'runCommands', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'usages', 'terraform', 'Microsoft, Docs', 'context7']. |
| prompt-claude-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-conductor | ai | needs-tool-mapping | 75 | Unmapped tools: Task. |
| prompt-crafter | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| prompt-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 16 same-name variants into one canonical agent. |
| prompt-evaluation-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-evaluator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-gemini-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-gpt-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-harvester | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-improve-prompt | ai | needs-tool-mapping | 75 | Unmapped tools: ['execute/runInTerminal']. |
| prompt-injection-defender | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-input-craftsman | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| prompt-librarian | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-optimizer | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| prompt-oss-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-psyche-cartographer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-psychometrist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-red-team | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prompt-regression-tester | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| promptiq | ai | needs-tool-mapping | 75 | Unmapped tools: ['execute/runInTerminal', 'search/codebase']. |
| proof | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| proposal-compliance-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| proposal-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| propositional-link-semantics-transform-wiki-links-from-associative-to-reasoned | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| propp | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| prose-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| prospective-memory-requires-externalization | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| prototyper | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| provenance-tracks-where-beliefs-come-from | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| provider-execution | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| provider-mention-routing | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| provider-smoke | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| pseudocode | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| psychologist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| public-comment-drafter | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| public-records-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| publish | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| publishing-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| pulumi-expert | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| pulumi-typescript-specialist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| puppeteer-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| pwa-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| pyspark-expert-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-backend-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-dev | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-development-django-pro | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-engineer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| python-engineer-data | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| python-expert-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-hyx-resilience | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| python-linter | testing | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| python-mcp-server-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-notebook-sample-builder | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'mslearnmcp/*', 'agent', 'ms-python.python/getPythonEnvironmentInfo', 'ms-python.python/getPythonExecutableCommand', 'ms-python.python/installPythonPackage', 'ms-python.python/configurePythonEnvironment', 'ms-toolsai.jupyter/configureNotebook', 'ms-toolsai.jupyter/listNotebookPackages', 'ms-toolsai.jupyter/installNotebookPackages', 'todo']. |
| python-optimizer | performance | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| python-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| python-pro-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| python-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| python-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| python-reviewer-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob"]. |
| python-specialist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-specialist-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| python-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| pytorch-build-resolver | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| pytorch-expert | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| qa | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| qa-automation | testing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| qa-automation-engineer | testing | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| qa-expert | testing | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking, playwright. Merged 5 same-name variants into one canonical agent. |
| qa-judge | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| qa-lead | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| qa-manual-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| qa-specialist | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| qa-test-agent | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| qa-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| qm-fabricator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| qm-indexer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| qm-planner | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| qm-reconciler | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| qm-session-analyst | research | needs-tool-mapping | 75 | Unmapped tools: []. |
| qm-session-doctor | frontend | needs-tool-mapping | 75 | Unmapped tools: []. |
| qm-sprout-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: []. |
| quality-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| quality-fixer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| quality-fixer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| quality-guardian | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| quality-playbook | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| quality-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| quality-system-engineer | testing | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| quant-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| quartermaster | backend | needs-tool-mapping | 75 | Unmapped tools: []. |
| queen-coordinator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| queries-evolve-during-search-so-agents-should-checkpoint | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| query-clarifier | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| query-listener | performance | needs-tool-mapping | 75 | Unmapped tools: ["Bash", "Read", "Write"]. |
| question-answer-metadata-enables-inverted-search-patterns | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| queue | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| quick-smoke-test | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| quickstart | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| quorum-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| quotation-verifier | ai | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| r-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob"]. |
| rabbitmq-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| raft-manager | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| rag-architect | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| rag-pipeline-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| rag-pipeline-reviewer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| rails-activerecord-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| rails-api-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rails-backend-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rails-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| rails-expert-backend | backend | requires-mcp | 85 | Requires MCP servers: context7, basic-memory. Merged 3 same-name variants into one canonical agent. |
| rails-expert-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| rails-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ralph-adapter-system | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| ralph-e2e-verifier | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ralph-loop-runner | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| ramanujan | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| random-note-resurfacing-prevents-write-only-memory | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| ranganathan | cloud | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| rank | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rapid-prototype-scout | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rapid-prototyper | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| rate-limit-communicator | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| rawls | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| react-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| react-component-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| react-expert | frontend | requires-mcp | 85 | Requires MCP servers: context7, basic-memory. Merged 3 same-name variants into one canonical agent. |
| react-native-dev | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| react-native-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| react-nextjs-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| react-performance-optimization | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| react-pro | frontend | requires-mcp | 85 | Requires MCP servers: context7, magic. Merged 3 same-name variants into one canonical agent. |
| react-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| react-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| react18-auditor | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'search', 'search/usages', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'edit/editFiles', 'web/fetch']. |
| react18-batching-fixer | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'search/usages', 'read/problems']. |
| react18-class-surgeon | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'search/usages', 'read/problems']. |
| react18-commander | frontend | needs-tool-mapping | 75 | Unmapped tools: ['agent', 'vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'search/usages', 'read/problems']. |
| react18-dep-surgeon | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'web/fetch']. |
| react18-test-guardian | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'search/usages', 'read/problems']. |
| react19-auditor | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'search', 'search/usages', 'web/fetch', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'edit/editFiles']. |
| react19-commander | frontend | needs-tool-mapping | 75 | Unmapped tools: [. |
| react19-dep-surgeon | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'web/fetch']. |
| react19-migrator | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'search/usages', 'read/problems']. |
| react19-test-guardian | frontend | needs-tool-mapping | 75 | Unmapped tools: ['vscode/memory', 'edit/editFiles', 'execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection', 'search', 'search/usages', 'read/problems']. |
| readability-refactor | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| reader | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| readme-en | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| readme-generator | documentation | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| readme-ja | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| readme-multi-agent | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| readme-zh | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 4 same-name variants into one canonical agent. |
| readme-zh-tw | documentation | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| real-estate-business-development-director | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-buyer-s-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-buyer-seller | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-client-relationship-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-concierge-relocation-specialist | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-creative-director | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-estimator-scope-of-work-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-investment-advisor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-legal-compliance-advisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-listing-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-market-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-property-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| real-estate-tech | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| real-estate-transaction-coordinator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| reality-checker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| realtime | security | requires-mcp | 85 | Requires MCP servers: laravel-boost. |
| realtime-collaboration-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| realtime-websocket-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| realworld-performance-report | performance | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| reasoning-visualizer | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| reasoningbank-learner | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| rebuttal-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Grep", "Glob"]. |
| receipt-verifier | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| recommendation-engine | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| recon-advisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| reconciliation-loops-that-compare-desired-state-to-actual-state-enable-drift-correction-without-continuous-monitoring | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| records-retention-advisor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| recruiter-triage-agent | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| recruitment-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| red | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| reddit-community-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| redis-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| reepl-linkedin | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| refactor | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| refactor-cleaner | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| refactor-productivity | productivity | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, replace, write_todos, activate_skill, read_many_files, ask_user]. Merged 2 same-name variants into one canonical agent. |
| refactor-prompt | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| refactor-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| refactor-surgeon | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| refactorer | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 2 same-name variants into one canonical agent. |
| refactorer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| refactoring-advisor | testing | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| refactoring-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| refactoring-specialist-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| refactoring-specialist-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| refactoring-specialist-writing | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| reference | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| reference-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| refine-requirement-or-issue | frontend | needs-tool-mapping | 75 | Unmapped tools: [, 'list_issues', 'githubRepo', 'search', 'add_issue_comment', 'create_issue', 'create_issue_comment', 'update_issue', 'delete_issue', 'get_issue', 'search_issues']. |
| refinement | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| refinement-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| reflection-synthesizes-existing-notes-into-new-insight | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| regulatory-monitor | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| reinforcement-learning-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| rejewski | ci-cd | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| relay | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| release-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| release-lead | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| release-manager | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. Merged 9 same-name variants into one canonical agent. |
| release-prep | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| release-swarm | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| relevance-check | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| relevance-summary | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| reliability-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| remix-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| remote-agent-dispatcher | ai | needs-tool-mapping | 75 | Unmapped tools: ["Bash", "Read"]. |
| remove-deadcode | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rene-descartes | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| repo-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| repo-architect-agent | ai | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "editFiles", "fetch", "new", "problems", "runCommands", "search", "terminalLastCommand"]. |
| repo-author | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| repo-layout | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| repo-scanner | frontend | needs-tool-mapping | 75 | Unmapped tools: "Read, triage:search_issues, triage:inspect_recent_commits, triage:inspect_code_paths, triage:check_recent_deploys". |
| repo-warden | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| report-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| report-compiler-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| report-distribution-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| report-generator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| report-generator-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| report-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: find. |
| report-reviser | writing | needs-tool-mapping | 75 | Unmapped tools: find. |
| report-writer | writing | needs-tool-mapping | 75 | Unmapped tools: find. |
| reporting-narrative | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| reproduce-issue | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| requirement-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| requirement-parser | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| requirements-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| requirements-analyst-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| research | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| research-agent | research | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| research-agent-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| research-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| research-architect-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-brief-generator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-codebase | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-coordinator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-daily-ops | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-data-curator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-dossier-writer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-expert | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| research-guardian | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-librarian | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-methods-reviewer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-orchestrator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-question-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-scientist | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| research-synthesizer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| research-writer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 12 same-name variants into one canonical agent. |
| resilience-engineer | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 2 same-name variants into one canonical agent. |
| resource-allocator | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| resource-management | mobile | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| resource-staleness-report | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| resp | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| responsible-ai-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| responsive-strategist | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| rest-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| resume-tailor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| retail-customer-returns | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| retrieval-utility-should-drive-design-over-capture-completeness | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| retrieval-verification-loop-tests-description-quality-at-scale | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| revenue-tracker | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| reverse-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| review | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| review-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-context | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-conventions | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-correctness | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-docs | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-fact-checker | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-frontend | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| review-judge | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-maintainability | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-notes | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| review-policy-author | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-prep | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| review-validator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| reviewer-academic | writing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| reviewer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| reviewer-backend | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Glob", "Grep", "Bash"]. Merged 2 same-name variants into one canonical agent. |
| reviewer-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: find. Merged 2 same-name variants into one canonical agent. |
| reviewer-general | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| reviewer-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| revision-coach-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| rfp-response-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| risk-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| risk-manager | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| risk-manager-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| risk-manager-devops | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| risk-manager-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| risk-of-bias-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| risk-scorer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| roadmap-planner | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| roblox-avatar-creator | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| roblox-experience-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| roblox-systems-scripter | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| robotics-engineer | productivity | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| rogerfisher | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| rogers | performance | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| role-analysis-reviewer-agent | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| role-field-makes-graph-structure-explicit | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rollup-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| roo-cli-interface | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| root | ai | needs-tool-mapping | 75 | Unmapped tools: []. |
| rosalind-franklin | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| rough-idea | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| rough-idea-for-implementation | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| rtk-testing-specialist | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| rubber-duck | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| rubber-duck-debugger | testing | requires-mcp | 85 | Requires MCP servers: basic-memory, sequential-thinking. |
| ruby-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| ruby-mcp-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ruby-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| rug | ai | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo']. |
| rule-advisor | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| run-operator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| run-supervisor | writing | needs-tool-mapping | 75 | Unmapped tools: Bash(run-controller, start:*), Bash(run-controller, watch:*), Bash(run-controller, status:*), SendMessage. |
| rust-auditor | security | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. |
| rust-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| rust-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| rust-engineer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rust-engineer-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| rust-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| rust-expert-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. |
| rust-mcp-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rust-pro | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| rust-pro-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rust-refactoring-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| rust-reviewer | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| rust-rtk | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| rust-systems | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| safety-specialist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| safla-neural | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| sage-council | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| sales-automator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| sales-automator-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sales-coach | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| sales-data-extraction-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| sales-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sales-engineer-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| sales-engineer-frontend | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| sales-engineer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| sales-outreach | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| salesforce-apex-triggers-development | testing | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| salesforce-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| salesforce-expert-agent | ai | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'sfdx-mcp/*', 'agent', 'todo']. |
| salesforce-flow-development | productivity | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| salesforce-ui-development-aura-lwc | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| salesforce-visualforce-development | architecture | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| sample | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sandbox-threat-model | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| sanity-check | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sast | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| sast-sca-security-analyzer | security | needs-tool-mapping | 75 | Unmapped tools: ["search/codebase", "search", "edit/editFiles", "web/fetch", "read/terminalLastCommand"]. |
| scada-attacker | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| scaffolder | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| scaffolding-enables-divergence-that-fine-tuning-cannot | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| scala-coder | frontend | requires-mcp | 85 | Requires MCP servers: scala-semantic. |
| scala-developer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| scala-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| scala-pro | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| scan-inventory | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| scan-researcher | research | needs-tool-mapping | 75 | Unmapped tools: Agent(claude-security:explore). |
| scan-verifier | backend | needs-tool-mapping | 75 | Unmapped tools: Agent(claude-security:explore). |
| scheduler | frontend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| schelling | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| schema | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| schema-enforcement-via-validation-agents-enables-soft-consistency | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| schema-evolution-follows-observe-then-formalize-not-design-then-enforce | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| schema-field-names-are-the-only-domain-specific-element-in-the-universal-note-pattern | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| schema-fields-should-use-domain-native-vocabulary-not-abstract-terminology | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| schema-templates-reduce-cognitive-overhead-at-capture-time | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| schema-validation-hooks-externalize-inhibitory-control-that-degrades-under-cognitive-load | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| schon | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| scientific-literature-researcher | research | requires-mcp | 85 | Requires MCP servers: bgpt. Merged 2 same-name variants into one canonical agent. |
| scientific-paper-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| scientist | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| scikit-learn-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| scope | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| scope-discoverer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| scope-guard | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| score | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| scout | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| scout-ai | ai | needs-tool-mapping | 75 | Unmapped tools: find. Merged 3 same-name variants into one canonical agent. |
| scout-backend | backend | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| scout-explorer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| scout-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| scout-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| scout-security | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| scribe | writing | needs-tool-mapping | 75 | Unmapped tools: [Read, Grep]. Merged 2 same-name variants into one canonical agent. |
| scrum-master | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| scrum-master-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| scrum-master-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| se-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search', 'web/fetch']. |
| se-devops-ci | devops | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| se-product-manager | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'githubRepo', 'create_issue', 'update_issue', 'list_issues', 'search_issues']. |
| se-responsible-ai | accessibility | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search']. |
| se-security | security | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search', 'problems']. |
| se-tech-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search', 'web/fetch']. |
| se-ux-designer | frontend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'search', 'web/fetch']. |
| search-ai-optimization-expert | performance | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'web/fetch', 'githubRepo', 'terminalCommand', 'edit/editFiles', 'problems']. |
| search-query-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| search-relevance-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| search-specialist | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| search-specialist-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| search-specialist-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| search-specialist-frontend | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| searcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| secrets-credential-hygiene-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| secrets-detector | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| section-508-accessibility-specialist | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| secure-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| secure-reviewer-ai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| secure-reviewer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| security-architect | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| security-architect-aidefence | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-audit | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-auditor | security | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 21 same-name variants into one canonical agent. |
| security-auditor-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-code-pr-reviewer | security | needs-tool-mapping | 75 | Unmapped tools: BashOutput. |
| security-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 10 same-name variants into one canonical agent. |
| security-expert | security | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. |
| security-fix-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-manager | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-research | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-researcher | security | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| security-review-prompt | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| security-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 17 same-name variants into one canonical agent. |
| security-scanner | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| security-specialist | security | requires-mcp | 85 | Requires MCP servers: basic-memory, zen. Merged 2 same-name variants into one canonical agent. |
| security-threat-modeler | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| seed-architect | architecture | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| seed-closer | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| selenium-expert | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| self-extension-requires-context-files-to-contain-platform-operations-knowledge-not-just-methodology | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| semantic-evaluator | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| semantic-model-auditor | security | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob", "Bash"]. |
| semmelweis | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| senior-backend-architect | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-cloud-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-code-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-frontend-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-product-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-project-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-secops-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| senior-software-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| sense-making-vs-storage-does-compression-lose-essential-nuance | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| sensei-junior-mentor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sensitivity-reader | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| sentinel | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| seo-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-authority-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-backlinks | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-cannibalization-detector | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-cluster | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-cluster-architecture | architecture | requires-mcp | 85 | Requires MCP servers: exa, fuse-browser, sequential-thinking. |
| seo-content | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| seo-content-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-content-planner | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-content-refresher | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-content-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-dataforseo | research | requires-mcp | 85 | Requires MCP servers: dataforseo. |
| seo-drift | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-ecommerce | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-expert | ai | requires-mcp | 85 | Requires MCP servers: exa, sequential-thinking, fuse-browser. |
| seo-flow | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-geo | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| seo-google | backend | needs-tool-mapping | 75 | Unmapped tools: #, needed, for, report/data, file, output. |
| seo-image-gen | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-images | security | requires-mcp | 85 | Requires MCP servers: fuse-browser. |
| seo-keyword-strategist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-local | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-local-security | security | requires-mcp | 85 | Requires MCP servers: exa, sequential-thinking, fuse-browser. |
| seo-maps | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-meta-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-podcast-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-schema | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| seo-sitemap | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-sitemap-research | research | requires-mcp | 85 | Requires MCP servers: fuse-browser. |
| seo-snippet-hunter | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| seo-specialist-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| seo-specialist-performance | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| seo-specialist-security | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| seo-strategist | architecture | needs-tool-mapping | 75 | Unmapped tools: [Read, WebFetch]. |
| seo-structure-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-sxo | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| seo-technical | security | needs-tool-mapping | 75 | Unmapped tools: #, needed, for, report/data, file, output. Merged 2 same-name variants into one canonical agent. |
| seo-visual | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| sequelize-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| serv | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| server | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| serverless-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| service-mesh-expert | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| session | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| session-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-boundary-hooks-implement-cognitive-bookends-for-orientation-and-reflection | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-end | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-handoff-creates-continuity-without-persistent-memory | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-investigator | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-manager | backend | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master, sequential-thinking, zen. |
| session-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-outputs-are-packets-for-future-selves | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-start | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| session-system | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| session-transcript-mining-enables-experiential-validation-that-structural-tests-cannot-provide | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| severity-triage | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| shadcn-ui-expert | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, shadcn, fuse-browser. |
| shannon | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| shellgate | linux | requires-mcp | 85 | Requires MCP servers: shellgate. |
| shepherd | documentation | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. |
| shield | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| shipwright | frontend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| shopify-expert | backend | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'terminalCommand', 'edit/editFiles', 'web/fetch', 'githubRepo', 'runTests', 'problems']. |
| short-video-editing-coach | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sidekiq-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| siem | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| signal-explorer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| signals-cli | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| silence-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| silence-composer | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| silent-failure-hunter | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| silent-failure-hunter-ai | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| silicon-friendly | ai | needs-tool-mapping | 75 | Unmapped tools: Task. |
| simon | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| simple-code-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| simple-code-reviewer-machine-learning | machine-learning | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| simplifier | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| simplifier-frontend | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 2 same-name variants into one canonical agent. |
| simulation | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| sisyphus-ultraworker | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| site-reliability-engineer | devops | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 3 same-name variants into one canonical agent. |
| skill-auditor | security | needs-tool-mapping | 75 | Unmapped tools: #, for, finding, anti-patterns, across, examples, for, validating, referenced, file, patterns, exist. Merged 3 same-name variants into one canonical agent. |
| skill-bundle-routing | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| skill-context-budgets-constrain-knowledge-system-complexity-on-agent-platforms | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| skill-evaluator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| skill-extractor | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| skill-improver | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| skill-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob"]. |
| skills-encode-methodology-so-manual-execution-bypasses-quality-gates | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| slack-archaeologist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| slack-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| slack-expert-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| slack-expert-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| slash-command-auditor | security | needs-tool-mapping | 75 | Unmapped tools: #, for, finding, anti-patterns, for, validating, referenced, file, patterns, exist. |
| sleuth | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| slop-hunter | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| slop-remover | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| small-world-topology-requires-hubs-and-dense-local-links | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| smart-agent-router | ai | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| smartpack-0vvvnb-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-0vvvnb-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-3b0gx7-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-3b0gx7-reviewer-1 | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-9pjhy5-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-9pjhy5-planner-1 | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-9pjhy5-reviewer-1 | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-aodz7v-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-aodz7v-planner-1 | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-aodz7v-reviewer-1 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-c8vcdx-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-dispatch-log | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-i0u93q-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-i0u93q-planner-1 | security | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-i0u93q-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-janrlf-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-janrlf-planner-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-janrlf-reviewer-1 | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpack-pr-draft | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-z0c9fd-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-z0c9fd-planner-1 | windows | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpack-z0c9fd-reviewer-1 | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpackdebt-dispatch-log | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-dsmh31-executor-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-dsmh31-planner-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-dsmh31-reviewer-1 | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpackdebt-exg19y-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-exg19y-planner-1 | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-exg19y-reviewer-1 | windows | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpackdebt-inexon-executor-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-inexon-executor-2 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-inexon-planner-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-inexon-planner-2 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-inexon-reviewer-1 | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpackdebt-inexon-reviewer-2 | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| smartpackdebt-ji2847-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| smartpackdebt-ji2847-reviewer-1 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| smoke-test | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| snapcompact-archive-context | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| sniper | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, fuse-browser. |
| sniper-faster | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, fuse-browser. |
| snow | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| sns-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-author | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-content-generator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-manager | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-media-clip-creator | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-media-copywriter | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-media-publisher | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| social-media-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-network-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| social-publishing-publisher | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| socrates | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| socratic-interviewer | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| socratic-mentor-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| software-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| software-engineer-agent | ai | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'search/codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'github']. |
| software-engineering-expert | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory, zen. |
| software-engineering-lead | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| solid-orchestrator | security | needs-tool-mapping | 75 | Unmapped tools: Task. |
| solidity-smart-contract-engineer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| solidjs-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| solo-founder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| solution-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: AskUserQuestion. Merged 2 same-name variants into one canonical agent. |
| solution-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| solutions-architect | architecture | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, google_web_search, read_many_files, ask_user, web_fetch]. Merged 2 same-name variants into one canonical agent. |
| solver | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| sona-learning-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| sonnet-reviewer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| soul | research | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| soul-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| soul-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| soul-general | general | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| soul-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| soul-testing | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| soul-writing | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| sound-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| source-attribution-enables-tracing-claims-to-foundations | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| source-extractor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| source-layout | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| source-pin | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| source-verification-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| source-verification-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| sovereign-health-systems-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| sow-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| spaced-repetition-scheduling-could-optimize-vault-maintenance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| sparc-orchestrator | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| spark | data | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. Merged 2 same-name variants into one canonical agent. |
| spatial-data-engineer | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| spatial-data-scientist | data | fully-compatible | 100 | Converted directly; no manual steps required. |
| spec-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| spec-analyzer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| spec-architect | architecture | requires-mcp | 85 | Requires MCP servers: sequential-thinking. |
| spec-developer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| spec-miner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| spec-orchestrator | productivity | requires-mcp | 85 | Requires MCP servers: sequential-thinking. |
| spec-planner | productivity | requires-mcp | 85 | Requires MCP servers: sequential-thinking. |
| spec-reviewer | productivity | needs-tool-mapping | 75 | Unmapped tools: []. |
| spec-reviewer-backend | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| spec-reviewer-security | security | requires-mcp | 85 | Requires MCP servers: ESLint, ide. |
| spec-tester | testing | needs-tool-mapping | 75 | Unmapped tools: Task. |
| spec-validator | testing | requires-mcp | 85 | Requires MCP servers: ide, sequential-thinking. |
| specialized-developer-advocate | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| specialized-mcp-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| specialized-model-qa | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| specialized-workflow-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| specification | backend | needs-tool-mapping | 75 | Unmapped tools: ['search/codebase', 'search/usages', 'edit/editFiles', 'vscode/extensions', 'web/fetch', 'vscode/openSimpleBrowser', 'read/problems', 'execute/runTests', 'read/terminalLastCommand', 'read/terminalSelection', 'execute/testFailure', 'vscode/vscodeAPI']. |
| specification-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| specifier | frontend | requires-mcp | 85 | Requires MCP servers: serena, sequential-thinking. |
| spine | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sponsored-projects-coordinator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| spreading-activation-models-how-agents-should-traverse | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| spring-boot-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| spring-boot-engineer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| spring-boot-engineer-cloud | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| spring-boot-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| sprint-prioritizer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| sprint-prioritizer-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| sql-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| sql-pro | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 7 same-name variants into one canonical agent. |
| sqlite-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| sqs-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| sre-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| sre-incident-responder | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| sre-site-reliability-engineer | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| stackhawk-security-onboarding | security | needs-tool-mapping | 75 | Unmapped tools: ['read', 'edit', 'search', 'shell', 'stackhawk-mcp/*']. |
| stackoverflow | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| stakeholder-map-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| stale-navigation-actively-misleads-because-agents-trust-curated-maps-completely | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| standards-ethics-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| standards-writing | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| starlight-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| starlight-orchestrator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| startup-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| startup-cto | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| state-tracker-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| statistician | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| statusline-setup | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Edit]. |
| stig-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| stigmergy-coordinates-agents-through-environmental-traces-without-direct-communication | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| storage-versus-thinking-distinction-determines-which-tool-patterns-apply | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| strategist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| strategist-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| strategy-duel-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| strauss | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| stream-craftsman | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| streaming | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| stripe-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| stripe-payments-integrator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| structure-architect-agent | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| structure-enables-navigation-without-reading-everything | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| structure-without-processing-provides-no-value | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| student-learning-uses-prerequisite-graphs-with-spaced-retrieval | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| studio-coach | frontend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| studio-operations | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| studio-producer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| studio-producer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| study-abroad-advisor | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| subagent-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| sublinear-goal-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| success-pattern-learner | security | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| sugar-orchestrator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| summarization-system | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| summarize | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| summary | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| summary-coherence-tests-composability-before-filing | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| supply-chain-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| supply-chain-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| support-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| support-automation-engineer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| support-responder | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| support-responder-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| support-triage-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| surge | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| surveyor | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| svelte-developer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| svelte-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| svelte-pro | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| svg-reviewer | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Grep", "Glob"]. |
| sw-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| swarm-issue | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| swarm-memory-manager | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| swarm-orchestrator | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| swarm-pr | embedded | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| swe | testing | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo']. |
| swift-build-resolver | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| swift-developer | mobile | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| swift-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| swift-ios-pro | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| swift-mcp-expert | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| swift-reviewer | mobile | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| swiftui-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| symfony-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| symfony-specialist-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| sync-coordinator | backend | requires-mcp | 85 | Requires MCP servers: github, claude-flow. |
| sync-coordinator-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| synthesis-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| system-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| system-prompt | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| system-prompt-flash | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| systems-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| systems-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| table-craftsman | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| tag-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tag-rot-applies-to-wiki-links-because-titles-serve-as-both-identifier-and-display-text | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| tailwind-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tailwind-frontend-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tailwindcss-expert | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, gemini-design, fuse-browser. |
| taleb | ai | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| tanstack-start-expert | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, shadcn, gemini-design, fuse-browser. |
| tasarim-kurator | frontend | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| task | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| task-checker | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| task-coordinator | productivity | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| task-decomposer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-decomposition-expert | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-distributor | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| task-executor | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| task-executor-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-generator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-manager | productivity | needs-tool-mapping | 75 | Unmapped tools: []. |
| task-master-initialization-specialist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-master-template-manager | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-orchestrator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| task-plan-architect | architecture | requires-mcp | 85 | Requires MCP servers: scala-semantic. |
| task-planner | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-planner-instructions | productivity | needs-tool-mapping | 75 | Unmapped tools: ["changes", "search/codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runNotebooks", "runTests", "search", "search/searchResults", "runCommands/terminalLastCommand", "runCommands/terminalSelection", "testFailure", "usages", "vscodeAPI", "terraform", "Microsoft, Docs", "azure_get_schema_for_Bicep", "context7"]. |
| task-prioritizer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| task-researcher-instructions | research | needs-tool-mapping | 75 | Unmapped tools: ["changes", "codebase", "edit/editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runNotebooks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "terraform", "Microsoft, Docs", "azure_get_schema_for_Bicep", "context7"]. |
| task-tree-triage | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| tauri-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tax-strategist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| taxcore-technical-writer | writing | needs-tool-mapping | 75 | Unmapped tools: ["codebase"]. |
| tdd-developer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| tdd-green-phase-make-tests-pass-quickly | testing | needs-tool-mapping | 75 | Unmapped tools: ['github/*', 'search/fileSearch', 'edit/editFiles', 'execute/runTests', 'execute/runInTerminal', 'execute/getTerminalOutput', 'execute/testFailure', 'read/readFile', 'read/terminalLastCommand', 'read/terminalSelection', 'read/problems', 'search/codebase']. |
| tdd-guide | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| tdd-london-swarm | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| tdd-prompt | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| tdd-red-phase-write-failing-tests-first | testing | needs-tool-mapping | 75 | Unmapped tools: ["github/*", "search/fileSearch", "edit/editFiles", "execute/runTests", "execute/runInTerminal", "execute/getTerminalOutput", "execute/testFailure", "read/readFile", "read/terminalLastCommand", "read/terminalSelection", "read/problems", "search/codebase"]. |
| tdd-refactor-phase-improve-quality-security | testing | needs-tool-mapping | 75 | Unmapped tools: ["github/*", "search/fileSearch", "edit/editFiles", "execute/runTests", "execute/runInTerminal", "execute/getTerminalOutput", "execute/testFailure", "read/readFile", "read/terminalLastCommand", "read/terminalSelection", "read/problems", "search/codebase"]. |
| team-configurator | backend | requires-mcp | 85 | Requires MCP servers: task-master, basic-memory, zen. |
| team-configurator-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| team-debugger | testing | needs-tool-mapping | 75 | Unmapped tools: TaskGet, TaskUpdate, SendMessage. |
| team-implementer | frontend | needs-tool-mapping | 75 | Unmapped tools: TaskGet, TaskUpdate, SendMessage. |
| team-lead | ai | needs-tool-mapping | 75 | Unmapped tools: Agent, TeamCreate, TeamDelete, TaskCreate, TaskGet, TaskUpdate, SendMessage. |
| team-lead-task-breakdown | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| team-reviewer | testing | needs-tool-mapping | 75 | Unmapped tools: TaskGet, TaskUpdate, SendMessage. |
| team-supervisor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| team-supervisor-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| team-worker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| team-worker-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tech-lead | productivity | needs-tool-mapping | 75 | Unmapped tools: []. |
| tech-lead-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| tech-lead-orchestrator | frontend | requires-mcp | 85 | Requires MCP servers: task-master, basic-memory. |
| tech-lead-orchestrator-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tech-lead-orchestrator-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| tech-writer | writing | needs-tool-mapping | 75 | Unmapped tools: find, fetch_content, fetch_content_cloak, get_search_content, code_search, codegraph_explore. |
| techdebt-csedqi-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| techdebt-csedqi-planner-1 | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| techdebt-csedqi-reviewer-2 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| techdebt-d3c6b0-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| techdebt-d3c6b0-reviewer-1 | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| techdebt-laimst-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| techdebt-n5uqeo-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| techdebt-n5uqeo-reviewer-1 | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| technical-artist | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| technical-consultant | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-content-evaluator | writing | needs-tool-mapping | 75 | Unmapped tools: ['edit', 'search', 'shell', 'web/fetch', 'runTasks', 'githubRepo', 'todos', 'runSubagent']. |
| technical-cto-advisor | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-debt-collector | testing | requires-mcp | 85 | Requires MCP servers: basic-memory. |
| technical-debt-remediation-plan | writing | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runTasks', 'runTests', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'github']. |
| technical-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-designer-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-director | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-planner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-sales-engineer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| technical-spike-research-mode | research | needs-tool-mapping | 75 | Unmapped tools: ['vscode', 'execute', 'read', 'edit', 'search', 'web', 'agent', 'todo']. |
| technical-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 8 same-name variants into one canonical agent. |
| technology-scout | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| telemetry-analyzer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| template-design-experts | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| temporal-media-must-convert-to-spatial-text-for-agent-traversal | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| temporal-processing-priority-creates-age-based-inbox-urgency | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| temporal-python-pro | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| temporal-separation-of-capture-and-processing-preserves-context-freshness | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ten-universal-primitives-form-the-kernel-of-every-viable-agent-knowledge-system | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tension-composer | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| tensorflow-expert | machine-learning | fully-compatible | 100 | Converted directly; no manual steps required. |
| terminal-helper | linux | needs-tool-mapping | 75 | Unmapped tools: ['execute/getTerminalOutput', 'execute/runInTerminal', 'read/terminalLastCommand', 'read/terminalSelection']. |
| terminal-integration-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| terminology-reviewer | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| terms | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| terra | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| terraform-agent | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ['read', 'edit', 'search', 'shell', 'terraform/*']. |
| terraform-architect | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| terraform-aws-implement | infrastructure | needs-tool-mapping | 75 | Unmapped tools: [execute/getTerminalOutput, execute/runInTerminal, read/problems, read/readFile, read/terminalSelection, read/terminalLastCommand, agent, edit/createDirectory, edit/createFile, edit/editFiles, search, web/fetch, todo]. |
| terraform-aws-planning | infrastructure | needs-tool-mapping | 75 | Unmapped tools: [read/readFile, read/viewImage, edit/editFiles, search, web/fetch, todo]. |
| terraform-engineer | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| terraform-expert | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| terraform-iac-reviewer | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'edit/editFiles', 'terminalCommand', 'search', 'githubRepo']. |
| terraform-specialist | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| terragrunt-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| terratest-module-testing | testing | needs-tool-mapping | 75 | Unmapped tools: ["codebase", "terminalCommand"]. |
| test | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-action-planning-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| test-architect | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| test-automation-engineer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| test-automation-expert | testing | requires-mcp | 85 | Requires MCP servers: basic-memory, zen. |
| test-automator | testing | requires-mcp | 85 | Requires MCP servers: context7, playwright. Merged 8 same-name variants into one canonical agent. |
| test-checker | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| test-context-search-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| test-debugger | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-engineer | testing | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 11 same-name variants into one canonical agent. |
| test-fix-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| test-generator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-long-runner | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-results-analyzer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| test-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-runner | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| test-strategist | testing | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| test-strategy-architect | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-structure | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| test-writer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| test-writer-fixer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testcafe-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testcases-manual | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| testing | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| testing-accessibility-auditor | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-api-tester | testing | requires-mcp | 85 | Requires MCP servers: vue-docs, nuxt-ui-remote, nuxt-remote. |
| testing-effect-could-enable-agent-knowledge-verification | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-evidence-collector | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-infrastructure | infrastructure | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| testing-performance-benchmarker | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-reality-checker | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-test-results-analyzer | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-tool-evaluator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| testing-workflow-optimizer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| text-comparison-validator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| text-vs-stream-json | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| the-agentskills-standard-embodies-progressive-disclosure-at-the-skill-level | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-balcony | backend | needs-tool-mapping | 75 | Unmapped tools: []. |
| the-derivation-engine-improves-recursively-as-deployed-systems-generate-observations | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-determinism-boundary-separates-hook-methodology-from-skill-methodology | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-fix-versus-report-decision-depends-on-determinism-reversibility-and-accumulated-trust | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-generation-effect-requires-active-transformation-not-just-storage | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-no-wrong-patches-guarantee-ensures-any-valid-module-combination-produces-a-valid-system | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-system-is-the-argument | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-vault-constitutes-identity-for-agents | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| the-vault-methodology-transfers-because-it-encodes-cognitive-science-not-domain-specifics | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| therapy-journal-uses-warm-personality-with-pattern-detection-for-emotional-processing | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| thinking-beast-mode | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| thomas-edison | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| thompson | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| thoughts-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| thoughts-locator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| threadmode-to-documentmode-transformation-is-the-core-value-creation-step | ci-cd | fully-compatible | 100 | Converted directly; no manual steps required. |
| threat-detection-engineer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| threat-intelligence-analyst | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| threat-modeler | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| threat-modeling-expert | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| three-capture-schools-converge-through-agent-mediated-synthesis | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| three-concurrent-maintenance-loops-operate-at-different-timescales-to-catch-different-classes-of-problems | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| throughput-matters-more-than-accumulation | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tiktok-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tiktok-strategist-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| time-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| time-agent-pkt | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| timeline-extraction-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| timestamp-precision-specialist | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| title-as-claim-enables-traversal-as-reasoning | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| title-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| titletext-fixtures | general | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| titus | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| todo | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 2 same-name variants into one canonical agent. |
| token | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| token-economist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| token-keeper | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| tone | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tool-batch-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| tool-call-presenter | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| tool-evaluator | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| tool-evaluator-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tool-expert | backend | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| tooling-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| tooling-engineer-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tooling-engineer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| tools-evasion-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tools-programmer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| topic-generator | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| topic-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| topological-organization-beats-temporal-for-knowledge-work | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| topology-optimizer | performance | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| touch | mobile | fully-compatible | 100 | Converted directly; no manual steps required. |
| toulmin | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| tour-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| trace | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tracer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tracking-measurement-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| trading-predictor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| trading-strategist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| trading-uses-conviction-tracking-with-thesis-outcome-correlation | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| traffic-analyzer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| traffic-intelligence | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| trails-transform-ephemeral-navigation-into-persistent-artifacts | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| transcript-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| transform-universal-vocabulary-to-domain-native-language-through-six-levels | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| translate | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| translation-lang-worker | writing | needs-tool-mapping | 75 | Unmapped tools: Skill, Agent. |
| translation-reviewer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| translator | general | fully-compatible | 100 | Converted directly; no manual steps required. |
| travel-planner | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| trend-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| trend-forecaster | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| trend-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| triage | ai | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| triage-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| triage-productivity | productivity | requires-mcp | 85 | Requires MCP servers: scala-semantic. |
| triage-router | networking | fully-compatible | 100 | Converted directly; no manual steps required. |
| triage-summarizer | frontend | needs-tool-mapping | 75 | Unmapped tools: "Read, triage:parse_review_command". |
| triz-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| trojan-skill-hunter | ai | needs-tool-mapping | 75 | Unmapped tools: ['codebase', 'search', 'usages', 'problems', 'edit/editFiles', 'githubRepo']. |
| trpc-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tune | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| turing | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| tutti-cli | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| tutti-handoff | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| tutti-model-allocation | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| tutti-model-allocation-model-tiers | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| tutti-runtime | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| twitter-ai-influencer-manager | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| twitter-engager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| twitter-engager-ai | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| type-consolidator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| type-design-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| type-field-enables-structured-queries-without-folder-hierarchies | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| typeorm-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| types | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| typescript-cockatiel-resilience | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-expert | frontend | requires-mcp | 85 | Requires MCP servers: context7, exa, sequential-thinking, fuse-browser. Merged 2 same-name variants into one canonical agent. |
| typescript-expert-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-mcp-server-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-pino-logging | cloud | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-pro | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-pro-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-pro-database | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-pro-frontend | frontend | requires-mcp | 85 | Requires MCP servers: context7, sequential-thinking. Merged 3 same-name variants into one canonical agent. |
| typescript-pro-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| typescript-specialist | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-specialist-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| typescript-specialist-backend | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| ue-blueprint-specialist | architecture | needs-tool-mapping | 75 | Unmapped tools: Task. |
| ue-gas-specialist | architecture | needs-tool-mapping | 75 | Unmapped tools: Task. |
| ue-replication-specialist | architecture | needs-tool-mapping | 75 | Unmapped tools: Task. |
| ue-umg-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| ui-analyzer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-architect | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| ui-auditor | frontend | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| ui-design-agent | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 9 same-name variants into one canonical agent. |
| ui-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-finish-gate-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-fixer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-programmer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-spec-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-test-agent | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-ux-design-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-ux-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 6 same-name variants into one canonical agent. |
| ui-ux-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-ux-master | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ui-ux-tester | frontend | needs-tool-mapping | 75 | Unmapped tools: chrome-mcp, computer-use. Merged 2 same-name variants into one canonical agent. |
| ui-visual-validator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ultimate-transparent-thinking-beast-mode | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| unbloat-remediator | frontend | needs-tool-mapping | 75 | Unmapped tools: [Bash, Edit]. |
| unit-test-generator | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| unity-addressables-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| unity-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| unity-developer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| unity-dots-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| unity-editor-tool-developer | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| unity-multiplayer-engineer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| unity-shader-graph-artist | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| unity-shader-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| unity-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| unity-ui-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: Task. |
| universal-executor | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| universal-executor-research | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| universal-janitor | productivity | needs-tool-mapping | 75 | Unmapped tools: [vscode/extensions, vscode/getProjectSetupInfo, vscode/installExtension, vscode/newWorkspace, vscode/runCommand, vscode/vscodeAPI, execute/getTerminalOutput, execute/runTask, execute/createAndRunTask, execute/runTests, execute/runInTerminal, execute/testFailure, execute/getTaskOutput, read/terminalSelection, read/terminalLastCommand, read/problems, read/readFile, 'github/*', edit/editFiles, search, web]. |
| universal-pr-comment-addresser | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| universal-reviewer | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| unreal-multiplayer-architect | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| unreal-specialist | game-development | needs-tool-mapping | 75 | Unmapped tools: Task. |
| unreal-systems-engineer | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| unreal-technical-artist | game-development | fully-compatible | 100 | Converted directly; no manual steps required. |
| unreal-world-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| unsticker | research | needs-tool-mapping | 75 | Unmapped tools: [Read, Bash]. |
| uplift-migrator | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| url-context-validator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| url-link-extractor | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| use-case-presets-dissolve-the-tension-between-composability-and-simplicity | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| uswds-developer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ux | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ux-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ux-design-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ux-designer | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. Merged 10 same-name variants into one canonical agent. |
| ux-flow-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| ux-researcher | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| ux-researcher-research | research | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| v2-improvements | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| v3-integration-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| v3-memory-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| v3-performance-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| v3-queen-coordinator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| v3-security-architect | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| v4-flash-worker | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| validate-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| validation-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| validation-archivist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| varela | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| vault-conventions-may-impose-hidden-rigidity-on-thinking | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vault-librarian | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| vault-migrator | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| vect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vector-database-engineer | database | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. Merged 2 same-name variants into one canonical agent. |
| vector-db-expert | database | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| vector-engineer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| vendor-risk-reviewer | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| vendor-scorecard-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| ventris | research | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| verbatim-risk-applies-to-agents-too | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| verification-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| verification-checklist | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| verification-runner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| verification-specialist | backend | requires-mcp | 85 | Requires MCP servers: basic-memory, context7, sequential-thinking, zen. |
| verified-endpoint-output | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| verifier | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| verifier-ai | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| verifier-frontend | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| version-delta-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| vertex-engine-inspector | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| vibe-coding-coach | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vibe-coding-coordinator | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory, task-master, context7, sequential-thinking, zen. |
| vibe-explainer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vibe-explorer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vibe-notetaking-is-the-emerging-industry-consensus-for-ai-native-self-organization | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| vibe-worker | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| video-editor | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| video-optimization-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| video-prompt-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| video-streaming-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| vigil | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| vincent-van-gogh | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| viral-content-strategist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| vision-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| visionary | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| visionary-manifestos-master | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| visionos-spatial-engineer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| visual-analysis-ocr | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| visual-asset-generator | ai | requires-mcp | 85 | Requires MCP servers: prompt-to-asset. |
| visual-asset-generator-backend | backend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| visual-brand-guidelines | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| visual-director | ai | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| visual-guardian | accessibility | fully-compatible | 100 | Converted directly; no manual steps required. |
| visual-regression-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| visual-storyteller | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| visual-tester | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| visualization-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| vitest-expert | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| vivid-memories-need-verification | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| voice-ai-integration-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| voice-assistant | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| voice-capture-is-the-highest-bandwidth-channel-for-agent-delegated-knowledge-systems | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| void-painter | productivity | needs-tool-mapping | 75 | Unmapped tools: [view, grep]. |
| volt | embedded | fully-compatible | 100 | Converted directly; no manual steps required. |
| vonneumann | game-development | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| vs-code-insiders-accessibility-tracker | accessibility | needs-tool-mapping | 75 | Unmapped tools: ['github/search_issues', 'github/issue_read', 'read']. |
| vscode-extension | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| vscode-tour-expert | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| vue-component-architect | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| vue-expert | frontend | requires-mcp | 85 | Requires MCP servers: basic-memory. Merged 5 same-name variants into one canonical agent. |
| vue-nuxt-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vue-pro | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vue-reviewer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vue-specialist | frontend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| vuln-scanner | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| vuln-verifier | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| vulnerability-analyst | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| vulnerability-reviewer | security | needs-tool-mapping | 75 | Unmapped tools: Agent. |
| vygotsky | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| warden | database | fully-compatible | 100 | Converted directly; no manual steps required. |
| warden-security | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| wasm-specialist | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| weak-type-eliminator | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| weather-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| weather-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| web | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| web-dev | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-explorer | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-gis-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-hunter | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-performance-auditor | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-reader | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| web-search-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-search-opencode | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| web-search-researcher | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| webassembly-engineer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| webassembly-specialist | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| webpack-expert | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| websearch | research | requires-mcp | 85 | Requires MCP servers: exa, fuse-browser. |
| website-designer | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| websocket-engineer | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| websocket-engineer-performance | performance | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| websocket-engineer-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| websocket-expert | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wechat-mini-program-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wechat-official-account-manager | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wechat-reader-test | testing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| weekly-comment-sync | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| weekly-recap | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| weibo-strategist | devops | fully-compatible | 100 | Converted directly; no manual steps required. |
| wellnizz | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wg-code-alchemist | frontend | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'search/codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runNotebooks', 'runTasks', 'search', 'search/searchResults', 'runCommands/terminalLastCommand', 'runCommands/terminalSelection', 'testFailure', 'usages', 'vscodeAPI']. |
| wg-code-sentinel | security | needs-tool-mapping | 75 | Unmapped tools: ['changes', 'codebase', 'edit/editFiles', 'extensions', 'web/fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runNotebooks', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']. |
| whimsy-injector | frontend | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| wiki-links-are-the-digital-evolution-of-analog-indexing | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| wiki-links-as-social-contract-transforms-agents-into-stewards-of-incomplete-references | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| wiki-links-create-navigation-paths-that-shape-retrieval | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| wiki-links-implement-graphrag-without-the-infrastructure | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. |
| william-shakespeare | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| windows-infra-admin | infrastructure | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| winfocus-afe3sm-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| winfocus-afe3sm-planner-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| winfocus-afe3sm-reviewer-1 | documentation | fully-compatible | 100 | Converted directly; no manual steps required. |
| winfocus-dispatch-log | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| winfocus-w7eys1-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| winfocus-w7eys1-planner-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| winfocus-w7eys1-reviewer-1 | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| winforms-expert | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| winston-churchill | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintest-cb0gpg-executor-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-cb0gpg-executor-2 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-cb0gpg-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintest-cb0gpg-reviewer-2 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintest-dispatch-log | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-f4w9gu-executor-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-f4w9gu-executor-3 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-f4w9gu-planner-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-f4w9gu-planner-3 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-f4w9gu-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintest-f4w9gu-reviewer-3 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintest-od5a0c-executor-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-od5a0c-executor-2 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintest-od5a0c-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintest-od5a0c-reviewer-2 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintrain-2twy3o-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-2twy3o-planner-1 | testing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-2twy3o-reviewer-1 | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintrain-dispatch-log | ai | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-hchc5z-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-hchc5z-planner-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-hchc5z-reviewer-1 | testing | fully-compatible | 100 | Converted directly; no manual steps required. |
| wintrain-yq8iba-executor-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-yq8iba-planner-1 | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wintrain-yq8iba-reviewer-1 | linux | fully-compatible | 100 | Converted directly; no manual steps required. |
| wip-limits-force-processing-over-accumulation | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wire | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wireless-pentester | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| witness-auditor | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| witness-curator | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| wittgenstein | security | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| wizard-designer | frontend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wolfgang-amadeus-mozart | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| wordpress-developer | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| wordpress-master | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| wordpress-master-architecture | architecture | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| wordpress-performance-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| wordpress-shopping-cart-engineer | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| work-planner | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| worker | ai | needs-tool-mapping | 75 | Unmapped tools: find, contact_supervisor. |
| worker-productivity | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| worker-specialist | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| worker-writing | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| workflow-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-automation | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 4 same-name variants into one canonical agent. |
| workflow-claude-commands-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-claude-settings-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-claude-skills-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-claude-subagents-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-concepts-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-coordinator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-director | productivity | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| workflow-improvement-analysis-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-improvement-implementer-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-improvement-planner-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-improvement-validator-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-optimizer | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-optimizer-performance | performance | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-orchestrator | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 5 same-name variants into one canonical agent. |
| workflow-recreate-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-research-agent | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflow-specialist | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| workflows | productivity | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| workshop-ta | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| workspace-app | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| world-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| world-builder | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| writer | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. Merged 4 same-name variants into one canonical agent. |
| writer-emergency | writing | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| writing-clarifier | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| writing-executor | writing | fully-compatible | 100 | Converted directly; no manual steps required. Merged 3 same-name variants into one canonical agent. |
| writing-for-audience-blocks-authentic-creation | security | fully-compatible | 100 | Converted directly; no manual steps required. |
| ws-verify-report | backend | requires-manual-conversion | 50 | No frontmatter/metadata detected; prompt extracted from raw text. |
| wu | backend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| wuwei-master | security | needs-tool-mapping | 75 | Unmapped tools: [view, glob]. |
| x-api-integration | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| x-twitter-intelligence-analyst | research | fully-compatible | 100 | Converted directly; no manual steps required. |
| x-twitter-scraper | frontend | requires-mcp | 85 | Requires MCP servers: xquik. |
| xiaohongshu-specialist | writing | fully-compatible | 100 | Converted directly; no manual steps required. |
| xr-cockpit-interaction-specialist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| xr-immersive-developer | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| xr-interface-architect | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| yak-shave-detector | productivity | needs-tool-mapping | 75 | Unmapped tools: [Read, Glob]. |
| yolo-ceo | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| yolo-cfo | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| yolo-coo | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| yolo-cto | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| you-operate-a-system-that-takes-notes | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| your-skill-name | backend | needs-tool-mapping | 75 | Unmapped tools: [claude, cursor, gemini]. |
| yt-scraper | backend | fully-compatible | 100 | Converted directly; no manual steps required. |
| zai-cli | ai | fully-compatible | 100 | Converted directly; no manual steps required. |
| zeigarnik-effect-validates-capture-first-philosophy-because-open-loops-drain-attention | productivity | fully-compatible | 100 | Converted directly; no manual steps required. |
| zero | architecture | fully-compatible | 100 | Converted directly; no manual steps required. |
| zhihu-strategist | frontend | fully-compatible | 100 | Converted directly; no manual steps required. |
| zhuangzi | frontend | requires-mcp | 85 | Requires MCP servers: plugin_hypermnesia-mcp_cortex, plugin_ai-architect-mcp-codebase_ai-architect. |
| zig-developer | backend | needs-tool-mapping | 75 | Unmapped tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]. |
| zk-steward | productivity | fully-compatible | 100 | Converted directly; no manual steps required. Merged 2 same-name variants into one canonical agent. |
| zos-sysprog | productivity | needs-tool-mapping | 75 | Unmapped tools: [read_file, grep_search, google_web_search, read_many_files, write_todos, ask_user, web_fetch]. Merged 2 same-name variants into one canonical agent. |
