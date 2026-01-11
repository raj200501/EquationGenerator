import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from equation_generator.storage import EquationStore


class StorageTests(unittest.TestCase):
    def test_append_equation_creates_file(self):
        with TemporaryDirectory() as temp_dir:
            base_dir = Path(temp_dir)
            store = EquationStore(base_dir=base_dir)
            store.ensure_headers()
            path = store.append_equation("arithmetic", "\\[1+1=2\\]")
            self.assertTrue(path.exists())
            content = path.read_text(encoding="utf-8")
            self.assertIn("\\[1+1=2\\]", content)

    def test_unknown_category_raises(self):
        with TemporaryDirectory() as temp_dir:
            base_dir = Path(temp_dir)
            store = EquationStore(base_dir=base_dir)
            store.ensure_headers()
            with self.assertRaises(ValueError):
                store.append_equation("unknown", "\\[1+1=2\\]")


if __name__ == "__main__":
    unittest.main()
