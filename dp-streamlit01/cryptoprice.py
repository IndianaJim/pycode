import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bs4 import BeautifulSoup
import requests
import json
import time

# Page layout - page expands to full width
st.set_page_config(layout="wide")
# Title
image = Image.open('bitcoinlogo1.png')
st.image(image, width=500)

