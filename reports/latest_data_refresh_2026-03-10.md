# 最新データ更新レポート（2026-03-10）

2026-03-10 時点で、現在動作するスクレイパーを live な upstream ソースに対して再実行し、SOTA データを取り直しました。

## 更新内容の概要

| ファイル | 更新前 | 更新後 | 増減 |
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
| `data/tasks/smcalflow.json` | 未収録 | 1 row | +1 新規 |

## 大きな変化

- **OGB** が最も大きく増加し、**244 → 481 rows** になりました。
- **NLP Progress** も大きく増加し、**559 → 692 rows** になりました。
- **EFF** は更新後も最も広いカバレッジを持ち、**109 datasets / 1748 rows** です。
- **HotpotQA**, **SQuAD**, **CheXpert**, **SNLI**, **CMRC** でも追加行が確認できました。
- **CoQA** と **RedditSOTA** は再取得しましたが、行数に変化はありませんでした。
- **SmCalFlow** は、これまで追跡されていなかった task file を新規生成しました。

## 更新後データ中で見つかった比較的新しいエントリ例

以下は「更新後データに含まれていた新しめの行」の例です。全体での最良値一覧という意味ではなく、今回の再取得で確認できた代表例です。

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
  - upstream 側のデータとして `2026-01-09` および `2026-01-11` の日付を持つエントリが存在しており、スクレイパーはそのまま保持しています。

## 実行・保守上のメモ

- 元の依存関係指定は現在の Python 3.12 環境ではそのまま動かなかったため、`requirements.txt` を現行環境向けに更新しました。
- `xtreme` スクレイパーは optional な `_jsonnet` 依存を必要とするため、今回は optional 扱いのままにしています。
- `cityscapes` は現在 `DataError(message=Got an unexpected number of SOTA tables.)` で失敗します。upstream ページ構造の変化が原因の可能性が高いです。

## サンプルコード

更新後の JSON task file を読み込んで、比較的新しいエントリを表示する簡単なサンプルを `examples/explore_latest_results.py` に追加しました。

実行例:

```bash
python examples/explore_latest_results.py
python examples/explore_latest_results.py --task-file data/tasks/eff.json --top 10
```
