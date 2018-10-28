"""
Class - User
"""

class User():

    def __init__(self, email, name, password, age):
        self.email = email
        self.name = name
        self.password = password
        self.age = age

    def __str__(self):
        return "Name: {} | Email: {} | Password: {} | Age: {}".format(str(self.name).title(), self.email, self.password, self.age)

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name \
           and self.email == other.email \
           and self.password == other.password \
           and self.age == other.age  if other else False

    def __ne__(self, other):
        return not self.__eq__(other)
