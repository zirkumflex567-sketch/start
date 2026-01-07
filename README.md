# Codex Autostart Kit

This repo is a browser-Codex bootstrapper. It gives Codex a single prompt and
simple Python scripts to check, fix, test, and (optionally) push changes.

## Start Prompt (copy/paste into Codex)

```
You are Codex running in a fresh repo. Do not ask questions. Follow this order:
1) Read GAME_CONTEXT.md, PROJECT_CONSTRAINTS.md, and TOMORROW_TASKS.md.
2) Run: python scripts/flow.py --auto
3) If flow reports missing dependencies, follow its suggested commands.
4) Re-run: python scripts/flow.py --auto
5) Execute tasks in TOMORROW_TASKS.md (sections B and C).
6) Run tests: python scripts/run_tests.py
7) If a git remote is configured and credentials are present, push changes:
   python scripts/flow.py --push
8) Finish with a short report of what you changed and what remains.
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

## Game docs

- `GAME_CONTEXT.md` - core vision and non-negotiables
- `PROJECT_CONSTRAINTS.md` - tools, paths, and legal rules
- `TOMORROW_TASKS.md` - Codex actions to prep the project
