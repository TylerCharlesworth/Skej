# gae libs
import webapp2
# project libs
import home, eventcreate, eventview

app = webapp2.WSGIApplication([
	webapp2.Route(r'/home', home.MainPage),
	webapp2.Route(r'/create', eventcreate.MainPage),
	webapp2.Route(r'/e/<event_id>', eventview.MainPage),
	webapp2.Route(r'/', webapp2.RedirectHandler, defaults={'_uri':'home'}),
], debug=True)
