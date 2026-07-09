import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score
)

# ---------------------------------
# Load Data
# ---------------------------------
path = ''
train = pd.read_csv(path)


# ---------------------------------
# Preprocessing
# ---------------------------------

scaler = StandardScaler()

X = scaler.fit_transform(train)


# ---------------------------------
# Search Best K
# ---------------------------------

results = []

# Try every second number
for k in range(2, 65, 2):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20
    )

    labels = kmeans.fit_predict(X)

    silhouette = silhouette_score(
        X,
        labels
    )

    calinski = calinski_harabasz_score(
        X,
        labels
    )

    davies = davies_bouldin_score(
        X,
        labels
    )

    results.append(
        {
            "k": k,
            "silhouette": silhouette,
            "calinski": calinski,
            "davies": davies
        }
    )


scores = pd.DataFrame(results)

print(scores)


# ---------------------------------
# Normalize Scores
# ---------------------------------

# Higher is better for silhouette and calinski
scores["silhouette_rank"] = (
    scores["silhouette"]
    .rank(ascending=False)
)

scores["calinski_rank"] = (
    scores["calinski"]
    .rank(ascending=False)
)

# Lower is better for davies
scores["davies_rank"] = (
    scores["davies"]
    .rank(ascending=True)
)


# Combined ranking

scores["total_score"] = (
    scores["silhouette_rank"]
    +
    scores["calinski_rank"]
    +
    scores["davies_rank"]
)


best_k = (
    scores
    .sort_values("total_score")
    .iloc[0]["k"]
)

best_k = int(best_k)


print(
    "Best number of clusters:",
    best_k
)


# ---------------------------------
# Train Final Model
# ---------------------------------

final_model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=50
)

final_labels = final_model.fit_predict(X)


# ---------------------------------
# Save Submission
# ---------------------------------

submission = pd.DataFrame(
    {
        "target": final_labels
    }
)

submission.to_csv(
    "submission.csv",
    index=False
)

print(submission.head())