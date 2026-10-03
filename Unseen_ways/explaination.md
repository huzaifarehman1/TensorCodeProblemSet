# Unseen Ways — Solution Explanation

## 1. Loading the Data

We first load the training dataset and separate the four numerical features from the class column.

```python
FEATURES = ["Feature_1", "Feature_2", "Feature_3", "Feature_4"]
TARGET = "class"

X = train[FEATURES].copy()
y = train[TARGET].copy()
```

The `class` column contains the original class information.

* `1` → Class 1
* `2` → Class 2
* `0` → Original class was lost

---

## 2. Standardizing the Features

Before applying t-SNE, the features are standardized using `StandardScaler`.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

This ensures that features with larger numerical scales do not dominate the transformation.

---

## 3. Reducing the Data to Two Dimensions

We use **t-SNE** to transform the four-dimensional feature space into two dimensions.

```python
tsne = TSNE(
    n_components=2,
    perplexity=30,
    learning_rate="auto",
    random_state=42
)

X_tsne = tsne.fit_transform(X_scaled)
```

The resulting two dimensions are stored as:

```python
TSNE_1
TSNE_2
```

We can now visualize the observations on a 2D scatter plot.

```python
sns.scatterplot(
    x=train["TSNE_1"],
    y=train["TSNE_2"],
    hue=y
)

plt.show()
```

The important observation is that the data forms two clearly separated regions.

t-SNE itself does **not** assign classes. It only provides a two-dimensional representation in which the structure of the data can be visualized.

---

## 4. Creating a Classification Rule

After observing the t-SNE plot, we use the first t-SNE component to separate the two regions.

Our rule is:

```python
lables = X_tsne[:, 0] > 0
```

This produces Boolean values:

* `False` → `0`
* `True` → `1`

We convert these to integers and add `1`:

```python
lables = np.asarray(lables, dtype=np.int16)
lables += 1
```

Therefore:

```text
TSNE_1 <= 0  → Cluster 1
TSNE_1 >  0  → Cluster 2
```

This gives us a predicted class for every observation.

---

## 5. Checking the Assigned Class Orientation

There is an important issue with this approach.

t-SNE has **no knowledge of which side represents Class 1 and which side represents Class 2**.

Therefore, even if the separation is completely correct, we could accidentally assign:

```text
Actual Class 1 → Predicted Class 2
Actual Class 2 → Predicted Class 1
```

In other words, the entire labeling could be flipped.

To check this, we compare our generated labels with the original labels that are still available.

```python
sns.scatterplot(
    x=train["TSNE_1"],
    y=train["TSNE_2"],
    hue=lables-y
)

plt.show()
```

For points whose original class is known, `lables - y` tells us whether our assigned class agrees with the original class.

For example:

```text
Predicted = 1, Actual = 1
1 - 1 =  0

Predicted = 2, Actual = 2
2 - 2 =  0
```

So a correctly oriented classification produces `0` for correctly classified known points.

If we accidentally flipped the labels:

```text
Predicted = 1, Actual = 2
1 - 2 = -1

Predicted = 2, Actual = 1
2 - 1 = +1
```

Therefore, the difference plot makes it easy to detect whether our manually assigned Class 1 / Class 2 orientation agrees with the known labels.

This is especially important because the numerical direction of a t-SNE component is arbitrary. A different t-SNE run can effectively mirror or rotate the visualization without changing the underlying structure.

---

## 6. Generating the Submission

Once the orientation has been verified, we create the submission file.

```python
submission = pd.DataFrame({
    "target": lables
})

submission.to_csv(
    "submission.csv",
    index=False
)
```

The final submission contains the predicted class for every observation.

---

## Summary

The complete approach is:

```text
4 Features
    ↓
StandardScaler
    ↓
t-SNE
    ↓
2D Representation
    ↓
Visualize the two regions
    ↓
Use TSNE_1 > 0 as the decision rule
    ↓
Convert the two sides to Class 1 / Class 2
    ↓
Compare predicted labels with known labels
    ↓
Verify that the class orientation is correct
    ↓
Generate submission.csv
```

No clustering algorithm is used.

The two groups are identified visually in the t-SNE representation, and the final labels are produced using a deterministic classification rule.

