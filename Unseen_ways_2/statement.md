# Unseen Ways

## The Story

During an experiment, researchers collected measurements from two different types of specimens.

Every specimen originally belonged to one of two classes:

* **Class 1**
* **Class 2**

The researchers first collected a set of specimens for which the correct class was known. This dataset can be used to learn the relationship between the measured features and the class.

The researchers still have the feature measurements for every specimen, but for many of them, the class label has been replaced with **0** which may originally be a 1 or a 2.


Your task is to use the labeled training data to predict the class of every specimen in this new, unseen dataset.

---

## The Problem

You are given two datasets:

### Training Data

The training dataset contains:

* Several numerical features describing each observation.
* A `class` column containing the known class.

The class can be:

* `1` — the observation belongs to Class 1
* `2` — the observation belongs to Class 2
* `0` — the observation belongs to either Class 1 or Class 2 but its original lable is lost
The training data should be used to learn patterns that distinguish the two classes.

### Test Data

The test dataset contains the same feature measurements, but the class labels are not provided.

Your goal is to predict the class of **every observation in the test dataset**.

For every test observation, you must assign either:

* `1`, or
* `2`

---

## Important Restriction

You **must not use clustering algorithms** to determine the class labels.

You may use:

* Supervised machine learning
* Statistical methods
* Mathematical analysis
* Feature engineering
* Rule-based classification
* Distance-based supervised methods
* Ensemble methods
* Other non-clustering approaches

The final prediction for every test observation must be either `1` or `2`.

---

## Input

Two datasets are provided:

### Training Dataset

The training dataset contains several numerical features and a `class` column.

Example:

| Feature_1 | Feature_2 | Feature_3 | class |
| --------: | --------: | --------: | ----: |
|      1.42 |      5.31 |      2.18 |     1 |
|      2.17 |      4.92 |      1.73 |     2 |
|      1.91 |      5.12 |      2.04 |     1 |
|       ... |       ... |       ... |   ... |

The `class` column contains the correct class for each training observation.

### Test Dataset

The test dataset contains the feature columns but does not contain the target class.

Example:

| Feature_1 | Feature_2 | Feature_3 |
| --------: | --------: | --------: |
|      2.01 |      5.44 |      1.91 |
|      1.73 |      4.81 |      2.36 |
|      3.12 |      6.02 |      1.47 |
|       ... |       ... |       ... |

The number of observations in the test dataset determines the required number of predictions.

---

## Task

Train a classification method using the labeled training data.

Then use the trained model or classification method to predict the class of **every observation in the test dataset**.

Each prediction must be either:

* `1` — Class 1
* `2` — Class 2

There must be exactly **one prediction for every test observation**.

---

## Evaluation Metric

Submissions are evaluated using:

**Classification Accuracy**

$$
\text{Accuracy}
=
\frac{\text{Number of Correct Predictions}}
{\text{Total Number of Test Observations}}
$$

A higher accuracy results in a better score.

---

## Submission Format

Your submission must be a CSV file containing exactly one column:

```text
target
```

Each row must contain the predicted class for the corresponding row of the test dataset.

Example:

| target |
| -----: |
|      1 |
|      2 |
|      1 |
|      1 |
|      2 |
|    ... |

The number of rows in the submission must be **exactly equal to the number of rows in the test dataset**.

The predictions must remain in the **same order as the test dataset**.

---

## Submission Requirements

Your submission must satisfy all of the following:

1. The CSV must contain a column named `target`.
2. Every value in `target` must be either `1` or `2`.
3. There must be exactly one prediction for every test observation.
4. The ordering of predictions must match the ordering of the test dataset.
5. No index column should be included unless explicitly requested.
6. The training labels must not be included in the submission.
7. NO visualization of test data is allowed or use of clustring algorithm

---

## Goal

Build a robust classifier that can correctly distinguish Class 1 from Class 2 even when the test observations come from a distribution that differs from the training data.

Careful analysis of the data is likely to be important.

**Good luck, and happy modeling!**
