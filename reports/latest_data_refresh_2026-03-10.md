# Latest data refresh summary (2026-03-10)

This refresh reran the currently working scrapers against their live upstream sources on 2026-03-10.

## What changed

| File | Before | After | Delta |
|---|---:|---:|---:|
| `data/tasks/chexpert.json` | 175 rows | 213 rows | +38 |
| `data/tasks/cmrc.json` | 54 rows | 57 rows | +3 |
| `data/tasks/coqa.json` | 43 rows | 43 rows | 0 |
| `data/tasks/eff.json` | 1714 rows | 1748 rows | +34 |
| `data/tasks/hotpotqa.json` | 71 rows | 83 rows | +12 |
| `data/tasks/nlp-progress.json` | 559 rows | 692 rows | +133 |
| `data/tasks/ogb.json` | 244 rows | 481 rows | +237 |
| `data/tasks/redditsota.json` | 32 rows | 32 rows | 0 |
| `data/tasks/snli.json` | 64 rows | 68 rows | +4 |
| `data/tasks/squad.json` | 451 rows | 469 rows | +18 |
| `data/tasks/smcalflow.json` | not present | 1 row | +1 new file |

## Biggest updates

- **OGB** grew the most: **244 → 481 rows**.
- **NLP Progress** also expanded significantly: **559 → 692 rows**.
- **EFF** remained the broadest source after refresh: **1748 rows** across **109 datasets**.
- **HotpotQA**, **SQuAD**, **CheXpert**, **SNLI**, and **CMRC** all picked up fresh rows.
- **CoQA** and **RedditSOTA** were re-scraped but row counts stayed flat.
- **SmCalFlow** produced a new task file that was not tracked in the repository before.

## A few notable “latest” entries seen in refreshed data

These are not global winners; they are recent rows found in the refreshed task files.

- **HotpotQA**
  - `2024-06-25` — `Mistral multi hop with very large source`
- **SQuAD**
  - `2023-09-29` — `RoberTa+Parallel+Adapters (single model)`
  - `2023-09-29` — `RoberTa+Fusion+Adapters (single model)`
- **CheXpert**
  - `2022-11-02` — `pm_rn50_0.15pp`
- **CMRC**
  - `2021-05-31` — `XLQA (single model)`
- **OGB**
  - entries dated `2026-01-09` and `2026-01-11` are present upstream and were preserved as-is by the scraper

## Operational notes

- The repository’s original dependency pins were too old for the current Python 3.12 environment, so `requirements.txt` was modernized.
- The `xtreme` scraper still depends on optional `_jsonnet` support and was left as an optional path.
- `cityscapes` currently fails with `DataError(message=Got an unexpected number of SOTA tables.)`, which suggests upstream page structure drift.

## Sample code

See `examples/explore_latest_results.py` for a simple way to load a refreshed JSON task file and print recent entries.

Example:

```bash
python examples/explore_latest_results.py
python examples/explore_latest_results.py --task-file data/tasks/eff.json --top 10
```
