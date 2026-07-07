# Explanation

## Observing the Data

The dataset contains only two features:

- `x`
- `y`

Since there are only two dimensions, the first step is to visualize the data using a scatter plot.

```python
plt.scatter(train["x"], train["y"])
```

The visualization clearly reveals **four compact, well-separated spherical groups** of Space Balls.

Because the clusters are:

- compact,
- roughly circular,
- and well separated,

**K-Means** is an excellent choice for this problem.

---

## Choosing the Number of Clusters

By inspecting the scatter plot, we can clearly identify **4 distinct groups**.

Therefore, we set

```python
n_clusters = 4
```

---

## Training K-Means

We fit a K-Means model on the training data.

```python
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
)

kmeans.fit(train)
```

K-Means works by repeatedly performing two steps:

1. Assign every point to its nearest centroid.
2. Move each centroid to the mean of the points assigned to it.

These steps are repeated until the cluster assignments stop changing.

---

## Predicting Cluster Labels

Once the model has learned the cluster centers, every point is assigned to its nearest centroid.

```python
predictions = kmeans.predict(train)
```

The predicted cluster IDs become our final answers.

---

## Creating the Submission

The competition expects a CSV file containing one column named **`target`**.

```python
submission = pd.DataFrame({
    "target": predictions
})

submission.to_csv("submission.csv", index=False)
```

The resulting file has the following format:

| target |
|--------:|
| 0 |
| 0 |
| 2 |
| 1 |
| ... |

---

