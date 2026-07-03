import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

path_train = ''
path_test = ''


# -------------------------
# Load data
# -------------------------
train = pd.read_csv(path_train)
test = pd.read_csv(path_test)

X_train = train[["height", "weight"]]
y_train = train["target"]


sns.heatmap(train.corr(),cmap='coolwarm',annot=True)
plt.show()

# -------------------------
# Feature Engineering
# -------------------------
def add_features(df):
    df = df.copy()
    df["height_m"] = df["height"] / 100.0
    df["bmi"] = df["weight"] / (df["height_m"] ** 2)
    return df

X_train = add_features(X_train)
test = add_features(test)

train = add_features(train)
sns.heatmap(train.corr(),cmap='coolwarm',annot=True)
plt.show()

# -------------------------
# Train Linear Model
# -------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------
# Predict
# -------------------------
preds = model.predict(test)

# -------------------------
# Save submission
# -------------------------
submission = pd.DataFrame({
    "target": preds
})

submission.to_csv("submission.csv", index=False)

print("Submission file created!")