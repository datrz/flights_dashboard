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