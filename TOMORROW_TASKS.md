# Tomorrow Tasks (Codex-first)

Goal: Codex prepares the project so you can start calmly with minimal setup.

## A) Preflight
1) Run: `python scripts/flow.py --auto`
2) If `SETUP_REPORT.md` has FAIL items, follow the suggested fixes.
3) Re-run `python scripts/flow.py --auto` until clean.

## B) Project skeleton (no Unity required)
1) Create base folders under `workspace/Project/Assets/_Project/`:
   - Scenes, Scripts, Prefabs, Art, Settings, UI, Data
2) Add a placeholder `Scenes/Bootstrap.unity` file (empty marker).
3) Create script stubs with TODOs only (no heavy logic):
   - `Scripts/AutoWalkController.cs`
   - `Scripts/DriftController.cs`
   - `Scripts/ChunkStreamManager.cs`
4) Create data stubs:
   - `Data/EncounterData.cs` (ScriptableObject stub)
   - `Data/ChunkData.cs` (ScriptableObject stub)

## C) Documentation pack
1) Write a short `workspace/Project/README_PROJECT.md`:
   - Scope, pillar summary, and immediate next tasks.
2) Add `workspace/Project/DESIGN_NOTES.md`:
   - Drift phases, encounter categories, UI tone notes.
3) Add `workspace/Project/BUILD_NOTES.md`:
   - Target platform, build settings reminders.

## D) Validation
1) Run: `python scripts/run_tests.py`
2) Ensure no FAIL entries in `SETUP_REPORT.md`.
