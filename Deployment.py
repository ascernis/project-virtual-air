import streamlit as st
import pandas as pd

# Title
st.title("Virtual Air: Atmosphere Simulation and Prediction Tool")
st.caption("Developed by TP057876 Chong Kyle")

st.divider()

# Dataset Visualisation
df = pd.read_csv("./data/cleanedAirQuality.csv")

st.header("Dataset Visualisation")
st.write(df)
st.download_button("Download Dataset", df, file_name="cleanedAirQuality")
st.divider()