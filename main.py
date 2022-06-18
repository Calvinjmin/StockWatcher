import pandas_datareader.data as web
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd

today = date.today()
yesterday = today - timedelta(days = 1) 
bmw = web.DataReader("BMW.DE", "yahoo", yesterday, today)

print( bmw )
