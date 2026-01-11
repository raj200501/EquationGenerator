"""Parser for natural-language equation descriptions."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List

NUMBER_WORDS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
}

OPERATORS = {
    "plus": "+",
    "minus": "-",
    "times": "\\cdot",
    "multiplied": "\\cdot",
    "divide": "/",
    "divided": "/",
    "equals": "=",
    "equal": "=",
    "open": "(",
    "close": ")",
    "parenthesis": "",
}

PHRASES = {
    "divided by": "/",
    "multiplied by": "\\cdot",
    "to the power of": "^",
    "raised to": "^",
    "open parenthesis": "(",
    "close parenthesis": ")",
}


@dataclass(frozen=True)
class ParseResult:
    tokens: List[str]
    equation: str


TOKEN_RE = re.compile(r"[a-zA-Z]+|[0-9]+|[()^=+\-*/]")


def normalize_description(description: str) -> str:
    """Normalize incoming description for tokenization."""
    normalized = description.strip().lower()
    for phrase, replacement in PHRASES.items():
        normalized = normalized.replace(phrase, f" {replacement} ")
    return normalized


def tokenize_description(description: str) -> List[str]:
    """Tokenize a normalized description into meaningful chunks."""
    normalized = normalize_description(description)
    raw_tokens = TOKEN_RE.findall(normalized)
    tokens: List[str] = []
    for token in raw_tokens:
        if token in NUMBER_WORDS:
            tokens.append(NUMBER_WORDS[token])
        elif token in OPERATORS:
            operator = OPERATORS[token]
            if operator:
                tokens.append(operator)
        else:
            tokens.append(token)
    return tokens


def _merge_power(tokens: Iterable[str]) -> List[str]:
    """Collapse power expressions into LaTeX-friendly exponent form."""
    merged: List[str] = []
    iterator = iter(tokens)
    for token in iterator:
        if token == "^":
            if not merged:
                merged.append(token)
                continue
            base = merged.pop()
            try:
                exponent = next(iterator)
            except StopIteration:
                merged.extend([base, token])
                break
            merged.append(f"{base}^{{{exponent}}}")
        else:
            merged.append(token)
    return merged


def parse_description(description: str) -> ParseResult:
    """Parse a description into a LaTeX-friendly equation string."""
    tokens = tokenize_description(description)
    merged_tokens = _merge_power(tokens)
    equation = " ".join(merged_tokens)
    equation = re.sub(r"\s+", " ", equation).strip()
    return ParseResult(tokens=merged_tokens, equation=equation)
