# python libs
import random, string
# gae libs
import webapp2
# third party libs
from libs import facebook
# project libs
from model import *
from common import Common

class MainPage(webapp2.RequestHandler):
	def get(self):
		tvals = {
			'FACEBOOK_APP_ID': Common.FACEBOOK_APP_ID,
			'DOMAIN': Common.DOMAIN,
		}

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
		template = Common.JINJA.get_template('create.html')
		self.response.write(template.render(tvals))

	def post(self):
		user = None
		if Common.TESTING:
			user = { 'uid': "TESTER", }
		else:
			user = facebook.get_user_from_cookie(self.request.cookies, Common.FACEBOOK_APP_ID, Common.FACEBOOK_APP_SECRET)
		if user: 
		    event = Event(
		    	admin = user["uid"],
		    	eventid = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10)),
		    	title = self.request.get('title'),
		    	description = self.request.get('description')
		    	)
		    event.put()
		    self.redirect('/e/' + event.eventid)
		else:
			self.redirect('/home?error')
			