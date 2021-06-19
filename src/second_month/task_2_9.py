from datetime import datetime
import pandas as pd
from dateutil import parser
import numpy as np

# 1.Write a Pandas program to create
# a) Datetime object for Jan 15 2012.

dt = datetime(2012, 1, 15)
print(dt)
# b) Specific date and time of 9:20 pm. -?
# c) Local date and time.
print(datetime.now())
# d) A date without time.

dt_without_time = dt.strftime("%y-%m-%d")
print("Date without time =", dt_without_time)
# e) Current date.
now = datetime.now()
current_date = now.strftime("%y-%m-%d")
print("Current Date =", current_date)
# f) Time from a datetime-same "%H:%M:%S"
# g) Current local time.
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


# 2.Write a Pandas program to print the day after and before a specified date. Also print the days between two given dates.

today = datetime(2021, 6, 19)
print("Current date:", today)
tomorrow = today + pd.Timedelta(days=1)
print("Tomorrow:", tomorrow)
yesterday = today - pd.Timedelta(days=1)
print("Yesterday:", yesterday)
date1 = datetime(2021, 6, 19)
date2 = datetime(2020, 6, 19)
print("\nDifference between two dates: ", (date1 - date2))


# 3. Write a Pandas program to create a date from a given year, month, day and another date from a given string format.
date1 = datetime(year=2021, month=10, day=16)
print(date1)
date2 = parser.parse("16 of October, 1993")
print(date2)

# 4. Write a Pandas program to create a date range using a startpoint date and a number of periods.
date_range = pd.date_range('2021-01-01', periods=16)
print(date_range)


# 5. Write a Pandas program to create a time series using three months frequency.

time_series = pd.date_range('1/1/2021', periods=10, freq='3M')
print(time_series)

