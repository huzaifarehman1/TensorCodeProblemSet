import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
# ============================================================
# Load Data
# ============================================================


train_path = ""
data = pd.read_csv(train_path)

X = data.drop(columns=["target"])
y = data["target"]

print(X.describe(),X.info())

# ============================================================
# Split Features and Target
# ============================================================

X = data.drop(columns=["target"])
Y = data["target"]

# ============================================================
# Train / Validation Split
# ============================================================

Xtrain, Xval, Ytrain, Yval = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

# ============================================================
# Model
# ============================================================

model = CatBoostRegressor(
    iterations=1000,
    learning_rate=0.05,
    loss_function="RMSE",
    eval_metric="R2",
    random_seed=42,
    verbose=100
)

model.fit(
    Xtrain,
    Ytrain,
    cat_features=list(range(10)),   # All 10 columns are categorical
    eval_set=(Xval, Yval),
    use_best_model=True,
    early_stopping_rounds=20
)

# ============================================================
# Evaluation
# ============================================================
test_path = ''
X = pd.read_csv(test_path)
pred = model.predict(X)
pd.DataFrame({
    "target": pred
}).to_csv("submission.csv", index=False)