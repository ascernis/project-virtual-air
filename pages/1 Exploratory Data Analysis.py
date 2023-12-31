import streamlit as st
import pandas as pd

st.title("Virtual Air: Atmosphere Simulation and Prediction Tool")
st.header("// Exploratory Data Analysis")

st.divider()

# Median Pollutant History
medianPollutants = pd.read_csv("./data/medianPollutants.csv")

st.header("Pollutant History of Beijing")
st.subheader("Displays the Pollutant's Levels throughout 2013-2017")

medianPollutantOption = st.selectbox("Pick Pollutant",
             ["PM2.5", "SO2", "NO2", "CO", "O3"])

st.write("Now Displaying: ", medianPollutantOption)

if medianPollutantOption == "PM2.5":
    st.bar_chart(data= medianPollutants,
                x= "Year",
                y= "Median PM2_5",
                color= None,
                width= 0,
                height= 0,
                use_container_width= True)
    
elif medianPollutantOption == "SO2":
    st.bar_chart(data=medianPollutants,
                 x="Year",
                 y="Median SO2",
                 color=None,
                 width=0,
                 height=0,
                 use_container_width=True)
    
elif medianPollutantOption == "NO2":
    st.bar_chart(data=medianPollutants,
                 x="Year",
                 y="Median NO2",
                 color=None,
                 width=0,
                 height=0,
                 use_container_width=True)
    
elif medianPollutantOption == "CO":
    st.bar_chart(data=medianPollutants,
                 x="Year",
                 y="Median CO",
                 color=None,
                 width=0,
                 height=0,
                 use_container_width=True)
    
elif medianPollutantOption == "O3":
    st.bar_chart(data=medianPollutants,
                 x="Year",
                 y="Median O3",
                 color=None,
                 width=0,
                 height=0,
                 use_container_width=True)
else:
    st.write("Select a pollutant to display its bar chart.")

st.divider()

# Median External Factors History
medianExFactors = pd.read_csv("./data/medianExFactors.csv")

st.header("External Factors History of Beijing")
st.subheader("Displays the External Factor's Levels throughout 2013-2017")

medianExFactorsOption = st.selectbox("Pick External Factor",
             ["Temperature", "Pressure", "DewPoint", "Rain"])

st.write("Now Displaying: ", medianExFactorsOption)

if medianExFactorsOption == "Temperature":
        st.bar_chart(data= medianExFactors,
                x= "Year",
                y= "Temperature",
                color= None,
                width= 0,
                height= 0,
                use_container_width= True)
        
elif medianExFactorsOption == "Pressure":
        st.bar_chart(data= medianExFactors,
                x= "Year",
                y= "Pressure",
                color= None,
                width= 0,
                height= 0,
                use_container_width= True)
        
elif medianExFactorsOption == "DewPoint":
        st.bar_chart(data= medianExFactors,
                x= "Year",
                y= "DewPoint",
                color= None,
                width= 0,
                height= 0,
                use_container_width= True)
        
elif medianExFactorsOption == "Rain":
        st.bar_chart(data= medianExFactors,
                x= "Year",
                y= "Rain",
                color= None,
                width= 0,
                height= 0,
                use_container_width= True)

else:
    st.write("Select an external factor to display its bar chart.")

st.divider()

# Correlation Analysis
st.header("Correlation Analysis")
st.subheader("Measures each Pollutant against each External Factor")

st.caption("This is the code written using the Pearson Correlation Coefficient.")

pearsonOption = st.selectbox("Pick Pollutant",
             ["PM2.5 Correlation", "SO2 Correlation", "NO2 Correlation", "CO Correlation", "O3 Correlation"])

st.write("Now Displaying: ", pearsonOption)

if pearsonOption == "PM2.5 Correlation":
    st.code('''
                selected_columns = ['PM2.5', 'Temperature', 'Pressure', 'DewPoint', 'Rain', 'WindDirection', 'WindSpeed']
                
                # Extract the selected columns from the DataFrame
                selected_data = df[selected_columns]

                # Drop rows with NaN values
                selected_data = selected_data.dropna()

                # Calculate Pearson's correlation coefficients
                tempCC, tempCC_p_value = pearsonr(selected_data['PM2.5'], selected_data['Temperature'])
                presCC, presCC_p_value = pearsonr(selected_data['PM2.5'], selected_data['Pressure'])
                dewpCC, dewpCC_p_value = pearsonr(selected_data['PM2.5'], selected_data['DewPoint'])
                rainCC, rainCC_p_value = pearsonr(selected_data['PM2.5'], selected_data['Rain'])
                wdCC, wdCC_p_value = pearsonr(selected_data['PM2.5'], selected_data['WindDirection'])
                wsCC, wsCC_p_value = pearsonr(selected_data['PM2.5'], selected_data['WindSpeed'])

                # Print results
                print(f"PM2.5 & Temperature: {tempCC} (p-value: {tempCC_p_value})")
                print(f"PM2.5 & Pressure: {presCC} (p-value: {presCC_p_value})")
                print(f"PM2.5 & DewPoint: {dewpCC} (p-value: {dewpCC_p_value})")
                print(f"PM2.5 & Rain: {rainCC} (p-value: {rainCC_p_value})")
                print(f"PM2.5 & WindDirection: {wdCC} (p-value: {wdCC_p_value})")
                print(f"PM2.5 & WindSpeed: {wsCC} (p-value: {wsCC_p_value})")
            ''', 
            language = "python", 
            line_numbers = True)
    
elif pearsonOption == "SO2 Correlation":
    st.code('''
                selected_columns = ['SO2', 'Temperature', 'Pressure', 'DewPoint', 'Rain', 'WindDirection', 'WindSpeed']

                # Extract the selected columns from the DataFrame
                selected_data = df[selected_columns]

                # Drop rows with NaN values
                selected_data = selected_data.dropna()

                # Calculate Pearson's correlation coefficients
                tempCC, tempCC_p_value = pearsonr(selected_data['SO2'], selected_data['Temperature'])
                presCC, presCC_p_value = pearsonr(selected_data['SO2'], selected_data['Pressure'])
                dewpCC, dewpCC_p_value = pearsonr(selected_data['SO2'], selected_data['DewPoint'])
                rainCC, rainCC_p_value = pearsonr(selected_data['SO2'], selected_data['Rain'])
                wdCC, wdCC_p_value = pearsonr(selected_data['SO2'], selected_data['WindDirection'])
                wsCC, wsCC_p_value = pearsonr(selected_data['SO2'], selected_data['WindSpeed'])

                # Print results
                print(f"SO2 & Temperature: {tempCC} (p-value: {tempCC_p_value})")
                print(f"SO2 & Pressure: {presCC} (p-value: {presCC_p_value})")
                print(f"SO2 & DewPoint: {dewpCC} (p-value: {dewpCC_p_value})")
                print(f"SO2 & Rain: {rainCC} (p-value: {rainCC_p_value})")
                print(f"SO2 & WindDirection: {wdCC} (p-value: {wdCC_p_value})")
                print(f"SO2 & WindSpeed: {wsCC} (p-value: {wsCC_p_value})")
                            ''', 
            language = "python", 
            line_numbers = True)
    
elif pearsonOption == "NO2 Correlation":
    st.code('''
                selected_columns = ['NO2', 'Temperature', 'Pressure', 'DewPoint', 'Rain', 'WindDirection', 'WindSpeed']

                # Extract the selected columns from the DataFrame
                selected_data = df[selected_columns]

                # Drop rows with NaN values
                selected_data = selected_data.dropna()

                # Calculate Pearson's correlation coefficients
                tempCC, tempCC_p_value = pearsonr(selected_data['NO2'], selected_data['Temperature'])
                presCC, presCC_p_value = pearsonr(selected_data['NO2'], selected_data['Pressure'])
                dewpCC, dewpCC_p_value = pearsonr(selected_data['NO2'], selected_data['DewPoint'])
                rainCC, rainCC_p_value = pearsonr(selected_data['NO2'], selected_data['Rain'])
                wdCC, wdCC_p_value = pearsonr(selected_data['NO2'], selected_data['WindDirection'])
                wsCC, wsCC_p_value = pearsonr(selected_data['NO2'], selected_data['WindSpeed'])

                # Print results
                print(f"NO2 & Temperature: {tempCC} (p-value: {tempCC_p_value})")
                print(f"NO2 & Pressure: {presCC} (p-value: {presCC_p_value})")
                print(f"NO2 & DewPoint: {dewpCC} (p-value: {dewpCC_p_value})")
                print(f"NO2 & Rain: {rainCC} (p-value: {rainCC_p_value})")
                print(f"NO2 & WindDirection: {wdCC} (p-value: {wdCC_p_value})")
                print(f"NO2 & WindSpeed: {wsCC} (p-value: {wsCC_p_value})")
                            ''', 
            language = "python", 
            line_numbers = True)
    
elif pearsonOption == "CO Correlation":
    st.code('''
                selected_columns = ['CO', 'Temperature', 'Pressure', 'DewPoint', 'Rain', 'WindDirection', 'WindSpeed']

                # Extract the selected columns from the DataFrame
                selected_data = df[selected_columns]

                # Drop rows with NaN values
                selected_data = selected_data.dropna()

                # Calculate Pearson's correlation coefficients
                tempCC, tempCC_p_value = pearsonr(selected_data['CO'], selected_data['Temperature'])
                presCC, presCC_p_value = pearsonr(selected_data['CO'], selected_data['Pressure'])
                dewpCC, dewpCC_p_value = pearsonr(selected_data['CO'], selected_data['DewPoint'])
                rainCC, rainCC_p_value = pearsonr(selected_data['CO'], selected_data['Rain'])
                wdCC, wdCC_p_value = pearsonr(selected_data['CO'], selected_data['WindDirection'])
                wsCC, wsCC_p_value = pearsonr(selected_data['CO'], selected_data['WindSpeed'])

                # Print results
                print(f"CO & Temperature: {tempCC} (p-value: {tempCC_p_value})")
                print(f"CO & Pressure: {presCC} (p-value: {presCC_p_value})")
                print(f"CO & DewPoint: {dewpCC} (p-value: {dewpCC_p_value})")
                print(f"CO & Rain: {rainCC} (p-value: {rainCC_p_value})")
                print(f"CO & WindDirection: {wdCC} (p-value: {wdCC_p_value})")
                print(f"CO & WindSpeed: {wsCC} (p-value: {wsCC_p_value})")
                            ''', 
            language = "python", 
            line_numbers = True)
    
elif pearsonOption == "O3 Correlation":
    st.code('''
                selected_columns = ['O3', 'Temperature', 'Pressure', 'DewPoint', 'Rain', 'WindDirection', 'WindSpeed']

                # Extract the selected columns from the DataFrame
                selected_data = df[selected_columns]

                # Drop rows with NaN values
                selected_data = selected_data.dropna()

                # Calculate Pearson's correlation coefficients
                tempCC, tempCC_p_value = pearsonr(selected_data['O3'], selected_data['Temperature'])
                presCC, presCC_p_value = pearsonr(selected_data['O3'], selected_data['Pressure'])
                dewpCC, dewpCC_p_value = pearsonr(selected_data['O3'], selected_data['DewPoint'])
                rainCC, rainCC_p_value = pearsonr(selected_data['O3'], selected_data['Rain'])
                wdCC, wdCC_p_value = pearsonr(selected_data['O3'], selected_data['WindDirection'])
                wsCC, wsCC_p_value = pearsonr(selected_data['O3'], selected_data['WindSpeed'])

                # Print results
                print(f"O3 & Temperature: {tempCC} (p-value: {tempCC_p_value})")
                print(f"O3 & Pressure: {presCC} (p-value: {presCC_p_value})")
                print(f"O3 & DewPoint: {dewpCC} (p-value: {dewpCC_p_value})")
                print(f"O3 & Rain: {rainCC} (p-value: {rainCC_p_value})")
                print(f"O3 & WindDirection: {wdCC} (p-value: {wdCC_p_value})")
                print(f"O3 & WindSpeed: {wsCC} (p-value: {wsCC_p_value})")
                            ''', 
            language = "python", 
            line_numbers = True)

st.write("\n")
st.write("Results for: ", pearsonOption)

# Tables for Pearson Coefficient
ccPM2_5 = pd.read_csv("./data/ccPM2.5.csv")
ccSO2 = pd.read_csv("./data/ccSO2.csv")
ccNO2 = pd.read_csv("./data/ccNO2.csv")
ccCO = pd.read_csv("./data/ccCO.csv")
ccO3 = pd.read_csv("./data/ccO3.csv")

if pearsonOption == "PM2.5 Correlation":
    st.table(data = ccPM2_5)

elif pearsonOption == "SO2 Correlation":
     st.table(data = ccSO2)

elif pearsonOption == "NO2 Correlation":
     st.table(data = ccNO2)

elif pearsonOption == "CO Correlation":
     st.table(data = ccCO)

elif pearsonOption == "O3 Correlation":
     st.table(data = ccO3)

else:
    st.write("Select a Pearson Correlation Analysis")