import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -----------------------------
# Load Data
# -----------------------------
train_path = ''
train = pd.read_csv(train_path)


# -----------------------------
# Visualize Training Data
# -----------------------------
plt.figure(figsize=(6, 6))
plt.scatter(train["x"], train["y"], s=35)
plt.title("Space Balls Training Data")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
# We see there are 4 clusters in spherical figures so we use kmean and n = 4
# -----------------------------
# Train K-Means
# -----------------------------
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
)

kmeans.fit(train)

# -----------------------------
# Predict Test Clusters
# -----------------------------
predictions = kmeans.predict(train)

# -----------------------------
# Create Submission
# -----------------------------
submission = pd.DataFrame({
    "target": predictions
})

submission.to_csv("submission.csv", index=False)

print("submission.csv created successfully!")

