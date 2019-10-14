import json

#Load Menu Data from JSON File
with open('data/menu.json') as f:
  menuItem = json.load(f)

def MenuItems():
    #Return the menu item list to app.py (Flask App)
    return menuItem
