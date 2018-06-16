"""
Hash table - example
"""

import ads_02_00_DB as DB
from B_Data_Structures.hashtable import HashTable

#ht.HashTable.SIZE = 20

def main():

    agenda = HashTable()
    print(agenda)

    print()
    for user in DB.user_to_add:
        if agenda.insert(user[0], user):
            print("User was added")
        else:
            print("User already has this key registered")

    agenda.insert(0, "Teste1")
    agenda.insert(10, "Teste2")
    agenda.insert(11, "Teste3")

    print()
    print(agenda.get(0))
    print(agenda.get("oscar@gmail.com"))
    print(agenda.get("John"))

    print()
    print(agenda)

if __name__ == "__main__":
    main()
    print("Done!!")
    