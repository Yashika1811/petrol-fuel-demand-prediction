import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
petrol_model = joblib.load(ROOT / "models" / "petrol_demand_model.pkl")
diesel_model = joblib.load(ROOT / "models" / "diesel_demand_model.pkl")
df = pd.read_csv(ROOT / "data" / "fuel_sales.csv", parse_dates=["date"])

st.set_page_config(page_title="Smart Fuel Demand Prediction", page_icon="⛽", layout="wide")
st.title("⛽ Smart Fuel Demand Prediction System")
st.caption("B.Tech CSE (AI/ML) project — demonstration dashboard")

st.sidebar.header("Prediction Inputs")
date = st.sidebar.date_input("Prediction date")
temperature = st.sidebar.number_input("Temperature (°C)", 0.0, 50.0, 28.0)
rainfall = st.sidebar.number_input("Rainfall (mm)", 0.0, 300.0, 2.0)
holiday = st.sidebar.selectbox("Holiday?", ["No", "Yes"])
is_holiday = 1 if holiday == "Yes" else 0

date_ts = pd.Timestamp(date)
day_of_week = date_ts.dayofweek
month = date_ts.month
is_weekend = int(day_of_week >= 5)

# Use the latest available history as a simple demo input for lag features.
latest = df.iloc[-1]
petrol_lag_1 = float(latest["petrol_sales_litres"])
petrol_lag_7 = float(df.iloc[-7]["petrol_sales_litres"])
petrol_roll_7 = float(df["petrol_sales_litres"].tail(7).mean())

diesel_lag_1 = float(latest["diesel_sales_litres"])
diesel_lag_7 = float(df.iloc[-7]["diesel_sales_litres"])
diesel_roll_7 = float(df["diesel_sales_litres"].tail(7).mean())

petrol_input = pd.DataFrame([{
    "day_of_week": day_of_week, "month": month, "is_weekend": is_weekend,
    "is_holiday": is_holiday, "temperature_c": temperature, "rainfall_mm": rainfall,
    "petrol_lag_1": petrol_lag_1, "petrol_lag_7": petrol_lag_7,
    "petrol_rolling_7": petrol_roll_7
}])

diesel_input = pd.DataFrame([{
    "day_of_week": day_of_week, "month": month, "is_weekend": is_weekend,
    "is_holiday": is_holiday, "temperature_c": temperature, "rainfall_mm": rainfall,
    "diesel_lag_1": diesel_lag_1, "diesel_lag_7": diesel_lag_7,
    "diesel_rolling_7": diesel_roll_7
}])

petrol_pred = max(0, float(petrol_model.predict(petrol_input)[0]))
diesel_pred = max(0, float(diesel_model.predict(diesel_input)[0]))

def level(value, low=2800, high=4300):
    if value < low:
        return "LOW"
    if value < high:
        return "MEDIUM"
    return "HIGH"

c1, c2 = st.columns(2)
with c1:
    st.metric("Predicted Petrol Demand", f"{petrol_pred:,.0f} L")
    st.write("Demand level:", level(petrol_pred))
with c2:
    st.metric("Predicted Diesel Demand", f"{diesel_pred:,.0f} L")
    st.write("Demand level:", level(diesel_pred))

st.subheader("Suggested Stock Buffer")
st.write(f"Petrol suggested planning quantity: **{petrol_pred*1.10:,.0f} L** (10% buffer)")
st.write(f"Diesel suggested planning quantity: **{diesel_pred*1.10:,.0f} L** (10% buffer)")

st.subheader("Historical Sales")
chart = df.set_index("date")[["petrol_sales_litres","diesel_sales_litres"]].tail(90)
st.line_chart(chart)

st.info("Demo note: lag values come from the included historical dataset. For a live station system, connect these features to the latest daily sales records.")
