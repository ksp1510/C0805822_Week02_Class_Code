import time

current_time = time.asctime().split(" ")

def currentDay():
    week = {'Sun':'Sunday','Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday',
            'Thu':'Thursday','Fri':'Friday','Sat':'Saturday'}
    return f"\nToday is: {week.get(current_time[0])}"

def currentDate():
    return f"\nToday's date is: {current_time[2]}/{current_time[1]}/{current_time[4]}"

def currentTime():
    return f"\nCurrent time is: {current_time[3]}"
