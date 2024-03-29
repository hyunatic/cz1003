#Import Datetime for Stall Query
from datetime import date, timedelta, datetime
import json

#Created by Amadeus
#Load Stall Data from JSON File
#File path is viewed from './app.py' Flask App directory
with open('model/stall.json') as data:
  stall = json.load(data)


def GetAllStall():
    #Return the Stall list to app.py (Flask App)
    return stall


def QueryStallByTimeSlot(timeslot, selecteddate):
    #Get the selected timeslot and split them into [730,930]
    timeslot = timeslot.split('-')
    #Create Empty Aray 
    filteredstall = []
    #Format date into 2019-11-10
    selecteddate = datetime.strptime(str(selecteddate), "%Y-%m-%d")
    #Format date to get the day like: Monday, Tuesday, Wednesday
    selecteddate = datetime.strftime(selecteddate, "%A")

    for i in range(len(stall)):
        #Check if the selected time is in the Opening hour range
        if(stall[i]['OpeningTime'] <= int(timeslot[0]) and stall[i]['ClosingTime'] >= int(timeslot[1])):
            days = stall[i]['Closed'].split(',')
            #Check if the day is not in the weekends, where all the stores are closed
            if(selecteddate != days[0] and selecteddate != days[1]):
                filteredstall.append(stall[i])
    #Return the filter stall list to app.py (Flask App)
    return filteredstall
