# Startup Guide (Windows-first)

Use this once to prepare a clean Windows machine for Codex-driven setup.

## 1) Core tools

- Git for Windows + Git LFS
- Python 3.11+
- Node.js 20 (nvm-windows recommended)

Verify in PowerShell:
```powershell
git --version
git lfs version
python --version
node --version
npm --version
```

## 2) Optional but recommended

- Visual Studio 2022 Build Tools (C# / .NET) if you build Unity or C# tools
- WSL2 + Ubuntu 24.04 for Linux scripts
- Cursor + Codex extension if you work locally

Verify in PowerShell:
```powershell
dotnet --info
```

Verify in WSL:
```bash
git --version
python3 --version
node --version
npm --version
```

## 3) Unity (only if needed)

- Unity Hub
- Unity 6 LTS (2D URP template)
- Windows Build Support

## 4) First run

From the repo root:
```bash
python scripts/flow.py --auto
```

Re-run until the report has no FAIL items.
