"""
LinearSearch
"""

from A_Algorithms.search_adt import Search

class LinearSearch(Search):
    """Linear search"""

    def search(self):
        self.comparisons = 0
        for pos, value in enumerate(self.list):
            self.comparisons += 1
            if value == self.item:
                return pos
        return -1

    @staticmethod
    def WorstCase(size):
        return size - 1

    @staticmethod
    def MaxSteps(size):
        return size
