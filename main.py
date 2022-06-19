import datetime
import pandas_datareader.data as web
import pandas as pd
from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days = 1) 
weekago = today - timedelta(days = 7)

tickers = ['TSLA', 'UAL']
data = {"day":{}, "week": {}}
percent_change = {"day": {}, "week": {}}
for t in tickers: 
    data["day"][t] = web.DataReader(t,'yahoo', yesterday, today)
    data["week"][t] = web.DataReader(t,'yahoo', weekago, today)
    percent_change["day"][t] = round(( data["day"][t].Close - data["day"][t].Open ) / (data["day"][t].Open) * 100 , 2)
    percent_change["week"][t] = round(( data["week"][t].iloc[4].Close - data["week"][t].iloc[0].Open ) / (data["week"][t].iloc[0].Open) * 100, 2)

# print(data["day"])
# print(percent_change["week"])
