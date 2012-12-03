# python libs
import random, string
# project libs
from model import *
from common import Vars, RequestHandler

class MainPage(RequestHandler):
	def get(self):
		tvals = self.tvals
		tvals['top'] = 'Hello, create event page!'

		tvals['content'] = """\
<div style="border:1px dotted black; width: 300px;">
<center><b>Create An Event</b></center>
<form action="/create" method="post">
<br />Event Title: <input type="text" name="title" />
<br />Description: <textarea name="description"></textarea>
<br /><center><input type="submit" value="Create" /></center>
</form>
</div>
"""

		# template render
		self.render('create.html')

	def post(self):
		if Vars.TESTING:
			self.profile = { 'id': "TESTER", }
		if self.profile: 
		    event = Event(
		    	admin = self.profile["id"],
		    	eventid = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10)),
		    	title = self.request.get('title'),
		    	description = self.request.get('description')
		    	)
		    event.put()
		    self.redirect('/e/' + event.eventid)
		else:
			self.redirect('/home?error')
			