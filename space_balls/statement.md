# Space Balls

## Problem Statement

Deep in the Andromeda Galaxy, astronomers have discovered a mysterious collection of floating **Space Balls**. Each Space Ball has two measurable properties that determine its location in space:

- `x`
- `y`

Scientists believe these Space Balls naturally belong to different **cosmic colonies**, but the colony labels were lost during transmission back to Earth.

Fortunately, observations suggest that the colonies formed naturally based on spatial proximity

Your mission is to reconstruct these hidden colonies by grouping the Space Balls into clusters.

---

## Input

The training dataset contains the following columns:

- `x` - x position of colony in 2D plane
- `y` - y poistion of colony in 2D plane



The test dataset is the same as training data so no need to download or use it
---

## Task
cluster the Space Balls  into the hidden cosmic colonies.

assign a cluster label to every Space Ball in the train dataset .  


---

## Output

For every Space Ball in the test dataset, predict its cluster ID.

The cluster IDs may be  integers (for example `0,1,2,3` or `5,8,12,17`)

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

| x | y |
|--:|--:|
| 10.4 | 8.9 |
| 11.3 | 9.5 |
| 61.1 | 58.7 |
| 59.6 | 61.0 |
| ... | ... |

### Example Prediction

| target |
|---------:|
| 0 |
| 0 |
| 2 |
| 2 |
| ... |

---

## Notes

- No cluster labels are provided in the training data.
- The number of hidden colonies is fixed for all datasets.
- Cluster IDs themselves are arbitrary; only the grouping of points matters.


---

## Submission

After predicting the cluster assignment for every sample in the test dataset:

1. Create a CSV file containing one prediction for each train sample.
2. Name the prediction column **`target`**.
3. Preserve the same row order as the train dataset.

Example:

| target |
|---------:|
| 0 |
| 0 |
| 2 |
| 1 |
| ... |

Save the file as **`submission.csv`** and upload it for evaluation.