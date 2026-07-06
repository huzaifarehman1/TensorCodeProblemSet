import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

# 1. Load Data Splits
train_data = pd.read_csv('train.csv')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv') # Backend target validation

X_train = train_data[['Speed_ms']]
y_train = train_data['target']

# 2. Setup Polynomial Pipeline (Degree = 2 due to physical scaling)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# 3. Model Optimization
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 4. Inferencing and Evaluation
predictions = model.predict(X_test_poly)
rmse_score = root_mean_squared_error(y_test, predictions)

print(f"Baseline Verification Validation RMSE: {rmse_score:.4f} meters")

# 5. Build Platform Submission Standard Output
submission = pd.DataFrame({'target': predictions})
submission.to_csv('submission.csv', index=False)
print("Successfully generated submission.csv!")
