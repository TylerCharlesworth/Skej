# python libs
import pprint
# gae libs
import webapp2
# third party libs
from libs import facebook
# project libs
from common import Common

class MainPage(webapp2.RequestHandler):
	def get(self):
		tvals = {
			'FACEBOOK_APP_ID': Common.FACEBOOK_APP_ID,
			'DOMAIN': Common.DOMAIN,
		}

		tvals['top'] = 'Hello, world!'

		# facebook
		user = facebook.get_user_from_cookie(self.request.cookies, Common.FACEBOOK_APP_ID, Common.FACEBOOK_APP_SECRET)
		if user:
			tvals['loggedin'] = True
			graph = facebook.GraphAPI(user["access_token"])
			profile = graph.get_object("me")
			# friends = graph.get_connections("me", "friends")
			tvals['content'] = '<a href="' + profile["link"] + '"><img src="//graph.facebook.com/' + user["uid"] + '/picture?type=square" border="0" /> ' + profile["name"] + '</a>'
			tvals['content'] += "\nuser = " + pprint.pformat(user)
			tvals['content'] += '\nprofile = ' + pprint.pformat(profile)
		else:
			tvals['loggedin'] = False
			tvals['content'] = ''
		
		# template render
		template = Common.JINJA.get_template('home.html')
		self.response.write(template.render(tvals))
