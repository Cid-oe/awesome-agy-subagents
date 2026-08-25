# Contributing

Thanks for helping grow the AGY ecosystem! There are two ways to contribute:
**import a new upstream repository** or **author a new agent directly**.

## Ground rules

- **No placeholder agents.** Every agent in `agents/` must come from a real
  public repository or be a real, complete contribution. Do not commit stubs.
- **No example/demo agents** in `agents/`. Example *usage* lives in
  `examples/`; authoring scaffolds live in `templates/`.
- **Preserve attribution.** Every agent records its upstream repo, author,
  license, and source URL in `agy.sources`.
- **Keep the license honest.** Verify the upstream license before importing.

## Authoring a new agent

1. Copy `templates/agent.md` to `agents/<category>/<name>.md`.
2. Fill in the frontmatter (`name`, `description`, `tools`, `mcpServers`) and
   write the system prompt in the body.
3. Validate it:

   ```bash
   python3 scripts/validate.py
   ```

4. Open a PR. CI and maintainers will check that the agent is complete,
   valid, and correctly categorized.

Categories are the 26 canonical slugs (see `scripts/agy.py`). Pick the closest
one; the maintainers can adjust during review.

## Importing a new upstream repository

1. Add the repo to `KNOWN_REPOS` in `scripts/discover.py` (or just run
   `scripts/run_all.py --discover` to search GitHub broadly).
2. Run the importer:

   ```bash
   python3 scripts/import.py      # clone matching repos
   python3 scripts/convert.py     # extract + convert + dedupe
   python3 scripts/validate.py
   python3 scripts/report.py
   python3 scripts/export.py
   ```

3. Review `reports/compatibility.md` for anything that landed in
   `requires-manual-conversion` and fix it or document why it's acceptable.
4. Open a PR with the new `agents/` files and updated `metadata/` and
   `reports/`.

## Improving the pipeline

The pipeline lives in `scripts/` with the shared library in `scripts/agy.py`.
Add support for new formats in `extract_agent`, new categories in
`CATEGORIES`, and new tool mappings in `TOOL_MAP`. Add tests where practical.

## License

By contributing, you agree that your contributions are licensed under the
MIT license (see [LICENSE](LICENSE)). Imported agents retain their upstream
licenses.
