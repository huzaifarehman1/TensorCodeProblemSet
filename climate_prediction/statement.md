# Forecasting Tomorrow

## Problem Statement

Weather changes over time, making it a classic example of **time series data**. Unlike ordinary datasets where samples are independent, time series observations are recorded in **chronological order**, and past values often influence future ones.

In this challenge, you are given historical daily weather measurements, including:

- Date
- Humidity
- Wind Speed
- Mean Pressure
- Mean Temperature

Your goal is to build a **time series forecasting model** that learns the temporal patterns in the data and predicts the **target** for unseen dates which represent mean temperature.

Unlike standard regression tasks, you should preserve the chronological nature of the data. Future information must **not** be used to predict the past.

---

## Input

The training dataset contains the following columns:

- `date` – Date of observation
- `humidity` – Average daily humidity
- `wind_speed` – Average daily wind speed
- `meanpressure` – Average daily atmospheric pressure
- `target` – Average daily temperature 

The test dataset contains:

- `date`
- `humidity`
- `wind_speed`
- `meanpressure`

---

## Task

Train a forecasting model using the historical weather data to predict the corresponding **`target`** values for every sample in the test dataset here target represent Daily Average Temperature.

---

## Output

For each sample in the test dataset, predict the corresponding **`target`**.

---

## Evaluation

Your predictions will be evaluated using:

- **R² score**


---

## Example

| date | meantemp | humidity | wind_speed | target |
|------|---------:|---------:|-----------:|-------:|
| 2013-01-01 | 10.0 | 84.5 | 0.00 | 1015.67        |
| 2013-01-02 | 7.4 | 92.0 | 2.98 | 1017.80         |
| 2013-01-03 | 7.17 | 87.0 | 4.63 | 1018.67        |
| 2013-01-04 | 8.67 | 71.33 | 1.23 | 1017.17       |
| 2013-01-05 | 6.0 | 86.83 | 3.70 | 1016.50        |

---

## Note

- The data is ordered chronologically.
- Avoid using future observations to predict earlier dates, as this would introduce **data leakage**.


---

## Submission

After generating predictions for the test dataset:

1. Create a CSV file containing **all predicted values**.
2. Name the prediction column **`target`**.
3. Ensure the CSV contains exactly one row per test sample, in the same order as the test dataset.

Example:

| target |
|------: |
| 12.34  |
| 13.08  |
| 11.91  |

Save the file as `submission.csv` and upload it for evaluation.