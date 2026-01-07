#!/usr/bin/env python3
import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def _run(cmd):
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False
        )
        return result.returncode == 0, result.stdout.strip()
    except Exception as exc:
        return False, str(exc)


def _which(cmd):
    return shutil.which(cmd) or ""


def _command_check(cmd):
    ok = bool(_which(cmd))
    version = ""
    if ok:
        ok, version = _run([cmd, "--version"])
    return {"ok": ok, "version": version}


def _git_lfs_check():
    if not _which("git"):
        return {"ok": False, "version": ""}
    ok, out = _run(["git", "lfs", "version"])
    return {"ok": ok, "version": out}


def run_checks():
    repo_root = Path(__file__).resolve().parents[1]
    os_name = platform.system()
    python_version = sys.version.split()[0]

    checks = {
        "git": _command_check("git"),
        "git-lfs": _git_lfs_check(),
        "python": {"ok": True, "version": python_version},
        "node": _command_check("node"),
        "npm": _command_check("npm")
    }

    optional = {
        "dotnet": _command_check("dotnet"),
        "msbuild": _command_check("msbuild")
    }

    git_remote_ok = False
    git_remote_out = ""
    if checks["git"]["ok"]:
        git_remote_ok, git_remote_out = _run(["git", "remote", "-v"])

    result = {
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "os": {
            "name": os_name,
            "version": platform.version()
        },
        "paths": {
            "repo_root": str(repo_root),
            "workspace_dir": str(repo_root / "workspace"),
            "logs_dir": str(repo_root / "logs"),
            "output_dir": str(repo_root / "output")
        },
        "checks": checks,
        "optional": optional,
        "git": {
            "remote_configured": git_remote_ok and bool(git_remote_out.strip()),
            "remote_output": git_remote_out
        }
    }
    return result


def _suggestions(os_name, checks, optional):
    suggestions = []
    if not checks["git"]["ok"]:
        suggestions.append("Install Git for Windows (includes Git LFS).")
    if not checks["git-lfs"]["ok"]:
        suggestions.append("Run: git lfs install")
    if not checks["node"]["ok"] or not checks["npm"]["ok"]:
        if os_name == "Windows":
            suggestions.append("Install Node 20 via nvm-windows.")
        else:
            suggestions.append("Install Node 20 (nvm recommended).")
    if os_name == "Windows" and (not optional["dotnet"]["ok"] or not optional["msbuild"]["ok"]):
        suggestions.append("Install Visual Studio 2022 Build Tools (.NET + MSBuild).")
    return suggestions


def write_report(data, report_path):
    os_name = data["os"]["name"]
    checks = data["checks"]
    optional = data["optional"]
    suggestions = _suggestions(os_name, checks, optional)

    lines = []
    lines.append("# Setup Report")
    lines.append("")
    lines.append(f"Generated: {data['generated_at']}")
    lines.append("")
    lines.append("## Required checks")
    for key, info in checks.items():
        status = "OK" if info["ok"] else "FAIL"
        version = f" ({info['version']})" if info["version"] else ""
        lines.append(f"- {status} {key}{version}")
    lines.append("")
    lines.append("## Optional checks")
    for key, info in optional.items():
        status = "OK" if info["ok"] else "FAIL"
        version = f" ({info['version']})" if info["version"] else ""
        lines.append(f"- {status} {key}{version}")
    lines.append("")
    lines.append("## Git remote")
    remote_status = "OK" if data["git"]["remote_configured"] else "FAIL"
    lines.append(f"- {remote_status} remote configured")
    if data["git"]["remote_output"]:
        lines.append("```")
        lines.append(data["git"]["remote_output"])
        lines.append("```")
    lines.append("")
    lines.append("## Suggestions")
    if suggestions:
        for item in suggestions:
            lines.append(f"- {item}")
    else:
        lines.append("- No missing items detected.")
    lines.append("")

    Path(report_path).write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print JSON to stdout.")
    parser.add_argument("--write-report", action="store_true", help="Write SETUP_REPORT.md.")
    parser.add_argument("--report-path", default="", help="Custom report path.")
    args = parser.parse_args()

    data = run_checks()
    if args.json:
        print(json.dumps(data, indent=2))
    if args.write_report:
        report_path = args.report_path or str(Path(__file__).resolve().parents[1] / "SETUP_REPORT.md")
        write_report(data, report_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
