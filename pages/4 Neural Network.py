import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Loads Neural Network Model
nnModel = joblib.load("./models/nn_CO_model.joblib")

# Title
st.title("Neural Network Model")
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
Station = decodingStation[stationNames]

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
WindDirection = decodingWD[WindDirection]

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
input_data = np.array([[WindDirection, Station, PM2_5, SO2, NO2, O3, Temperature, Pressure, DewPoint, Rain, WindSpeed]])
prediction_probabilities = nnModel.predict(input_data)
low_polution = prediction_probabilities[0][0]
prediction_probabilities = np.array([[low_polution],[1 - low_polution]])

# Display Prediction
predicted_class = np.argmax(prediction_probabilities)
st.write(f"Prediction: {predicted_class}")

# Display Prediction Probabilities
st.write(f"Prediction Probabilities: {prediction_probabilities}")

# Intepretation
pollutionLevel = {0: "Low Pollution", 1: "Moderate Pollution", 2: "High Pollution"}
predictedLabel = pollutionLevel[predicted_class]
st.write(f"Predicted Class: {predictedLabel}")