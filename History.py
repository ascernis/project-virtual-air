import streamlit as st
import pandas as pd

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