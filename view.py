# project libs
import common
from model import *

class MainPage(common.RequestHandler):
	def get(self, event_id):
		tvals = self.tvals
		
		event = Event.getById(event_id)

		if event:
			tvals['eventid'] = event.eventid
			tvals['admin'] = event.admin
			tvals['etitle'] = tvals['title'] = event.title
			tvals['description'] = event.description
			tvals['maxattendees'] = event.maxattendees
			tvals['attendees'] = event.attendees
		else:
			tvals['eventid'] = event_id
			tvals['title'] = 'Event Not Found'

		self.render('view.html')  # template render

	def post(self, event_id):
		if(self.request.get('attend')):
			event = Event.getById(event_id)
			userid = int(self.users.current)
			if(userid not in event.attendees):
				if(event.maxattendees == len(event.attendees)):
					self.redirect('e/' + event_id + '?max')
					return
				event.attendees.append(userid)
				event.put()
		if(self.request.get('unattend')):
			event = Event.getById(event_id)
			userid = int(self.users.current)
			if(userid in event.attendees):
				event.attendees.remove(userid)
				event.put()
		self.redirect('/e/' + event_id)
