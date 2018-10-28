"""
Spy
"""

class Spy():

    PUBLIC_P = 2833 # public (prime) modulus
    PUBLIC_G = 3667  # public (prime) base

    def __init__(self, secret, machine):
        self.__secret = secret
        self.__shared_key = None
        self.__machine = machine
        self.public_value = pow(Spy.PUBLIC_G, self.__secret) % Spy.PUBLIC_P

    def set_shared_key(self, friend):
        self.__shared_key = pow(friend.public_value, self.__secret) % Spy.PUBLIC_P

    def speak(self, secret_message):
        return self.__machine.encrypt(secret_message, self.__shared_key)

    def listen(self, secret_message):
        return self.__machine.decrypt(secret_message, self.__shared_key)

    def whisper(self):
        return self.__shared_key
