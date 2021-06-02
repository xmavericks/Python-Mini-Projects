# How to print current datetime in Python
Desired Output:
Current Date and Time
2021-02-15 15:13:58.592418

Solution Code - 

from datetime import datetime           # importing datetime module from
print("Current Date and Time")
print(datetime.now())                   # This line will print datetime like - 2021-02-15 15:13:58.592418
print(datetime.date(datetime.now()))    # This line will print date only like - 2021-02-15 (as we are calling only date from datetime)
print(datetime.time(datetime.now()))    # This line will print time only like - 15:13:58.592487 (as we are calling only time from datetime)

# EOF reached
