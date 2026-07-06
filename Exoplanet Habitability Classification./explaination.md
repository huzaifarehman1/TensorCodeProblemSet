# Problem Analysis & Mathematical Insight

## Algorithmic Shift: Classification
While regression maps inputs to continuous outputs, classification forces the model to draw a *decision boundary* separating distinct classes. Habitability is a complex "Goldilocks Zone" problem. For example, a planet is only habitable if the temperature is *just right* AND the stellar flux is moderate. 

Because these features depend on one another (e.g., high CO2 might offset low stellar flux due to the greenhouse effect), a simple linear model like Logistic Regression might struggle to capture the nuances.

## Recommended Approaches
1. **Tree-Based Models:** Algorithms like Random Forests or Gradient Boosting Classifiers (XGBoost/LightGBM) excel here. They inherently handle non-linear boundaries by creating multi-layered logical splits (e.g., *If Temp > 250 AND Stellar_Flux < 1.5*).
2. **Feature Scaling:** If experimenting with distance-based algorithms like Support Vector Machines (SVM) or Neural Networks, competitors must normalize the data first (using `StandardScaler`), as `CO2_ppm` values are much larger than `Stellar_Flux` values and could skew the model.
3. **Evaluation Metric (F1-Score):** F1-Score is the harmonic mean of Precision and Recall. It penalizes models that just guess '0' for everything, ensuring the algorithm actually learns the underlying planetary physics.
