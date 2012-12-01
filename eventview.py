# python libs
import random, string
import pprint
# gae libs
import webapp2
from google.appengine.ext import db
# project libs
from model import *

class MainPage(webapp2.RequestHandler):
	def get(self, event_id):
		self.response.write('Hello, event '+event_id+'!')
		
		# look for event in db
		event = Event.all().filter('eventid =', event_id).get()

		if event:
			self.response.write('<br /><pre><b>Event:</b> ' + event.eventid + '\n<b>Admin:</b> ' + event.admin + '\n<b>Title:</b> ' + event.title + '\n<b>Desc:</b> ' + event.description + '</pre>')
		else:
			self.response.write('<br />Event ' + event_id + ' is invalid.')
		# nav
		self.response.write('<br /><a href="/">/</a>')
		self.response.write('<br /><a href="/home">/home</a>')
		self.response.write('<br /><a href="/create">/create</a>')
		random_event_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10))
		self.response.write('<br /><a href="/e/'+random_event_id+'">/e/'+random_event_id+'</a>')