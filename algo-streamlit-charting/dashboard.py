# algovibes https://www.youtube.com/watch?v=Km2KDo6tFpQ&t=304s

import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Streamlit Finance Dashboard')
tickers = ('TSLA', 'AAPL', 'GBTC', 'ETHE', 'SPY', 'BTC-USD', 'ETH-USD')
dropdown = st.multiselect('Pick your asset', tickers)

start = st.date_input('Start',value = pd.to_datetime('2021-01-01'))
end = st.date_input('End',value = pd.to_datetime('today'))

if len(dropdown) > 0:
    df = yf.download(dropdown, start, end)['Adj Close']
    st.line_chart(df)