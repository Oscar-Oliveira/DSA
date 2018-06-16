"""
Queue
"""

from B_Data_Structures.queue_adt import QueueADT

class Queue_built_in_list(QueueADT):

    def __init__(self):
        self.Items = []

    def insert(self, obj):
        self.Items.append(obj)

    def remove(self):
        return_value = self.Items[0]
        del self.Items[0]
        return return_value

    def is_empty(self):
        return self.Items == []
