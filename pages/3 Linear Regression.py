import streamlit as st
import pandas as pd
import joblib

# Load Linear Regression Model
lrModel = joblib.load("./models/lr_CO_model.joblib")

# Title
st.title("Linear Regression Model")
st.header("// Machine Learning")

st.divider()

# Decoding Station Names
decodingStation = {
    'Aotizhongxin': 0,
    'Changping': 1,
    'Dingling': 2,
    'Dongsi': 3,
    'Guanyuan': 4,
    'Gucheng': 5,
    'Huairou': 6,
    'Nongzhanguan': 7,
    'Shunyi': 8,
    'Tiantan': 9,
    'Wanliu': 10,
    'Wanshouxigong': 11
}

stationNames = st.selectbox("Station", list(decodingStation.keys()))
Station = decodingStation.get(stationNames, -1)  # Use -1 as a default value if the station name is not found

# Decoding Wind Direction
decodingWD = {
    'NNW': 6,
    'N': 3,
    'NW': 7,
    'NNE': 5,
    'ENE': 1,
    'E': 0,
    'NE': 4,
    'W': 13,
    'SSW': 11,
    'WSW': 15,
    'SE': 9,
    'WNW': 14,
    'SSE': 10,
    'ESE': 2,
    'S': 8,
    'SW': 12,
    'nan': 16
}

WindDirection = st.selectbox("WindDirection", list(decodingWD.keys()))
WindDirection = decodingWD.get(WindDirection, -1)  # Use -1 as a default value if the wind direction is not found

# Pollutants Slider
PM2_5 = st.slider("PM2.5", min_value=2, max_value=1000)
SO2 = st.slider("SO2", min_value=0, max_value=500)
NO2 = st.slider("NO2", min_value=1, max_value=290)
O3 = st.slider("O3", min_value=0, max_value=1100)

# External Factor Sliders
Temperature = st.slider("Temperature", min_value=-20, max_value=45)
Pressure = st.slider("Pressure", min_value=900, max_value=1100)
DewPoint = st.slider("DewPoint", min_value=-45, max_value=45)
Rain = st.slider("Rain", min_value=0, max_value=100)
WindSpeed = st.slider("WindSpeed", min_value=0, max_value=15)

# Prediction Function
prediction = lrModel.predict([[WindDirection, Station, PM2_5, SO2, NO2, O3, Temperature, Pressure, DewPoint, Rain, WindSpeed]])

# Display Prediction
st.write(f"Prediction: {prediction}")

# Display Prediction Probabilities (adjusted for regression)
st.write("Prediction Probabilities: N/A")

# Interpretation
pollutionLevel = {0: "Low Pollution", 1: "Moderate Pollution", 2: "High Pollution"}

# Handle cases where the station or wind direction is not found
if Station == -1 or WindDirection == -1:
    st.write("Invalid Station or Wind Direction. Please select valid values.")
else:
    # Handle cases where the rounded prediction is outside the expected range
    rounded_prediction = int(round(prediction[0]))
    predictionLabel = pollutionLevel.get(rounded_prediction, "Unknown Pollution Level")
    st.write(f"Predicted Class: {predictionLabel}")