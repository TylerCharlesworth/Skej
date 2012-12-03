# python libs
import os, jinja2
# gae libs
import webapp2
# third party libs
from libs import facebook

class Vars:
	DOMAIN = "skej.tyworks.net"
	FACEBOOK_APP_ID = "496743440358938"
	FACEBOOK_APP_SECRET = "490fa8b35557153faba84c2eb37d0d0c"
	TESTING = os.environ['SERVER_SOFTWARE'].startswith('Dev')

class RequestHandler(webapp2.RequestHandler):
	tvals = {
		'FACEBOOK_APP_ID': Vars.FACEBOOK_APP_ID,
		'DOMAIN': Vars.DOMAIN,
	}
	graph = None
	profile = None

	def __init__(self, request, response):
		self.initialize(request, response)
		# facebook
		user = facebook.get_user_from_cookie(self.request.cookies, Vars.FACEBOOK_APP_ID, Vars.FACEBOOK_APP_SECRET)
		if user:
			self.graph = facebook.GraphAPI(user["access_token"])
			self.profile = self.graph.get_object("me")
			self.tvals['profile'] = self.profile
		# friends = graph.get_connections("me", "friends")

	def render(self, tname):
		TEMPLATES_DIR = 'templates'
		jinja_env = jinja2.Environment(
			loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), TEMPLATES_DIR)))
		template = jinja_env.get_template(tname)
		self.response.write(template.render(self.tvals))
