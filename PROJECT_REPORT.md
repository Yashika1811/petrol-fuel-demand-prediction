# Project Report — Smart Fuel Demand Prediction System

## 1. Title
Smart Fuel Demand Prediction System Using Machine Learning

## 2. Introduction
Fuel stations need to maintain enough stock to meet customer demand. Too little stock can create shortages, while too much stock can increase storage and planning problems. This project uses machine learning to predict daily petrol and diesel demand from historical sales, calendar and weather-related features.

## 3. Problem Statement
To develop a machine learning system that estimates the expected quantity of petrol and diesel sold on a future day.

## 4. Objectives
1. Collect and prepare daily fuel-sales data.
2. Analyze factors that affect demand.
3. Create useful time-based and lag features.
4. Train multiple regression models.
5. Compare models using MAE and R².
6. Build a simple prediction dashboard.
7. Make the project reproducible and publishable on GitHub.

## 5. Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Git and GitHub

## 6. Machine Learning
The project compares Linear Regression, Random Forest and Gradient Boosting. A time-based train/test split is used so that future records are not used to train a model that predicts the past.

## 7. Evaluation
MAE (Mean Absolute Error) measures average prediction error in litres. R² indicates how well the model explains variation in the target.

## 8. Limitations
The starter dataset is synthetic. Real-world performance will depend on the quality and quantity of actual station data, weather data and local demand patterns.

## 9. Future Scope
- Live weather API
- Multiple fuel stations
- 7-day demand forecasting
- Inventory optimization
- Online deployment
- Automated daily data updates

## 10. Conclusion
The project demonstrates how machine learning can support fuel-demand planning. It is designed as a student project and can be extended into a real operational decision-support system.
