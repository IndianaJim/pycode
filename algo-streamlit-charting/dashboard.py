import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Streamlit Finance Dashboard')
tickers = ('TSLA', 'AAPL', 'GBTC', 'ETHE', 'SPY', 'BTC-USD', 'ETH-USD')
dropdown = st.multiselect('Pick your asset', tickers)