#!/bin/bash

command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is required but it's not installed. Aborting."; exit 1; }

PYTHON_SCRIPT_PATH="engine.py"

python3 "${PYTHON_SCRIPT_PATH}" "$@"

# make script executable with: chmod +x sparrow.sh