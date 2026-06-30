# MNIST_Classifier

## Problem Statement

Handwritten digit recognition is a fundamental problem in computer vision and machine learning. In this task, you are given images of handwritten digits (0–9), and your goal is to correctly classify each image into its corresponding digit.

Each image has been flattened into a vector of pixel values, where each feature represents the grayscale intensity of a pixel.

---

## Input

Each sample contains **784 features**, representing a flattened 28 × 28 grayscale image:

- `pixel1, pixel2, ..., pixel784`

Each value ranges from 0 to 255 and represents pixel intensity.

---

## Output

The target is a multi-class label in the `target` column:

- `0` → digit zero  
- `1` → digit one  
- `2` → digit two  
- ...  
- `9` → digit nine  

---

## Task

Train a classification model that learns to map pixel intensities to their correct digit labels. Your model should generalize well to unseen handwritten digit images.

---

## Dataset

You are provided with:

### Training Set
- Contains 784 pixel features
- Includes a `target` column (digit class)

### Test Set
- Contains 784 pixel features 
For each input sample in test data, predict the corresponding **target**


---

## Evaluation

Your predictions will be evaluated using:

- **Accuracy Score**

---

## Output Format

For each test sample, predict the digit label.

Submit a CSV file containing a single column:

| target |
|------:|
| 7 |
| 2 |
| 1 |
| ... |

Save the file as:

```
submission.csv
```

---

## Notes

- Each pixel represents grayscale intensity (0–255).