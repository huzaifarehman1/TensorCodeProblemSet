# Space Balls 2

## Problem Statement

Deep in the Andromeda Galaxy, astronomers have discovered a mysterious collection of floating **Space Balls**. 

Each Space Ball exists in a hidden 5-dimensional cosmic space. Scientists can measure five different properties that describe the position of each Space Ball:

- `x1`
- `x2`
- `x3`
- `x4`
- `x5`

Scientists believe that these Space Balls naturally belong to different **cosmic colonies**, but the colony labels were lost during transmission back to Earth.

Fortunately, observations suggest that the colonies formed naturally based on similarity in this 5-dimensional space positions.

Your mission is to reconstruct these hidden colonies by grouping the Space Balls into clusters.

---

## Input

The training dataset contains the following columns:

- `x1` - first spatial dimension
- `x2` - second spatial dimension
- `x3` - third spatial dimension
- `x4` - fourth spatial dimension
- `x5` - fifth spatial dimension


The test dataset is the same as training data, so no need to download or use it.

---

## Task

Cluster the Space Balls into their hidden cosmic colonies.

Assign a cluster label to every Space Ball in the train dataset.

---

## Output

For every Space Ball in the dataset, predict its cluster ID.

The cluster IDs may be any integers:

The actual cluster numbers do not matter. Only the grouping is evaluated.

---

## Evaluation

Your submission will be evaluated using the **Adjusted Rand Index (ARI)**.

The Adjusted Rand Index compares your predicted clustering with the hidden ground-truth clustering while ignoring the actual numeric values of cluster IDs.

- **1.0** indicates a perfect clustering.
- **0.0** corresponds to random clustering.
- Negative values indicate clustering worse than random chance.

---

## Example

### Training Data

| x1 | x2 | x3 | x4 | x5 |
|---:|---:|---:|---:|---:|
| 10.4 | 8.9 | 5.1 | 7.8 | 12.3 |
| 11.3 | 9.5 | 5.6 | 8.1 | 11.9 |
| 61.1 | 58.7 | 62.4 | 59.3 | 64.2 |
| 59.6 | 61.0 | 60.8 | 62.2 | 63.5 |

---

### Example Prediction

| target |
|-------:|
| 0 |
| 0 |
| 2 |
| 2 |

---

## Notes

- No cluster labels are provided in the training data.
- The number of hidden colonies is fixed for all datasets.
- Cluster IDs themselves are arbitrary.
- Distance calculations should consider all five dimensions.

---

## Submission

After predicting the cluster assignment for every sample:

1. Create a CSV file containing one prediction for each train sample.
2. Name the prediction column **`target`**.
3. Preserve the same row order as the train dataset.

Example:

| target |
|-------:|
| 0 |
| 0 |
| 2 |
| 1 |

Save the file as:
