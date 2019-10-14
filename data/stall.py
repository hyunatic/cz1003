#Import Datetime for Stall Query
from datetime import date, timedelta, datetime
import json

#Load Stall Data from JSON File
with open('data/stall.json') as data:
  stall = json.load(data)


def GetAllStall():
    #Return the Stall list to app.py (Flask App)
    return stall


def QueryStallByTimeSlot(timeslot, selecteddate):
    timeslot = timeslot.split('-')
    filteredstall = []
    selecteddate = datetime.strptime(str(selecteddate), "%Y-%m-%d")
    selecteddate = datetime.strftime(selecteddate, "%A")

    for i in range(len(stall)):
        if(stall[i]['OpeningTime'] <= int(timeslot[0]) and stall[i]['ClosingTime'] >= int(timeslot[1])):
            days = stall[i]['Closed'].split(',')
            if(selecteddate != days[0] and selecteddate != days[1]):
                filteredstall.append(stall[i])
    #Return the filter stall list to app.py (Flask App)
    return filteredstall
