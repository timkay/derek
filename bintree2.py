import math

debug = False
width = 7

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f'Node({self.value})'

none = Node('▢')
none.left, none.right = none, none
tee = '┴'
dash = '─'

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
    def remove(self, *values):
        """Removes a node from the tree"""
        for value in values:
            parent, node = self.find2(value, value)
            # if node is None then value was not found
            if node:
                # n will replace node
                if node.left is None:
                    n = node.right
                # elif node.right is None:
                #     n = node.left
                elif node.left.right is None:
                    n = node.left
                    n.right = node.right
                else:
                    p, n = node.left, node.left.right
                    while n.right:
                        p, n = n, n.right
                    p.right = n.left
                    n.left, n.right = node.left, node.right
                if node == parent.left:
                    parent.left = n
                else:
                    parent.right = n
        return self
    def print(self, what=None):
        """Prints the tree"""
        if what is not None:
            print('---', what, '---')
        print_tree(self.root.right)
        return self

# The print tree code is isolated here to post on StackOverflow

def print_tree(node):
    if node is None: return
    def get_depth(node, level = 0):
        if node is None: return level
        return level + 1 + max(get_depth(node.left), get_depth(node.right))
    def recurse(node, level=0, side=None, fill=' '):
        if level >= depth: return
        if i == level:
            recurse(node.left or none, level + 1, 'b' if node == none else 'l', dash if side == 'r' else fill)
            print(' ' * len(str(node.value)) if side == 'b' else node.value, end='')
            recurse(node.right or none, level + 1, 'b' if node == none else 'r', dash if side == 'l' else fill)
        else:
            recurse(node.left or none, level + 1, 'b' if node == none else 'l', fill)
            s = fill * len(str(node.value))
            if i == level + 1:
                wid = len(str(node.value))
                half = (wid - 1) // 2
                if side == 'b':
                    s = ' ' * wid
                else:
                    s = dash * half + tee + dash * half + dash * (wid % 2 == 0)
            print(s, end='')
            recurse(node.right or none, level + 1, 'b' if node == none else 'r', fill)
    depth = get_depth(node)
    for i in range(0, depth):
        print(f'{i:<3}', end='')
        recurse(node)
        print()
    print()

print()
print()
tree = BinTree()
tree.add(3, 1, 4, 1, 5, 9, 2, 6).print('added digits of pi')
tree.add(math.pi).print('added pi')
tree.add(math.e).print('added e')
tree.add(3).print('added 3, which matches root')
tree.add(1, 2, 3, 4, 5, 6).print('added sequence 1..6')
# print('find(2) -->', tree.find(2))
# print('find(88) -->', tree.find(88))
# tree.remove(3).print('removed 3')
# tree.remove(3).print('removed 3')
# tree.remove(3).print('removed 3')
# tree.remove(1).print('removed 1')
# tree.remove(1).print('removed 1')
# tree.remove(1).print('removed 1')
# tree.add(2.99).print('add 2.99')
# tree.remove(4).print('remove 4')
# tree.remove(5).print('remove 5')
# tree.remove(6).print('remove 6')
# tree.remove(4, 5, 6).print('removed 4 5 6')
print('done')
