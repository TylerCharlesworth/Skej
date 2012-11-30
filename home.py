# python libs
import random, string, os, pprint
# gae libs
import webapp2, jinja2
# third party libs
from libs import facebook
# project libs
import eventcreate, eventview

# constants
FACEBOOK_APP_ID = "496743440358938"
FACEBOOK_APP_SECRET = "490fa8b35557153faba84c2eb37d0d0c"
TEMPLATES_DIR = 'templates'

# global vars
jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), TEMPLATES_DIR)))

# render home
class MainPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')

		top_msg = 'Hello, world 4!'

		# facebook
		user = facebook.get_user_from_cookie(self.request.cookies, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
		if user:
			fb_logged = True
			graph = facebook.GraphAPI(user["access_token"])
			profile = graph.get_object("me")
			# friends = graph.get_connections("me", "friends")
			user_msg = '<a href="' + profile["link"] + '"><img src="//graph.facebook.com/' + user["uid"] + '/picture?type=square" border="0" /> ' + profile["name"] + '</a>'
			user_msg += "\nuser = " + pprint.pformat(user)
			user_msg += '\nprofile = ' + pprint.pformat(profile)
		else:
			fb_logged = False
			user_msg = ''
		
		# template render
		template_values = {
			'FACEBOOK_APP_ID': FACEBOOK_APP_ID,
			'DOMAIN': 'http://localhost:8080',
			'random_event_id': ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(10)),
			'top_msg': top_msg,
			'fb_logged': fb_logged,
			'user_msg': user_msg,
		}
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	webapp2.Route(r'/home', MainPage),
	webapp2.Route(r'/create', eventcreate.MainPage),
	webapp2.Route(r'/e/<event_id>', eventview.MainPage),
	webapp2.Route(r'/', webapp2.RedirectHandler, defaults={'_uri':'home'}),
], debug=True)