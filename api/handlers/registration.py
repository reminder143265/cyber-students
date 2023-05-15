from json import dumps
from logging import info
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from .base import BaseHandler

class RegistrationHandler(BaseHandler):

    @coroutine
    def post(self):
        try:
            body = json_decode(self.request.body)
            email = body['email'].lower().strip()
            if not isinstance(email, str):
                raise Exception()
            password = body['password']
            if not isinstance(password, str):
                raise Exception()
            name = body['name']
            if not isinstance(name, str):
                raise Exception()
            address = body['address']
            if not isinstance(address, str):
                raise Exception()
            dob = body['dob']
            if not isinstance(dob, str):
                raise Exception()
            phone = body['phone']
            if not isinstance(phone, str):
                raise Exception()
            disability = body['disability']
            if not isinstance(disability, str):
                raise Exception()       
            display_name = body.get('display_name')
            if display_name is None:
                display_name = email
            if not isinstance(display_name, str):
                raise Exception()
        except Exception as e:
            self.send_error(400, message='You must provide an email address, password and display name!')
            return

        if not email:
            self.send_error(400, message='The email address is invalid!')
            return

        if not password:
            self.send_error(400, message='The password is invalid!')
            return
          
        if not name:
            self.send_error(400, message='The display name is invalid!')
            return
        
        if not address:
            self.send_error(400, message='The address is invalid!')
            return
        
        if not dob:
            self.send_error(400, message='The date of birth is invalid!')
            return
        
        if not phone:
            self.send_error(400, message='The phone number is invalid!')
            return
        
        if not disability:
            self.send_error(400, message='The input is invalid!')
            return
        
        if not display_name:
            self.send_error(400, message='The display name is invalid!')
            return

        user = yield self.db.users.find_one({
          'email': email
        }, {})

        if user is not None:
            self.send_error(409, message='A user with the given email address already exists!')
            return
        
        salt = os.urandom(16)
        
        kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
        passphrase_bytes = bytes(password, "utf-8")
        hashed_passphrase = kdf.derive(passphrase_bytes)
        
        key = b'Nc5Y-2MJ6kGb93v2pKNRiThfUcZ8C4NPl4lb8UPXFOc='
        f = Fernet(key)

        
        yield self.db.users.insert_one({
            'email': email,
            'password': hashed_passphrase,
            'name': name,
            'address': f.encrypt(bytes(address, "utf-8")),
            'dob': f.encrypt(bytes(dob, "utf-8")),
            'phone': f.encrypt(bytes(phone, "utf-8")),
            'disability': f.encrypt(bytes(disability, "utf-8")),
            'display_name': display_name,
            'salt': salt
        })

        self.set_status(200)
        self.response['email'] = email
        self.response['password'] = password
        self.response['name'] = name
        self.response['address'] = address
        self.response['dob'] = dob
        self.response['phone'] = phone
        self.response['disability'] = disability
        self.response['display_name'] = display_name
        

        self.write_json()
