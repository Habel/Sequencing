from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty(required = True)
    pw   = db.StringProperty(required = True)
    privilege = db.IntegerProperty(default=0)
