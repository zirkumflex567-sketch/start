#!/usr/bin/env python3
import argparse
from datetime import datetime
from pathlib import Path


def run_bootstrap(root_path):
    root = Path(root_path).resolve()
    logs_dir = root / "logs"
    output_dir = root / "output"
    workspace_dir = root / "workspace"

    logs_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    workspace_dir.mkdir(parents=True, exist_ok=True)

    workspace_readme = workspace_dir / "README.md"
    if not workspace_readme.exists():
        workspace_readme.write_text(
            "# Workspace\n\n"
            "Put generated or cloned projects here.\n",
            encoding="utf-8"
        )

    log_file = logs_dir / "bootstrap.log"
    log_file.write_text(
        f"Bootstrapped at {datetime.utcnow().isoformat(timespec='seconds')}Z\n",
        encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="", help="Root folder for output directories.")
    args = parser.parse_args()

    root = Path(args.root) if args.root else Path(__file__).resolve().parents[1]
    run_bootstrap(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
