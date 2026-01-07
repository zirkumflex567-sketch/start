# Codex Autostart Kit

This repo is a browser-Codex bootstrapper. It gives Codex a single prompt and
simple Python scripts to check, fix, test, and (optionally) push changes.

## Start Prompt (copy/paste into Codex)

```
You are Codex running in a fresh repo. Do not ask questions. Follow this order:
1) Run: python scripts/flow.py --auto
2) If flow reports missing dependencies, follow its suggested commands.
3) Re-run: python scripts/flow.py --auto
4) Run tests: python scripts/run_tests.py
5) If a git remote is configured and credentials are present, push changes:
   python scripts/flow.py --push
6) Finish with a short report of what you changed and what remains.
```

## One-command local start

```bash
python scripts/flow.py --auto
```

## What this does

- Checks required tools and paths.
- Writes a `SETUP_REPORT.md` with missing items and suggestions.
- Creates a clean workspace (`workspace/`, `logs/`, `output/`).
- Runs a minimal test suite.
- Pushes if a git remote exists (only when `--push` is used).

## Startup guide

See `STARTUP_GUIDE.md` for Windows setup notes and recommended tooling.
