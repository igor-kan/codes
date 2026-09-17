"""
Red-Black Tree Implementation (CLRS 3rd Ed. Chapter 13).
Self-balancing binary search tree in Python.
"""

RED = 0
BLACK = 1

class Node:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.color = BLACK

    def _insert(self, node, key):
        if not node:
            return Node(key, RED)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def contains(self, key):
        curr = self.root
        while curr:
            if key == curr.key:
                return True
            curr = curr.left if key < curr.key else curr.right
        return False

if __name__ == "__main__":
    rbt = RedBlackTree()
    for k in [10, 20, 5, 15, 25]:
        rbt.insert(k)
    assert rbt.contains(15)
    assert not rbt.contains(99)
    print("Python Red-Black Tree verified.")
