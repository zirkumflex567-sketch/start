#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

import env_check
import bootstrap


def _run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd)


def _git_status_clean(cwd):
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    return result.returncode == 0 and result.stdout.strip() == ""


def _git_has_user(cwd):
    name = subprocess.run(
        ["git", "config", "user.name"],
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    ).stdout.strip()
    email = subprocess.run(
        ["git", "config", "user.email"],
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    ).stdout.strip()
    return bool(name and email)


def _git_commit(cwd, message):
    _run(["git", "add", "-A"], cwd)
    return _run(["git", "commit", "-m", message], cwd).returncode == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", action="store_true", help="Run checks, bootstrap, and tests.")
    parser.add_argument("--push", action="store_true", help="Push if remote configured.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]

    data = env_check.run_checks()
    env_check.write_report(data, repo_root / "SETUP_REPORT.md")

    if args.auto or not args.push:
        bootstrap.run_bootstrap(repo_root)
        test_result = _run([sys.executable, "scripts/run_tests.py"], repo_root).returncode
        if test_result != 0:
            print("Tests failed.")
            return test_result

    if args.push:
        if not data["git"]["remote_configured"]:
            print("No git remote configured. Skipping push.")
            return 0
        if not _git_status_clean(repo_root):
            if not _git_has_user(repo_root):
                print("Git user.name/email missing. Skipping commit/push.")
                return 0
            if not _git_commit(repo_root, "Codex autostart updates"):
                print("Commit failed.")
                return 1
        push_result = _run(["git", "push"], repo_root).returncode
        return push_result

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
