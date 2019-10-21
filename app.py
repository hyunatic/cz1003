#Import Python Web Framework (Flask)
from flask import Flask, render_template, request, flash
#Get Stall Data stored in function/stall.py
from function.stall import GetAllStall, QueryStallByTimeSlot
#Get Menu Items stored in function/menuitems.py
from function.menuitems import StallMenu
#Get Time Related Functions and Store filtering based on data and time
from function.time import GetDay, GetDayOnly, GetTimeRange, GetCurrentTime
#Get Stripe Public Key Used for Credit Card Payment
from function.stripe import GetStripeKey
#Import Stall search function as a class function using HTML WTForms Python Framework
from form.SearchStallByDate import SearchStallByDate
#Import Waiting List function as a class function using HTML WTForms Python Framework
from form.QueueSystem import QueueSystem
#Import chatbot function
from function.chatbot import ChatBotReply

#Initialize Flask App
app = Flask(__name__)

#Calling GetAllStall function in data/stall.py
Stall = GetAllStall()
#Calling GetDay function in data/time.py (2019-09-10)
GetDay = GetDay()
#Calling GetDayOnly function in data/time.py (Wednesday)
DayOnly = GetDayOnly()
#Get Stripe Key used for credit card payment [This is test mode only]
key = GetStripeKey()

#Whenever user access our website link: https://cz1003.herokuapp.com/
@app.route("/")
def HomePage():
    #It will give users home.html page
    return render_template('home.html')

#Whenever user access our website link: https://cz1003.herokuapp.com/stall
#GET Request happens when you just load the page normally
#POST request happens when you send additional data to this page.
#For Example: When user search stall function
@app.route("/stall", methods=['GET', 'POST'])
def StallPage():
    form = SearchStallByDate(request.form)
    stalltab = "active"
    searchtab = ""
    if request.method == 'POST' and form.validate():
        timeslot = dict(form.timeslot.choices).get(form.timeslot.data)
        date = form.date.data
        filteredstall = QueryStallByTimeSlot(timeslot, date)
        stalltab = ""
        searchtab = "active"
        #It will give user stall.html after the user has used the search function
        #The Additional Parameters is to pass data [Stall, Menu] into the HTML page as propeties
        return render_template('stall.html', stall = Stall, today = GetDay, form=form, filteredstall=filteredstall, stalltab=stalltab, searchtab=searchtab)
    elif request.method == 'GET':
        #It will give users stall.html page by default
        #The Additional Parameters is to pass data [Stall, Menu] into the HTML page as propeties
        return render_template('stall.html', stall = Stall, today = GetDay, form=form, stalltab=stalltab, searchtab=searchtab)

#Whenever user access our website link: https://cz1003.herokuapp.com/menu/1
#GET Request happens when you just load the page normally with parameters
#POST request happens when you send additional data to this page.
#For Example: When user use the waiting list function
@app.route("/menu/<string:id>", methods=['GET','POST'])
def MenuPage(id):
    queuenumber = 0
    form = QueueSystem(request.form)
    
    #Get Current time
    currenttime = int(GetCurrentTime())
    #Get the filtered stalls based on their ID
    MenuItems = StallMenu(id)

    #Get the filtered stall based on their ID that are unavailable

    if request.method == 'POST' and form.validate():
        queuenumber = form.queuenumber.data
        queuenumber = int(queuenumber) * 2
        #It will give user menu.html after the user has used the waiting list function
        #The Additional Parameters is to pass data [Stall, Menu] into the HTML page as propeties
        return render_template('menu.html',id=id, stall = Stall, menu = MenuItems, today = GetDay, day = DayOnly, key=key, form=form, queuenumber=queuenumber, currenttime=currenttime)
    else:
        #It will give users menu.html page by default
        #The Additional Parameters is to pass data [Stall, Menu] into the HTML page as propeties
        return render_template('menu.html',id=id, stall = Stall, menu = MenuItems, today = GetDay, day = DayOnly, key=key, form=form, queuenumber=queuenumber, currenttime=currenttime)

#Whenever user access our website link: https://cz1003.herokuapp.com/thanks
#GET Request happens when you just load the page normally with parameters
#POST request happens when you send additional data to this page.
#For Example: Whenever successfully paid for the food [No money was used in the project]
@app.route("/thanks", methods=['GET','POST'])
def Thanks():
    return render_template('thanks.html')

#Returns a reply for chatbot
@app.route("/chatbot", methods=['GET'])
def ChatBot():
    userText = request.args.get('msg')
    reply = ChatBotReply(userText)
    #Display Output to HTML at StallPage
    return reply

@app.errorhandler(404) 
def not_found(e):
    #inbuilt function which takes error as parameter 
    #It will give users 404.html page by default
    #This is handle user types in any random link in our website like https://cz1003.herokuapp.com/haha or etc...
    return render_template("404.html")  

if __name__ == "__main__":
    #Run Flask Web Application
    app.run(debug=True)
