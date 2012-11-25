# python libs
import random, string
# gae libs
import webapp2
# project libs
import eventcreate
import eventview

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello, world 1!')
		#nav
		self.response.write('<br /><a href="/">/</a>')
		self.response.write('<br /><a href="/home">/home</a>')
		self.response.write('<br /><a href="/create">/create</a>')
		random_event_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10))
		self.response.write('<br /><a href="/e/'+random_event_id+'">/e/'+random_event_id+'</a>')

app = webapp2.WSGIApplication([
	webapp2.Route(r'/home', MainPage),
	webapp2.Route(r'/create', eventcreate.MainPage),
	webapp2.Route(r'/e/<event_id>', eventview.MainPage),
	webapp2.Route(r'/', webapp2.RedirectHandler, defaults={'_uri':'home'}),
], debug=True)