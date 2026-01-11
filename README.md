# EquationGenerator

EquationGenerator is a CLI + interactive tool that turns plain-English descriptions of math into LaTeX equations. It writes the generated LaTeX into category-specific `.tex` files and ships a ready-to-compile `main.tex` document that assembles all of the generated content.

## Features

- Parse short natural-language descriptions of mathematical expressions
- Generate LaTeX formatted equations
- Append generated equations to category `.tex` files
- Build a full LaTeX document with all generated output

## Directory Structure

```plaintext
.
├── src/
│   ├── equation_generator/
│   │   ├── cli.py
│   │   ├── parser.py
│   │   ├── renderer.py
│   │   ├── storage.py
│   ├── equations/
│   │   ├── arithmetic.tex
│   │   ├── algebra.tex
│   │   ├── trigonometry.tex
│   │   ├── calculus.tex
│   │   ├── linear_algebra.tex
│   │   ├── statistics.tex
│   │   ├── geometry.tex
│   │   ├── complex_numbers.tex
│   │   ├── number_theory.tex
│   │   ├── probability.tex
│   │   ├── library.tex
│   ├── generate_equation.py
│   ├── main.tex
├── scripts/
│   ├── run.sh
│   ├── smoke_test.sh
│   ├── verify.sh
├── tests/
│   ├── test_cli.py
│   ├── test_parser.py
│   ├── test_storage.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+ (3.11 recommended)
- (Optional) A TeX distribution (TeX Live, MiKTeX, etc.) if you want to compile `src/main.tex` into a PDF

### Installation

There are no external dependencies, but the standard installation step is still supported:

```bash
python -m pip install -r requirements.txt
```

## Usage

### Generate a single equation (CLI)

```bash
./scripts/run.sh "five plus three equals eight" --category arithmetic
```

This appends the generated LaTeX into `src/equations/arithmetic.tex` and prints the output path.

### Print only (no file write)

```bash
./scripts/run.sh "two plus two equals four" --print-only
```

### Interactive mode

```bash
python src/generate_equation.py
```

You will be prompted for a description and category. Type `quit` to exit.

### Compile the LaTeX document (optional)

If `pdflatex` is installed:

```bash
cd src
pdflatex main.tex
```

The resulting `main.pdf` includes all category `.tex` files and the appendix library.

## Verified Quickstart (commands executed successfully)

```bash
python -m pip install -r requirements.txt
./scripts/run.sh "five plus three equals eight" --category arithmetic
```

## Verification

The canonical verification entrypoint is:

```bash
./scripts/verify.sh
```

This command:

1. Installs Python dependencies (none beyond the standard library).
2. Runs the unit tests.
3. Executes a smoke test that validates the README example, ensuring the CLI prints the expected LaTeX and writes to the category file.

## Troubleshooting

- **`pdflatex` not found**: Install TeX Live (Linux), MiKTeX (Windows), or MacTeX (macOS). The CLI works without a TeX distribution; compilation is optional.
- **Permission denied on scripts**: Run `chmod +x scripts/*.sh` to mark scripts as executable.
