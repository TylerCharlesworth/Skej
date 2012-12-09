# python libs
import random, string
# project libs
from model import *
import common

class MainPage(common.RequestHandler):
	def get(self):
		self.render('create.html')  # template render

	def post(self):
		if self.users.current: 
		    event = Event(
		    	admin = int(self.users.current),
		    	eventid = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10)),
		    	title = self.request.get('title'),
		    	description = self.request.get('description'),
		    	maxattendees = int(self.request.get('maxattendees')),
		    	)
		    event.put()
		    self.redirect('/e/' + event.eventid)
		else:
			self.redirect('/home?error')
			