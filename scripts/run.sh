#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "Usage: ./scripts/run.sh \"description\" [--category CATEGORY] [--print-only]"
  echo "Example: ./scripts/run.sh \"five plus three equals eight\" --category arithmetic"
  exit 1
fi

export PYTHONPATH="$(pwd)/src${PYTHONPATH:+:$PYTHONPATH}"
python -m equation_generator.cli "$@"
