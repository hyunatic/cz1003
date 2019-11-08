#import WTForm python library
from wtforms import Form, SelectField, validators
#import html date input field
from wtforms.fields.html5 import DateField
#Get Time Related Functions and Store filtering based on data and time
from function.time import GetTimeRange

#Call GetTimeRange function located in data/time.py
#Created by Amadeus
TimeSlot = GetTimeRange()

class SearchStallByDate(Form):
    #Create input tag in HTML with built-in Error Handling

    #User must input something
    #User can only type in date
    date = DateField('date', [validators.DataRequired()], format='%Y-%m-%d')
    #Creates are dropdown list
    #Insert Hourly Time Tuple in the selection
    timeslot = SelectField('Timeslot', [validators.DataRequired()], choices=TimeSlot)