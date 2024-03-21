import math

width = 3

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
    def tree(self, depth, between):
        if depth == 0:
            print(' ' * between, '{value:^{width}}'.format(value=self.value, width=width), end='')
            return
        if self.left:
            self.left.tree(depth - 1, between)
        else:
            sentinel.tree(depth - 1, between)
        if self.right:
            self.right.tree(depth - 1, between)
        else:
            sentinel.tree(depth - 1, between)
    def __str__(self):
        return f'Node({self.value})'

sentinel = Node(' - ')
sentinel.left = sentinel
sentinel.right = sentinel

class BinTree():
    def __init__(self):
        self.root = Node(-math.inf)
    def find2(self, pivot, value=None):
        """
        Finds a parent and node in the tree, if a matching value exists.
        Otherwise, returns the parent (and None) where the value can be added.
        Pivot on math.-inf or math.inf to find the left-most or right-most child.
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
        parent, node = self.find2(value, value)
        if node:
            pass
    def print(self, what=None):
        """Prints the whole tree in order"""
        if what is not None:
            print(f'{what}:', end='')
        if self.root.right is not None:
            self.root.right.print()
        print()
        return self
    def tree(self, what=None):
        """Prints the whole tree as a tree"""
        deepest = 5
        if what is not None:
            print(f'{what}:')
        if self.root.right is not None:
            for depth in range(0, deepest):
                print(width, 2**(deepest-1), 2**depth, 2**(deepest-1) - 2**depth, 2**depth + 1)
                between = int(width * (2**(deepest-1) - 2**depth) / (2**depth + 1))
                print(f'{between:<10}', end='')
                self.root.right.tree(depth, between)
                print()
        return self

tree = BinTree()
tree.add(3, 1, 4, 1, 5, 9, 2, 6).print('added digits of pi')
tree.add(10).print('added 10')
tree.add(3).print('added 3, which matches root')
tree.tree()
tree.add(1, 2, 3, 4, 5, 6).print('added sequence')
print('find(2) -->', tree.find(2))
print('find(88) -->', tree.find(88))
print('done')
