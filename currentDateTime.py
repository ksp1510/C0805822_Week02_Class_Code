import time

# import is used to import time library of python

current_time = time.asctime().split(" ")  # Here current time tuple is accessed using asctime()
# and is splitted and stored as list items in current_time.

# Following function returns which day is today from the current_time list
def currentDay():
    week = {'Sun': 'Sunday', 'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday',
            'Thu': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday'}
    print(f"\nToday is: {week.get(current_time[0])}")


# Following function returns which date is today from the current_time list in dd/mmm/yyyy format
def currentDate():
    print(f"Today's date is: {current_time[2]}/{current_time[1]}/{current_time[4]}")


# Following function returns current system time from the current_time list in hh:mm:ss & 24hrs format
def currentTime():
    print(f"Current time is: {current_time[3]}")
