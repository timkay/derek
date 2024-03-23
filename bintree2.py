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

# none = Node('☐')
none = Node('▢')
none.left = none
none.right = none
tee = '┴'
tee2 = '┘└'
# dash = '—'
dash = '─'

class BinTree():
    def __init__(self):
        self.root = Node(-math.inf)
        print('root', self.root)
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
        if self.root.right is None: return self
        def get_maxdepth(node, depth = 0):
            if node is None: return depth
            return depth + 1 + max(get_maxdepth(node.left), get_maxdepth(node.right))
        def recurse(node, depth=0, side=None, fill=' '):
            if depth >= maxdepth: return
            if i == depth:
                recurse(node.left or none, depth + 1, 'l', dash if side == 'r' else fill)
                print(node.value, end='')
                recurse(node.right or none, depth + 1, 'r', dash if side == 'l' else fill)
            else:
                recurse(node.left or none, depth + 1, 'l', fill)
                if i == depth + 1:
                    wid = len(str(node.value))
                    half = int(wid / 2)
                    if wid == 2 * half + 1:
                        s = dash * half + tee + dash * half
                    else:
                        s = dash * (half - 1) + tee + dash * half
                    print(s, end='')
                else:
                    print(fill * len(str(node.value)), end='')
                recurse(node.right or none, depth + 1, 'r', fill)
        maxdepth = get_maxdepth(self.root.right)
        for i in range(0, maxdepth):
            print(f'{i:<3}', end='')
            recurse(self.root.right)
            print()
        print()
        return self
print()
print()
tree = BinTree()
tree.add(3, 1, 4, 1, 5, 9, 2, 6).print('added digits of pi')
tree.add(999999).print('added 999999')
tree.add(3).print('added 3, which matches root')
tree.add(1, 2, 3, 4, 5, 6).print('added sequence 1..6')
print('find(2) -->', tree.find(2))
print('find(88) -->', tree.find(88))
tree.remove(3).print('removed 3')
tree.remove(3).print('removed 3')
tree.remove(3).print('removed 3')
tree.remove(1).print('removed 1')
tree.remove(1).print('removed 1')
tree.remove(1).print('removed 1')
tree.remove(4).print('remove 4')
tree.remove(5).print('remove 5')
tree.remove(6).print('remove 6')
tree.remove(4, 5, 6).print('removed 4 5 6')
print('done')
