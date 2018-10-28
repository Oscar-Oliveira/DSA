"""
Search Examples
"""

import os, pathlib, sys
sys.path.append(str(pathlib.Path(os.path.dirname(__file__)).parent))
from _Tools import Tools

from A_Algorithms.search_linear import LinearSearch
from A_Algorithms.search_binary import BinarySearch
from A_Algorithms.search_binary_recursive import BinarySearchRecursive

search_class = LinearSearch

@Tools.execTime
def search_element(item, list_):
    Tools.pprint(list_)
    search_instance = search_class(item, list_)
    print("N: {}".format(len(list_)))
    print("Max. Steps: {}".format(search_class.MaxSteps(len(list_))))
    print("Position of {}: {}".format(item, search_instance.search()))
    print("Comparisions: {}".format(search_instance.comparisons))

def example1():
    item = 2
    list_ = [1, 2, 3, 4, 5, 6, 7]
    search_element(item, list_)

def example2(n):
    list_ = list(range(1, n + 1))
    item = list_[search_class.WorstCase(n)]
    search_element(item, list_)

def main():

    example1()

    print()
    for i in [10, 100, 10000, 1000000]:
        example2(i)
        print()

if __name__ == "__main__":
    main()
    print("Done!!")
