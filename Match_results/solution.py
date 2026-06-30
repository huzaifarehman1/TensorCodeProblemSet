import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ============================================================
# Load the training data
# ============================================================
train_path = ""

train_df = pd.read_csv(train_path)

trainX = train_df.drop(columns=["target"])
trainY = train_df["target"]

# ============================================================
# info of the training data
# ============================================================

print(train_df.info())
print(train_df.describe())

# ============================================================
# Build the model
# ============================================================
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

# ============================================================
# Train the model
# ============================================================
pipeline.fit(trainX, trainY)

# ============================================================
# Load the test data
# ============================================================
test_path = ""

testX = pd.read_csv(test_path)

# ============================================================
# Generate predictions
# ============================================================
predictions = pipeline.predict(testX)

# ============================================================
# Save submission
# ============================================================
submission = pd.DataFrame({
    "target": predictions
})

submission.to_csv("submission.csv", index=False)

print("Submission saved as submission.csv")