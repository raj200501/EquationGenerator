import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

from equation_generator.cli import run


class CliTests(unittest.TestCase):
    def test_cli_writes_equation(self):
        with TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "equations"
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                result = run([
                    "five plus three equals eight",
                    "--category",
                    "arithmetic",
                    "--output-dir",
                    str(output_dir),
                ])
            self.assertEqual(result, 0)
            content = (output_dir / "arithmetic.tex").read_text(encoding="utf-8")
            self.assertIn("\\[5 + 3 = 8\\]", content)
            self.assertIn("Generated LaTeX", buffer.getvalue())

    def test_cli_print_only(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = run(["two plus two equals four", "--print-only"])
        self.assertEqual(result, 0)
        self.assertIn("\\[2 + 2 = 4\\]", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
