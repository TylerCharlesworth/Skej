import webapp2
import random, string

class MainPage(webapp2.RequestHandler):
	def get(self, event_id):
		self.response.write('Hello, event '+event_id+'!')
		self.response.write('<br /><a href="/">/</a>')
		self.response.write('<br /><a href="/home">/home</a>')
		random_event_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10))
		self.response.write('<br /><a href="/e/'+random_event_id+'">/e/'+random_event_id+'</a>')