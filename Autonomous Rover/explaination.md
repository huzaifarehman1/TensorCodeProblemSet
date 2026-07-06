## Solution Approach

### 1. Data Loading and Visualization
The training dataset is loaded using **Pandas**, and the input feature (**Speed_ms**) is separated from the target values. A **pairplot** is then generated using **Seaborn** to visualize the relationship between the feature and the target. This helps identify the overall trend in the data before selecting a model.

### 2. Observation
From the visualization, the relationship between **Speed_ms** and the target appears to be **quadratic** rather than linear. Because of this curved pattern, a simple linear model would not be sufficient to capture the relationship accurately.

### 3. Polynomial Feature Generation
To model the quadratic relationship, **PolynomialFeatures** with **degree = 2** is applied. This automatically creates additional polynomial terms, allowing the model to learn non-linear patterns while still using a linear regression algorithm internally.

### 4. Data Preprocessing
The generated polynomial features are standardized using **StandardScaler**. Standardization ensures that all features have a similar scale, which helps the optimization process and improves the stability of the regression model.

### 5. Building the Pipeline
A **Pipeline** is created to combine polynomial feature generation, feature scaling, and model training into a single workflow. This guarantees that the exact same preprocessing steps are applied during both training and prediction.

### 6. Model Training
A **Lasso Regression** model is trained on the transformed data. Lasso applies **L1 regularization**, which automatically reduces the coefficients of unnecessary polynomial features toward zero, effectively performing feature selection while fitting the regression model.

### 7. Generating Predictions
The trained pipeline is used to predict the target values for the unseen test dataset. Since preprocessing is included in the pipeline, the test data automatically undergoes the same polynomial transformation and scaling before prediction.

### 8. Submission
The predicted values are saved into a CSV file containing a single column named **`target`**. This file is then ready for submission and evaluation.