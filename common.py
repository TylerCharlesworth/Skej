import os, jinja2

class Common:
	DOMAIN = "skej.tyworks.net"
	FACEBOOK_APP_ID = "496743440358938"
	FACEBOOK_APP_SECRET = "490fa8b35557153faba84c2eb37d0d0c"
	TESTING = os.environ['SERVER_SOFTWARE'].startswith('Dev')
	TEMPLATES_DIR = 'templates'
	JINJA = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), TEMPLATES_DIR)))
