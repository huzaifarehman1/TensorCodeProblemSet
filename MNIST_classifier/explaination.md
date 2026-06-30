# Solution Approach

## 1. Loading the Dataset

The training and test datasets are loaded separately and create Dataset object for easy loading.
---

## 2. Device Agnostic Code

Before creating the model, the available hardware is detected.

If a CUDA-compatible GPU is available, the model is trained on the GPU; otherwise, it falls back to the CPU automatically.

This allows the exact same code to run efficiently on both personal computers and machines equipped with NVIDIA GPUs without any modifications.

---

## 3. Checking the Class Distribution

Before training, the number of samples belonging to each digit is displayed.

This helps determine whether the dataset is balanced. If one or more digits appeared significantly less often than the others, techniques such as weighted loss functions or oversampling might be required.

on checking the data we find that it is nearly balanced, no special handling for class imbalance is necessary.

---

## 4. Creating a Custom Dataset

A custom PyTorch `Dataset` is created to serve the data efficiently during training.

The pixel values are also divided by **255**, changing their range from **0–255** to **0–1**.

Normalizing the input prevents very large feature values from making optimization unstable and generally allows neural networks to converge faster.

---

## 5. Train-Validation Split

Instead of training on the entire dataset, 20% of the images are kept aside for validation.

The validation set is never used to update the model's weights. Instead, it provides an unbiased estimate of how well the model performs on unseen handwritten digits after every epoch preventing Overfitting.

---


## 6. Choosing a Dense Neural Network

Each MNIST image originally has a size of **28 × 28** pixels. However, in this dataset every image has already been flattened into a single vector containing **784 values**.

Since the images are already represented as feature vectors and the task is relatively straightforward, there is no need to reshape the data back into images and use convolutional layers.

A fully connected (Dense) neural network is therefore sufficient to learn the mapping between the pixel values and the corresponding digit.

---

## 7. Multiple Hidden Layers

The network gradually reduces the feature dimension:

```
784 → 512 → 256 → 128 → 10
```

The larger hidden layers learn many useful combinations of pixels, while the smaller layers compress these learned features into increasingly informative representations before making the final prediction.

This gradual reduction generally learns better representations than directly mapping 784 inputs to 10 outputs.

---

## 8. Using GELU Activation

After every hidden layer, a **GELU** activation function is applied.

GELU introduces non-linearity, allowing the network to learn much more complex relationships between pixels.
GELU dont have the exploding gradient or vanishing gradient problem like Tanh or Sigmoid and it also dont have Dying RELU problem so its better in optimization and training stability.

---

## 9. Cross Entropy Loss

The task is to classify each image into one of **10 possible digits** so we use Classic Classification loss called Cross Entropy Loss.

Since Cross Entropy internally applies Softmax, an additional Softmax layer is unnecessary.

---

## 11. Adam Optimizer

The model is trained using the Adam optimizer.

Adam allowing the network to converge much faster than standard gradient descent with very little manual tuning.

---

## 12. Validation After Every Epoch

After each epoch, the model is evaluated on the validation set.

Monitoring validation accuracy helps verify that the network is learning useful patterns instead of simply memorizing the training data.

Validation loss is also reported because it often reveals overfitting before the accuracy begins to decrease.

---

## 13. Making Predictions

Once training is complete, every test image is passed through the trained network.

The output layer produces ten scores—one for each possible digit returning a tensor of shape (batch,10) here 10 is for probability of each class.

The digit corresponding to the largest score is selected as the final prediction using `argmax` at dim = 1 giving us tensor of shape (batch,1).

---

## 14. Creating the Submission File

Finally, all predicted digits are stored in a CSV file containing a single column named **`target`**.

The rows are kept in the same order as the test dataset so that each prediction corresponds to the correct image.

The resulting `submission.csv` file is then ready for evaluation.