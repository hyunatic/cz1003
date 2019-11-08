#Import Date function for query
from datetime import date, timedelta, datetime

#Created by Iskandar
def GetCurrentTime():
    #Create today's time in this format (2040)
    currenttime = datetime.now().strftime("%H%M")
    #Pass this value to app.py
    return currenttime

def GetDay():
    #Create today's date in this format (Saturday, 2019-09-10)
    today = date.today().strftime("%A, %Y-%m-%d")
    #Pass this value to app.py
    return today


def GetDayOnly():
    #Create today's date in this format (Saturday)
    day = date.today().strftime("%A")
    #Pass this value to app.py
    return day

#This function is not used in the project
def GetWeek():
    #Create today's date in this format (2019-09-10)
    d1 = date.today().strftime("%Y-%m-%d")
    dates = [d1]
    for i in range(1, 7):
        dates.append(d1 + timedelta(days=i))
    #Pass this value to app.py
    return dates


def GetTimeRange():
    #Initalize Tuple
    time = [
        ('730-830', '730-830'),
        ('830-930', '830-930'),
        ('930-1030', '930-1030'),
        ('1030-1130', '1030-1130'),
        ('1130-1230', '1130-1230'),
        ('1230-1330', '1230-1330'),
        ('1330-1430', '1330-1430'),
        ('1430-1530', '1430-1530'),
        ('1530-1630', '1530-1630'),
        ('1630-1730', '1630-1730')
    ]
    #pass this value to app.py
    return time
    