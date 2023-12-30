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
st.divider()

# History
medianPollutants = pd.read_csv("./data/defaultAirQuality.csv")

st.header("Beijing's Air Quality History")
st.subheader("PM2.5")
st.bar_chart(data= medianPollutants,
             x= "Year",
             y= "PM2_5",
             color= None,
             width= 0,
             height= 0,
             use_container_width= True)

st.subheader("PM10")
st.bar_chart(data= medianPollutants,
             x= "Year",
             y= "PM10",
             color= None,
             width= 0,
             height= 0,
             use_container_width= True)

st.subheader("SO2")
st.bar_chart(data= medianPollutants,
             x= "Year",
             y= "SO2",
             color= None,
             width= 0,
             height= 0,
             use_container_width= True)

st.subheader("NO2")
st.bar_chart(data= medianPollutants,
             x= "Year",
             y= "NO2",
             color= None,
             width= 0,
             height= 0,
             use_container_width= True)

st.subheader("CO")
st.bar_chart(data= medianPollutants,
             x= "Year",
             y= "CO",
             color= None,
             width= 0,
             height= 0,
             use_container_width= True)

st.subheader("O3")
st.bar_chart(data= medianPollutants,
             x= "Year",
             y= "O3",
             color= None,
             width= 0,
             height= 0,
             use_container_width= True)