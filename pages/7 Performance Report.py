import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Performance Report")

# Importing Tables
## Random Forest
rf_PM2_5_performance = pd.read_csv("./data/rf_PM2_5_performance.csv")
rf_SO2_performance = pd.read_csv("./data/rf_SO2_performance.csv")
rf_NO2_performance = pd.read_csv("./data/rf_NO2_performance.csv")
rf_CO_performance = pd.read_csv("./data/rf_CO_performance.csv")
rf_O3_performance = pd.read_csv("./data/rf_O3_performance.csv")

## Linear Regression
lr_PM2_5_performance = pd.read_csv("./data/lr_PM2_5_performance.csv")
lr_SO2_performance = pd.read_csv("./data/lr_SO2_performance.csv")
lr_NO2_performance = pd.read_csv("./data/lr_NO2_performance.csv")
lr_CO_performance = pd.read_csv("./data/lr_CO_performance.csv")
lr_O3_performance = pd.read_csv("./data/lr_O3_performance.csv")

## Neural Network
nn_PM2_5_performance = pd.read_csv("./data/nn_PM2_5_performance.csv")
nn_SO2_performance = pd.read_csv("./data/nn_SO2_performance.csv")
nn_NO2_performance = pd.read_csv("./data/nn_NO2_performance.csv")
nn_CO_performance = pd.read_csv("./data/nn_CO_performance.csv")
nn_O3_performance = pd.read_csv("./data/nn_O3_performance.csv")

## Support Vector Machine
svm_PM2_5_performance = pd.read_csv("./data/svm_PM2_5_performance.csv")
svm_SO2_performance = pd.read_csv("./data/svm_SO2_performance.csv")
svm_NO2_performance = pd.read_csv("./data/svm_NO2_performance.csv")
svm_CO_performance = pd.read_csv("./data/svm_CO_performance.csv")
svm_O3_performance = pd.read_csv("./data/svm_O3_performance.csv")

modelOption = st.selectbox("Select Machine Learning Model:",
                           ["Random Forest", "Linear Regression", "Neural Network", "Support Vector Machine"])

if modelOption == "Random Forest":
    st.write("Now Displaying: ", modelOption)
    
    st.subheader("Performance Reports")
    st.caption("PM2.5")
    st.table(rf_PM2_5_performance)

    st.caption("SO2")
    st.table(rf_SO2_performance)

    st.caption("NO2")
    st.table(rf_NO2_performance)

    st.caption("CO")
    st.table(rf_CO_performance)

    st.caption("O3")
    st.table(rf_O3_performance)

elif modelOption == "Linear Regression":
    st.write("Now Displaying: ", modelOption)
    
    st.subheader("Performance Reports")
    st.caption("PM2.5")
    st.table(lr_PM2_5_performance)

    st.caption("SO2")
    st.table(lr_SO2_performance)

    st.caption("NO2")
    st.table(lr_NO2_performance)

    st.caption("CO")
    st.table(lr_CO_performance)

    st.caption("O3")
    st.table(lr_O3_performance)

elif modelOption == "Neural Network":
    st.write("Now Displaying: ", modelOption)
    
    st.subheader("Performance Reports")
    st.caption("PM2.5")
    st.table(nn_PM2_5_performance)

    st.caption("SO2")
    st.table(nn_SO2_performance)

    st.caption("NO2")
    st.table(nn_NO2_performance)

    st.caption("CO")
    st.table(nn_CO_performance)

    st.caption("O3")
    st.table(nn_O3_performance)

elif modelOption == "Support Vector Machine":
    st.write("Now Displaying: ", modelOption)
    
    st.subheader("Performance Reports")
    st.caption("PM2.5")
    st.table(svm_PM2_5_performance)

    st.caption("SO2")
    st.table(svm_SO2_performance)

    st.caption("NO2")
    st.table(svm_NO2_performance)

    st.caption("CO")
    st.table(svm_CO_performance)

    st.caption("O3")
    st.table(svm_O3_performance)