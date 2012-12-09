# project libs
import common
from model import *

class MainPage(common.RequestHandler):
	def get(self):
		tvals = self.tvals
		
		events = Event.getByUserId(self.users.current)

		tvals['events'] = events

		self.render('me.html')  # template render