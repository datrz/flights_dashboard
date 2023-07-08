# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import time
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import seaborn as sns
import folium


st.set_page_config(layout="wide")

# Setup Control Side Panel to the left of the page
st.sidebar.title("Control Panel")
st.sidebar.header("Select a page to view")
page = st.sidebar.selectbox("Page", ["Home", "Data", "Model", "About"])

# Setup Home Page
if page == "Home":
    st.title("Welcome to the NYC Taxi Fare Prediction App")
    st.write("This app predicts the **NYC Taxi Fare** using the **Random Forest Regressor** model.")
    st.write("Please select a page on the left.")

# Setup Data Page
if page == "Data":
    st.title("NYC Taxi Fare Data")
    st.write("The data used in this app is from the Kaggle competition [New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/data).")
    st.write("The data is a subset of the full dataset, containing 55 million records and 11 columns. The data used in this app is a subset of 100,000 records and 8 columns.")
    st.write("The following is a description of the columns:")
    st.write("* **key** - Unique identifier of the record")
    st.write("* **fare_amount** - The taxi fare (target variable)")
    st.write("* **pickup_datetime** - Date and time of pickup")
    st.write("* **pickup_longitude** - Longitude coordinate of pickup location")
    st.write("* **pickup_latitude** - Latitude coordinate of pickup location")
    st.write("* **dropoff_longitude** - Longitude coordinate of dropoff location")
    st.write("* **dropoff_latitude** - Latitude coordinate of dropoff location")
    st.write("* **passenger_count** - Number of passengers")
    st.write("The following is a sample of the data:")
    st.write("![Sample Data](https://raw.githubusercontent.com/leexa90/streamlit-taxi-fare-prediction/main/images/sample_data.png)")
    st.write("The following is a histogram of the target variable:")
    st.write("![Target Variable](https://raw.githubusercontent.com/leexa90/streamlit-taxi-fare-prediction/main/images/target_variable
    .png)")
    st.write("The following is a scatter plot of the pickup and dropoff locations:")