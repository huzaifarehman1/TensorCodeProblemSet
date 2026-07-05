# Shot Classifer

## THIS PROBLEM IS TAKEN FROM `CHINA OLYMPIAD OF AI 2024`

## Problem Statement

A research team  is studying how spatial coordinates influence a Top player shot.

They have collected a dataset of points in a 2D plane. Each point represents a location:

- `x_loc` — X-coordinate of the point
- `y_loc` — Y-coordinate of the point

if the ball go in target than it is labeled as `1` else it is labeled as `0`, each point has been assigned a binary label.
.

Your task is to make a model to classify new points and assign either a 0 if shot misses target and 1 if shot hits target.

---

## Task

Given a point’s coordinates `(x_loc, y_loc)`, predict whether it belongs to class **0 or 1**.

.

---

## Input

A CSV file containing:

- `x_loc` — X-coordinate of the point
- `y_loc` — Y-coordinate of the point
- `target`— 0 if shot misses target and 1 if shot hits target.

---

## Output

For each row in the test dataset, predict the corresponding **target**:

- `0` → shot missed
- `1` → target hit

---

## Restrictions

the following restrictions apply:

- Only **Dense Layer Neural Networks** are allowed 
- No other type of model is allowed
- Deep learning architectures with more than 2 hidden layers are **not allowed** the maximum hidden layers allowed are 2.
- your input layer must take `2` inputs and no hidden layer can have more than `8` neurons and output layer must have `1` neuron this mean the smallest possible architecture is `[2,1,1,1]` and largest possible architecture is `[2,8,8,1]`  
- External datasets are **not allowed**.
- Pretrained models are **not allowed**.
- the maximum number of weight updates allowed for your model  are `100`
- you can not use other layers than Dense layer (Fully connected layer)
- you can freely choose all other components (loss functions,activation function,optimizer,learning rates etc)

- Feature engineering is fully allowed

---

## Evaluation

Your predictions will be evaluated using:

- **Precision**

Higher score indicates better alignment with the hidden decision boundary.

---

## Example

| x_loc | y_loc | target |
|-------|-------|--------|
| 1.2   | 3.4   | 0      |
| -2.1  | 4.5   | 1      |
| 0.0   | -1.8  | 0      |



---

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing predictions for all rows.
2. Name the column exactly: `target`
3. Ensure predictions are in the same order as the test set.
4. Save the file as `submission.csv`.