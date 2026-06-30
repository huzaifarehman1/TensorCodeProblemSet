# 🏠 Alternative Universe House Price Prediction

## Problem Statement

David is analyzing housing prices in an alternative universe where standard real-world assumptions about geography and pricing do not fully apply. He has collected a dataset containing house prices influenced by both observable and partially unknown factors.

In this universe, house prices depend on measurable features as well as hidden environmental effects that are not directly observable.

---

## Task

Your goal is to build a regression model that learns the relationship between the available features and house prices.

Given the features of a house, predict its **market price**.

---

## Input

A CSV file containing:

- `Area` — A continuous numerical feature representing the size or spatial extent of the house. This value may be **negative or positive** due to non-standard spatial representation in this universe.
- `Unknown` — A categorical feature (`YES/NO`) representing an unobserved condition affecting house pricing. The exact meaning is not provided and may encode hidden structural or environmental effects.
- `target` — The target variable representing the house’s market price.

---

## Output

For each input sample, predict the corresponding **target**.

---

## Evaluation

Your predictions will be evaluated using a regression metric such as:

- **R² Score**

---

## Example

| Area   | Unknown | Price  |
|--------|--------|--------|
| -0.401 | NO     | -0.005 |
| -0.028 | NO     | 1.860  |
| 0.525  | NO     | 4.625  |
| 0.919  | NO     | 6.595  |
| 0.779  | NO     | 5.895  |

---

## Notes

- The `Area` feature may contain negative values and does not follow standard physical interpretation.
- The `Unknown` feature may represent latent factors not explicitly described in the dataset.
- The `target` representing price may contain negative values and does not follow standard physical interpretation.
- Traditional feature engineering may be limited due to missing contextual information.

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