#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONPATH="$(pwd)"
.venv/bin/python -m src.benchmark.compare --input data/codigo --output results/
.venv/bin/python plot-results.py
