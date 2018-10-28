"""
Selection Sort
"""

from A_Algorithms.sort_adt import Sort

class SelectionSort(Sort):
    """SelectionSort"""

    @staticmethod
    def sort(list_, show_steps=False):
        if show_steps:
            SelectionSort.sort_print(list_)
        else:
            SelectionSort.sort_no_print(list_)

    @staticmethod
    def sort_no_print(list_):
        """Sort list with no step prints"""
        for i in range(len(list_) - 1):
            min_index = i
            for j in range(i+1, len(list_)):
                if list_[j] < list_[min_index]:
                    min_index = j
            list_[min_index], list_[i] = list_[i], list_[min_index] # swap

    @staticmethod
    def sort_print(list_):
        """Sort list with step prints"""
        print(" " * 5, list_)
        for i in range(len(list_) - 1):
            min_index = i
            for j in range(i+1, len(list_)):
                if list_[j] < list_[min_index]:
                    min_index = j
            print("{}<->{}".format(list_[i], list_[min_index]), end=" ")
            list_[min_index], list_[i] = list_[i], list_[min_index] # swap
            print(list_)
