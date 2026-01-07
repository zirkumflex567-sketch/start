@echo off
setlocal

cd /d "%~dp0\.."
python scripts\flow.py --auto

echo.
echo Setup complete. Review SETUP_REPORT.md for any missing items.
pause
