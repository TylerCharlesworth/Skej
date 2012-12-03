# python libs
import pprint
# project libs
from common import Vars, RequestHandler

class MainPage(RequestHandler):
	def get(self):
		tvals = self.tvals
		tvals['top'] = 'Hello, world!'

		if self.profile:
			tvals['content'] = '<a href="' + self.profile["link"] + '"><img src="//graph.facebook.com/' + self.profile["id"] + '/picture?type=square" border="0" /> ' + self.profile["name"] + '</a>'
			tvals['content'] += '\nprofile = ' + pprint.pformat(self.profile)
		else:
			tvals['content'] = ''
		
		# template render
		self.render("home.html")
