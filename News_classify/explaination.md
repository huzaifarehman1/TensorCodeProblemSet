# News Classification Model (Short Explanation)

## Overview

This solution builds a **Transformer-based text classification model** that predicts the category of a news headline using a custom-trained **BPE tokenizer**.

---

## 1. Data Preparation

- Reads `train.csv` and `test.csv`
- If `text.txt` does not exist, it is created from all training headlines
- This file is used to train the tokenizer

---

## 2. Tokenizer (BPE)

A **Byte Pair Encoding (BPE)** tokenizer is trained from scratch:

- Normalization: `NFD + Lowercase`
- Pre-tokenization: `Whitespace`
- Special tokens:
  - `[PAD]` → Used to pad sequences so all inputs have the same length. Ignored by the model during attention.
  - `[CLS]` → Added at the beginning of every sequence. Its final hidden state is used as the **global representation** for classification.
  - `[SEP]` → Separator token used to mark the end of a sentence or separate segments (mainly useful in sentence-pair tasks).
  - `[UNK]` → Represents unknown words that are not present in the tokenizer vocabulary.
- Max sequence length: `300` is a good starting point
- Padding and truncation enabled so we can do tensor batch processing

Each sentence is converted into:
- `input_ids`
- `attention_mask`

---

## 3. Dataset

Custom PyTorch `Dataset`:

- Encodes each text using the tokenizer
- Stores:
  - Token IDs
  - Attention mask
  - target (for training only)

Output format:
```text
((ids, mask), label)
```

---

## 4. Model Architecture

A **Transformer Encoder classifier**:

- Token Embedding + Positional Embedding
- Transformer Encoder (4 layers, 8 heads)
- LayerNorm (before and after encoder) so embedding are refined 
- Uses `[CLS]` token representation which now hold entire sequence information
- apply Final Linear layer on `[CLS]` → class prediction

---

## 5. Mask Handling

- HuggingFace-style mask:
  - `1 = real token`
  - `0 = padding`
- PyTorch expects:
  - `True = ignore padding`
- So mask is inverted:
```python
src_key_padding_mask = ~mask
```

---

## 6. Training

- Loss: `CrossEntropyLoss`
- Optimizer: `AdamW`
- Batch size: `8`
- Learning rate: `1e-4`
- Trained for multiple epochs with live loss printing

---

## 7. Prediction

- Model switches to evaluation mode
- Predictions generated on test set
- Argmax used to get final class
- Saved as:
```text
submission.csv
```

---

## Output Format

| target |
|--------|
| 2 |
| 0 |
| 4 |
| ... |

---

## Key Idea

The model learns **contextual meaning of news headlines** using a Transformer encoder trained on tokenized text, then classifies each headline into its correct category.