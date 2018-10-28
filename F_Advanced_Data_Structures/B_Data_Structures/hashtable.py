"""
HashTable
"""

class HashTable():

    SIZE = 10

    class node():
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __str__(self):
            return "{}: {}".format(self.key, self.value)

    def __init__(self):
        self.__data = [[] for _ in range(HashTable.SIZE)]

    @staticmethod
    def hash(key):
        if isinstance(key, str):
            key = sum(ord(x) for x in key)
        return key % HashTable.SIZE

    def insert(self, key, value):
        if not self.get(key):
            data = HashTable.node(key, value)
            self.__data[HashTable.hash(key)].append(data)
            return True
        return False

    def get(self, key):
        block = self.__data[HashTable.hash(key)]
        for _, value in enumerate(block):
            if value.key == key:
                return value.value
        return None

    def __str__(self):
        return_value = "["
        for block in self.__data:
            return_value += "\n["
            for item in block:
                return_value += str(item) + ", "
            return_value += "],"
        return return_value + "]"
