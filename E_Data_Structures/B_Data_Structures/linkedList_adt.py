"""
LinkedList ADT
"""

class LinkedListADT():

    class Node:

        def __init__(self, obj=None, next_=None):
            self.__obj = obj
            self.next = next_

        def get(self):
            """return element"""
            return self.__obj

        def __str__(self):
            return str(self.__obj)

        def __eq__(self, other):
            if other:
                return self.__obj == other
            return False

        def __ne__(self, other):
            return not self.__eq__(other)

    def add(self, obj):
        """Adds element to list"""
        raise NotImplementedError("Must implement this")

    def remove(self, obj):
        """removes element from list"""
        raise NotImplementedError("Must implement this")

    def search(self, obj):
        """search element"""
        raise NotImplementedError("Must implement this")

    def print(self):
        """print list"""
        raise NotImplementedError("Must implement this")

    def print_reversed(self):
        """print list reversed"""
        raise NotImplementedError("Must implement this")
