"""
Quick Sort
"""

from A_Algorithms.sort_adt import Sort

class QuickSort(Sort):
    """QuickSort"""

    @staticmethod
    def sort(list_, show_steps=False):
        if show_steps:
            QuickSort.sort_print(list_, 0, len(list_)-1, ['-'] * len(list_))
        else:
            QuickSort.sort_no_print(list_, 0, len(list_)-1)

    @staticmethod
    def sort_no_print(list_, first, last):
        """Sort list with no step prints"""
        if first < last:
            in_place = QuickSort.partition_no_print(list_, first, last)
            # sort left of in_place element
            QuickSort.sort_no_print(list_, first, in_place-1)
            # sort right of in_place element
            QuickSort.sort_no_print(list_, in_place+1, last)

    @staticmethod
    def partition_no_print(list_, first, last):
        pivot = list_[first]
        left = first + 1
        right = last
        while True:
            while left <= right and list_[left] <= pivot:
                left += 1
            while right >= left and list_[right] >= pivot:
                right -= 1
            if left <= right:
                list_[right], list_[left] = list_[left], list_[right]
            else: break
        # swaps pivot and right, left elements are lower than pivot
        # and right elements are greather tha pivor
        list_[first], list_[right] = list_[right], list_[first]
        return right

    @staticmethod
    def format_list(pivot, list_):
        formated_string = "["
        sep = ""
        for item, value  in enumerate(list_):
            temp = "{}P{}" if value == pivot else "{}{}"
            formated_string += temp.format(sep, value)
            sep = ", "
        formated_string += "]"
        return formated_string

    @staticmethod
    def sort_print(list_, first, last, inPlace):
        """Sort list with step prints"""
        if first < last:
            print("_" * 30)
            print("{}".format(QuickSort.format_list(list_[first], list_[first:last+1])))
            in_place = QuickSort.partition_print(list_, first, last)
            inPlace[in_place] = list_[in_place]
            print(inPlace)
            QuickSort.sort_print(list_, first, in_place-1, inPlace)
            QuickSort.sort_print(list_, in_place+1, last, inPlace)
        elif first == last:
            print("_" * 30)
            inPlace[first] = list_[first]
            print(inPlace)

    @staticmethod
    def partition_print(list_, first, last):
        pivot = list_[first]
        left = first + 1
        right = last
        while True:
            while left <= right and list_[left] <= pivot:
                left += 1
            while right >= left and list_[right] >= pivot:
                right -= 1
            if left <= right:
                list_[right], list_[left] = list_[left], list_[right]
                print("{} {}<->{}".format(QuickSort.format_list(list_[first], list_[first:last+1]), list_[right], list_[left]))
            else: break
        list_[first], list_[right] = list_[right], list_[first]
        print("{} P{}<->{}".format(QuickSort.format_list(list_[right], list_[first:last+1]), pivot, list_[first]))
        return right
