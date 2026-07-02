# Molecular Class 

## THIS PROBLEM IS TAKEN FROM `BENIN OLYMPIAD OF AI`

## Problem Statement

Sara is developing an AI system to determine whether a chemical compound belongs to a specific molecular class. Each molecule is represented by a collection of numerical features and Binary Categorical Features describing its chemical properties and structure.

Your task is to build a **binary classification model** that learns from the training data and predicts whether each molecule belongs to the target molecular class.

---

## Dataset

The dataset is adapted from the **Benin National Olympiad of Artificial Intelligence (NOAI)**.

Each sample represents a single molecule described by several numerical features extracted from its chemical structure.

### Training Data

The training CSV contains:

- Neumerical and Categorical features combined
- Total 284 features from `f1` to `f284`
- A `target` column indicating the class:
  - **0** → Molecule does **not** belong to the target class
  - **1** → Molecule **belongs** to the target class

### Test Data

The test CSV contains only the molecular features.

Your goal is to predict the probability that the sample belong to class `1` .

---

## Classes

There are **2** possible classes:

- **0** — Negative
- **1** — Positive

---

## Evaluation Metric

Submissions are evaluated using **Roc-AOC-Score**.

---

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing **all predicted probabilty of class 1**.
2. Name the prediction column **`target`**.
3. Ensure the CSV contains exactly one row per test sample, in the same order as the test data.

Example:

| target |
|--------:|
| 0.82 |
| 0.35 |
| 0.17 |

where:

- `target` contain the predicted probability that the sample belong to class `1`.

Save the file as `submission.csv` and upload it for evaluation.

