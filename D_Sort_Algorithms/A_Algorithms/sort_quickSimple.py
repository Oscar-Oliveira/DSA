"""
Quick Sort Simple
"""

from A_Algorithms.sort_adt import Sort

class QuickSortSimple(Sort):
    """QuickSort"""

    @staticmethod
    def sort(list_, show_steps=False):
        sorted_list = QuickSortSimple.sort_print(list_) if show_steps \
           else QuickSortSimple.sort_no_print(list_)
        del list_[:]
        list_ += sorted_list

    @staticmethod
    def sort_no_print(list_):
        """Sort list with no step prints"""
        if len(list_) > 1:
            pivot = list_[0]
            lower = [i for i in list_[1:] if i <= pivot]
            greather = [i for i in list_[1:] if i > pivot]
            return QuickSortSimple.sort_no_print(lower) \
                   + [pivot] \
                   + QuickSortSimple.sort_no_print(greather)
        return list_

    @staticmethod
    def sort_print(list_, level=0):
        """Sort list with step prints"""
        if len(list_) > 1:
            pivot = list_[0]
            lower = [i for i in list_[1:] if i <= pivot]
            greather = [i for i in list_[1:] if i > pivot]
            print("  " * level, lower, "<", pivot, "<", greather)
            result = QuickSortSimple.sort_print(lower, level + 1) \
                   + [pivot] \
                   + QuickSortSimple.sort_print(greather, level + 1)
            print("  " * level, ">", result)
            return result
        return list_
