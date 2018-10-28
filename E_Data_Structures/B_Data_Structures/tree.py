"""
Tree ADT
"""

from B_Data_Structures.tree_adt import TreeADT

class Tree(TreeADT):

    END = "\n"

    def __init__(self):
        self.root = None

    def insert(self, obj, node=None):
        if not self.root:
            self.root = TreeADT.Node(obj)
        else:
            if node is None:
                node = self.root
            if node.obj > obj:
                if node.left is None:
                    node.left = TreeADT.Node(obj)
                else:
                    self.insert(obj, node.left)
            else:
                if node.right is None:
                    node.right = TreeADT.Node(obj)
                else:
                    self.insert(obj, node.right)

    def traverseInorder(self):
        self._traverseInorder(self.root)

    def traversePreorder(self):
        self._traversePreorder(self.root)

    def traversePostorder(self):
        self._traversePostorder(self.root)

    def _traverseInorder(self, node):
        if node is not None:
            self._traverseInorder(node.left)
            print(node.obj, end=Tree.END)
            self._traverseInorder(node.right)

    def _traversePreorder(self, node):
        if node is not None:
            print(node.obj, end=Tree.END)
            self._traversePreorder(node.left)
            self._traversePreorder(node.right)

    def _traversePostorder(self, node):
        if node is not None:
            self._traversePostorder(node.left)
            self._traversePostorder(node.right)
            print(node.obj, end=Tree.END)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("   " * level, node)
        if node.left:
            print("<", end="")
            self.print_tree(node.left, level+1)
        if node.right:
            print(">", end="")
            self.print_tree(node.right, level+1)
