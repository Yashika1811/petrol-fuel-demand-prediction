
import pandas as pd
import joblib

# Load the saved ML model
model = joblib.load("models/fuel_demand_model.pkl")

print("PETROL DEMAND PREDICTION")
print("-----------------------")

# Take input from the user
day = int(input("Enter day of month (1-31): "))
month = int(input("Enter month (1-12): "))
day_of_week = int(input("Enter day of week (0=Monday, 6=Sunday): "))

weekend = int(input("Is it a weekend? (0=No, 1=Yes): "))
holiday = int(input("Is it a holiday? (0=No, 1=Yes): "))

temperature = float(input("Enter temperature in Celsius: "))
previous_sales = float(input("Enter previous day's petrol sales in litres: "))
price = float(input("Enter petrol price per litre: "))

# Arrange inputs in the same order used during training
features = pd.DataFrame([{
    "Day": day,
    "Month": month,
    "DayOfWeek": day_of_week,
    "Weekend": weekend,
    "Holiday": holiday,
    "Temperature": temperature,
    "Previous_Day_Sales": previous_sales,
    "Price_Per_Litre": price
}])

# Predict demand
prediction = model.predict(features)[0]

print("\nPredicted petrol demand:", round(prediction, 2), "litres")
