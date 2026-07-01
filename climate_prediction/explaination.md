# Solution Approach

## Overview

This solution treats the problem as a **supervised regression task**. Instead of predicting the target directly from the current day's features, it first creates **time-series features** that capture historical trends and seasonal patterns.

The final model is a **Gradient Boosting Regressor** trained on these engineered features.

---

## Feature Engineering

### 1. Lag Features

Past values often contain valuable information about future observations.

For each feature, lag features are created for multiple window sizes:

- 1 day
- 2 days
- 3 days
- 4 days
- 5 days
- 6 days
- 7 days
- 14 days

Example:

- `humidity_7_lag`
- `wind_speed_3_lag`

These features provide the model with historical context.

---

### 2. Rolling Statistics

For every window (except 1 cause it will be same as lag 1), the following statistics are computed:

- Rolling Mean
- Rolling Standard Deviation

These summarize recent trends and variability.

Example:

- `humidity_7_mean`
- `humidity_7_std`

---

### 3. Calendar Features

The `date` column is converted into useful numerical features:

- Month
- Day
- Day of Week
- Day of Year
- Quarter

These help the model learn recurring temporal patterns.

---

### 4. Cyclic Encoding

Since time is periodic, months and days are encoded using sine and cosine transformations.

Examples:

- `month_sin`
- `month_cos`
- `day_sin`
- `day_cos`

This allows the model to understand that:

- December and January are close together.
- The beginning and end of a year are adjacent.
we use the formual sin(2*pi*day/365) and cos(2*pi*day/365) to make the period of these function equall to year length (and number of months for month_cos and month_sin)
---

## 5. Data Preprocessing and Visualization

Creating lag and rolling features introduces missing values at the beginning of the dataset.

These rows are removed before training.
we create heatmap for features first to see which are important for our data and use method='spearman' so we can see non linear relations as well.
after inspection we dont remove any feature as all are important

---

## 6. Model

The model used is:

- **Gradient Boosting Regressor**

Input features are standardized using **StandardScaler** before training.
We use this as its a common expert practice to first try a very strong model capable of overfitting and than reducing its complexity to reduce varience this decrese compute and helps in finding the best model 

---

## 7. Test-Time Feature Generation

The test set does not contain historical values required for lag and rolling features.

To solve this, the last **14** rows of the training data are appended before the test data.

Feature engineering is then applied to the combined dataset, after which the initial training rows are discarded.

This ensures that every test sample has sufficient historical context consistent with that of training data.

---

## 8. Output

The model predicts the target value for every test sample.

Predictions are saved in:

`submission.csv`

with a single column:

| target |
|--------:|
| ... |
| ... |
| ... |