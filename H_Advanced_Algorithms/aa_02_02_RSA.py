"""
RSA
See: https://www.youtube.com/watch?v=9m9MsYUV-qw
See: https://www.schneier.com/essays/archives/1999/03/cryptography_the_imp.html
See: https://pypi.python.org/pypi/rsa
"""

from A_Classes.rsa import RSA

class Person():

    def __init__(self):
        self.public_key, self.__private_key, self.encript, self.__decript = RSA.make()

    def send(self, message, person):
        return person.encript(message)

    def receive(self, message):
        return self.__decript(message)

    def __str__(self):
        return "Public key: {} | Private key: {}".format(self.public_key, self.__private_key)

def main():

    Alice = Person()
    Bob = Person()
    Eve_enemy_spy = Person()

    # Alice wants to send secrely message 100100 to Bob
    message_from_alice = Alice.send(100100, Bob)

    print("Message encripted (public):", message_from_alice)

    message_received_bob = Bob.receive(message_from_alice)
    print("Message decripted by Bob:", message_received_bob)

    # Eve tries to decrypt the message addresses to Bob
    message_received_eve = Eve_enemy_spy.receive(message_from_alice)
    print("Message decripted by Eve:", message_received_eve)

    print()
    print(Alice)
    print(Bob)
    print(Eve_enemy_spy)

if __name__ == '__main__':
    main()
    print("Done!!")
