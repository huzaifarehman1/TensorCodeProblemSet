import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# 1. Load Data Splits
train_data = pd.read_csv('train.csv')
X_test = pd.read_csv('test.csv')
y_test = pd.read_csv('y_test.csv') # Backend target validation

# 2. Separate Features and Targets
X_train = train_data[['Temp_K', 'Methane_ppm', 'CO2_ppm', 'Stellar_Flux']]
y_train = train_data['target']

# 3. Model Optimization (Using Random Forest for non-linear feature interaction)
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
model.fit(X_train, y_train)

# 4. Inferencing and Evaluation
predictions = model.predict(X_test)
score = f1_score(y_test['target'], predictions)

print(f"Baseline Verification Validation F1-Score: {score:.4f}")

# 5. Build Platform Submission Standard Output
submission = pd.DataFrame({'target': predictions})
submission.to_csv('submission.csv', index=False)
print("Successfully generated submission.csv!")
