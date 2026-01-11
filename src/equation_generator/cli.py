"""Command-line interface for EquationGenerator."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from equation_generator.parser import parse_description
from equation_generator.renderer import render_latex
from equation_generator.storage import EquationStore


DEFAULT_BASE_DIR = Path(__file__).resolve().parent.parent / "equations"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate LaTeX equations from natural-language descriptions.")
    parser.add_argument(
        "description",
        nargs="?",
        help="Equation description (e.g., 'five plus three equals eight').",
    )
    parser.add_argument(
        "--category",
        default="arithmetic",
        help="Equation category (default: arithmetic).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_BASE_DIR,
        help="Directory containing category .tex files (default: src/equations).",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Print LaTeX instead of writing to category file.",
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.description:
        parser.print_help()
        return 1

    store = EquationStore(base_dir=args.output_dir)
    store.ensure_headers()

    parse_result = parse_description(args.description)
    latex_equation = render_latex(parse_result.equation)

    if args.print_only:
        print(latex_equation)
        return 0

    try:
        path = store.append_equation(args.category, latex_equation)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(f"Generated LaTeX: {latex_equation}")
    print(f"Saved to: {path}")
    return 0


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
