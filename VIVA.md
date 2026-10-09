# Viva Questions — Smart Fuel Demand Prediction

1. What is the aim of the project?
   - To predict daily petrol and diesel demand using machine learning.

2. Why did you use regression?
   - The output is a continuous value such as litres of fuel sold.

3. Why not randomly split the data?
   - Random splitting can allow future information to influence training. A time-based split is more appropriate for forecasting.

4. What is MAE?
   - Mean Absolute Error is the average absolute difference between actual and predicted values.

5. What is R²?
   - It measures how much variation in the target is explained by the model.

6. Why use lag features?
   - Previous sales often contain useful information about future demand.

7. Why compare multiple models?
   - Different models can learn different patterns. Comparing them helps select a better model.

8. What is a synthetic dataset?
   - Data generated for development or demonstration rather than collected from real customers or a real station.

9. What is the biggest limitation?
   - The starter dataset is synthetic, so it cannot prove real-world accuracy.

10. How can the project be improved?
   - Use real anonymized station data, live weather data, multi-day forecasting and inventory optimization.
