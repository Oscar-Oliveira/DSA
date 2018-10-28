"""
Sort Example 1
"""

import random
import os, pathlib, sys
sys.path.append(str(pathlib.Path(os.path.dirname(__file__)).parent))
from _Tools import Tools

from A_Algorithms.sort_bubble import BubbleSort
from A_Algorithms.sort_bubbleShort import BubbleSortShort
from A_Algorithms.sort_selection import SelectionSort
from A_Algorithms.sort_insertion import InsertionSort
from A_Algorithms.sort_merge import MergeSort
from A_Algorithms.sort_quick import QuickSort
from A_Algorithms.sort_quickSimple import QuickSortSimple

# --------------------------
# CHANGE HERE
sort_class = BubbleSortShort
# --------------------------

@Tools.execTime
def sort_element(list_):
    print("Unsorted list: ", end="")
    Tools.pprint(list_, 5)
    sort_class.sort(list_, True)
    print("Sorted list: ", end="")
    Tools.pprint(list_, 5)

def main():

    list_ = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(list_)
    sort_element(list_)
    print()

if __name__ == "__main__":
    main()
    print("Done!!")
