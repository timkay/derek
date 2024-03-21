import math

width = 7

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def print(self):
        if self.left != None:
            self.left.print()
        print(' ', self.value, end='')
        if self.right != None:
            self.right.print()
    def __str__(self):
        return f'Node({self.value})'

sentinel = Node('-')
sentinel.left = sentinel
sentinel.right = sentinel

class BinTree():
    def __init__(self):
        self.root = Node(-math.inf)
    @staticmethod
    def f(parent, node, pivot, value=None):
        while node and node.value != value:
            parent, node = node, node.left if pivot < node.value else node.right
        return parent, node
    def find2(self, pivot, value=None):
        """
        Finds a parent and node in the tree, if a matching value exists.
        Otherwise, returns the parent (and None) where the value can be added.
        Pivot on math.-inf or math.inf to find the left-most or right-most child.
        """
        return self.f(self.root, self.root.right, pivot, value)
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
        parent, node = self.find2(value, value)
        # if node is None then value was not found
        if node is None:
            return
        if node == parent.left:
            # need new parent.left
            p, n = self.f(parent, node, math.inf)
            p.right = n.left
            n.left = node.left
            n.right = node.right
            parent.left = n
        else:
            # need new parent.right
            p, n = self.f(parent, node, -math.inf)
            pass
                
    def print(self, what=None):
        """Prints the whole tree in order"""
        if what is not None:
            print(f'{what}:', end='')
        if self.root.right is not None:
            self.root.right.print()
        print()
        return self

tree = BinTree()
tree.add(3, 1, 4, 1, 5, 9, 2, 6).print('added digits of pi')
tree.add(10).print('added 10')
tree.add(3).print('added 3, which matches root')
tree.add(1, 2, 3, 4, 5, 6).print('added sequence 1..6')
print('find(2) -->', tree.find(2))
print('find(88) -->', tree.find(88))
print('done')
