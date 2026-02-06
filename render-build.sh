#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(pwd)"
echo "Build root: ${ROOT_DIR}"

if [[ ! -f requirements.txt ]]; then
  echo "requirements.txt missing; creating an empty file for Render."
  printf "# Auto-created for Render build\n" > requirements.txt
fi

pip install -r requirements.txt
