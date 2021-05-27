import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

# Page layout - page expands to full width
st.set_page_config(layout="wide")
# Title
image = Image.open('bitcoinlogo1.png')
st.image(image, width=500)
st.title("Crypto Price App")
st.markdown("""
This app retrieves current prices for top 100 crypto tokens.
""")

# Page layout - continued
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

#sidebar + main panel
col1.header('imput options')

