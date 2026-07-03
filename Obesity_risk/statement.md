# Obesity Score Prediction

## Problem Statement

A medical research team has collected data about individuals to study obesity levels based on basic body measurements.

For each person, they recorded:

- Height (in centimeters)
- Weight (in kilograms)

Using internal medical analysis, each individual has been assigned an **obesity score**. However, the exact formula used to compute this score has not been revealed.

Your task is to build a model that can learn the relationship between height, weight, and the obesity score.

---

## Task

Given a person’s height and weight, predict their **obesity score**.

You are expected to discover meaningful transformations of the input features that improve prediction performance.

---

## Input

A CSV file containing:

- `height` — Height of the person in **centimeters (cm)**
- `weight` — Weight of the person in **kilograms (kg)**

---

## Output

For each row in the test dataset, predict the corresponding **target** representing `obesity score`.

---

## Restrictions


- Only **linear models** are allowed (e.g., Linear Regression, Ridge, Lasso, ElasticNet, Linear SVM).
- Tree-based models (Random Forest, XGBoost, LightGBM, CatBoost) are **not allowed**.
- Neural networks are **not allowed**.
- External datasets are **not allowed**.

Feature engineering, scaling, and transformations are fully allowed and encouraged.

---

## Evaluation

Your predictions will be evaluated using:

- **R² Score**

Higher score indicates better performance.

---

## Example

| height (cm) | weight (kg) | target |
|-------------|-------------|--------|
| 170.0       | 70.0        | 22.8   |
| 160.0       | 55.0        | 21.5   |
| 180.0       | 90.0        | 27.8   |

A person with:

- height = 175 cm
- weight = 68 kg

should have their **obesity score** predicted accordingly.

---

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing all predicted values.
2. Name the column exactly: `target`
3. Ensure predictions are in the same order as the test set.
4. Save the file as `submission.csv`.