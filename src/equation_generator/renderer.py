"""Rendering helpers for LaTeX equations."""

from __future__ import annotations


def render_latex(equation: str) -> str:
    """Wrap an equation in display math delimiters.

    Args:
        equation: Equation string already formatted with LaTeX-friendly tokens.

    Returns:
        Display math string ready for LaTeX documents.
    """
    sanitized = equation.strip()
    return f"\\[{sanitized}\\]"
