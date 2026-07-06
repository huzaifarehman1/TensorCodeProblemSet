import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.linear_model import Lasso
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline

# Load Data Splits

path_train = ''
test_path = ''

train_data = pd.read_csv(path_train)
X_test = pd.read_csv(test_path)


X_train = train_data[['Speed_ms']]
y_train = train_data['target']

sns.pairplot(train_data)
plt.show()
# this show quadratic relation
# Setup Polynomial Pipeline (Degree = 2 ) cause relation is quadratic

model = Pipeline([
    ('poly',PolynomialFeatures(degree=2)),
    ('std',StandardScaler()),
    ('model',Lasso()) # we use Lasso to automatically remove unwanted polynomial features this it acts as a feature select
])
model.fit(X_train,y_train)


# 4. Inferencing and Evaluation
predictions = model.predict(X_test)

# 5. Build Platform Submission Standard Output
submission = pd.DataFrame({'target': predictions})
submission.to_csv('submission.csv', index=False)
print("Successfully generated submission.csv!")
