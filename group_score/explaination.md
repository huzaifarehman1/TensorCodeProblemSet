## Solution Approach

### 1. Split the Dataset

The training data is divided into **training** and **validation** sets using an 80:20 split.

The training set is used to learn the hidden scoring function, while the validation set is used to measure how well the model generalizes to unseen data. This also enables early stopping to reduce overfitting.

---
### 2. Data Analysis
We use info and describe methods of data and find that all features are categorical in range [0-99]

### 3. Choose CatBoost

The dataset consists entirely of **categorical features**, where each feature represents a category rather than a numerical quantity.

CatBoost is specifically designed for this type of data. Unlike many traditional machine learning algorithms, it can process categorical features directly without requiring manual preprocessing such as one-hot encoding or label encoding. It also learns complex interactions between different categories automatically.

---

### 4. Train the Model

The CatBoost Regressor is trained using the training set.

During training:

- **RMSE** is used as the optimization objective because this is a regression problem.
- **R²** is monitored on the validation set to evaluate prediction quality.
- A small learning rate is used so the model gradually improves its predictions over many boosting iterations.

Each boosting iteration builds a new decision tree that focuses on correcting the errors made by the previous trees, allowing the model to learn increasingly complex relationships.

---

### 5. Apply Early Stopping

Training includes **early stopping**.

If the validation score does not improve for several consecutive iterations, training stops automatically and the model from the best validation score is retained.

This prevents unnecessary training and helps reduce overfitting.

---

### 6. Predict the Test Set

After training is complete, the final model is used to predict the target value for every sample in the test dataset.

Since the test set contains the same categorical features as the training data, the model can directly apply the relationships it has learned.

---

### 7. Generate Submission

The predicted values are stored in a CSV file named **`submission.csv`** containing a single column:

- `target`

This file is then submitted for evaluation.