import math

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def cut(self):
        """Removes the entire tree structure"""
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
    def __str__(self):
        return f'Node({self.value})'
class BinTree():
    def __init__(self):
        self.root = Node(-math.inf)
    def cut(self):
        """Removes the entire tree structure"""
        #Is this feature necessary? Why not rely on the garbage collector?
        self.root.right.cut()
        self.root.right = None
        return self
    def print(self, what=None):
        """Prints the whole tree in order"""
        if what is not None:
            print(f'{what}:', end='')
        if self.root.right is not None:
            self.root.right.print()
        print()
        return self
    def find2(self, pivot, value=None):
        """
        Finds a parent and node in the tree, if a matching value exists.
        Otherwise, returns the parent and None where the value can be added.
        """
        parent, node = self.root, self.root.right
        while node and node.value != value:
            parent, node = node, node.left if pivot < node.value else node.right
        return parent, node
    def find(self, value):
        return self.find2(value, value)[1]
    def add(self, *values):
        """Adds a node to the tree. Ignores duplicates."""
        for value in values:
            parent, node = self.find2(value)
            if value < parent.value:
                parent.left = Node(value)
            else:
                parent.right = Node(value)
        return self
    def remove(self, value):
        """Removes a node from the tree"""
        node, parent = self.find(value)

tree = BinTree()
tree.add(3, 1, 4, 1, 5, 9, 2, 6).print('added digits of pi')
tree.add(10).print('added 10')
tree.add(3).print('added 3, which matches root')
tree.cut().print('cut')
tree.add(1, 2, 3, 4, 5, 6).print('added sequence')
print('find(2) -->', tree.find(2))
print('find(88) -->', tree.find(88))
print('done')
