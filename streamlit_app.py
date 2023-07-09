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
import requests
from bs4 import BeautifulSoup

st.set_page_config(layout="wide")

###### SIDEBAR ######
# create select menu
st.sidebar.title('Select Menu')
st.sidebar.subheader('Select the page you want to see')
page = st.sidebar.selectbox('Page',['Main Page', 'Map', 'Statistics', 'About'], label_visibility="hidden")

###### DOWNLOAD DATA ######

url = 'https://my.flightradar24.com/dtrzc/flights'
response = requests.get(url)

# Now response.text will contain the HTML content of the page
html_content = response.text

# create en empty table with the following columns DATE, FLIGHT, REG, FROM, TO, DIST, DEP, ARR, AIRLINE, AIRCRAFT, SEAT, NOTE
df = pd.DataFrame(columns=['DATE', 'FLIGHT', 'REG', 'FROM', 'TO', 'DIST', 'DEP', 'ARR', 'AIRLINE', 'AIRCRAFT', 'SEAT', 'NOTE'])

# Assuming `html_doc` is your HTML document
soup = BeautifulSoup(html_content, 'html.parser')

def get_data(cell, element, attr=None, value=None):
    """Extracts data from a BeautifulSoup object and handles exceptions."""
    try:
        if attr and value:
            result = None
            results = cell.find_all(element)
            for res in results:
                if res.get(attr) == value:
                    result = res.get('data-tooltip-value')
                    break
            if result is None:
                result = cell.text.strip()
        else:
            result = cell.text.strip()
        return result
    except AttributeError:
        return 'N/A'


flights = []
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        flight = {}
        flight['DATE'] = get_data(cells[0], 'span', 'class', 'inner-date')
        flight['FLIGHT'] = get_data(cells[1], 'td')
        flight['REG'] = get_data(cells[2], 'td')
        flight['FROM'] = get_data(cells[3], 'span', 'class', 'tooltip')
        flight['TO'] = get_data(cells[4], 'span', 'class', 'tooltip')
        flight['DIST'] = get_data(cells[5], 'td')
        flight['DEP'] = get_data(cells[6], 'td')
        flight['ARR'] = get_data(cells[7], 'td')
        flight['AIRLINE'] = get_data(cells[8], 'span', 'class', 'tooltip')
        flight['AIRCRAFT'] = get_data(cells[9], 'span', 'class', 'tooltip')
        flight['SEAT'] = get_data(cells[10], 'td')
        flight['NOTE'] = get_data(cells[11], 'td')
        flight['CLASS'] = get_data(cells[12], 'span', 'class', 'circle-icon class-economy tooltip')
        flight['REASON'] = get_data(cells[12], 'span', 'class', 'circle-icon reason-leisure tooltip')
        flights.append(flight)

df = pd.DataFrame(flights)

# load flights.csv
df_preloaded = pd.read_csv('flights.csv')

# add additional column with inverted index of the index
df_preloaded['flight_count'] = df_preloaded.index.values[::-1]+1

# check if the flights from df are already in df_preloaded
# if not, add them to df_preloaded
# take combination of DATE, FLIGHT
for index, row in df.iterrows():
    if not df_preloaded[(df_preloaded['DATE'] == row['DATE']) & (df_preloaded['FLIGHT'] == row['FLIGHT'])].empty:
        #print('Flight already in df_preloaded')
        continue
    else:
        df_preloaded = pd.concat([df_preloaded, row], ignore_index=True)

# ====== MAIN PAGE VIEW ======

if page == 'Main Page':
    # Print the dataframe in streamlit
    st.write(df_preloaded)