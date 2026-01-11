"""Interactive equation generator (legacy entrypoint)."""

from __future__ import annotations

from pathlib import Path

from equation_generator.parser import parse_description
from equation_generator.renderer import render_latex
from equation_generator.storage import EquationStore


DEFAULT_BASE_DIR = Path(__file__).resolve().parent / "equations"


def main() -> None:
    store = EquationStore(base_dir=DEFAULT_BASE_DIR)
    store.ensure_headers()

    print("EquationGenerator interactive mode. Type 'quit' to exit.")
    while True:
        user_input = input("Enter a mathematical description: ").strip()
        if user_input.lower() == "quit":
            break

        category = input(
            f"Enter the category ({', '.join(store.available_categories())}): "
        ).strip().lower()

        try:
            parse_result = parse_description(user_input)
            latex_equation = render_latex(parse_result.equation)
            path = store.append_equation(category, latex_equation)
        except ValueError as exc:
            print(str(exc))
            continue

        print(f"Generated LaTeX: {latex_equation}")
        print(f"Saved to: {path}")


if __name__ == "__main__":
    main()
