# Function Detective

## Problem Statement

Your friend loves creating mathematical puzzles. This time, they secretly designed a **deterministic polynomial function** using three variables:

- `x1`
- `x2`
- `x3`

The function has one important rule:

- Its polynomial degree is **at most 8**.

Your friend then evaluated this hidden function on many different inputs and recorded the results in a dataset.

Your challenge is to become a **Function Detective**. Using the provided training data, infer the hidden polynomial and predict its output for new unseen inputs.

---

## Input

The training dataset contains four columns:

- `x1`
- `x2`
- `x3`
- `target`

where `target` is the output of the hidden polynomial.

The test dataset contains only:

- `x1`
- `x2`
- `x3`

---

## Task

Train a regression model that learns your friend's hidden polynomial function and predicts the corresponding `target` values for every sample in the test dataset.

---

## Output

For each input sample in test data, predict the corresponding **target**.

---

## Evaluation

Your predictions will be evaluated using a regression metric such as:

- **R² Score**

---

## Example

| x1 | x2 | x3 | target |
|----:|----:|----:|-------:|
| 0.536 | 0.788 | 0.348 | 0.982 |
| 0.544 | 0.571 | 0.130 | 0.715 |
| 0.764 | 0.099 | 0.790 | 1.172 |
| 0.704 | 0.664 | 0.272 | 1.196 |
| 0.982 | 0.161 | 0.140 | 1.935 |

---


## Note

- The hidden function is **deterministic** (the same input always produces the same output).
- The hidden function is a **polynomial of degree no greater than 8**.
- No random noise has been added to the target values.

---

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