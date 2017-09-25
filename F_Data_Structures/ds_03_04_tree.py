"""
tree - example
"""

import ds_03_00_users as DB
from A_Classes.user import User
from B_Data_Structures.tree import Tree

def transverse(tree):
    tree.print_tree()
    print()
    tree.traverseInorder()
    print()
    tree.traversePreorder()
    print()
    tree.traversePostorder()

def example1():
    '''example from slides'''
    Tree.END = " "
    tree = Tree()
    example_from_slides = ["P", "F", "S", "B", "H", "G", "R", "Y", "T", "Z", "W"]
    for u in example_from_slides:
        tree.insert(u)
    transverse(tree)

def example2():
    Tree.END = "\n"
    tree = Tree()
    for user in DB.user_to_add:
        tree.insert(User(*user))
    transverse(tree)

def main():
    #example1()
    example2()

if __name__ == "__main__":
    main()
    print("Done!!")
