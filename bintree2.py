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
        # if node is None then value was not found
        if node:
            if node == parent.left:
                if node.right is None:
                    parent.left = node.left
                else:
                    # need new parent.left, so look for right-most element
                    p, n = node, node.right
                    while n.right:
                        p, n = n, n.right
                    p.right = n.left
                    n.left, n.right = node.left, node.right
                    parent.left = n
            else:
                if node.left is None:
                    parent.right = node.right
                else:
                    # need new parent.right, so look for left-most element
                    p, n = node, node.left
                    while n.left:
                        p, n = n, n.left
                    p.left = n.right
                    n.left, n.right = node.left, node.right
                    parent.right = n
        return self  
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
tree.remove(3).print('removed 3')
print('done')
