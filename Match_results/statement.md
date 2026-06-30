# Match Result

## Problem Statement

Two teams are competing in an unknown sport where the winner is decided using three primary scores. Unfortunately, the official rulebook given to you explaining how these scores determine the winner was destroyed in a fire.

Luckily, records from previous matches survived. Each record contains the three scores along with the winning team. By studying these historical matches, your task is to uncover the hidden decision rule and predict the winner of current matches.

---

## Input

Each sample contains three features:

- `Team1_score`
- `Team2_score`
- `Evaluation_score`

The training dataset also includes the target column:

- `target` => which is categorical with the following categories

- `0` → Match won by **Team 1**
- `1` → Match won by **Team 2**

---

## Task

Train a binary classification model using the historical match data. Your model should learn the hidden relationship between the three scores and the match outcome, then predict the winner for every match in the test dataset.

---

## Output

The target is a binary label:

- `0` → Match won by **Team 1**
- `1` → Match won by **Team 2**

For each input sample in test data, predict the corresponding **target**.

---

## Evaluation

Predictions will be evaluated using the **F1 Score**.

---

## Example

| Team1_score | Team2_score | Evaluation_score | target |
|------------:|------------:|-----------------:|-------:|
| -2.509 | -2.127 | -2.527 | 0 |
| 9.014 | -0.531 | -3.342 | 0 |
| 4.640 | 7.091 | -6.477 | 0 |
| 1.973 | -3.200 | 2.145 | 0 |
| -6.880 | -8.237 | 7.314 | 0 |

---

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing all predicted labels.
2. Name the prediction column **`target`**.
3. Ensure the CSV contains exactly one row per test sample, in the same order as the test dataset.

Example:

| target |
|-------:|
| 0 |
| 1 |
| 0 |

Save the file as `submission.csv` and upload it for evaluation.