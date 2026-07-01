# Group Score

## Problem Statement

A research institute is studying how different combinations of people perform when working together.

Each participant is described by **10 attributes**, such as their background, preferences, experience group, and other anonymized characteristics.

The institute has developed a **hidden scoring system** that evaluates how well a particular combination of attributes performs as a group. The exact scoring function is unknown and can involve complex interactions between the attributes.

Using this data, your task is to learn this hidden scoring system and predict the score for new groups.

---

## Input

The training dataset contains the following columns:

- `cat_0`
- `cat_1`
- `cat_2`
- `cat_3`
- `cat_4`
- `cat_5`
- `cat_6`
- `cat_7`
- `cat_8`
- `cat_9`
- `target`

Each  feature takes an integer value:


The test dataset contains the same features but does **not** include the `target` column.

---

## Task

Train a regression model that learns the hidden scoring function from the training data and predicts the score (`target`) for every sample in the test dataset.

---

## Output

For every row in the test dataset, predict the corresponding **target** value.

---

## Evaluation

Your predictions will be evaluated using:

- **R² Score**



---


## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing one prediction for each test sample.
2. Name the prediction column **`target`**.
3. Keep the rows in the same order as the test dataset.

Example:

| target |
|--------:|
| 1.28 |
| -0.64 |
| 2.91 |

Save the file as **`submission.csv`** and upload it for evaluation.