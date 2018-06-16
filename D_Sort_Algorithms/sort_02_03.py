"""
Sort Example 3
"""

import random
import os, pathlib, sys
sys.path.append(str(pathlib.Path(os.path.dirname(__file__)).parent))
from _Tools import Tools

from A_Algorithms import *

@Tools.execTime
def sort_element(list_, sort_class):
    Tools.pprint(list_)
    sort_class.sort(list_)
    Tools.pprint(list_)

def main():

    unsorted_list = list(range(1000))

    sort_classes = [
        sort_bubble.BubbleSort,
        sort_bubbleShort.BubbleSortShort,
        sort_selection.SelectionSort,
        sort_insertion.InsertionSort,
        sort_merge.MergeSort,
        sort_quick.QuickSort,
        sort_quickSimple.QuickSortSimple,
    ]

    """
    Test with and without randonization
    """
    random.shuffle(unsorted_list)

    for _, sort_class in enumerate(sort_classes):
        list_ = unsorted_list[:]
        print(sort_class.__name__)
        sort_element(list_, sort_class)
        print()

if __name__ == "__main__":
    main()
    print("Done!!")
