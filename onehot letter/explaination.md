# Solution Explanation

## Overview

The goal of this problem is to recover the original letter from a neural network output vector.

The neural network receives a one-hot encoded letter vector of size 26 and transforms it into a 50-dimensional output vector.

The model architecture is:

```
Input (26)
    |
    v
Linear Layer (26 → 128)
    |
   ReLU
    |
    v
Linear Layer (128 → 50)
    |
    v
Output Vector (50)
```

The model is deterministic because it is initialized with a fixed random seed:

```python
torch.manual_seed(35)
```

Therefore, we can recreate the exact same model and calculate the expected output for every possible letter.

The main idea is to create a fingerprint for each letter and compare unknown output vectors with these fingerprints.

---

## Step 1: Recreate the Neural Network

The model is rebuilt with the same architecture:

Using the same random seed guarantees that the weights are identical.

---

## Step 2: Generate Letter Fingerprints

There are only 26 possible letters so the `Search Space` is small.

For every letter:

1. Create a one-hot vector of length 26.
2. Set the corresponding position to `1`.
3. Pass it through the neural network.
4. Store the generated 50-dimensional output.

Example:

```
A → [1,0,0,0,...,0] → Neural Network → Output Vector

B → [0,1,0,0,...,0] → Neural Network → Output Vector
```

After generating all letters:

```
Fingerprint[0]  → A
Fingerprint[1]  → B
Fingerprint[2]  → C
...
Fingerprint[25] → Z
```

These fingerprints represent the exact network outputs for every possible input.

---

## Step 3: Load Test Data

The test dataset contains only the neural network output vectors.

---

## Step 4: Compare Vectors

For every test sample, the output vector is compared against all 26 fingerprints.

Cosine similarity is used as the comparison metric.

Cosine similarity measures how similar two vectors are:

- Value close to `1` means very similar.
- Lower values mean less similarity.

The process:

```
Unknown Output Vector

        |
        |
Compare with A fingerprint
Compare with B fingerprint
Compare with C fingerprint
...
Compare with Z fingerprint

        |
        v

Select highest similarity
```

The fingerprint with the highest similarity gives the original letter.

---


## Step 5: Create Submission

All predictions are stored in a dataframe:

```python
submission = pd.DataFrame({
    "target": predictions
})
```

The final file is:

```
submission.csv
```

with the format:

| target |
|--------|
| 3 |
| 1 |
| 26 |

---