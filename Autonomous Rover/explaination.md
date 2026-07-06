# Problem Analysis & Mathematical Insight

## Physics Overview
The stopping behavior of moving objects is closely bound to standard kinetic equations. Total braking distance typically correlates quadratically with velocity ($d \propto v^2$) because the kinetic energy dissipation work required scales directly with the square of the speed ($E_k = \frac{1}{2}mv^2$). 

The baseline kinematics generating this telemetry can be represented using:
$$d = \alpha v^2 + \beta v + \epsilon$$

Where:
- $v$ represents `Speed_ms`
- $\alpha$ captures the kinetic kinetic friction constant
- $\beta$ covers structural reaction delays 
- $\epsilon$ introduces physical sensor variance ($\mathcal{N}(0, \sigma^2)$)

## Recommended Approaches
1. **Polynomial Feature Transformation:** Since standard linear lines cannot properly accommodate the parabolic arc curves caused by kinetic acceleration bounds, mapping the inputs via a second-degree polynomial (`PolynomialFeatures(degree=2)`) before wrapping it in a Linear Regression pipeline will provide an exceptional structural match.
2. **Evaluation Metric:** Performance is scored on Root Mean Squared Error (RMSE) to directly measure the average distance error in meters.
