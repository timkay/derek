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
        self.root = None
    def cut(self):
        """Removes the entire tree structure"""
        if self.root:
            self.root.cut()
            del self
            self.root = None
    def add(self, *values):
        """Adds a node to the tree. Ignores duplicates."""
        for value in values:
            node = self.root
            if node is None:
                self.root = node = Node(value)
                continue
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
        if self.root:
            self.root.print()
            print()
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

# print('added digits of pi:', end='')
tree = BinTree().add(3, 1, 4, 1, 5, 9, 2, 6).print()      #.print('added digits of pi')


# class binTree():
#     def __init__(self, _root=None):
#         self.active = False # Is this node in the structure?
#         self.value = None
#         self.connected = True # If False, will be removed by scan().
#         if _root == None:
#             self.root = self
#         else:
#             self.root = _root
#     def cut(self):
#         """Removes the entire tree structure"""
#         if self.active:
#             self.left.cut()
#             self.right.cut()
#         self.connected = False
#         del self
#     def add(self, value):
#         """Adds an item to the tree. Ignores duplicates."""
#         item = self
#         while True:
#             if not item.active:
#                 break
#             if value < item.value:
#                 item = item.left
#             elif value > item.value:
#                 item = item.right
#             else:
#                 return self
#         item.value = value
#         item._activate()
#         return self
#     def populate(self, *args):
#         """Adds multiple items to the tree"""
#         for i in args:
#             self.add(i)
#         return self
#     def print(self):
#         """Prints the whole tree in order"""
#         if self.active:
#             self.left.print()
#             print(self.value)
#             self.right.print()
#         return self
#     def remove(self):
#         """Drops a value from the tree"""
#         if self.root == self:
#             extraRoot = binTree()
#             self.left.reroot(extraRoot)
#             self.right.reroot(extraRoot)
#         self.left.reorganize()
#         self.right.reorganize()
#         self.connected = False
#         self.root.scan()
#         del self
#         if "extraRoot" in locals():
#             return extraRoot
#     def reorganize(self):
#         """Regenerates the tree structure from the root"""
#         if self.active:
#             if self.root == self:
#                 extraRoot = binTree()
#                 self.reroot(extraRoot)
#             self.root.add(self.value)
#             self.left.reorganize()
#             self.right.reorganize()
#         self.connected = False
#         del self
#         if "extraRoot" in locals():
#             return extraRoot
#     def reroot(self, root=None):
#         """Rebinds the tree structure to a different root"""
#         if root == None:
#             root = self
#         if self.active:
#             self.left.reroot(root)
#             self.right.reroot(root)
#         self.root = root
#         return self
#     def find(self, value):
#         """Finds an item in the tree."""
#         item = self
#         while item.active:
#             if value < item.value:
#                 item = item.left
#             elif value > item.value:
#                 item = item.right
#             elif value == item.value:
#                 return item, True
#         return None, False
#         return self
#     def scan(self):
#         """Checks a tree structure for sanity."""
#         if self.active:
#             self.left.scan()
#             if not self.left.connected:
#                 del self.left
#                 self.left = binTree()
#             self.right.scan()
#             if not self.right.connected:
#                 del self.right
#                 self.right = binTree()
#     def _activate(self):
#         self.left = binTree(self.root)
#         self.right = binTree(self.root)
#         self.active = True
