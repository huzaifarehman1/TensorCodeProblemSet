import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

# ============================================================
# Load the training data
# ============================================================
train_path = ""

train_df = pd.read_csv(train_path, index_col=0)

# Separate features and target
trainX = train_df.drop(columns=["target"])
trainY = train_df["target"]

# ============================================================
# Visualize the training data
# ============================================================
sns.scatterplot(
    data=trainX,
    x="Area",
    y=trainY,
    hue="Unknown"
)
plt.show()

# ============================================================
# Preprocessing
# ============================================================
# - Encode the categorical feature "Unknown"
# - Standardize the numerical feature "Area"
preprocessor = ColumnTransformer([
    ("categorical", OrdinalEncoder(), ["Unknown"]),
    ("numerical", StandardScaler(), ["Area"])
])

# ============================================================
# Create the machine learning pipeline
# ============================================================
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# ============================================================
# Train the model
# ============================================================
model.fit(trainX, trainY)


# ============================================================
# Load the test data
# ============================================================
test_path = ""

testX = pd.read_csv(test_path)

# ============================================================
# Generate predictions
# ============================================================
test_predictions = model.predict(testX)

# ============================================================
# Save predictions for submission
# ============================================================
submission = pd.DataFrame({
    "target": test_predictions
})

submission.to_csv("submission.csv", index=False)

print("Submission file saved as 'submission.csv'.")