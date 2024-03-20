import math

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def cut(self):
        """Removes the entire tree structure"""
        """Is it necessary to del each node?"""
        if self.left:
            self.left.cut()
        if self.right:
            self.right.cut()
        del self
    def print(self):
        if self.left:
            self.left.print()
        print(' ', self.value, end='')
        if self.right:
            self.right.print()
class BinTree():
    def __init__(self):
        self.root = Node(-math.inf)
    def cut(self):
        """Removes the entire tree structure"""
        self.root.right.cut()
        return self
    def add(self, *values):
        """Adds a node to the tree. Ignores duplicates."""
        for value in values:
            node = self.root
            while node:
                if value < node.value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(value)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(value)
                        break
        return self
    def print(self, what=None):
        """Prints the whole tree in order"""
        if what is not None:
            print(f'{what}:', end='')
        self.root.print()
        return self
    def find(self, value):
        """Finds a node in the tree."""
        node = self
        while node is not None:
            if node.value == value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right

tree = BinTree()
tree.add(3, 1, 4, 1, 5, 9, 2, 6).print('added digits of pi')
tree.add(10).print('added 10')
tree.add(3).print('added 3, which matches root')
