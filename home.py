# project libs
import common

class MainPage(common.RequestHandler):
	def get(self):
		tvals = self.tvals
		tvals['top'] = 'Hello, world!'

		if self.users and self.users.current:
			# tvals['content'] = '<a href="' + self.profile["link"] + '"><img src="//graph.facebook.com/' + self.profile["id"] + '/picture?type=square" border="0" /> ' + self.profile["name"] + '</a>'
			# tvals['content'] += '\nprofile = ' + pprint.pformat(self.profile)
			tvals['content'] = 'logged in'
		else:
			tvals['content'] = 'not logged in'
		
		# template render
		self.render("home.html")
