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

###### MAIN PAGE ######

url = 'https://my.flightradar24.com/dtrzc/flights'
response = requests.get(url)

# Now response.text will contain the HTML content of the page
html_content = response.text

# create en empty table with the following columns DATE, FLIGHT, REG, FROM, TO, DIST, DEP, ARR, AIRLINE, AIRCRAFT, SEAT, NOTE
df = pd.DataFrame(columns=['DATE', 'FLIGHT', 'REG', 'FROM', 'TO', 'DIST', 'DEP', 'ARR', 'AIRLINE', 'AIRCRAFT', 'SEAT', 'NOTE'])

# Assuming `html_doc` is your HTML document
soup = BeautifulSoup(html_content, 'html.parser')

st.write(soup)

def get_data(cell, element, attr=None, value=None):
    """Extracts data from a BeautifulSoup object and handles exceptions."""
    try:
        if attr and value:
            result = cell.find(element, {attr: value}).get('data-tooltip-value')
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
        flight['date'] = get_data(cells[0], 'span', 'class', 'inner-date')
        flight['flight'] = get_data(cells[1], 'td')
        flight['reg'] = get_data(cells[2], 'td')
        flight['from'] = get_data(cells[3], 'span', 'class', 'tooltip')
        flight['to'] = get_data(cells[4], 'span', 'class', 'tooltip')
        flight['dist'] = get_data(cells[5], 'td')
        flight['dep_time'] = get_data(cells[6], 'td')
        flight['arr_time'] = get_data(cells[7], 'td')
        flight['airline'] = get_data(cells[8], 'span', 'class', 'tooltip')
        flight['aircraft'] = get_data(cells[9], 'span', 'class', 'tooltip')
        flight['seat'] = get_data(cells[10], 'td')
        flight['note'] = get_data(cells[11], 'td')
        flight['class'] = get_data(cells[12], 'span', 'class', 'circle-icon class-economy tooltip')
        flight['reason'] = get_data(cells[12], 'span', 'class', 'circle-icon reason-leisure tooltip')
        flights.append(flight)

df = pd.DataFrame(flights)

if page == 'Main Page':
    # Print the dataframe in streamlit
    st.write(df)