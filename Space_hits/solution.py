import pandas as pd
import numpy as np

from sklearn.decomposition import PCA


# -----------------------------
# Load Data
# -----------------------------
train_path = ""

X = pd.read_csv(train_path).drop(columns=['target'])




# -----------------------------
# Analyze Feature Variance
# -----------------------------
variances = X.var()

print("Feature Variances:")
print(variances.sort_values(ascending=False))




# -----------------------------
# Apply PCA
# -----------------------------
# Reduce all features into 1 dimension

pca = PCA(
    n_components=1
)

X_reduced = pca.fit_transform(
    X
)


print(
    "Explained Variance:",
    pca.explained_variance_ratio_[0]
)


# -----------------------------
# Create Submission
# -----------------------------

submission = pd.DataFrame({
    "target": X_reduced[:,0]
})


submission.to_csv(
    "submission.csv",
    index=False
)


print(submission.head())