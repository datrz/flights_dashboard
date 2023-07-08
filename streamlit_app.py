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

###### SIDEBAR ######
# create select menu
st.sidebar.title('Select Menu')
st.sidebar.subheader('Select the page you want to see')
page = st.sidebar.selectbox(['Main Page', 'Map', 'Statistics', 'About'], index=0)

###### MAIN PAGE ######

# create en empty table with the following columns DATE, FLIGHT, REG, FROM, TO, DIST, DEP, ARR, AIRLINE, AIRCRAFT, SEAT, NOTE
df = pd.DataFrame(columns=['DATE', 'FLIGHT', 'REG', 'FROM', 'TO', 'DIST', 'DEP', 'ARR', 'AIRLINE', 'AIRCRAFT', 'SEAT', 'NOTE'])
