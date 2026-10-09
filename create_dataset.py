import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

data = pd.DataFrame({
    "Date": dates
})

data["Day"] = data["Date"].dt.day
data["Month"] = data["Date"].dt.month
data["DayOfWeek"] = data["Date"].dt.dayofweek
data["Weekend"] = (data["DayOfWeek"] >= 5).astype(int)

data["Holiday"] = np.random.choice(
    [0, 1],
    size=len(data),
    p=[0.9, 0.1]
)

data["Temperature"] = np.random.normal(
    loc=27,
    scale=6,
    size=len(data)
).round(1)

data["Previous_Day_Sales"] = np.random.normal(
    loc=4500,
    scale=700,
    size=len(data)
).round(0)

data["Price_Per_Litre"] = np.random.uniform(
    94,
    105,
    size=len(data)
).round(2)

data["Petrol_Demand"] = (
    2500
    + data["Previous_Day_Sales"] * 0.55
    + data["Weekend"] * 300
    + data["Holiday"] * 500
    - data["Price_Per_Litre"] * 20
    + data["Temperature"] * 15
    + np.random.normal(0, 250, len(data))
).round(0)

data.to_csv("data/fuel_demand.csv", index=False)

print("Dataset created successfully!")
print(data.head())
print("\nDataset shape:", data.shape)