#!/usr/bin/env bash
set -euo pipefail

# Refresh all scrapers that currently work in a stock Python 3.12 environment.
# XTREME is intentionally skipped because it requires optional _jsonnet support.
# Cityscapes is intentionally skipped because the upstream page structure has drifted.

cd "$(dirname "$0")/.."

commands=(
  eff
  reddit
  snli
  squad
  nlp-progress
  smcalflow
  record
  hotpotqa
  coqa
  chexpert
  cmrc
  ogb
)

for cmd in "${commands[@]}"; do
  echo "==> Running $cmd"
  python3 -m sota_extractor "$cmd"
done

echo "Done. Refreshed task files are under data/tasks/."
