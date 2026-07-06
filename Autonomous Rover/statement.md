# Autonomous Rover: Stopping Distance Prediction

## Problem Description
An autonomous navigation system requires a highly accurate model to determine the exact stopping distance needed when the brakes are applied on a rover tracking simulation. Given the telemetry logs across multiple controlled trials, your task is to design a regression algorithm that maps the initialization speeds to the final stopping distances.

## Dataset Structure
You are provided with two data subsets:
- `train.csv`: Data contains both historical initial velocity entries and the true recorded target distances.
- `X_test.csv`: Independent velocity attributes for evaluation.

### Feature Attributes
- **Speed_ms**: Continuous floating value tracking the initialization speed profile of the rover in meters per second ($m/s$).
- **target**: Continuous floating value representing the true metric baseline halting displacement in meters ($m$).

## Submission Rules
- Output your finalized evaluations inside a single CSV file named exactly `submission.csv`.
- The column header must be exactly named `target`.
- Maintain row orders to match the sample distribution order structured across `X_test.csv`.
