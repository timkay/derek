eimport math

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
    def __str__(self):
        return f'Node({self.value})'
class BinTree():
    def __init__(self):
        self.root = Node(-math.inf)
    def cut(self):
        """Removes the entire tree structure"""
        self.root.right.cut()
        self.root.right = None
        return self
    def add(self, *values):
        """Adds a node to the tree. Ignores duplicates."""
        for value in values:
            node = self.root
            while node:
                if value < node.value:
                    if node.left is None:
                        node.left = Node(value)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(value)
                        break
                    node = node.right
        return self
    def print(self, what=None):
        """Prints the whole tree in order"""
        if what is not None:
            print(f'{what}:', end='')
        if self.root.right is not None:
            self.root.right.print()
        print()
        return self
    def find(self, value):
        """Finds a node in the tree."""
        parent = self.root
        node = parent.right
        while node is not None:
            if node.value == value:
                return node, parent
            if value < node.value:
                parent, node = node, node.left
            else:
                parent, node = node, node.right
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
