## Solution Approach

### 1. Data Loading
The training dataset is loaded using **Pandas**, and the input features (`x1`, `x2`, `x3`) are separated from the target values.

### 2. Feature Engineering
Since the hidden function is guaranteed to be a **polynomial of degree at most 8**, polynomial features are generated to allow a linear model to learn non-linear relationships.

Instead of manually creating interaction and power terms, **PolynomialFeatures** automatically generates all polynomial combinations up to the selected degree.

### 3. Model Selection
Rather than assuming the correct polynomial degree, four candidate degrees are evaluated which we believe are the most probable:
- Degree 2
- Degree 3
- Degree 4
- Degree 5
- Degree 6
- Degree 7

For each degree, a pipeline containing polynomial feature generation, feature scaling, and **Lasso Regression** is evaluated using **5-fold Cross Validation** with the **R² score**.

The degree with the highest average R² score is selected as the final model.

### 4. Feature Scaling
After polynomial expansion, the magnitude of the generated features can vary significantly.

To ensure all features contribute fairly during optimization, **StandardScaler** is used to standardize every feature before training.

### 5. Model Training
The final pipeline is rebuilt using the selected polynomial degree and trained on the entire training dataset.

**Lasso Regression** is used because it can automatically reduce the influence of unnecessary polynomial terms through L1 regularization, helping prevent overfitting and also doing feature selection by itself.

### 6. Generating Predictions
The trained pipeline is applied to the unseen test dataset. Since preprocessing is included inside the pipeline, the same polynomial expansion and feature scaling are automatically performed before predictions are generated.

### 7. Submission
The predicted values are saved in a CSV file with a single column named **`target`**. This file is then ready for submission and evaluation.