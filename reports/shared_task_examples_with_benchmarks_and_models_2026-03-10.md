# 共通 task / subtask 名で見た benchmark 例と代表モデル（2026-03-10）

このメモでは、`sota-extractor` と Papers with Code (`jul-28-evaluation-tables.json.gz`) の両方に**同じ名前で存在した task / subtask** をいくつか抜き出し、その下にある benchmark 名（≒ dataset 名）と、各 benchmark から代表として 1 つのモデル名を並べています。

代表モデルの選び方: 各 benchmark の row のうち、`paper_date` が最も新しいものを優先して 1 つ採用しています。日付が無い場合は、その benchmark 内の先頭側の行から 1 つ拾われることがあります。

## 抜粋した共通名

## Question Answering (task)

- `sota-extractor` 側 benchmark 数: **14**
- PWC 側 benchmark 数: **153**

### `sota-extractor` 側
- **bAbi 20 QA (10k training examples)** → 代表モデル: `SDNC`
- **bAbi 20 QA (1k training examples)** → 代表モデル: `QRN`
- **bAbi Children's Book comprehension CBtest CN** → 代表モデル: `NSE`
- **bAbi Children's Book comprehension CBtest NE** → 代表モデル: `NSE`
- **CNN Comprehension test** → 代表モデル: `ReasoNet`
- **CoQA (Conversational Question Answering Challenge)** → 代表モデル: `XLNet + MMFT + ADA (single model)`
- **Daily Mail Comprehension test** → 代表モデル: `ReasoNet`
- **HotpotQA** → 代表モデル: `Mistral multi hop with very large sources`
- **Reading comprehension MCTest-160-all** → 代表モデル: `Wang-et-al`
- **Reading comprehension MCTest-500-all** → 代表モデル: `Wang-et-al`
- **SQuAD1.1** → 代表モデル: `{ANNA} (single model)`
- **SQuAD2.0** → 代表モデル: `RoberTa+Parallel+Adapters (single model)`
- …ほか 2 件

### PWC 側
- **adversarial_qa** → 代表モデル: `—`
- **AGI Eval** → 代表モデル: `Orca 2-7B`
- **AgriQA** → 代表モデル: `—`
- **AI2 Kaggle Dataset** → 代表モデル: `Our Approach w/o IR`
- **Aristo Kaggle Allen AI 8th grade questions** → 代表モデル: `Cardal`
- **AviationQA** → 代表モデル: `KGT5`
- **bAbi** → 代表モデル: `ours`
- **Bamboogle** → 代表モデル: `ReST meets ReAct (PaLM 2-L + Google Search)`
- **BBH** → 代表モデル: `Shakti-LLM (2.5B)`
- **BioASQ** → 代表モデル: `GPT-4`
- **BLURB** → 代表モデル: `GPT-4`
- **BoolQ** → 代表モデル: `Shakti-LLM (2.5B)`
- …ほか 141 件

## Natural Language Inference (task)

- `sota-extractor` 側 benchmark 数: **3**
- PWC 側 benchmark 数: **43**

### `sota-extractor` 側
- **MultiNLI** → 代表モデル: `XLNet-Large (2019)`
- **SciTail** → 代表モデル: `Hierarchical BiLSTM Max Pooling (2018)`
- **SNLI** → 代表モデル: `Unlexicalized features`

### PWC 側
- **ANLI** → 代表モデル: `—`
- **ANLI test** → 代表モデル: `T5-3B (explanation prompting)`
- **ANLI-all** → 代表モデル: `—`
- **ANLI-r3** → 代表モデル: `—`
- **AX** → 代表モデル: `T5`
- **BioNLI** → 代表モデル: `BioLinkBert`
- **CommitmentBank** → 代表モデル: `PaLM 2-S (one-shot)`
- **e-SNLI** → 代表モデル: `UnitedSynT5 (3B)`
- **FarsTail** → 代表モデル: `mBERT`
- **fever-nli** → 代表モデル: `—`
- **GLUE** → 代表モデル: `—`
- **HANS** → 代表モデル: `Roberta-large`
- …ほか 31 件

## Machine Translation (task)

- `sota-extractor` 側 benchmark 数: **9**
- PWC 側 benchmark 数: **84**

### `sota-extractor` 側
- **LDC En-De BLEU** → 代表モデル: `Transformer+BR-CSGAN`
- **Multi30k-Task1(en-fr fr-en de-en en-de)** → 代表モデル: `—`
- **news-test-2014 En-De BLEU** → 代表モデル: `Transformer+BR-CSGAN`
- **news-test-2014 En-Fr BLEU** → 代表モデル: `Transformer (big)`
- **news-test-2015 En-De BLEU** → 代表モデル: `S2Tree+5gram NPLM`
- **news-test-2016 En-Ro BLEU** → 代表モデル: `GRU BPE90k`
- **WMT 2014 EN-DE** → 代表モデル: `Transformer Big + BT (2018)`
- **WMT14(en-fr fr-en)** → 代表モデル: `—`
- **WMT16 (de-en en-de)** → 代表モデル: `—`

### PWC 側
- ** ACCURAT balanced test corpus for under resourced languages Russian-Estonian** → 代表モデル: `Multilingual Transformer`
- **20NEWS** → 代表モデル: `tensorflow/tensor2tensor`
- **ACCURAT balanced test corpus for under resourced languages Estonian-Russian** → 代表モデル: `Multilingual Transformer`
- **ACES** → 代表モデル: `metricx_xxl_DA_2019`
- **Alexa Point of View** → 代表モデル: `T5`
- **Arba Sicula** → 代表モデル: `Many-to-Many`
- **Business Scene Dialogue EN-JA** → 代表モデル: `Transformer-base`
- **Business Scene Dialogue JA-EN** → 代表モデル: `Transformer-base`
- **FLoRes-200** → 代表モデル: `GenTranslate-7B`
- **flores95-devtest eng-X** → 代表モデル: `SeamlessM4T-NLLB-1.3B`
- **flores95-devtest X-eng** → 代表モデル: `SeamlessM4T-NLLB-1.3B`
- **FRMT (Chinese - Mainland)** → 代表モデル: `PaLM 2`
- …ほか 72 件

## Visual Question Answering (task)

- `sota-extractor` 側 benchmark 数: **9**
- PWC 側 benchmark 数: **30**

### `sota-extractor` 側
- **COCO Visual Question Answering (VQA) abstract 1.0 multiple choice** → 代表モデル: `LSTM blind`
- **COCO Visual Question Answering (VQA) abstract images 1.0 open ended** → 代表モデル: `LSTM blind`
- **COCO Visual Question Answering (VQA) real images 1.0 multiple choice** → 代表モデル: `joint-loss`
- **COCO Visual Question Answering (VQA) real images 1.0 open ended** → 代表モデル: `joint-loss`
- **COCO Visual Question Answering (VQA) real images 2.0 open ended** → 代表モデル: `d-LSTM+nI`
- **Visual Genome (pairs)** → 代表モデル: `CMN`
- **Visual Genome (subjects)** → 代表モデル: `CMN`
- **Visual7W** → 代表モデル: `MCB+Att.`
- **VQA** → 代表モデル: `—`

### PWC 側
- **AID-VQA** → 代表モデル: `SkySense-O`
- **AMBER** → 代表モデル: `RLAIF-V 12B`
- **BenchLMM** → 代表モデル: `Sphinx-V2-1K`
- **CLEVR** → 代表モデル: `NeSyCoCo Neuro-Symbolic`
- **COCO (Common Objects in Context)** → 代表モデル: `—`
- **COCO Visual Question Answering (VQA) real images 2.0 open ended** → 代表モデル: `MaMMUT (2B)`
- **EarthVQA** → 代表モデル: `SOBA`
- **GQA** → 代表モデル: `LocVLM-L`
- **GRIT** → 代表モデル: `OFA`
- **MapEval-Visual** → 代表モデル: `Claude-3.5-Sonnet`
- **MM-Vet** → 代表モデル: `PIIP-LLaVA (Vicuna-7B, ConvNeXt-L, CLIP-L )`
- **MM-Vet (w/o External Tools)** → 代表モデル: `Emu-14B`
- …ほか 18 件

## Text Classification (task)

- `sota-extractor` 側 benchmark 数: **2**
- PWC 側 benchmark 数: **101**

### `sota-extractor` 側
- **AG News** → 代表モデル: `XLNet (2019)`
- **DBpedia** → 代表モデル: `XLNet (2019)`

### PWC 側
- **20 Newsgroups** → 代表モデル: `RoBERTaGCN`
- **20NEWS** → 代表モデル: `LinearSVM+TFIDF`
- **ade_corpus_v2Ade_corpus_v2_classification** → 代表モデル: `—`
- **Adverse Drug Events (ADE) Corpus** → 代表モデル: `Spark NLP`
- **AffCon 2020 Emotion Detection** → 代表モデル: `BERT-based Ensembles`
- **AG News** → 代表モデル: `Qwen2.5-32B + CAPO`
- **ag_news** → 代表モデル: `—`
- **Amazon-2** → 代表モデル: `LHTR`
- **Amazon-5** → 代表モデル: `XLNet`
- **amazon_polarity** → 代表モデル: `—`
- **amazon_reviews_multi** → 代表モデル: `—`
- **An Amharic News Text classification Dataset** → 代表モデル: `Naive Bayes using count vectorizer features`
- …ほか 89 件

## Common Sense Reasoning (task)

- `sota-extractor` 側 benchmark 数: **1**
- PWC 側 benchmark 数: **24**

### `sota-extractor` 側
- **ReCoRD** → 代表モデル: `LUKE (single model)`

### PWC 側
- **ARC (Challenge)** → 代表モデル: `LLaMA-3 8B + MixLoRA`
- **ARC (Easy)** → 代表モデル: `Mixtral 8x7B (0-shot)`
- **BIG-bench (Causal Judgment)** → 代表モデル: `PaLM 540B (few-shot, k=3)`
- **BIG-bench (Date Understanding)** → 代表モデル: `PaLM 540B (few-shot,k=3)`
- **BIG-bench (Disambiguation QA)** → 代表モデル: `PaLM 540B (few-shot, k=3)`
- **BIG-bench (Known Unknowns)** → 代表モデル: `PaLM-540B (few-shot, k=5)`
- **BIG-bench (Logical Sequence)** → 代表モデル: `Chinchilla-70B (few-shot, k=5)`
- **BIG-bench (Sports Understanding)** → 代表モデル: `PaLM 540B (few-shot, k=3)`
- **BIG-bench (Winowhy)** → 代表モデル: `PaLM-62B (few-shot, k=5)`
- **CODAH** → 代表モデル: `BERT Large`
- **CommonsenseQA** → 代表モデル: `GPT-4o (HPT)`
- **CrowdSource QA** → 代表モデル: `BERT`
- …ほか 12 件

## Open-Domain Question Answering (subtask)

- `sota-extractor` 側 benchmark 数: **2**
- PWC 側 benchmark 数: **15**

### `sota-extractor` 側
- **Quasar** → 代表モデル: `R^3 (2018)`
- **SearchQA** → 代表モデル: `R^3 (2018)`

### PWC 側
- **DuReader** → 代表モデル: `ERNIE 2.0 Large`
- **ELI5** → 代表モデル: `Fourier Transformer`
- **KILT: ELI5** → 代表モデル: `arxiv.org/abs/2103.06332`
- **KILT: HotpotQA** → 代表モデル: `T5-base`
- **KILT: Natural Questions** → 代表モデル: `Re2G`
- **KILT: TriviaQA** → 代表モデル: `Re2G`
- **Natural Questions** → 代表モデル: `UnitedQA (Hybrid)`
- **Natural Questions (short)** → 代表モデル: `EMDR2`
- **Quasar** → 代表モデル: `Denoising QA`
- **SearchQA** → 代表モデル: `Locality-Sensitive Hashing`
- **SQuAD1.1** → 代表モデル: `DrQA`
- **SQuAD1.1 dev** → 代表モデル: `Blended RAG`
- …ほか 3 件

## Visual Question Answering (subtask)

- `sota-extractor` 側 benchmark 数: **4**
- PWC 側 benchmark 数: **30**

### `sota-extractor` 側
- **GQA - Visual Reasoning in the Real World** → 代表モデル: `LXMERT (2019)`
- **TextVQA** → 代表モデル: `M4C (2020)`
- **VizWiz dataset** → 代表モデル: `Pythia`
- **VQAv2** → 代表モデル: `UNITER (2019)`

### PWC 側
- **AID-VQA** → 代表モデル: `SkySense-O`
- **AMBER** → 代表モデル: `RLAIF-V 12B`
- **BenchLMM** → 代表モデル: `Sphinx-V2-1K`
- **CLEVR** → 代表モデル: `NeSyCoCo Neuro-Symbolic`
- **COCO (Common Objects in Context)** → 代表モデル: `—`
- **COCO Visual Question Answering (VQA) real images 2.0 open ended** → 代表モデル: `MaMMUT (2B)`
- **EarthVQA** → 代表モデル: `SOBA`
- **GQA** → 代表モデル: `LocVLM-L`
- **GRIT** → 代表モデル: `OFA`
- **MapEval-Visual** → 代表モデル: `Claude-3.5-Sonnet`
- **MM-Vet** → 代表モデル: `PIIP-LLaVA (Vicuna-7B, ConvNeXt-L, CLIP-L )`
- **MM-Vet (w/o External Tools)** → 代表モデル: `Emu-14B`
- …ほか 18 件

## Dialogue State Tracking (subtask)

- `sota-extractor` 側 benchmark 数: **2**
- PWC 側 benchmark 数: **7**

### `sota-extractor` 側
- **Second dialogue state tracking challenge** → 代表モデル: `Zhong et al. (2018)`
- **Wizard-of-Oz** → 代表モデル: `Zhong et al. (2018)`

### PWC 側
- **CoSQL** → 代表モデル: `RASAT+PICARD`
- **MMConv** → 代表モデル: `PaCE`
- **MULTIWOZ 2.1** → 代表モデル: `DeepStruct multi-task w/ finetune`
- **MULTIWOZ 2.2** → 代表モデル: `SGP-DST (small)`
- **Second dialogue state tracking challenge** → 代表モデル: `T5 (span)`
- **SIMMC2.0** → 代表モデル: `PaCE`
- **Wizard-of-Oz** → 代表モデル: `T5 (span)`

## Chunking (subtask)

- `sota-extractor` 側 benchmark 数: **2**
- PWC 側 benchmark 数: **5**

### `sota-extractor` 側
- **CoNLL 2003** → 代表モデル: `Word + Char + MFVI (2020)`
- **Penn Treebank** → 代表モデル: `Suzuki and Isozaki (2008)`

### PWC 側
- **CoNLL 2000** → 代表モデル: `BERT-CRF (Replicated in AdaSeq)`
- **CoNLL 2003** → 代表モデル: `Def2Vec`
- **CoNLL 2003 (English)** → 代表モデル: `Wang et al., 2020`
- **CoNLL 2003 (German)** → 代表モデル: `Wang et al., 2020`
- **Penn Treebank** → 代表モデル: `ACE`

## Dialogue Act Classification (subtask)

- `sota-extractor` 側 benchmark 数: **2**
- PWC 側 benchmark 数: **5**

### `sota-extractor` 側
- **ICSI Meeting Recorder Dialog Act (MRDA) corpus** → 代表モデル: `SGNN (2018)`
- **Switchboard corpus** → 代表モデル: `SGNN (2018)`

### PWC 側
- **EMOTyDA** → 代表モデル: `Hierarchical Fusion`
- **ICSI Meeting Recorder Dialog Act (MRDA) corpus** → 代表モデル: `Hierarchical Fusion`
- **Switchboard corpus** → 代表モデル: `Speaker`
- **Switchboard Dialog Act Corpus** → 代表モデル: `Speaker-change Aware CRF`
- **Switchboard dialogue act corpus** → 代表モデル: `Speaker-change Aware CRF`

## Disentanglement (subtask)

- `sota-extractor` 側 benchmark 数: **2**
- PWC 側 benchmark 数: **3**

### `sota-extractor` 側
- **Linux IRC** → 代表モデル: `Wang and Oard (2009)`
- **Ubuntu IRC** → 代表モデル: `Linear (2008)`

### PWC 側
- **3DIdent** → 代表モデル: `InfoNCE (Normal, Box)`
- **KITTI-Masks** → 代表モデル: `InfoNCE (Laplace, Box)`
- **Natural Sprites** → 代表モデル: `SlowVAE`
