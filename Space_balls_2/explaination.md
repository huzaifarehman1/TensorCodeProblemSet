# Space Balls 2 - Solution Explanation

## Overview

The goal of this problem is to discover hidden groups (clusters) of Space Balls without using any labels.

Each Space Ball is represented by 5 numerical features:

* `x1`
* `x2`
* `x3`
* `x4`
* `x5`

Since there are no target labels available, this is an **unsupervised learning** problem.

The solution uses **KMeans clustering** and automatically searches for the best number of clusters.

---

# 1. Loading the Data

The dataset is loaded using pandas.

```python
train = pd.read_csv(path)
```

The dataset contains only the features. The hidden colony labels are not available.

---

# 2. Feature Scaling

KMeans groups points based on Euclidean distance.

The distance between two points is:


d=sqrt{(x_1-y_1)^2+(x_2-y_2)^2+...+(x_5-y_5)^2}


If one feature has a larger numerical range than other features, it can dominate the distance calculation.

To avoid this, the features are standardized:

```python
scaler = StandardScaler()

X = scaler.fit_transform(train)
```

After scaling, all dimensions contribute equally to clustering.

---

# 3. Finding the Best Number of Clusters

KMeans requires the number of clusters (`k`) before training.

Since the true number of cosmic colonies is unknown, different values of `k` are tested.

The solution checks:

```
2, 4, 6, 8, ... , 64
```

For every value of `k`:

1. Train a KMeans model.
2. Generate cluster labels.
3. Evaluate clustering quality.

---

# 4. Clustering Evaluation Metrics

Three different clustering metrics are used.

## Silhouette Score

The Silhouette Score measures how close each point is to points in its own cluster compared to other clusters.

Higher values indicate better separated clusters.

Range:

```
-1 to 1
```

Higher is better.

---

## Calinski-Harabasz Score

The Calinski-Harabasz Score evaluates:

* separation between clusters
* compactness inside clusters

Higher values indicate better clustering.

---

## Davies-Bouldin Score

The Davies-Bouldin Score measures similarity between clusters.

Lower values mean:

* clusters are more separated
* clusters overlap less

Lower is better.

---

# 5. Combining the Metrics

The metrics have different scales, so ranking is used instead of directly adding values.

For each metric:

* Silhouette Score is ranked with higher values first.
* Calinski-Harabasz Score is ranked with higher values first.
* Davies-Bouldin Score is ranked with lower values first.

Then the ranks are combined:

```python
total_score = (
    silhouette_rank
    +
    calinski_rank
    +
    davies_rank
)
```

The `k` with the smallest total score is selected as the best number of clusters.

---

# 6. Training the Final KMeans Model

After selecting the best `k`, a final KMeans model is trained:

```python
final_model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=50
)
```

`n_init=50` runs KMeans multiple times with different initializations and chooses the best result.

This makes the clustering more stable because KMeans can produce different results depending on initialization.

---

# 7. Generating Cluster Labels

The final model assigns every Space Ball to a cluster:

```python
final_labels = final_model.fit_predict(X)
```

The generated cluster IDs represent the discovered colonies.

---

# 8. Creating Submission File

The predictions are stored in the required format:

```python
submission = pd.DataFrame(
    {
        "target": final_labels
    }
)
```

The final file:

```
submission.csv
```

contains:

| target     |
| ---------- |
| cluster_id |
| cluster_id |
| cluster_id |

with one prediction for every Space Ball.

---