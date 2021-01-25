#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This program using a Artificial Recurrent Neural Network called LSTM (Long Short Term Memory) 
# to predict the closing stock price of a corporation (Apple Inc.) using the past 60 day stock price.


# In[5]:


#Imports
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# In[8]:


#Get the stock quote
df = web.DataReader('AAPL', data_source = 'yahoo', start='2012-01-01', end='2020-12-31')
df


# In[9]:


plt.figure(figsize=(16,8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize = 18)
plt.show()


# In[ ]:




