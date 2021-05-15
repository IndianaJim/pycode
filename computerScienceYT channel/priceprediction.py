# program uses an artificial recurrent neural network called long short term memory (lstm) to predict the closing price using past 60 day stock price.

#import the libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethiryeight')
