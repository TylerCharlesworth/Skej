# python libs
import os, jinja2
# gae libs
import webapp2
# project libs
from model import *

class RequestHandler(webapp2.RequestHandler):
	tvals = {
		'FACEBOOK_APP_ID': Vars.FACEBOOK_APP_ID,
		'DOMAIN': Vars.DOMAIN,
	}
	users = None

	def __init__(self, request, response):
		self.initialize(request, response)  # req'd by superclass
		self.users = users(self.request.cookies)  # facebook

	def render(self, tname):
		self.tvals['currentuser'] = self.users.current
		self.tvals['users'] = self.users.resolveUsers()
		jinja_env = jinja2.Environment(
			loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), Vars.TEMPLATES_DIR)))
		template = jinja_env.get_template(tname)
		self.response.write(template.render(self.tvals))
