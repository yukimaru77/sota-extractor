# `sota-extractor` と Papers with Code evaluation tables の比較メモ（2026-03-10）

このメモは、`sota-extractor` で再取得できた leaderboard 系データと、Papers with Code のアーカイブ `jul-28-evaluation-tables.json.gz` を、**ベンチマーク（≒ dataset ごとの評価表）** という観点で比較したものです。

---

## まず用語の説明

この比較では、用語を次のように読んでいます。

### ベンチマーク
この文脈では、おおざっぱに

- **dataset**
- **評価指標 (metric)**
- **その上に並ぶモデルスコア表 (leaderboard)**

をまとめて「ベンチマーク」とみなしています。

実務上は、**dataset ごとの leaderboard 1枚** と考えるとわかりやすいです。

例:
- `SQuAD1.1`
- `SQuAD2.0`
- `ogbg-molhiv`
- `HotpotQA`

---

### task
大きな問題カテゴリです。

例:
- `Question Answering`
- `Natural Language Inference`
- `Graph Property Prediction`

---

### subtask
`task` の下位カテゴリです。

例:
- `Open-Domain Question Answering`
- `Dialogue State Tracking`
- `Visual Question Answering`

---

### dataset
評価対象のデータセット名です。

この比較では、**dataset 数が、あなたの感覚でいうベンチマーク数に一番近い指標**です。

---

### row
leaderboard 上の 1 行です。通常はだいたい **1モデル分のスコア** に対応します。

---

## 今回比較した対象

### `sota-extractor` 側
今回の再実行で成功した以下の 12 系統を集計しました。

- `chexpert`
- `cmrc`
- `coqa`
- `eff`
- `hotpotqa`
- `nlp-progress`
- `ogb`
- `record`
- `reddit`
- `smcalflow`
- `snli`
- `squad`

失敗したもの:
- `cityscapes`
- `xtreme`

### Papers with Code 側
比較対象に使ったファイル:

- `jul-28-evaluation-tables.json.gz`

取得元:
- Hugging Face dataset: `pwc-archive/files`

---

## 結論

**Papers with Code の `evaluation-tables.json` は、`sota-extractor` の 13〜14 種類だけを集めたものではありません。**

規模差が非常に大きく、PWC 側のほうが task / subtask / dataset / rows のすべてで圧倒的に多いです。

---

## 数の比較

### ユニーク task 数
- `sota-extractor`: **96**
- PWC: **2254**

### ユニーク subtask 数
- `sota-extractor`: **21**
- PWC: **2245**

### ユニーク dataset 数
- `sota-extractor`: **229**
- PWC: **8467**

### モデルスコア行数 (`row` 数)
- `sota-extractor`: **3899**
- PWC: **155456**

---

## 重なり具合（名前の完全一致ベース）

### task 名
- 共通 task 数: **42**
- `sota-extractor` 側 96 task のうち PWC にもある割合: **43.8%**
- PWC 側 2254 task のうち `sota-extractor` にもある割合: **1.9%**

### subtask 名
- 共通 subtask 数: **13**
- `sota-extractor` 側 21 subtask のうち PWC にもある割合: **61.9%**
- PWC 側 2245 subtask のうち `sota-extractor` にもある割合: **0.6%**

### dataset 名
- 共通 dataset 数: **146**
- `sota-extractor` 側 229 dataset のうち PWC にもある割合: **63.8%**
- PWC 側 8467 dataset のうち `sota-extractor` にもある割合: **1.7%**

---

## 解釈

この比較から言えることはかなり明確です。

- `sota-extractor` は、いくつかの既知 leaderboard / まとめサイトを集約するツール
- PWC evaluation tables は、それよりはるかに広い範囲の leaderboard / benchmark を含んでいる

特に、あなたが気にしていた **「ベンチマーク数」** に最も近い dataset 数で比べると、

- `sota-extractor`: **229**
- PWC: **8467**

なので、**PWC が `sota-extractor` の 13 種類だけで説明できる可能性は低い**、というより、ほぼ否定してよいです。

---

## 補足: この比較の注意点

この比較は **名前の完全一致** ベースです。したがって、以下のズレは残ります。

- 表記ゆれ
- 大文字小文字の違い
- task / subtask 階層の切り方の違い
- dataset 名の別名・短縮名

ただし、`229 vs 8467` の差は非常に大きいため、表記ゆれだけでは説明できません。

---

## 参考: PWC にだけ大量に見られる task 例

例:
- `2D Object Detection`
- `3D Object Detection`
- `3D Human Pose Estimation`
- `3D Semantic Segmentation`
- `4D Panoptic Segmentation`

この時点で、PWC 側がより広い分野を扱っていることがわかります。

---

## 参考: `sota-extractor` 側にだけ見られる task 例

例:
- `Chinese Reading Comprehension`
- `Task-Oriented Dialogue as Dataflow Synthesis`
- `Abstract Games with Hints`
- `Scientific Question Answering`

これは、`sota-extractor` 側が独自のまとめソースや命名を一部含んでいるためです。

---

## 最終結論

あなたの関心に合わせて一言でまとめると、

> **ベンチマーク = dataset ごとの leaderboard** と考えても、Papers with Code の evaluation tables は `sota-extractor` の 13〜14 種類だけでは全く説明できません。

つまり、`sota-extractor` を全部回しても、PWC evaluation tables 全体の benchmark coverage には届きません。
