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




###### MAIN PAGE ######

# create en empty table with the following columns DATE, FLIGHT, REG, FROM, TO, DIST, DEP, ARR, AIRLINE, AIRCRAFT, SEAT, NOTE
df = pd.DataFrame(columns=['DATE', 'FLIGHT', 'REG', 'FROM', 'TO', 'DIST', 'DEP', 'ARR', 'AIRLINE', 'AIRCRAFT', 'SEAT', 'NOTE'])

# create funtionality to add a new flight
st.sidebar.header('Add a new flight')
date = st.sidebar.date_input('Date')
flight = st.sidebar.text_input('Flight number')
reg = st.sidebar.text_input('Registration')
from_ = st.sidebar.text_input('From')
to = st.sidebar.text_input('To')
dist = st.sidebar.number_input('Distance')
dep = st.sidebar.time_input('Departure')
arr = st.sidebar.time_input('Arrival')
airline = st.sidebar.text_input('Airline')
aircraft = st.sidebar.text_input('Aircraft')
seat = st.sidebar.text_input('Seat')
note = st.sidebar.text_input('Note')
if st.sidebar.button('Add flight'):
    df = df.append({'DATE': date, 'FLIGHT': flight, 'REG': reg, 'FROM': from_, 'TO': to, 'DIST': dist, 'DEP': dep, 'ARR': arr, 'AIRLINE': airline, 'AIRCRAFT': aircraft, 'SEAT': seat, 'NOTE': note}, ignore_index=True)
    df.to_csv('data.csv', index=False)

# create funtionality to delete a flight
st.sidebar.header('Delete a flight')
flight = st.sidebar.text_input('Flight number')
if st.sidebar.button('Delete flight'):
    df = df[df['FLIGHT'] != flight]
    df.to_csv('data.csv', index=False)

