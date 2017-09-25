"""
LinkedList 
"""

from B_Data_Structures.linkedList_adt import LinkedListADT

class LinkedList(LinkedListADT):

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, obj):
        self.head = LinkedListADT.Node(obj, self.head)
        self.length += 1

    def remove(self, obj):
        if self.head:
            if self.head == obj:
                self.head = self.head.next
                self.length -= 1
                return obj
            parent = self.head
            while parent != None and parent.next != obj:
                parent = parent.next
            if parent:
                parent.next = parent.next.next
                self.length -= 1
                return obj
        return None

    def search(self, obj):
        node = self.head
        while node != None and node != obj:
            node = node.next
        return node

    def print(self):
        node = self.head
        while node:
            print(node)
            node = node.next
        print()

    def print_reversed(self):
        self._print_reversed(self.head)

    def _print_reversed(self, node):
        if node:
            self._print_reversed(node.next)
            print(node)
