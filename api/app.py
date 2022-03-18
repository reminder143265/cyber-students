from concurrent.futures import ThreadPoolExecutor
from motor import MotorClient
from tornado.web import Application

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS

from .handlers.welcome import WelcomeHandler
from .handlers.registration import RegistrationHandler
from .handlers.login import LoginHandler
from .handlers.logout import LogoutHandler
from .handlers.user import UserHandler

class Application(Application):

    def __init__(self):
        handlers = [
            (r'/cyber/?', WelcomeHandler),
            (r'/cyber/api/?', WelcomeHandler),
            (r'/cyber/api/registration', RegistrationHandler),
            (r'/cyber/api/login', LoginHandler),
            (r'/cyber/api/logout', LogoutHandler),
            (r'/cyber/api/user', UserHandler)
        ]

        settings = dict()

        super(Application, self).__init__(handlers, **settings)

        self.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.executor = ThreadPoolExecutor(WORKERS)

