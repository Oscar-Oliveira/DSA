"""
Bubble Sort
"""

from A_Algorithms.sort_adt import Sort

class BubbleSort(Sort):
    """BubbleSort"""

    @staticmethod
    def sort(list_, show_steps=False):
        if show_steps:
            BubbleSort.sort_print(list_)
        else:
            BubbleSort.sort_no_print(list_)

    @staticmethod
    def sort_no_print(list_):
        """Sort list with no step prints"""
        for i in range(len(list_)-1, 0, -1):
            for j in range(i):
                if list_[j] > list_[j+1]:
                    list_[j], list_[j+1] = list_[j+1], list_[j]

    @staticmethod
    def sort_print(list_):
        """Sort list with step prints"""
        print(" " * 5, list_)
        for i in range(len(list_)-1, 0, -1):
            print("_" * 30)
            for j in range(i):
                print(j, j+1, end=" ")
                if list_[j] > list_[j+1]:
                    list_[j], list_[j+1] = list_[j+1], list_[j] # swap
                    print(">", end=" ") # mark swap
                else: print("|", end=" ") # mark no swap
                print(list_)
