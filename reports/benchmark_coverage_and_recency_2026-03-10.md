# 全スクレイパー実行結果まとめ（2026-03-10）

このレポートは `sota-extractor` の **CLI から実行できる全スクレイパー 14 件** を再実行し、取得できた JSON を集計して作成したものです。関心を **「ベンチマークごとのモデルスコア一覧」** に絞って、何件集まったかと、各ベンチマーク/サブタスクでどこまで新しい年の結果が取れているかを一覧化しています。

## 集計サマリ

- 実行対象スクレイパー数: **14**
- 成功したスクレイパー数: **12**
- 失敗したスクレイパー数: **2**
- 集まったトップレベルのベンチマーク(task)数: **108**
- 集まったサブタスク数: **21**
- task + subtask の合計数: **129**
- task/subtask 配下の dataset 数合計: **251**
- モデルスコア行(row)数合計: **3899**

## スクレイパー別 実行状況

| scraper | 実行結果 | 主なソースURL | 備考 |
|---|---|---|---|
| `chexpert` | 成功 | https://stanfordmlgroup.github.io/competitions/chexpert/ | data/tasks/chexpert.json |
| `cityscapes` | 失敗/未出力 | https://www.cityscapes-dataset.com/benchmarks/#pixel-level-results | 出力JSONなし |
| `cmrc` | 成功 | http://ymcui.com/cmrc2018/ / http://ymcui.com/cmrc2019/ | data/tasks/cmrc.json |
| `coqa` | 成功 | https://stanfordnlp.github.io/coqa/ | data/tasks/coqa.json |
| `eff` | 成功 | https://github.com/AI-metrics/AI-metrics | data/tasks/eff.json |
| `hotpotqa` | 成功 | https://hotpotqa.github.io/ | data/tasks/hotpotqa.json |
| `nlp-progress` | 成功 | https://github.com/sebastianruder/NLP-progress | data/tasks/nlp-progress.json |
| `ogb` | 成功 | https://ogb.stanford.edu/docs/leader_nodeprop/ etc. | data/tasks/ogb.json |
| `record` | 成功 | https://sheng-z.github.io/ReCoRD-explorer/ | data/tasks/record.json |
| `reddit` | 成功 | https://github.com/RedditSota/state-of-the-art-result-for-machine-learning-problems | data/tasks/redditsota.json |
| `smcalflow` | 成功 | https://microsoft.github.io/task_oriented_dialogue_as_dataflow_synthesis/ | data/tasks/smcalflow.json |
| `snli` | 成功 | https://nlp.stanford.edu/projects/snli/ | data/tasks/snli.json |
| `squad` | 成功 | https://rajpurkar.github.io/SQuAD-explorer/ | data/tasks/squad.json |
| `xtreme` | 失敗/未出力 | https://sites.research.google/xtreme | 出力JSONなし |

## ベンチマーク / サブタスクごとの最新年

定義: 各 task / subtask の配下にある全 dataset・subdataset の `paper_date` を走査し、最も新しい **年** を表示しています。日付が取れていないものは `—` としました。

| scraper | 種別 | ベンチマーク名 | 親タスク | datasets数 | rows数 | 最新年 |
|---|---|---|---|---:|---:|---:|
| `chexpert` | task | Multi-Label Classification |  | 1 | 213 | 2022 |
| `cmrc` | task | Chinese Reading Comprehension |  | 2 | 57 | 2021 |
| `coqa` | task | Question Answering |  | 1 | 43 | 2020 |
| `eff` | task | Abstract Games with Hints |  | 2 | 45 | — |
| `eff` | task | Abstract Strategy Games |  | 0 | 0 | — |
| `eff` | task | Abstract Strategy Games with Rule Learning |  | 0 | 0 | — |
| `eff` | task | Adversarial Defense |  | 0 | 0 | — |
| `eff` | task | Arcade Game Transfer Learning |  | 0 | 0 | — |
| `eff` | task | Artificial General Intelligence |  | 0 | 0 | — |
| `eff` | task | Automated Circuit Design |  | 0 | 0 | — |
| `eff` | task | Automated Interrogation |  | 0 | 0 | — |
| `eff` | task | Automated Security |  | 0 | 0 | — |
| `eff` | task | Bias Avoidance |  | 0 | 0 | — |
| `eff` | task | Casual Conversation Turing Test |  | 1 | 15 | — |
| `eff` | task | Catastrophic Forgetting Avoidance |  | 0 | 0 | — |
| `eff` | task | Classification Under Uncertainty |  | 0 | 0 | — |
| `eff` | task | Code Generation |  | 2 | 5 | — |
| `eff` | task | Complex Conditional Image Generation |  | 0 | 0 | — |
| `eff` | task | Conditional Expression Parsing |  | 0 | 0 | — |
| `eff` | task | Constrained Problem Solving |  | 0 | 0 | — |
| `eff` | task | Explainable Machine Learning |  | 0 | 0 | — |
| `eff` | task | Functional Robustness |  | 0 | 0 | — |
| `eff` | task | Image Classification |  | 8 | 214 | — |
| `eff` | task | Image Generation |  | 1 | 6 | — |
| `eff` | task | Language Creation Games |  | 0 | 0 | — |
| `eff` | task | Language Games |  | 0 | 0 | — |
| `eff` | task | Language Modelling |  | 3 | 41 | — |
| `eff` | task | Machine Translation |  | 5 | 33 | — |
| `eff` | task | Mathematical Proofs |  | 0 | 0 | — |
| `eff` | task | Music Autotagging |  | 1 | 4 | — |
| `eff` | task | Objective Function Reinforcement Learning |  | 0 | 0 | — |
| `eff` | task | Omitted-Variable Bias Correction |  | 0 | 0 | — |
| `eff` | task | One shot learning: ingest important truths from a single example |  | 0 | 0 | — |
| `eff` | task | Pedestrian Detection |  | 0 | 0 | — |
| `eff` | task | Predictable Artificial General Intelligence |  | 0 | 0 | — |
| `eff` | task | Privacy Fairness |  | 0 | 0 | — |
| `eff` | task | Privacy Preserving Machine Learning |  | 0 | 0 | — |
| `eff` | task | Question Answering |  | 10 | 126 | — |
| `eff` | task | Restricted Reproduction |  | 0 | 0 | — |
| `eff` | task | Reward Hacking Avoidance |  | 0 | 0 | — |
| `eff` | task | Safe Exploration |  | 0 | 0 | — |
| `eff` | task | Scalable Supervised Learning |  | 0 | 0 | — |
| `eff` | task | Scientific Paper Comprehension |  | 0 | 0 | — |
| `eff` | task | Scientific Question Answering |  | 1 | 9 | — |
| `eff` | task | Scientific Result Extraction |  | 0 | 0 | — |
| `eff` | task | Security Bug Detection |  | 0 | 0 | — |
| `eff` | task | Side Effect Mitigation |  | 0 | 0 | — |
| `eff` | task | Simple Video Games |  | 57 | 1150 | — |
| `eff` | task | Speech Recognition |  | 10 | 65 | — |
| `eff` | task | Spoken Language Games |  | 0 | 0 | — |
| `eff` | task | Strategy Game Rule Learning |  | 0 | 0 | — |
| `eff` | task | Transfer learning: apply relevant knowledge from a prior setting to a new slightly different one |  | 0 | 0 | — |
| `eff` | task | Underconstrained Problem Solving |  | 0 | 0 | — |
| `eff` | task | Video Activity Recognition |  | 0 | 0 | — |
| `eff` | task | Video Games |  | 0 | 0 | — |
| `eff` | task | Vision |  | 0 | 0 | — |
| `eff` | task | Visual Question Answering |  | 8 | 35 | — |
| `hotpotqa` | task | Question Answering |  | 1 | 83 | 2024 |
| `nlp-progress` | task | Character Level Models |  | 3 | 43 | — |
| `nlp-progress` | task | Combinatory Categorical Grammar |  | 0 | 0 | — |
| `nlp-progress` | task | Common Sense |  | 6 | 22 | — |
| `nlp-progress` | task | Constituency Parsing |  | 1 | 19 | — |
| `nlp-progress` | task | Coreference Resolution |  | 2 | 12 | — |
| `nlp-progress` | task | Dependency Parsing |  | 1 | 19 | — |
| `nlp-progress` | task | Dialogue |  | 0 | 0 | — |
| `nlp-progress` | task | Grammatical Error Correction |  | 12 | 57 | — |
| `nlp-progress` | task | Lexical Normalization |  | 1 | 4 | — |
| `nlp-progress` | task | Machine Translation |  | 1 | 13 | — |
| `nlp-progress` | task | Multimodal |  | 0 | 0 | — |
| `nlp-progress` | task | Named Entity Recognition |  | 3 | 42 | — |
| `nlp-progress` | task | Natural Language Inference |  | 2 | 10 | — |
| `nlp-progress` | task | Paraphrase Generation |  | 2 | 4 | — |
| `nlp-progress` | task | Part-Of-Speech Tagging |  | 3 | 24 | — |
| `nlp-progress` | task | Question Answering |  | 0 | 0 | — |
| `nlp-progress` | task | Reading Comprehension |  | 2 | 10 | — |
| `nlp-progress` | task | Relationship Extraction |  | 2 | 14 | — |
| `nlp-progress` | task | Semantic Parsing |  | 0 | 0 | — |
| `nlp-progress` | task | Semantic Role Labeling |  | 2 | 11 | — |
| `nlp-progress` | task | Semantic Textual Similarity |  | 1 | 6 | — |
| `nlp-progress` | task | Sentiment Analysis |  | 1 | 4 | — |
| `nlp-progress` | task | Shallow Syntax |  | 0 | 0 | — |
| `nlp-progress` | task | Stance Detection |  | 1 | 2 | — |
| `nlp-progress` | task | Subjectivity Analysis |  | 1 | 5 | — |
| `nlp-progress` | task | Summarization |  | 3 | 46 | — |
| `nlp-progress` | task | Taxonomy Learning |  | 0 | 0 | — |
| `nlp-progress` | task | Temporal Processing |  | 0 | 0 | — |
| `nlp-progress` | task | Text Classification |  | 2 | 13 | — |
| `nlp-progress` | task | Word Level Models |  | 4 | 63 | — |
| `nlp-progress` | task | Word Sense Disambiguation |  | 2 | 32 | — |
| `nlp-progress` | subtask | ↳ Parsing | Combinatory Categorical Grammar | 3 | 15 | — |
| `nlp-progress` | subtask | ↳ Supertagging | Combinatory Categorical Grammar | 2 | 14 | — |
| `nlp-progress` | subtask | ↳ Dialogue Act Classification | Dialogue | 2 | 12 | — |
| `nlp-progress` | subtask | ↳ Dialogue State Tracking | Dialogue | 2 | 9 | — |
| `nlp-progress` | subtask | ↳ Disentanglement | Dialogue | 2 | 13 | — |
| `nlp-progress` | subtask | ↳ Generative-Based Chatbots | Dialogue | 1 | 5 | — |
| `nlp-progress` | subtask | ↳ Retrieval-Based Chatbots | Dialogue | 2 | 6 | — |
| `nlp-progress` | subtask | ↳ Multimodal Emotion Recognition | Multimodal | 3 | 4 | — |
| `nlp-progress` | subtask | ↳ Multimodal Sentiment Analysis | Multimodal | 1 | 2 | — |
| `nlp-progress` | subtask | ↳ Visual Question Answering | Multimodal | 4 | 7 | — |
| `nlp-progress` | subtask | ↳ Open-Domain Question Answering | Question Answering | 2 | 12 | — |
| `nlp-progress` | subtask | ↳ Amr Parsing | Semantic Parsing | 4 | 37 | — |
| `nlp-progress` | subtask | ↳ Drs Parsing | Semantic Parsing | 1 | 12 | — |
| `nlp-progress` | subtask | ↳ Paraphrase Identification | Semantic Textual Similarity | 1 | 8 | — |
| `nlp-progress` | subtask | ↳ Chunking | Shallow Syntax | 2 | 9 | — |
| `nlp-progress` | subtask | ↳ Sentence Compression | Summarization | 1 | 4 | — |
| `nlp-progress` | subtask | ↳ Hypernym Discovery | Taxonomy Learning | 4 | 23 | — |
| `nlp-progress` | subtask | ↳ Temporal Information Extraction | Temporal Processing | 2 | 4 | — |
| `nlp-progress` | subtask | ↳ Timex Normalisation | Temporal Processing | 2 | 5 | — |
| `nlp-progress` | subtask | ↳ Word Sense Induction | Word Sense Disambiguation | 2 | 11 | — |
| `nlp-progress` | subtask | ↳ Wsd Lexical Sample Task: | Word Sense Disambiguation | 1 | 5 | — |
| `ogb` | task | Graph Property Prediction |  | 4 | 103 | 2026 |
| `ogb` | task | Link Property Prediction |  | 6 | 157 | 2025 |
| `ogb` | task | Node Property Prediction |  | 5 | 221 | 2026 |
| `record` | task | Common Sense Reasoning |  | 1 | 12 | 2020 |
| `reddit` | task | ASR |  | 1 | 2 | — |
| `reddit` | task | Classification |  | 7 | 14 | — |
| `reddit` | task | Computer Vision |  | 0 | 0 | — |
| `reddit` | task | Instance Segmentation |  | 1 | 1 | — |
| `reddit` | task | Language Modelling |  | 2 | 10 | — |
| `reddit` | task | Machine Translation |  | 3 | 4 | — |
| `reddit` | task | Named entity recognition |  | 0 | 0 | — |
| `reddit` | task | Natural Language Inference |  | 0 | 0 | — |
| `reddit` | task | Person Re-identification |  | 0 | 0 | — |
| `reddit` | task | Question Answering |  | 0 | 0 | — |
| `reddit` | task | Text Classification |  | 0 | 0 | — |
| `reddit` | task | Visual Question Answering |  | 1 | 1 | — |
| `smcalflow` | task | Task-Oriented Dialogue as Dataflow Synthesis |  | 1 | 1 | 2020 |
| `snli` | task | Natural Language Inference |  | 1 | 68 | — |
| `squad` | task | Question Answering |  | 2 | 469 | 2023 |