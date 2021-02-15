# How to print current datetime in Python

Desired Output:

Current Date and Time
2021-02-15 15:09:35.387310

Solution Code - 

from datetime import datetime           # importing datetime module from
print("Current Date and Time")
print(datetime.now())                   # This line will print datetime like - 2021-02-15 15:09:35.387310
print(datetime.date(datetime.now()))    # This line will print datetime like - 2021-02-15 (Only date as we are calling only date from datetime)
print(datetime.time(datetime.now()))
