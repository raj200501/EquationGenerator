#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="${1:-/tmp/equation_generator_smoke}"
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

export PYTHONPATH="$(pwd)/src${PYTHONPATH:+:$PYTHONPATH}"

EXPECTED='\[5 + 3 = 8\]'
RESULT=$(python -m equation_generator.cli "five plus three equals eight" --category arithmetic --output-dir "$OUTPUT_DIR" --print-only)

if [[ "$RESULT" != "$EXPECTED" ]]; then
  echo "Smoke test failed: expected '$EXPECTED' but got '$RESULT'" >&2
  exit 1
fi

python -m equation_generator.cli "five plus three equals eight" --category arithmetic --output-dir "$OUTPUT_DIR"

if ! grep -Fq "$EXPECTED" "$OUTPUT_DIR/arithmetic.tex"; then
  echo "Smoke test failed: equation not written to output file." >&2
  exit 1
fi

echo "Smoke test passed."
