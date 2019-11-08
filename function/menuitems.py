#Import Java Script Object Notation (JSON) module
import json
from function.time import GetCurrentTime, GetDayOnly

#Created by Iskandar
#Load Menu Data from JSON File
#File path is viewed from './app.py' Flask App directory
with open('model/menu.json') as data:
  menuItem = json.load(data)

def MenuItems():
    #Return the full menu item list to app.py (Flask App)
    return menuItem

def StallMenu(stallid):
  #Create and empty list
  filteredMenuItem = []
  for i in range(0,len(menuItem)):
    #Compare the StallID and append to the array
    if stallid == menuItem[i]["StallID"]:
      filteredMenuItem.append(menuItem[i])
  #Returns the filtered menu list of current stall
  return filteredMenuItem
 
def SpecialMenu(stallid):
  #Get Current StallID Menu as a list
  filteredMenuItems = StallMenu(stallid)
  #Generate empty list to a unique store special menu items based on current time
  specialMenuItems = []
  #Get Current Time
  currenttime = int(GetCurrentTime())
  #Get Current Day [Monday, Tuesday ....]
  day = GetDayOnly()
  for i in range(0,len(filteredMenuItems)):
      #Check For Unavailable Day is not today
      if(day != filteredMenuItems[i]["Unavailable"]):
        #Check if this item is in the special menu
        if (filteredMenuItems[i]["SpecialMenuStartTime"] != 0 or filteredMenuItems[i]["SpecialMenuEndTime"] != 0):
          #Check For Current Time not within stall special menu time slot
          if not(filteredMenuItems[i]["SpecialMenuStartTime"] < currenttime < filteredMenuItems[i]["SpecialMenuEndTime"]):
            specialMenuItems.append(filteredMenuItems[i])
  #Returns the filtered special menu list
  return specialMenuItems    

def UnavailableDayMenu(stallid):
  #Get Current StallID Menu as a list
  filteredMenuItems = StallMenu(stallid)
  #Generate empty list to a unique store special menu items based on current time
  UnavailableItems = []
  #Get Current Day [Monday, Tuesday ....]
  day = GetDayOnly()
  for i in range(0,len(filteredMenuItems)):
    #check for Unavailable day is today
    if(day == filteredMenuItems[i]["Unavailable"]):
      UnavailableItems.append(filteredMenuItems[i])
  return UnavailableItems

def AvailableMenu(stallid):
   #Get Current StallID Menu as a list
  filteredMenuItems = StallMenu(stallid)
  #Generate empty list to a unique store special menu items based on current time
  AvailableItems = []
  #Get Current Time
  currenttime = int(GetCurrentTime())
  #Get Current Day [Monday, Tuesday ....]
  day = GetDayOnly()
  for i in range(0,len(filteredMenuItems)):
    #Check For Unavailable Day is not today
    if(day != filteredMenuItems[i]["Unavailable"]):
      #Check if this item is in the normal menu
      if (filteredMenuItems[i]["SpecialMenuStartTime"] == 0 or filteredMenuItems[i]["SpecialMenuEndTime"] == 0):
        AvailableItems.append(filteredMenuItems[i])
        #Check For Current Time within stall special menu time slot
      if filteredMenuItems[i]["SpecialMenuStartTime"] < currenttime < filteredMenuItems[i]["SpecialMenuEndTime"]:
        AvailableItems.append(filteredMenuItems[i])
  return AvailableItems