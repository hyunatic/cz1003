import json

#Load Menu Data from JSON File
#File path is viewed from './app.py' Flask App directory
with open('model/menu.json') as data:
  menuItem = json.load(data)

def MenuItems():
    #Return the menu item list to app.py (Flask App)
    return menuItem
