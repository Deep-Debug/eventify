from application.resources.event_handler import EventEndpoint, EventsEndpoint
from application.resources.authentication import Authentication
from application.resources.organizer_handler import OrganizerEndPoint, OrganizersEndpoint, UnauthenticateOrganizerEndPoint
from application.resources.registerEvent_handler import AddRegisterEvents
from application.resources.payment_handler import AddPayment
from application.resources.registerEvent_handler import DeleteRegisteredEvents

from application.resources.authentication_handler import RegistrationEndpoint, LoginEndpoint
from application.resources.organizer_handler import OrganizerEndPoint, OrganizersEndpoint
from application.resources.subscriber_handler import SubscrtiberEndpoint

def initialize_routes(api):
    api.add_resource(EventsEndpoint, '/events')
    api.add_resource(EventEndpoint, '/event/<id>', '/event')
    api.add_resource(Authentication, '/auth')
    api.add_resource(RegistrationEndpoint, '/registration')
    api.add_resource(LoginEndpoint, '/login')
    api.add_resource(OrganizersEndpoint,'/organizers')
    api.add_resource(OrganizerEndPoint,'/organizer','/organizer/<id>','/authenticate/<id>')
    api.add_resource(UnauthenticateOrganizerEndPoint,'/unauthOrganizers')
    api.add_resource(AddRegisterEvents, '/registerEvent', '/registerEvent/<id>')
    api.add_resource(AddPayment, '/addPayment', '/getPayments/<id>')
    api.add_resource(DeleteRegisteredEvents, '/deleteEvent/<id>')
    api.add_resource(SubscrtiberEndpoint,'/subscribe')
