# Solution Approach

## Overview

This solution uses a **Convolutional Neural Network (CNN)** implemented in PyTorch to classify CIFAR-100 images into their corresponding **20 coarse classes**. Since the dataset is provided as flattened pixel values in CSV format, the first step is to reconstruct each image before feeding it into the network.

---

## Data Preprocessing

The dataset is loaded from CSV files using a custom `Dataset` class.

- Training data contains both pixel values and the `target` column.
- Test data contains only pixel values.
- Pixel intensities are normalized from **[0, 255]** to **[0, 1]** for more stable training.
- Each image is reshaped from a vector of **3072 values** into a **3 × 32 × 32 RGB image**.

The training dataset is further divided into:
- **90% Training Set**
- **10% Validation Set**

using `random_split`.

---

## Model Architecture

The model follows a standard CNN design for image classification.

### Feature Extraction

Several convolutional layers are used to learn increasingly complex image features.

Each convolution block consists of:

- Convolution (`Conv2D`)
- Batch Normalization
- GELU Activation

The convolution layers progressively increase the number of feature maps:

```
3 → 64 → 128 → 256 → 512
```
we use batch Normalization to stabalize training and reduce distribution shift in between layers and use gelu as a modren activation function it dont have gradient vanishing or gradient exploding or dying relu problem
### Downsampling

`MaxPool2D` layers reduce the spatial dimensions of the feature maps meaning it reduce height and width of each feature map, allowing the network to capture larger receptive fields while reducing computational cost .

### Global Feature Aggregation

Instead of flattening a large feature map directly, the model applies:

```
AdaptiveAvgPool2D(1×1)
```

This converts every feature map into a single representative value regardless of its spatial size, reducing the number of trainable parameters and improving generalization.

### Classification Head

The pooled features are passed through fully connected layers:

```
512
↓
256
↓
20 output classes
```

The final layer produces logits for the 20 coarse CIFAR-100 categories.

---

## Training

The model is trained using:

- **Loss Function:** Cross Entropy Loss
- **Optimizer:** AdamW


For each epoch:

1. Forward pass
2. Compute classification loss
3. Backpropagation
4. Update model parameters

Training loss is recorded after every epoch.

---

## Validation

After each training epoch, the model is evaluated on the validation set.

Prediction is obtained by selecting the class with the highest output score using:

```
argmax(logits)
```

Validation accuracy is computed as:

```
Correct Predictions / Total Samples
```

This provides an estimate of how well the model generalizes to unseen data.

---

## Test Prediction

Once training is complete:

- The model is switched to evaluation mode.
- Predictions are generated for every test image.
- The predicted class index is stored in a single column named:

```
target
```

Finally, the predictions are saved as:

```
submission.csv
```

which is ready for evaluation or competition submission.

---

## Why This Architecture?

This architecture was chosen because it provides a good balance between simplicity and performance.

- Convolution layers learn local visual patterns and also introduce inductive bias.
- Batch Normalization stabilizes and accelerates training and reduce dietribution shift in between layers.
- GELU offers smoother nonlinear activation than ReLU and better gradient flow than Tanh and Sigmoid.
- Max Pooling reduces computation while preserving important features.
- Adaptive Average Pooling removes the need for manually computing flatten dimensions and reduces parameters.
- AdamW provides efficient optimization with improved regularization through decoupled weight decay.

Overall, the model is lightweight, easy to train, and well suited for CIFAR-100 image classification.