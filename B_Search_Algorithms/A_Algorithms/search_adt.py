"""
Search ADT
"""

class Search():
    """Abstract class"""

    def __init__(self, item, list):
        """
        Class initializer
        :param item: element to find
        :param list: list of elements (can be unsorted)
        """
        self.item = item
        self.list = list
        self.comparisons = 0

    def search(self):
        """
        Search element in list
        :returns: element position if found, -1 otherwise
        """
        raise NotImplementedError("Must implement this")

    @staticmethod
    def WorstCase(size):
        """
        Gets the worst case element for the search method applied
        :returns: worst case element position
        """
        raise NotImplementedError("Must implement this")

    @staticmethod
    def MaxSteps(size):
        """
        Returns the number of steps for the worst case
        :returns: worst case number of steps
        """
        raise NotImplementedError("Must implement this")
