## Solution Approach

### 1. Data Loading
The training dataset is loaded using **Pandas**. The three input features (`Team1_score`, `Team2_score`, and `Evaluation_score`) are separated from the target labels.

### 2. Feature Scaling
Before training the model, all numerical features are standardized using **StandardScaler**. This transforms each feature to have a mean of 0 and a standard deviation of 1, allowing the optimization process of Logistic Regression to converge more efficiently.

### 3. Model Selection
We dont know for the moment that data is linear or not so we make a hypothesis that data is linearly seperable and if the linear model worked with high metric than our hypothesis is correct

### 4. Building the Pipeline
A **Pipeline** is created to combine feature scaling and model training into a single workflow. This ensures that the exact same preprocessing steps are automatically applied to both the training and test data.

### 5. Model Training
A **Logistic Regression** classifier is trained using the preprocessed training data. The model learns a linear decision boundary that separates matches won by Team 1 from those won by Team 2 However if we tune the parameter of class_weight = 'balanced' in model the performance drop which suggests that actuall decision boundry dont have many overlap in labels and the data is 100% seprated by linear line without many overlaps.

### 5. Generating Predictions
The trained pipeline is used to predict the winners of the unseen matches in the test dataset. Since preprocessing is part of the pipeline, the test features are automatically standardized before prediction.

### 6. Submission
The predicted labels are stored in a CSV file with a single column named **`target`**. This file is then ready to be submitted for evaluation.