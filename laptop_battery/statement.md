# Laptop Battery Charge Prediction

## Problem Statement

Ali has been tracking his laptop’s charging behavior. Every time his laptop battery runs out, he plugs it in and records:

- The number of hours the laptop is charged
- The battery percentage gained after charging

Over time, he has collected this data in a CSV file.


## Task

Your goal is to build a regression model that learns the relationship between charging time and battery gain.

Given the number of hours a laptop is charged, predict the **battery percentage gained**.

## Input

A CSV file containing:

- `Hours_Charged` — Number of hours the laptop was charged
- `target` — Battery percentage gained after charging

## Output

For each input value of `Hours_Charged`, predict the corresponding `target`.

## Evaluation

Your predictions will be evaluated using a regression metric as:

- R² Score

## Example

| Hours_Charged | target |
|--------------|----------------|
| 1.0          | 20             |
| 2.0          | 40             |
| 3.5          | 70             |

If the laptop is charged for **2.5 hours**, your model should estimate the expected battery gain.

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing **all predicted values**.
2. Name the prediction column **`target`**.
3. Ensure the CSV contains exactly one row per test sample, in the same order as the test data.

Example:

| target |
|--------:|
| 0.82 |
| 1.35 |
| 2.17 |

Save the file as `submission.csv` and upload it for evaluation.