import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


class TestSmoke(unittest.TestCase):
    def test_env_check_json(self):
        repo_root = Path(__file__).resolve().parents[1]
        cmd = [sys.executable, "scripts/env_check.py", "--json"]
        result = subprocess.run(cmd, cwd=repo_root, stdout=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        self.assertIn("checks", data)

    def test_bootstrap_creates_dirs(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmpdir:
            cmd = [sys.executable, "scripts/bootstrap.py", "--root", tmpdir]
            result = subprocess.run(cmd, cwd=repo_root)
            self.assertEqual(result.returncode, 0)
            root = Path(tmpdir)
            self.assertTrue((root / "logs").exists())
            self.assertTrue((root / "output").exists())
            self.assertTrue((root / "workspace").exists())


if __name__ == "__main__":
    unittest.main()
