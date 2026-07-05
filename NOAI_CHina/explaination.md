# Shot Classifier — Solution Explanation

## Overview

This problem involves classifying 2D spatial points `(x_loc, y_loc)` into:

- `1` → shot hits target  
- `0` → shot misses target  


---

## Approach

A constrained **dense neural network (fully connected only)** is used as required by the competition rules.

Since raw coordinates have a full circle decision boundry under scatter plot,feature engineering is applied inside the model to improve learnability by making geometric features to exploit the decision boudry in a better way.

---

## Feature Engineering

From each input point `(x, y)`, the model computes:

- Radial distance:
\[
r^2 = x^2 + y^2
\]

- Angular component:
\[
\theta = \tan^{-1}(y/x)
\]

Both features are normalized (mean 0, variance 1) and concatenated:


These transformed features provide a geometry-aware representation of the shot space.
These comes from Domain knowledge

---

## Model Architecture

A shallow MLP is used under strict constraints:

This satisfies:
- Maximum 2 hidden layers
- Maximum 8 neurons per layer
- Fully connected layers only
 
We use the model with Architecture `[2,8,8,1]` as the more the neurons the more powerful out model becomes andd under such tight contrained every single neuron is valuable to create correct decision boundry so we use maximum neuron possible.

we use `Tanh` activation in between hidden layers as for two main reasons
- `Tanh` is `0 centered function` so our contrained model can easily learn the boundry, Deep learning models learn better when each layer get 0 centered inputs and under tight constrains this becomes very valuable
- It dont have `dying RelU` problem like RELU,GELU,Leaky Relu since `Dying Relu` can cause lost of neurons in our model which reduce the capability of our models very much.

At end we use Sigmoid to get probability `[0-1]` for our binary label


---

## Training Setup

- Loss function: Binary Cross Entropy (BCELoss)
- Optimizer: Adam
- Learning rate: 0.001
- Epochs: 100 since 
- Batch size: full dataset

in this way we use full batch for best possible gradients and update per epoc under contrain that update steps should be no more than `100` in total 


---

## Prediction Strategy

For each test sample:

1. Forward pass through the network
2. Output probability in range [0, 1]
3. Apply threshold:
   - ≥ 0.5 → class `1`
   - < 0.5 → class `0`

---

## Submission Format

- File name: `submission.csv`
- Column: `target`
- Values: binary predictions (0 or 1)
- Order must match test set exactly
