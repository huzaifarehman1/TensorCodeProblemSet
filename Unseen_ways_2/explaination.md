# Unseen Ways — t-SNE + Random Forest

## Approach

This solution uses **t-SNE to discover a separation in the training data**, then uses a Random Forest to learn that separation from the original features.

### 1. Feature Preparation

Four numerical features are selected:

```python
Feature_1, Feature_2, Feature_3, Feature_4
```

The features are standardized using `StandardScaler` so that they have comparable scales.

### 2. t-SNE

t-SNE reduces the four-dimensional feature space to two dimensions:

```text
Feature Space
     ↓
 StandardScaler
     ↓
    t-SNE
     ↓
TSNE_1, TSNE_2
```

The resulting points are visualized to examine whether the data naturally separates into two regions.

### 3. Creating Labels

A simple boundary is created using the first t-SNE coordinate:

```python
TSNE_1 <= 0 → Class 1
TSNE_1 > 0  → Class 2
```

this way we get back all the lost lables eleminating `0`.

These generated labels are then used as the target for the classifier.

### 4. Random Forest

A Random Forest with:

```python
n_estimators=100
max_depth=4
```

is trained on the **original standardized features** and the labels generated from t-SNE.

Five-fold cross-validation is used to check how well the Random Forest can reproduce the generated labels.

### 5. Test Prediction

The trained Random Forest predicts the class of every test observation.

The predictions are saved as:

```text
submission.csv
```

with a single `target` column containing only `1` or `2`.

## Key Idea

The method is essentially:

```text
Features
   ↓
Standardization
   ↓
t-SNE
   ↓
Find separation using TSNE_1
   ↓
Generate labels
   ↓
Random Forest learns the boundary
   ↓
Predict test classes
```

The original `class` column is used for visualization/comparison, but the Random Forest is trained using the **t-SNE-derived labels**.
