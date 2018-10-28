"""
Hash - built-in dictionary
"""

import ads_02_00_DB as DB
from A_Classes import users

def main():

    app_users = users.users()

    for user in DB.user_to_add:
        if app_users.add_user(*user):
            print("User was added")
        else:
            print("User already has this email registered")

    print()
    app_users.print_user("oscar@gmail.com")
    app_users.print_user("oscar@outlook.com")

    print()
    print(app_users.authenticate_user("oscar@gmail.com", "oscar"))
    print(app_users.authenticate_user("oscar@gmail.com", "dfsgfds"))

    print()
    app_users.list()

if __name__ == "__main__":
    main()
    print("Done!!")
    