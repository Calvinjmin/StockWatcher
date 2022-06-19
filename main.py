import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd

today = date.today()
yesterday = today - timedelta(days = 1) 

tickers = ['TSLA', 'UAL']
data = {}
percent_change = {}
for t in tickers:
   data[t] = web.DataReader(t,'yahoo', yesterday, today ).reset_index()
   percent_change[t] = ( data[t].Close - data[t].Open ) / (data[t].Open) * 100

print(percent_change['TSLA'])

