"""
Bloom filter
"""		

class BloomFilter():
    """
    Simple bloom filter implementation
    Not for production! Only for demonstration
    """

    def __init__(self, size=10):
        '''
        bit_array is implemented as a list, to reduce dependencies
        of external libs. should be an dedicated data structure to hold bits
        '''
        self.__size = size
        self.__bit_array = [0] * size

    @staticmethod
    def hash(word, size, seed):
        '''
        Simple demo hash function
        "There must also be k different hash functions defined, each of which
        maps or hashes some set element to one of the m array positions,
        generating a uniform random distribution."
        '''
        hash_ = 0
        for x in word:
            hash_ += ord(x)
        return (hash_ % size) + seed

    def get_h1_h2(self, word):
        return (BloomFilter.hash(word, self.__size -3, 0), \
                BloomFilter.hash(word, self.__size -3, 3))

    def add(self, word):
        h1, h2 = self.get_h1_h2(word)
        self.__bit_array[h1] = 1
        self.__bit_array[h2] = 1

    def exists(self, word):
        h1, h2 = self.get_h1_h2(word)
        return self.__bit_array[h1] == 1 and self.__bit_array[h2] == 1

    def __str__(self):
        return str(self.__bit_array)
