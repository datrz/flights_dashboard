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

# create a title
st.title("Data Science Project")
# create a subtitle
st.subheader("This is a subtitle")
# create a text
st.text("Hello Streamlit")
# create a header
st.header("This is a header")
# create a subheader
st.subheader("This is a subheader")
# create a markdown
st.markdown("### This is a markdown")
# create a button
st.button("Simple button")
# create a checkbox
st.checkbox("Simple checkbox")
# create a radio button
st.radio("Simple radio button", ("option 1", "option 2"))
# create a selectbox
st.selectbox("Simple selectbox", ("option 1", "option 2"))
# create a multiselect
st.multiselect("Simple multiselect", ("option 1", "option 2"))
# create a file uploader
st.file_uploader("Simple file uploader")
# create a color picker
st.color_picker("Simple color picker")
# create a date input
st.date_input("Simple date input")
# create a time input
st.time_input("Simple time input")
# create a text input
st.text_input("Simple text input")
# create a number input
st.number_input("Simple number input")
# create a text area
st.text_area("Simple text area")
# create a slider
st.slider("Simple slider")
# create a progress bar
st.progress(50)
# create a spinner
st.spinner("Simple spinner")
# create a balloon
st.balloons()
# create a code
st.code("print('Hello Streamlit')")
# create a json
st.json({"name": "John", "age": 30})
# create a dataframe
st.dataframe(pd.DataFrame({"name": ["John", "Mary"], "age": [30, 25]}))
# create a table
st.table(pd.DataFrame({"name": ["John", "Mary"], "age": [30, 25]}))
# create a line chart
st.line_chart(pd.DataFrame({"name": ["John", "Mary"], "age": [30, 25]}))
# create a area chart
st.area_chart(pd.DataFrame({"name": ["John", "Mary"], "age": [30, 25]}))
# create a bar chart
st.bar_chart(pd.DataFrame({"name": ["John", "Mary"], "age": [30, 25]}))
# create a pyplot
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])
st.pyplot(fig)
