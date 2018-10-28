"""
Diffie–Hellman key exchange and Symmetric key
"""

from A_Classes.symmetrickey import SymmetricKey
from A_Classes.spy import Spy

Alice = Spy(secret=2642, machine=SymmetricKey)
Bob = Spy(secret=8249, machine=SymmetricKey)

Eve_enemy_spy = Spy(secret=0000, machine=SymmetricKey)

print("Alice shares publically:", Alice.public_value)
print("Bob shares publically:", Bob.public_value)

print()
print("-" * 30, "Top secret", "-" * 30)

Alice.set_shared_key(Bob)
Bob.set_shared_key(Alice)

# Eve tries to compute a shared key with Alice to understand her messages
Eve_enemy_spy.set_shared_key(Alice)

print("Key computed by Alice:", Alice.whisper())
print("Key computed by Bob:", Bob.whisper())
print("Key computed by Eve:", Eve_enemy_spy.whisper())

print()
alice_message = Alice.speak("meeting London tower 9h30")
print("Alice says loudly:", alice_message)

print()
message_understanded_by_Bob = Bob.listen(alice_message)
print("Bob understand:", message_understanded_by_Bob)

message_understanded_by_Eve = Eve_enemy_spy.listen(alice_message)
print("Eve understand:", message_understanded_by_Eve)
