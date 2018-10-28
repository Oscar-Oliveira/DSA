"""
stack - example
"""

import ds_03_00_users as DB
from A_Classes.user import User
from B_Data_Structures.stack import Stack

def main():

    stack = Stack()

    for user in DB.user_to_add:
        print(user)
        stack.push(User(*user))

    print()
    while not stack.is_empty():
        print(stack.pop())

if __name__ == "__main__":
    main()
    print("Done!!")
