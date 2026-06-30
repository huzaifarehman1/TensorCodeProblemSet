## Solution Approach

### 1. Data Loading and Visualization
The training dataset is loaded using **Pandas**, and the features are separated from the target values. A scatter plot is then created to visualize the relationship between **Area** and the house price while coloring the points based on the **Unknown** categorical feature. This helps determine whether a linear relationship exists and whether the categorical feature influences the target.

### 2. Observation:
in the plot we say a decision wise linear line which showcase a direct influence of the **Unknown** variable on the target so we do Ordinal encoding on it to exploit the decision wise linear relation.

### 3. Data Preprocessing
Before training the model, each feature is preprocessed appropriately:

- The **Unknown** categorical feature is converted into numerical values using **Ordinal Encoding**.
- The **Area** numerical feature is standardized using **StandardScaler** so that it has a mean of 0 and a standard deviation of 1 making it easier for model to learn from it.

A **ColumnTransformer** is used to apply the correct preprocessing technique to each column.

### 4. Building the Pipeline
A **Pipeline** is created to combine preprocessing and model training into a single workflow. This ensures that the same preprocessing steps are automatically applied during both training and prediction, reducing the chance of inconsistencies.

### 5. Model Training
A **Linear Regression** model is trained using the preprocessed training data. The model learns the relationship between the input features (`Area` and `Unknown`) and the target house price.

### 6. Generating Predictions
The trained pipeline is used to predict house prices for the unseen test dataset. Since preprocessing is part of the pipeline, the test data is automatically transformed before predictions are made.

### 7. Submission
The predicted values are stored in a CSV file with a single column named **`target`**. This file is then ready to be submitted for evaluation.