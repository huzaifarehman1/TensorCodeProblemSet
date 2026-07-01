# CIFAR-10 Image Classification

## Problem Statement

Ali is building an image recognition system that can automatically identify objects in photographs. To train his model, he collected thousands of small color images belonging to different object categories.

Each image is represented by its RGB pixel values, and the goal is to predict which object appears in the image.

Your task is to build a **multi-class classification model** that learns from the training data and predicts the correct class for each image in the test set.

---

## Dataset

The dataset is based on the **CIFAR-10** image dataset.

Each image:

- Has a resolution of **32 × 32** pixels
- Contains **3 color channels (RGB)**
- Is flattened into **3072 numerical features**
  - First 1024 values → Red channel
  - Next 1024 values → Green channel
  - Last 1024 values → Blue channel

### Training Data

The training CSV contains:

- 3072 pixel features
- `target` column containing the image class

### Test Data

The test CSV contains only the 3072 pixel features.

Your goal is to predict the missing class labels.

---

## Classes

There are **10** possible classes:

| Label | Class |
|-------:|-------|
| 0 | airplane |
| 1 | automobile |
| 2 | bird |
| 3 | cat |
| 4 | deer |
| 5 | dog |
| 6 | frog |
| 7 | horse |
| 8 | ship |
| 9 | truck |

---

## Evaluation Metric

Submissions are evaluated using **Classification Accuracy**.

\[
\text{Accuracy}=\frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}
\]

Higher accuracy indicates better performance.

---

## Submission Format

Your submission must be a CSV file with the following format:

| ID | target |
|---:|-------:|
| 0 | 3 |
| 1 | 8 |
| 2 | 1 |
| ... | ... |

where:

- `ID` is the row index from the test dataset.
- `target` is the predicted class label (an integer from **0–9**).

---

Good luck, and happy modeling!