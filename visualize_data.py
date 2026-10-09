
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data/fuel_demand.csv")

# Convert Date column into date format
data["Date"] = pd.to_datetime(data["Date"])

# Graph 1: Petrol demand over time
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Petrol_Demand"])
plt.title("Petrol Demand Over Time")
plt.xlabel("Date")
plt.ylabel("Petrol Demand (Litres)")
plt.tight_layout()
plt.savefig("petrol_demand_over_time.png")
plt.show()

# Graph 2: Average demand by month
monthly_demand = data.groupby("Month")["Petrol_Demand"].mean()

plt.figure(figsize=(8, 5))
monthly_demand.plot(kind="bar")
plt.title("Average Petrol Demand by Month")
plt.xlabel("Month")
plt.ylabel("Average Demand (Litres)")
plt.tight_layout()
plt.savefig("monthly_petrol_demand.png")
plt.show()

print("Graphs created successfully!")
