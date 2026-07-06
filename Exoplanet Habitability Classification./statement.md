# Exoplanet Habitability Classification

## Problem Description
An orbital space telescope has been scanning distant star systems, recording atmospheric and thermal telemetry from various exoplanets. Your task is to build a machine learning model capable of classifying whether a newly discovered exoplanet is mathematically habitable (`1`) or inhospitable (`0`).

Unlike simple linear trajectory systems, planetary habitability depends on a delicate, non-linear balance of multiple factors. 

## Dataset Structure
You are provided with two data subsets:
- `train.csv`: Contains the historical telemetry features and the true habitability classification.
- `test.csv`: Contains only the independent features for the evaluation phase.

### Feature Attributes
- **Temp_K**: Surface temperature in Kelvin.
- **Methane_ppm**: Atmospheric methane concentration in parts per million.
- **CO2_ppm**: Atmospheric carbon dioxide concentration in parts per million.
- **Stellar_Flux**: Radiation received from the host star (Earth = 1.0).
- **target**: Binary classification integer (`1` for Habitable, `0` for Inhospitable).

## Submission Rules
- Output your finalized evaluations inside a single CSV file named exactly `submission.csv`.
- The column header must be exactly named `target`.
- Maintain row orders to match the sample distribution order structured across `test.csv`.
- Your model will be evaluated using the **F1-Score** metric to account for any class imbalances.
