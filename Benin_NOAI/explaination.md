# Solution Approach

This solution uses **Logistic Regression**, a simple yet effective algorithm for binary classification.

Instead of immediately choosing a complex model, we first test the hypothesis that the classes can be separated using a linear decision boundary. Logistic Regression is an excellent baseline because it is fast to train, easy to interpret, and often performs surprisingly well on structured tabular data.

## Approach

1. Load the training dataset.
2. Separate the input features and the target labels.
3. Train a **Logistic Regression** model.
4. Load the test dataset.
5. Predict the probability that each sample belongs to the positive class using:

```python
model.predict_proba(test)[:, 1]
```
we use `l1_ratio=1` meaning we use L1 penelty so this will act as feature selector automatically selecting most useful features we use `solver='saga'` which is capable of solving all penelty and in the way is the best solver we increase `max_iter` to cause convergence

6. Save these probabilities in `submission.csv`.


## Why Start with a Simple Model?

One of the most important skills in machine learning competitions is **hypothesis testing**.

Before trying complex ensemble methods or deep learning models, it is good practice to ask:

> *"Can this problem already be solved well with a simple linear model?"*

Many datasets—even those from prestigious competitions and olympiads such as the **Benin National Olympiad of AI (NOAI)**—can achieve competitive performance using straightforward techniques.

Starting with a simple baseline helps you:

- Understand the difficulty of the problem.
- Establish a performance benchmark.
- Decide whether more sophisticated models are actually necessary.
- Save significant development time.

Complex models should be introduced only after a simple baseline indicates there is room for improvement.

## Using Complex Model

After using a DL model we see that it achieve the same score as Logistic Regression meaning this means
`The data is Linearly Seperable`

## Conclusion

This makes Logistic Regression our final Model and proves out hypothesis correct.