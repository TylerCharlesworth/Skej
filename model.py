# python libs
import os
# gae libs
from google.appengine.ext import db
# third party libs
from libs import facebook

class Vars:
	DOMAIN = "skej.tyworks.net"
	TEMPLATES_DIR = 'templates'
	FACEBOOK_APP_ID = "496743440358938"
	FACEBOOK_APP_SECRET = "490fa8b35557153faba84c2eb37d0d0c"
	TESTING = os.environ['SERVER_SOFTWARE'].startswith('Dev')
	DEFAULTFIELDS = ['id','name','gender','link','picture']

class Event(db.Model):
	eventid = db.StringProperty(required=True)
	admin = db.IntegerProperty(required=True)
	title = db.StringProperty()
	description = db.StringProperty(multiline=True)
	createdate = db.DateTimeProperty(auto_now_add=True)
	attendees = db.ListProperty(int)
	maxattendees = db.IntegerProperty()

	@staticmethod
	def getById(id):
		return Event.all().filter('eventid =', id).get()

	@staticmethod
	def getByUserId(id):
		events = Event.all().filter('attendees =', id).fetch(200)
		events_ids = set()
		for event in events:
			events_ids.add(event.eventid)

		aevents = Event.all().filter('admin =', id).fetch(200)
		for event in aevents:
			if event.eventid not in events_ids:
				events.append(event)
				events_ids.add(event.eventid)

		return events

class users():
	ids = None
	graph = None
	current = None
	users = None

	def __init__(self,cookies):
		self.ids = set()
		user = facebook.get_user_from_cookie(cookies, Vars.FACEBOOK_APP_ID, Vars.FACEBOOK_APP_SECRET)
		if user:
			self.loggedIn = True
			# self.currentToken = user["access_token"]
			self.graph = facebook.GraphAPI(user["access_token"])
			self.current = int(user['uid'])
			self.addId(user['uid'])
			# self.profile = self.graph.get_object("me")
			# friends = graph.get_connections("me", "friends")
		else:
			self.graph = facebook.GraphAPI()
		if Vars.TESTING:
			self.current = 11111

	def addId(self,id):
		self.ids.add(id)

	def resolveUsers(self):
		if not self.users:
			if len(self.ids):
				self.users = self.graph.get_objects(self.ids, Vars.DEFAULTFIELDS)
		return self.users
		# TODO: if users object doesn't have all ids, query for newly added ids