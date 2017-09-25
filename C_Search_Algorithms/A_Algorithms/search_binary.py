"""
BinarySearch
"""

from math import ceil, log
from A_Algorithms.search_adt import Search

class BinarySearch(Search):
    """Binary search"""

    def search(self):
        self.comparisons = 0
        start = 0
        end = len(self.list) - 1
        while start <= end:
            self.comparisons += 1
            mid = ceil((start + end) / 2)
            if self.list[mid] == self.item:
                return mid
            if self.list[mid] > self.item:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    @staticmethod
    def WorstCase(size):
        return 0

    @staticmethod
    def MaxSteps(size):
        return ceil(log(size, 2))
