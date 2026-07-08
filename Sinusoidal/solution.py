import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


# -----------------------------
# Load Data
# -----------------------------

train_path = ""
test_path = ""


train = pd.read_csv(train_path)
test = pd.read_csv(test_path)



# -----------------------------
# Transform Target
# -----------------------------
# y = e^(f(x))
# log(y) = f(x)

train["target"] = np.log(
    train["target"]
)



# -----------------------------
# Analyze Relationships
# -----------------------------
for i in train.columns:
    sns.scatterplot(
        train,
        x=i,
        y='target')

    #plt.show()



# -----------------------------
# Choose Hidden X Feature
# -----------------------------
# After looking at pairplot choose the feature

chosen = "feature_2"


X_train = train[[chosen]]

y_train = train["target"]



# -----------------------------
# Train Linear Regression
# -----------------------------

model = LinearRegression()

model.fit(
    X_train,
    y_train
)





# -----------------------------
# Predict Test
# -----------------------------

X_test = test[[chosen]]

# Predict f(x)
prediction = model.predict(
    X_test
)


# Convert back:
# sin(f(x))

prediction = np.exp(
    prediction
)



# -----------------------------
# Submission
# -----------------------------

submission = pd.DataFrame({
    "target": prediction
})


submission.to_csv(
    "submission.csv",
    index=False
)


print(submission.head())