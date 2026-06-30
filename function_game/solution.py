import pandas as pd

from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# ============================================================
# Load the training data
# ============================================================
train_path = ""

train_df = pd.read_csv(train_path)

trainX = train_df.drop(columns=["target"])
trainY = train_df["target"]

# ============================================================
# Find the best polynomial degree
# ============================================================
best_degree = None
best_score = float("-inf")

for degree in [2 ,3, 4, 5, 6, 7]:

    pipeline = Pipeline([
        ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scaler", StandardScaler()),
        ("model", Lasso(alpha=1e-4, max_iter=100000))
    ])

    score = cross_val_score(
        pipeline,
        trainX,
        trainY,
        cv=5,
        scoring="r2"
    ).mean()

    print(f"Degree {degree}: {score:.6f}")

    if score > best_score:
        best_score = score
        best_degree = degree

print(f"\nSelected Degree: {best_degree}")

# ============================================================
# Train the final model
# ============================================================
pipeline = Pipeline([
    ("poly", PolynomialFeatures(degree=best_degree, include_bias=False)),
    ("scaler", StandardScaler()),
    ("model", Lasso(alpha=1e-4, max_iter=100000))
])

pipeline.fit(trainX, trainY)

# ============================================================
# Predict on the test set
# ============================================================
test_path = ""

testX = pd.read_csv(test_path)

predictions = pipeline.predict(testX)

# ============================================================
# Save submission
# ============================================================
pd.DataFrame({
    "target": predictions
}).to_csv("submission.csv", index=False)

print("Submission saved as submission.csv")