# Space Hits

## Problem Statement

A space agency is monitoring thousands of asteroids traveling through the solar system.

Each asteroid is described by many numerical measurements collected from onboard sensors, including its velocity, trajectory, rotation, composition, temperature, reflected light intensity, and several other hidden characteristics.

Scientists have discovered that transmitting every measurement back to Earth is too expensive. Instead, each asteroid must be represented by **a single numerical value** while preserving as much information about its original properties as possible.

Your task is to design a compression method that transforms every high-dimensional asteroid observation into **one informative feature**.

The compressed representation should retain as much of the original information as possible while reducing the data to exactly one dimension.

---

## Input

You are given a CSV file containing measurements of multiple asteroids.

Each row represents one asteroid.

Each column represents a numerical feature.

Example:

```
feature_0, feature_1, feature_2, ..., feature_n
```

All features are numerical.

---

## Task

Reduce every asteroid's feature vector to **exactly one numerical value**.

Your transformed feature should preserve the maximum possible amount of information contained in the original dataset.

The output must contain one value for every asteroid while preserving the original row order.

---

## Output

Create a CSV file containing exactly one column:

```
target
```

Example:

| target |
|--------------------|
| 3.42 |
| -1.15 |
| 0.68 |

---

## Evaluation

Your solution will be evaluated based on r2_score against the actual 1-D output with higest information
---

## Submission

After generating the compressed representation:

1. Create a CSV file.
2. Add a column named `target`.
3. Include one value for every asteroid.
4. Preserve the original row order.
5. Save the file as:

```
submission.csv
```

Upload this file for evaluation.

---

## Notes

- Every observation must be reduced to exactly one dimension.
- The original dataset may contain highly correlated features.
- Removing redundant information can significantly improve the quality of the compressed representation.