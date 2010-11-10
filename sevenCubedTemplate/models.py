import cgi
import os
import datetime


from google.appengine.ext import db
from google.appengine.api import users

class User(db.Model):
    goog_user = db.UserProperty()
    firstName = db.StringProperty()
    lastName = db.StringProperty()
   
    
