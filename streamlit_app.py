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

flights = []

for row in soup.find_all('tr'):
    flight = {}
    cells = row.find_all('td')
    if cells:
        flight['date'] = cells[0].find('span', {'class': 'inner-date'}).text
        flight['flight'] = cells[1].text.strip()
        flight['reg'] = cells[2].text.strip()
        flight['from'] = cells[3].find('span', {'class': 'tooltip'}).get('data-tooltip-value')
        flight['to'] = cells[4].find('span', {'class': 'tooltip'}).get('data-tooltip-value')
        flight['dist'] = cells[5].text.strip()
        flight['dep_time'] = cells[6].text.strip()
        flight['arr_time'] = cells[7].text.strip()
        flight['airline'] = cells[8].find('span', {'class': 'tooltip'}).get('data-tooltip-value')
        flight['aircraft'] = cells[9].find('span', {'class': 'tooltip'}).get('data-tooltip-value')
        flight['seat'] = cells[10].text.strip()
        flight['note'] = cells[11].text.strip()
        flight['class'] = cells[12].find('span', {'class': 'circle-icon class-economy tooltip'}).get('data-tooltip-value')
        flight['reason'] = cells[12].find('span', {'class': 'circle-icon reason-leisure tooltip'}).get('data-tooltip-value')
        flights.append(flight)

df = pd.DataFrame(flights)

if page == 'Main Page':
    # Print the dataframe in streamlit
    st.write(df)