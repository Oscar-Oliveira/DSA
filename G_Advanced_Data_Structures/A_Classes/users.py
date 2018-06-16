"""
Users - using python dictionary and hashlib to encript password
"""

import hashlib
from A_Classes.user import User

class users():

    def __init__(self):
        self.users = dict()

    def add_user(self, email, name, password, age):
        if not self.users.get(email):
            self.users[email] = User(email, name, \
                hashlib.sha256(password.encode('utf-8')).hexdigest(), age)
            return True
        return False

    def get_user(self, email):
        if self.users.get(email):
            return self.users[email]
        return None

    def print_user(self, email):
        if self.users.get(email):
            print(self.users[email])
        else:
            print("User does not exist!")

    def authenticate_user(self, email, password):
        if self.get_user(email) and \
           self.users[email].password == hashlib.sha256(password.encode('utf-8')).hexdigest():
            return True
        return False

    def list(self):
        for _, x in self.users.items():
            self.print_user(x.email)

    @staticmethod
    def Info():
        """
        - hashlib.algorithms_available method lists all the algorithms available
        in the system.
        - hashlib.algorithms_guaranteed only lists the algorithms present in the
        module. md5, sha1, sha224, sha256, sha384, sha512 are always present.
        """
        print(hashlib.algorithms_guaranteed)
