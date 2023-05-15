from tornado.web import authenticated

from .auth import AuthHandler
from cryptography.fernet import Fernet

class UserHandler(AuthHandler):

    @authenticated
    def get(self):
        key = b'Nc5Y-2MJ6kGb93v2pKNRiThfUcZ8C4NPl4lb8UPXFOc='
        f = Fernet(key)

        self.set_status(200)
        self.response['email'] = self.current_user['email']
        self.response['password'] = self.current_user['password']
        self.response['name'] = f.decrypt(self.current_user['name']).decode()
        self.response['address'] = f.decrypt(self.current_user['address']).decode()
        self.response['dob'] = f.decrypt(self.current_user['dob']).decode()
        self.response['phone'] = f.decrypt(self.current_user['phone']).decode()
        self.response['disability'] = f.decrypt(self.current_user['disability']).decode()
        self.response['display_name'] = self.current_user['display_name']
        self.write_json()
