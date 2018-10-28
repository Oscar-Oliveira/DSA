"""
Insertion Sort
"""

from A_Algorithms.sort_adt import Sort

class InsertionSort(Sort):
    """InsertionSort"""

    @staticmethod
    def sort(list_, show_steps=False):
        if show_steps:
            InsertionSort.sort_print(list_)
        else:
            InsertionSort.sort_no_print(list_)

    @staticmethod
    def sort_no_print(list_):
        """Sort list with no step prints"""
        for index in range(1, len(list_)):
            currentvalue = list_[index]
            position = index
            while position > 0 and list_[position-1] > currentvalue:
                list_[position] = list_[position - 1]
                position -= 1
            list_[position] = currentvalue

    @staticmethod
    def sort_print(list_):
        """Sort list with step prints"""
        print(list_)
        for index in range(1, len(list_)):
            currentvalue = list_[index]
            position = index
            pushed = " "
            while position > 0 and list_[position-1] > currentvalue:
                pushed += ">" + str(list_[position - 1]) + " "
                list_[position] = list_[position - 1]
                position -= 1
            list_[position] = currentvalue
            print("{} ?{} +{}[{}->{}]".format(list_, pushed.rstrip(), currentvalue, index, position))
