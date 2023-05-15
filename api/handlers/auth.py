from datetime import datetime
from time import mktime
from tornado.gen import coroutine

from .base import BaseHandler

class AuthHandler(BaseHandler):

    @coroutine
    def prepare(self):
        super(AuthHandler, self).prepare()

        if self.request.method == 'OPTIONS':
            return

        try:
            token = self.request.headers.get('X-Token')
            if not token:
              raise Exception()
        except:
            self.current_user = None
            self.send_error(400, message='You must provide a token!')
            return

        user = yield self.db.users.find_one({
            'token': token
        }, {
            'email': 1,
            'display_name': 1,
            'expiresIn': 1,
        #   'password': 1,
            'name': 1,
            'address': 1,
            'dob': 1,
            'phone': 1,
            'disability': 1
        })

        if user is None:
            self.current_user = None
            self.send_error(403, message='Your token is invalid!')
            return

        current_time = mktime(datetime.now().utctimetuple())
        if current_time > user['expiresIn']:
            self.current_user = None
            self.send_error(403, message='Your token has expired!')
            return

        self.current_user = {
            'email': user['email'],
            'display_name': user['display_name'],
            'password': user['password'],
            'name': user['name'],
            'address': user['address'],
            'dob': user['dob'],
            'phone': user['phone'],
            'disability': user['disability']
        }from datetime import datetime
from time import mktime
from tornado.gen import coroutine

from .base import BaseHandler

class AuthHandler(BaseHandler):

    @coroutine
    def prepare(self):
        super(AuthHandler, self).prepare()

        if self.request.method == 'OPTIONS':
            return

        try:
            token = self.request.headers.get('X-Token')
            if not token:
              raise Exception()
        except:
            self.current_user = None
            self.send_error(400, message='You must provide a token!')
            return

        user = yield self.db.users.find_one({
            'token': token
        }, {
            'email': 1,
            'display_name': 1,
            'expiresIn': 1,
        #   'password': 1,
            'name': 1,
            'address': 1,
            'dob': 1,
            'phone': 1,
            'disability': 1
        })

        if user is None:
            self.current_user = None
            self.send_error(403, message='Your token is invalid!')
            return

        current_time = mktime(datetime.now().utctimetuple())
        if current_time > user['expiresIn']:
            self.current_user = None
            self.send_error(403, message='Your token has expired!')
            return

        self.current_user = {
            'email': user['email'],
            'display_name': user['display_name'],
            'password': user['password'],
            'name': user['name'],
            'address': user['address'],
            'dob': user['dob'],
            'phone': user['phone'],
            'disability': user['disability']
        }
