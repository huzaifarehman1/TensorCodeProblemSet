# Space Hits - Solution Explanation

## Problem Understanding

The goal of this problem is to compress a high-dimensional asteroid dataset into exactly **one dimension** while preserving as much information as possible.

Each asteroid is represented using multiple numerical features. However, the dataset may contain redundant information and hidden patterns that can be represented using fewer dimensions.

The task is to find the most informative one-dimensional representation of the original data.

---

# Feature Variance Analysis

Before reducing the dimensions, we analyze the variance of each feature.

Variance measures how much a feature changes across different samples.

Features with larger variance often contain stronger patterns in the dataset.

```python
variances = X.var()
```

The variances are sorted to understand the importance of different features:

```python
variances.sort_values(ascending=False)
```

This analysis helps understand whether the dataset contains dominant directions of variation.

---

# Principal Component Analysis

To reduce all features into a single value, we use Principal Component Analysis (PCA).

PCA creates new features called principal components. These components are combinations of the original features.

The first principal component is:

\[
PC_1 = w_1x_1+w_2x_2+...+w_nx_n
\]

where:

- \(x_i\) are the original features.
- \(w_i\) are learned weights.

The weights are chosen so that the first component captures the maximum possible variance from the original dataset.

Since the required output has only one dimension, we keep only:

\[
PC_1
\]

---

# Why We Do Not Apply Feature Scaling

Normally, PCA is often used with feature scaling because features may have different units.

For example:

```
Temperature: 20 - 40
Population: 100000 - 5000000
```

Without scaling, the larger numerical range could dominate the principal components.

However, in this problem, variance differences are meaningful.

The features with higher variance contain important information about the hidden structure of the data.

Applying `StandardScaler` would force every feature to have the same variance and remove this useful information.

Therefore, PCA is applied directly on the original feature values.

---

# Applying PCA

PCA is applied with one component:

```python
pca = PCA(n_components=1)

X_reduced = pca.fit_transform(X)
```

The result is a single numerical value for every sample.

---

# Explained Variance

PCA provides the explained variance ratio:

```python
pca.explained_variance_ratio_[0]
```

This represents how much information from the original dataset is preserved by the one-dimensional representation.

A higher value means the compressed feature retains more of the original structure.

---



# Final Output

The submission contains one column:

```
target
```

Each row contains the one-dimensional compressed representation of the corresponding asteroid.

The original order of samples is preserved.