#!/usr/bin/env python3
"""Small example for exploring the refreshed SOTA JSON files.

Usage:
    python examples/explore_latest_results.py
    python examples/explore_latest_results.py --task-file data/tasks/ogb.json --top 10
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List


DEFAULT_TASK_FILE = Path("data/tasks/ogb.json")


def iter_datasets(datasets: Iterable[dict]) -> Iterable[dict]:
    for dataset in datasets or []:
        yield dataset
        yield from iter_datasets(dataset.get("subdatasets", []))


def iter_rows(task_file: Path) -> Iterable[Dict]:
    tasks: List[dict] = json.loads(task_file.read_text())
    for task in tasks:
        for dataset in iter_datasets(task.get("datasets", [])):
            sota = dataset.get("sota") or {}
            metrics = sota.get("metrics", [])
            for row in sota.get("rows", []) or []:
                yield {
                    "task": task.get("task", ""),
                    "dataset": dataset.get("dataset", ""),
                    "model_name": row.get("model_name", ""),
                    "paper_title": row.get("paper_title", ""),
                    "paper_date": row.get("paper_date", ""),
                    "metrics": row.get("metrics", {}),
                    "metric_names": metrics,
                }


def sort_key(row: Dict) -> tuple:
    return (row.get("paper_date", ""), row.get("model_name", ""))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-file", type=Path, default=DEFAULT_TASK_FILE)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()

    rows = sorted(iter_rows(args.task_file), key=sort_key, reverse=True)
    print(f"Loaded {len(rows)} rows from {args.task_file}")
    print()

    for row in rows[: args.top]:
        metric_pairs = ", ".join(f"{k}={v}" for k, v in row["metrics"].items()) or "(no metrics)"
        print(f"[{row['paper_date'] or 'unknown'}] {row['task']} / {row['dataset']}")
        print(f"  model : {row['model_name'] or '(missing)'}")
        print(f"  paper : {row['paper_title'] or '(missing)'}")
        print(f"  scores: {metric_pairs}")
        print()


if __name__ == "__main__":
    main()
