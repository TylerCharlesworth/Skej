# gae libs
import webapp2
# project libs
import home, me, create, view

app = webapp2.WSGIApplication([
	webapp2.Route(r'/home', home.MainPage),
	webapp2.Route(r'/me', me.MainPage),
	webapp2.Route(r'/create', create.MainPage),
	webapp2.Route(r'/e/<event_id>', view.MainPage),
	webapp2.Route(r'/', webapp2.RedirectHandler, defaults={'_uri':'home'}),
], debug=True)
