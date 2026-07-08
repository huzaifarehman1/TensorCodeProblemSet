# Exponential Signal

## Problem Statement

A space communication satellite is collecting signals from a distant planet.

The satellite receives a continuous wave signal, but due to transmission constraints, the original signal formula is not stored. The scientists only have a collection of input-output measurements.

After studying the signal generator, scientists discovered that the signal follows this hidden structure:


y = e^(f(x))

However due to Transmission error we got `distorted duplications` meaning our data have more than 1 features among these x is hidden and these new signals are noisy and dont contain the actual x 


Your task is to analyze the received data, and make a model that produce `y` given entire dataset with distorted duplications among with the actual `x` is hidden

---

## Input

You are given a CSV file containing the recorded signal measurements and Distorted Duplications.

Each row represents one observation from the satellite.

The file contains:

```
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,target
```

where:

- `target` is the received signal value.

---

## Task

Build a regression system that predicts the signal value for unseen input values.

Your solution should:

- Analyze the relationship between `features` and `target`.
- Discover the hidden mathematical pattern.
- Generate accurate predictions.

---

## Output

Create a CSV file containing one column:

```
target
```

Each row should contain the predicted signal value for the corresponding test sample.

Example:

| target |
|--------|
| 0.42 |
| -0.76 |
| 0.91 |

---

## Evaluation

Your submission will be evaluated using the:

**R² Score**

---

## Notes


- if a feature is useless than every single number in that feature is useless (:Hint)


Good luck, and recover the lost signal!