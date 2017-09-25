"""
Queue ADT
"""

class QueueADT():

    class Node:
        def __init__(self, obj=None, next=None):
            self.__obj = obj
            self.next = next

        def __str__(self):
            return str(self.__obj)

    def remove(self):
        raise NotImplementedError("Must implement this")

    def insert(self):
        raise NotImplementedError("Must implement this")

    def is_empty(self):
        raise NotImplementedError("Must implement this")
