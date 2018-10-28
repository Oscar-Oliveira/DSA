"""
BinarySearch - recursive
"""

from math import ceil
from A_Algorithms.search_binary import BinarySearch

class BinarySearchRecursive(BinarySearch):
    """Recursive Binary search"""

    def solve(self, start, end):
        """Recursive function that compare mid point"""
        if start > end:
            return -1
        mid = ceil((start + end) / 2)
        self.comparisons += 1
        if self.list[mid] == self.item:
            return mid
        if self.item < self.list[mid]:
            return self.solve(start, mid-1)
        return self.solve(mid+1, end)

    def search(self):
        self.comparisons = 0
        return self.solve(0, len(self.list) - 1)
