from google.appengine.ext import db

class Event(db.Model):
	eventid = db.StringProperty()
	admin = db.StringProperty()
	title = db.StringProperty()
	description = db.StringProperty(multiline=True)
	createdate = db.DateTimeProperty(auto_now_add=True)
