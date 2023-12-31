import streamlit as st
import pandas as pd

# Title
st.title("Virtual Air: Atmosphere Simulation and Prediction Tool")
st.header("// Home")
st.caption("Developed by TP057876 Chong Kyle from APD3F2305CS(DA)")

st.write("Hey! My name is Kyle and I am a final year student from Asia Pacific University.")
st.write("Project Virtual Air is my FYP and it measures the performance of several machine learning algorithms using the Beijing Air Quality Dataset.")
st.write("This Streamlit app will host my Exploratory Data Analysis as well as the performance and code for the following algorithms: Random Forest, Linear Regression, Neural Network, and Support Vector Machine.")

st.divider()

# Dataset Visualisation
df = pd.read_csv("./data/cleanedAirQuality.csv")

st.header("Dataset Visualisation")

st.write("This simple visualisation showcases the cleaned Dataset that I will be using for machine learning purposes.")
st.write("If you would like to download the cleaned dataset or the original dataset, please click on the buttons below!")

st.write(df)

st.link_button("Download Original Dataset", 
               "https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data",
               help = "Brings the user to the original dataset repository")

st.download_button("Download Cleaned Dataset", 
                   df.to_csv(), 
                   file_name= "cleanedAirQuality.csv",
                   help = "Downloads the cleaned dataset for the user")

st.divider()