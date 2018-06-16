"""
Queue
"""

from B_Data_Structures.queue_adt import QueueADT

class Queue_with_head_and_tail(QueueADT):

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insert(self, T):
        node = QueueADT.Node(T)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove(self):
        return_value = self.head
        self.head = self.head.next
        self.length -= 1
        if self.is_empty():
            self.tail = None
        return return_value

    def is_empty(self):
        return self.length == 0
