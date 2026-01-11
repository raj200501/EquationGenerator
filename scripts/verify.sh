#!/usr/bin/env bash
set -euo pipefail

python -m pip install -r requirements.txt

export PYTHONPATH="$(pwd)/src${PYTHONPATH:+:$PYTHONPATH}"
python -m unittest discover -s tests -p "test_*.py"

./scripts/smoke_test.sh
