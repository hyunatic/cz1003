#import WTForm python library
from wtforms import Form, validators
#import html number input field
from wtforms.fields.html5 import IntegerField

class QueueSystem(Form):
    #Create input tag in HTML with built-in Error Handling
    #User must type 1 or More
    #User must input something
    #User can only type in whole numbers
    queuenumber = IntegerField('Queue' , [validators.NumberRange(min=1), validators.Required()])