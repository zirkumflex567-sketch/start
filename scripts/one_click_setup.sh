#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python scripts/flow.py --auto

echo ""
echo "Setup complete. Review SETUP_REPORT.md for any missing items."
