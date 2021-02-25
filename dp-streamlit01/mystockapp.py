import yfinance as yf
import streamlit as st
import pandas as pd

st.write ("""
# Simple Stock Proce App

Shown are the stock closing price and volume of AAPL

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start='2010-01-01', end='2021-02-24')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
