import streamlit as st
import pandas as pd
import joblib
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("."))


model = joblib.load("artifacts/model.pkl")

st.set_page_config(page_title="Delivery Time Predictor", layout="centered")

st.title("Delivery Time Prediction System")
st.write("Enter order details to predict delivery time")


distance = st.number_input("Distance (km)", min_value=0.0, value=5.0)

weather = st.selectbox(
    "Weather",
    ["Clear", "Foggy", "Rainy", "Snowy", "Windy"]
)

traffic = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle = st.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

prep_time = st.number_input("Preparation Time (min)", min_value=0.0, value=20.0)

experience = st.number_input("Courier Experience (years)", min_value=0.0, value=3.0)


if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame([{
        "Distance_km": distance,
        "Weather": weather,
        "Traffic_Level": traffic,
        "Time_of_Day": time_of_day,
        "Vehicle_Type": vehicle,
        "Preparation_Time_min": prep_time,
        "Courier_Experience_yrs": experience
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Delivery Time: {round(prediction, 2)} minutes")