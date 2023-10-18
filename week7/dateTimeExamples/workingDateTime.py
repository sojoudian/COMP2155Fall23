"""import datetime

today = datetime.datetime.now()
print(today)"""

from datetime import *
today = datetime.now()
print(datetime.now())

yeaar = today.year
month = today.month
day = today.day
print(f"{yeaar}-{month}-{day}")
print(f"{yeaar}/{month}/{day}")