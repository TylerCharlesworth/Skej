# python libs
import random, string
# gae libs
import webapp2
# project libs
from model import *

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello, create event page!')
		self.response.write("""\
<div style="border:1px dotted black; width: 300px;">
<center><b>Create An Event</b></center>
<form action="/create" method="post">
<br />Creator ID: <input type="text" name="admin_id" />
<br />Event ID: <input type="text" name="id" />
<br />Event Title: <input type="text" name="title" />
<br />Description: <textarea name="description"></textarea>
<br /><center><input type="submit" value="Create" /></center>
</form>
</div>
""")
		# nav
		self.response.write('<br /><a href="/">/</a>')
		self.response.write('<br /><a href="/home">/home</a>')
		self.response.write('<br /><a href="/create">/create</a>')
		random_event_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10))
		self.response.write('<br /><a href="/e/'+random_event_id+'">/e/'+random_event_id+'</a>')

	def post(self):
	    event = Event()
	    event.admin = self.request.get('admin_id')
	    event.eventid = self.request.get('id')
	    event.title = self.request.get('title')
	    event.description = self.request.get('description')
	    event.put()
	    self.redirect('/e/')