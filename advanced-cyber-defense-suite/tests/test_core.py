import tempfile
import unittest
from pathlib import Path

from tatlib.integrity import create_manifest, verify_manifest
from tatlib.logs import summarize_log


class IntegrityTests(unittest.TestCase):
    def test_create_and_verify(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "data"
            root.mkdir()
            (root / "hello.txt").write_text("hello", encoding="utf-8")
            manifest = Path(tmp) / "manifest.json"
            create_manifest(root, manifest)
            result = verify_manifest(root, manifest)
            self.assertEqual(result["status"], "OK")

    def test_detect_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "data"
            root.mkdir()
            target = root / "hello.txt"
            target.write_text("before", encoding="utf-8")
            manifest = Path(tmp) / "manifest.json"
            create_manifest(root, manifest)
            target.write_text("after", encoding="utf-8")
            result = verify_manifest(root, manifest)
            self.assertIn("hello.txt", result["changed"])


class LogTests(unittest.TestCase):
    def test_log_patterns(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "app.log"
            path.write_text("ERROR: failed\nlogin failed\nall good\n", encoding="utf-8")
            result = summarize_log(path)
            self.assertEqual(result["total_lines"], 3)
            self.assertEqual(result["counts"]["error"], 1)
            self.assertEqual(result["counts"]["authentication_failure"], 1)


if __name__ == "__main__":
    unittest.main()
