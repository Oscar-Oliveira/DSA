"""
LinkedList - example
"""

import ds_03_00_users as DB
from A_Classes.user import User
from B_Data_Structures.linkedList import LinkedList

def main():

    linked_list = LinkedList()

    for user in DB.user_to_add:
        print(user)
        linked_list.add(User(*user))

    print()
    linked_list.print()
    linked_list.print_reversed()

    print()

    DB.user_to_add.append(("user3@gmail.com", "user3", "user3", 31))

    for user in range(len(DB.user_to_add)):
        user = DB.user_to_add[user]
        print("search:", user)
        user = linked_list.search(User(*user))
        if user:
            print(" found: ", user)
        else:
            print(" User does not exist")

    for user in range(len(DB.user_to_add)):
        user = DB.user_to_add[user]
        print("search:", user)
        user = linked_list.remove(User(*user))
        if user:
            print(" removed: ", user)
        else:
            print(" User does not exist")

    print(linked_list.length)

if __name__ == "__main__":
    main()
    print("Done!!")
