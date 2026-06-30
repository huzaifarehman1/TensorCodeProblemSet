# Headline Detective

## Problem Statement

Every day, thousands of news articles are published covering a wide range of topics. To help readers quickly organize information, news platforms automatically assign each article to its appropriate category.

You are given a collection of news headlines along with their corresponding categories. Your mission is to become a **Headline Detective** by learning the patterns in the text and correctly classifying unseen headlines.

---

## Input

The training dataset contains two columns:

- `Text`
- `target`

where `target` is the category of the news headline having 5 possible values from 0 to 4.


The test dataset contains only:

- `Text`

---

## Task

Train a text classification model that learns from the training data and predicts the correct **target** for every headline in the test dataset.

---

## Output

For each news headline in the test dataset, predict its corresponding **target**.
where target ∈ {0 , 1 , 2 , 3 , 4}
---

## Evaluation

Your predictions will be evaluated using:

- **Accuracy**

---

## Example

| Text | Label |
|------|-------|
| Apple unveils its latest smartphone lineup. | 0 |
| Local team wins the national championship. | 1 |
| Government announces new tax reforms. | 2 |
| Scientists discover a promising cancer treatment. | 3 |
| Stock markets close at a record high. | 4 |

---

## Note

- Each headline belongs to **exactly one** category.
- The text has been collected from real-world news sources.

---

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing **all predicted labels**.
2. Name the prediction column **`target`**.
3. Ensure the CSV contains exactly one row per test sample, in the same order as the test data.

Example:

| Label |
|-------|
| 0 |
| 1 |
| 2 |

Save the file as `submission.csv` and upload it for evaluation.