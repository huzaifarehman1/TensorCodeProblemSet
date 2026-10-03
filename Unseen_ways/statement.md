# Unseen Ways

## The Story

During an experiment, researchers collected measurements from two different types of specimens. Every specimen originally belonged to one of two classes:

* **Class 1**
* **Class 2**

Each specimen was recorded using several measurable features. Unfortunately, during the transfer of the data, some of the original class information was lost.

The researchers still have the feature measurements for every specimen, but for some of them, the class label has been replaced with **0**.

Your task is to recover the missing information.

---

## The Problem

You are given a dataset containing observations from **two classes**. Each observation has several numerical features and a class label.

The class label can be:

* `1` — the observation belongs to Class 1
* `2` — the observation belongs to Class 2
* `0` — the original class was lost

Your goal is to predict the original class of **every observation whose label is `0`**.

You may use the observations whose classes are known (`1` or `2`) to learn the relationship between the features and the class.

For every observation with a missing class, you must assign either:

* `1`, or
* `2`

After your predictions, **no `0` labels should remain**.

---

## Important Restriction

You are **not allowed to use any clustering algorithm**.

You may use any appropriate supervised learning technique, feature-based analysis,rule based spliting, or other non-clustering approach to determine the missing classes.

---

## Input

The input dataset contains:

* Several numerical features describing each observation.
* A `class` column containing `0`, `1`, or `2`.

A class value of `0` means that the original class is unknown and must be predicted.

---

## Output

For every row whose original class is `0`, output the predicted class:

* `1` for Class 1
* `2` for Class 2

Every missing class must be replaced with either `1` or `2` and the rest should remain the same.

---
## Evaluation Metric

Submissions are evaluated using **Classification Accuracy**.

---
## Submission Format

Your submission must be a CSV file with the following format:

| target |
|------:|
| 1 |
| 2 |
| 1 |
| 1 |
| ... |

where:

- `target` is the predicted class label (an integer either **1** or **2**).
do this for all datapoints even for those whoms class is initially given the number of rows in submission is equall to that of the input file.

---

Good luck, and happy modeling!

