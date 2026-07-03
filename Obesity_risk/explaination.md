# Solution Explanation

## Overview

The objective of this challenge is to predict an individual's **obesity score** using only their **height** and **weight**. Since only linear models are allowed, choosing the right features becomes most important.

---

## Step 1: Explore the Data

Before training a model, we first inspect how each feature relates to the target.

A simple way to do this is by visualizing the correlation matrix.

```python
sns.heatmap(train.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Before Feature Engineering")
plt.show()
```

From the heatmap, we observe that neither **height** nor **weight** has a little relation indivisually with the target.

This suggests that the relationship between the features and the target is not refined much for our linear model to exploit it. 

---

## Step 2: Apply Domain Knowledge

The dataset contains measurements of a person's height and weight.

A well-known medical metric that combines these measurements is **Body Mass Index (BMI)**.

The BMI formula is:

```
BMI = weight / (height in meters)²
```

Since height is stored in **centimeters**, it must first be converted to **meters**.

```python
height_m = train["height"] / 100
train["bmi"] = train["weight"] / (height_m ** 2)
```

This creates a new feature that better represents a person's body composition.

---

## Step 3: Verify the New Feature

After creating the BMI feature, we inspect the correlation matrix again.

```python
sns.heatmap(train.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation After Feature Engineering")
plt.show()
```

The new heatmap shows that **BMI has a perfect correlation with the target** individually.

This confirms that BMI is a much more informative feature for predicting the obesity score.

---

## Step 4: Train the Model

With the engineered BMI feature added, we train a **Linear Regression** model.

Although the model itself is simple, the improved feature representation allows it to capture the relationship between the inputs and the target much more effectively.

The same BMI feature is also created for the test dataset before generating predictions.

---

## Key Takeaway

This problem demonstrates an important principle in machine learning:

> **Better features often lead to bigger improvements than more complex models.**

Instead of searching for a more powerful algorithm, we used **domain knowledge** to engineer a meaningful feature. By transforming the original measurements into **BMI**, a simple linear model is able to achieve much better performance while satisfying all of the problem's restrictions.