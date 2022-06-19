import datetime
import pandas_datareader.data as web
import pandas as pd
import colorama
from colorama import Fore
from colorama import Style
from datetime import date
from datetime import timedelta

colorama.init()
today = date.today()
yesterday = today - timedelta(days = 1) 
weekago = today - timedelta(days = 7)
monthago = today - timedelta(days = 30)

tickers = ['SPY', 'AAPL', 'AMZN','META', 'DKNG', 'COF', 'BTC-USD', 'ETH-USD'] 
data = {"day":{}, "week": {}, "month": {} }
percent_change = {"day": {}, "week": {}, "month": {} }
end_price = {}

for t in tickers:
    print(t)
    data["day"][t] = web.DataReader(t,'yahoo', yesterday, today)
    data["week"][t] = web.DataReader(t,'yahoo', weekago, today)
    data["month"][t] = web.DataReader(t,'yahoo', monthago, today)

    week_length = int(len(data["week"][t].index) - 1)
    month_length = int(len(data["month"][t].index) - 1)

    percent_change["day"][t] = round(( data["day"][t].iloc[0].Close - data["day"][t].iloc[0].Open ) / (data["day"][t].iloc[0].Open) * 100 , 2)
    percent_change["week"][t] = round(( data["week"][t].iloc[week_length].Close - data["week"][t].iloc[0].Open ) / (data["week"][t].iloc[0].Open) * 100, 2)
    percent_change["month"][t] = round(( data["month"][t].iloc[month_length].Close - data["month"][t].iloc[0].Open ) / (data["month"][t].iloc[0].Open) * 100, 2)

    end_price[t] = round(data["day"][t].iloc[0].Close, 2)

# print(Fore.BLUE + Style.BRIGHT + "Data Printing - Daily" + Style.RESET_ALL)
# print( data["day"] )

# print(Fore.BLUE + Style.BRIGHT + "Data Printing - Weekly" + Style.RESET_ALL)
# print(data["week"])
