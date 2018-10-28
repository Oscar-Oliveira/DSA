"""
Merge Sort
"""

from A_Algorithms.sort_adt import Sort

class MergeSort(Sort):
    """MergeSort"""

    @staticmethod
    def sort(list_, show_steps=False):
        if show_steps:
            MergeSort.sort_print(list_)
        else:
            MergeSort.sort_no_print(list_)

    @staticmethod
    def sort_no_print(list_):
        """Sort list with no step prints"""
        if len(list_) > 1:
            mid = int(len(list_)/2)
            left = list_[:mid]
            right = list_[mid:]
            # Split
            MergeSort.sort(left)
            MergeSort.sort(right)
            # sort
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list_[k] = left[i]
                    i += 1
                else:
                    list_[k] = right[j]
                    j += 1
                k += 1
            # left leftovers
            while i < len(left):
                list_[k] = left[i]
                i += 1
                k += 1
            # right leftovers
            while j < len(right):
                list_[k] = right[j]
                j += 1
                k += 1

    @staticmethod
    def sort_print(list_, level=0):
        """Sort list with step prints"""
        print("  " * level, list_)
        if len(list_) > 1:
            mid = int(len(list_)/2)
            left = list_[:mid]
            right = list_[mid:]
            # Split
            MergeSort.sort_print(left, level + 1)
            MergeSort.sort_print(right, level + 1)
            # sort
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list_[k] = left[i]
                    i += 1
                else:
                    list_[k] = right[j]
                    j += 1
                k += 1
            # left leftovers
            while i < len(left):
                list_[k] = left[i]
                i += 1
                k += 1
            # right leftovers
            while j < len(right):
                list_[k] = right[j]
                j += 1
                k += 1
        print("  " * level, " >", list_)
