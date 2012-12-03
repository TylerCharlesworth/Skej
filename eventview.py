# python libs
import random, string
# gae libs
import webapp2
from google.appengine.ext import db
# project libs
from model import *
from common import Vars, RequestHandler

class MainPage(RequestHandler):
	def get(self, event_id):
		tvals = self.tvals
		tvals['top'] = 'Hello, event '+event_id+'!'
		
		# look for event in db
		event = Event.all().filter('eventid =', event_id).get()

		if event:
			tvals['content'] = '<pre><b>Event:</b> ' + event.eventid + '\n<b>Admin:</b> ' + event.admin + '\n<b>Title:</b> ' + event.title + '\n<b>Desc:</b> ' + event.description + '</pre>'
			tvals['title'] = event.title
		else:
			tvals['content'] = 'Event ' + event_id + ' is invalid.'
			tvals['title'] = 'Event Not Found'
	
		# template render
		self.render('view.html')
