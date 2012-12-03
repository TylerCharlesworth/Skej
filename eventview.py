# python libs
import random, string
# gae libs
import webapp2
from google.appengine.ext import db
# project libs
from model import *
from common import Common

class MainPage(webapp2.RequestHandler):
	def get(self, event_id):
		tvals = {
			'FACEBOOK_APP_ID': Common.FACEBOOK_APP_ID,
			'DOMAIN': Common.DOMAIN,
		}

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
		template = Common.JINJA.get_template('view.html')
		self.response.write(template.render(tvals))
