"""
Bubble Sort Short
"""

from A_Algorithms.sort_adt import Sort

class BubbleSortShort(Sort):
    """
    Modified BubbleSort to stop early if the list has become sorted.
    """

    @staticmethod
    def sort(list_, show_steps=False):
        if show_steps:
            BubbleSortShort.sort_print(list_)
        else:
            BubbleSortShort.sort_no_print(list_)

    @staticmethod
    def sort_no_print(list_):
        """Sort list with no step prints"""
        exchanges = True
        iterations = len(list_) - 1
        while iterations > 0 and exchanges:
            exchanges = False
            for i in range(iterations):
                if list_[i] > list_[i+1]:
                    list_[i], list_[i+1] = list_[i+1], list_[i] # swap
                    exchanges = True
            iterations -= 1

    @staticmethod
    def sort_print(list_):
        """Sort list with step prints"""
        print(" " * 5, list_)
        exchanges = True
        iterations = len(list_) - 1
        while iterations > 0 and exchanges:
            exchanges = False
            print("_" * 30)
            for i in range(iterations):
                print(i, i+1, end=" ")
                if list_[i] > list_[i+1]:
                    list_[i], list_[i+1] = list_[i+1], list_[i] # swap
                    exchanges = True
                    print(">", end=" ") # mark swap
                else: print("|", end=" ") # mark no swap
                print(list_)
            iterations -= 1
