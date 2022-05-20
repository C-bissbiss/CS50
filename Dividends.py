import pandas_datareader.data as web
import pandas as pd
import datetime as dt
from datetime import datetime

today = datetime.now()
end=datetime.today()
start=today.replace(year=today.year-1)
dividends = web.DataReader('IBM', 'yahoo-dividends', start, end)
dividends.head()
mean=dividends['value'].mean()
print(mean)