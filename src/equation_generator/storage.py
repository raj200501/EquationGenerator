"""Storage helpers for generated equations."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable


DEFAULT_CATEGORIES = {
    "arithmetic": "arithmetic.tex",
    "algebra": "algebra.tex",
    "trigonometry": "trigonometry.tex",
    "calculus": "calculus.tex",
    "linear algebra": "linear_algebra.tex",
    "statistics": "statistics.tex",
    "geometry": "geometry.tex",
    "complex numbers": "complex_numbers.tex",
    "number theory": "number_theory.tex",
    "probability": "probability.tex",
}


@dataclass
class EquationStore:
    base_dir: Path
    categories: Dict[str, str] | None = None

    def __post_init__(self) -> None:
        if self.categories is None:
            self.categories = DEFAULT_CATEGORIES
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def available_categories(self) -> Iterable[str]:
        return self.categories.keys()

    def category_path(self, category: str) -> Path:
        if category not in self.categories:
            raise ValueError(f"Unknown category '{category}'.")
        return self.base_dir / self.categories[category]

    def append_equation(self, category: str, latex_equation: str) -> Path:
        path = self.category_path(category)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            content = path.read_text(encoding="utf-8")
            marker = "\\end{align*}"
            if marker in content:
                stripped = latex_equation.strip()
                if stripped.startswith("\\[") and stripped.endswith("\\]"):
                    stripped = stripped[2:-2].strip()
                insertion_line = f"\\\\text{{Generated:}}\\\\quad {stripped} \\\\"
                insertion_point = content.rfind(marker)
                updated = (
                    content[:insertion_point].rstrip()
                    + "\n"
                    + insertion_line
                    + "\n"
                    + content[insertion_point:].lstrip()
                )
                path.write_text(updated, encoding="utf-8")
                return path
        with path.open("a", encoding="utf-8") as handle:
            handle.write(latex_equation.rstrip() + "\n")
        return path

    def ensure_headers(self) -> None:
        for category, filename in self.categories.items():
            path = self.base_dir / filename
            if path.exists():
                continue
            header = (
                f"% Auto-generated equations for {category}.\n"
                "% Append new equations using the EquationGenerator CLI.\n"
            )
            path.write_text(header, encoding="utf-8")
