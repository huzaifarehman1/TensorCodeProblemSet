# Solution Explanation

## Problem Understanding

The target is not generated directly from the input features. Instead, it is created by applying an exponential transformation to a hidden linear relationship.

The hidden process follows:


y = e^{f(x)}



Additionally, the original input feature is hidden among several distorted copies and unrelated features. The objective is to identify the correct feature, recover the hidden linear relationship, and predict the target values for unseen samples.

---

# Mathematical Insight

The exponential function is invertible.

Applying the natural logarithm to both sides gives:

ln(y) = ln(e^f(x)) = f(x)

After this transformation, the problem becomes a simple.

---

# Transforming the Target

The first step is to transform the target values using the natural logarithm.

```python
train["target"] = np.log(train["target"])
```

---

# Feature Analysis

The dataset contains multiple features, but only one represents the original hidden input.

To identify it, we visualize the relationship between every feature and the transformed target.

The correct feature  display a clear linear relationship with the transformed target.

The remaining features either appear noisy or have no obvious linear trend.

After identifying the correct feature visually, it is selected manually and we came to relize that relation is linear meaning `f(x) = wx + b`.

```python
chosen = "feature_x"
```

---

# Linear Regression

Once the correct feature has been identified, a linear regression model is trained.

The model learns:

ln(y)=wx+b


After training, the model predicts the logarithm of the target for the test samples.

---

# Recovering the Original Signal

The model predicts:

ln(y)

To recover the original target values during prediction, we apply the exponential function:

e^ln(y) = y

In code:

```python
prediction = np.exp(prediction)
```

These recovered values become the final predictions.

---
--

# Final Output

The generated submission file contains a single column:

```
target
```

where each value is the predicted signal after applying the inverse transformation to the linear regression output.

The original order of the samples is preserved.