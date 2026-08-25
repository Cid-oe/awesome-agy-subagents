# Plugin Template

A multi-agent AGY plugin bundles several related subagents under one plugin
directory. This mirrors the layout the importer understands (the `agents/`
directory holds the subagents).

```
my-plugin/
├── plugin.json                # plugin manifest
└── agents/
    ├── agent-one.md
    └── agent-two.md
```

## plugin.json

```json
{
  "name": "my-plugin",
  "description": "Short description of what this plugin's agents do.",
  "version": "1.0.0",
  "agents": ["agent-one", "agent-two"]
}
```

## Agent file

Each file in `agents/` follows `templates/agent.md`. Keep `name` slugs unique
within the plugin.

## Importing a plugin

If your plugin lives in a public repository, add it to `KNOWN_REPOS` in
`scripts/discover.py` and run `python3 scripts/run_all.py` — the importer
discovers `agents/` directories recursively under any `plugins/*/` path.
