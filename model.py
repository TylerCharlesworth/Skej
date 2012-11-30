from google.appengine.ext import db

class Event(db.Model):
	eventid = db.StringProperty()
	admin = db.StringProperty()
	title = db.StringProperty()
	description = db.StringProperty(multiline=True)
	createdate = db.DateTimeProperty(auto_now_add=True)

class User(db.Model):
	id = db.StringProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	updated = db.DateTimeProperty(auto_now=True)
	name = db.StringProperty(required=True)
	profile_url = db.StringProperty(required=True)
	access_token = db.StringProperty(required=True)
