
# coding: utf-8

# In[33]:


import numpy as py
import pandas as pd
from scipy import stats
from decimal import Decimal

def stats_value(path):
    
    data = pd.read_csv(path)
    df = data[['Date', 'Close']]
    df.index = pd.to_datetime(df['Date'])
    df = df.drop('Date', axis=1)
    df_mean = Decimal(df['Close'].mean()).quantize(Decimal("0.0001"), rounding = "ROUND_HALF_UP")
    df_variance = Decimal(df['Close'].std()).quantize(Decimal("0.0001"), rounding = "ROUND_HALF_UP")
    df_skewness = Decimal(stats.skew(df['Close'])).quantize(Decimal("0.0001"), rounding = "ROUND_HALF_UP")
    df_kurtosis = Decimal(stats.skew(stats.kurtosis(df['Close']))).quantize(Decimal("0.0001"), rounding = "ROUND_HALF_UP")
    
    
    print('Sample mean:', df_mean)
    print('Sample variance:', df_variance)
    print('Sample Adjusted skewness:', df_skewness)
    print('Sample Adjusted excess kurtosis:', df_kurtosis)


stats_value('/Users/zhaoencong/Desktop/IBM.csv')

