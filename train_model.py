import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("data/fuel_demand.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

# Select input features
X = data[
    [
        "Day",
        "Month",
        "DayOfWeek",
        "Weekend",
        "Holiday",
        "Temperature",
        "Previous_Day_Sales",
        "Price_Per_Litre"
    ]
]

# Select target
y = data["Petrol_Demand"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")

# Make predictions
y_pred = model.predict(X_test)

# Calculate performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("-----------------")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))
# Save the trained model
joblib.dump(model, "models/fuel_demand_model.pkl")

print("Model saved successfully!")