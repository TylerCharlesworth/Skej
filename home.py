import webapp2
import random, string
import event

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello, world!')
		self.response.write('<br /><a href="/">/</a>')
		self.response.write('<br /><a href="/home">/home</a>')
		random_event_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10))
		self.response.write('<br /><a href="/e/'+random_event_id+'">/e/'+random_event_id+'</a>')

app = webapp2.WSGIApplication([
	webapp2.Route(r'/home', MainPage),
	webapp2.Route(r'/e/<event_id>', event.MainPage),
	webapp2.Route(r'/', webapp2.RedirectHandler, defaults={'_uri':'home'}),
], debug=True)