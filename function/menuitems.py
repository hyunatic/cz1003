import json

#Load Menu Data from JSON File
#File path is viewed from './app.py' Flask App directory
with open('model/menu.json') as data:
  menuItem = json.load(data)

def MenuItems():
    #Return the full menu item list to app.py (Flask App)
    return menuItem

def StallMenu(stallid):
  #Create and empty list
  filteredMenuItem = [];
  for i in range(0,len(menuItem)):
    #Compare the StallID and append to the array
    if stallid == menuItem[i]["StallID"]:
      filteredMenuItem.append(menuItem[i])
  #Returns the filtered menu list
  return filteredMenuItem
 
def UnavailableMenu(stallid):
    #Get Current StallID Menu as a list
  filteredMenuItem = StallMenu(stallid)
  for i in range(0,len(filteredMenuItem)):
      if MenuItem.SpecialMenuStartTime > currenttime or MenuItem.SpecialMenuEndTime < currenttime
    
          

