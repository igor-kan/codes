"""Red-black tree insertion with recolouring and rotations."""
RED, BLACK = True, False


class Node:
    __slots__ = ("key", "color", "left", "right", "parent")

    def __init__(self, key: int, color: bool = RED) -> None:
        self.key, self.color = key, color
        self.left = self.right = self.parent = None


class RedBlackTree:
    def __init__(self) -> None:
        self.nil = Node(0, BLACK)
        self.root = self.nil

    def _rotate_left(self, x: Node) -> None:
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x: Node) -> None:
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key: int) -> None:
        node = Node(key)
        node.left = node.right = self.nil
        parent, current = None, self.root
        while current is not self.nil:
            parent = current
            current = current.left if key < current.key else current.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self._fix(node)

    def _fix(self, node: Node) -> None:
        while node.parent and node.parent.color is RED:
            parent = node.parent
            grand = parent.parent
            if parent is grand.left:
                uncle = grand.right
                if uncle.color is RED:
                    parent.color = uncle.color = BLACK
                    grand.color = RED
                    node = grand
                else:
                    if node is parent.right:
                        node = parent
                        self._rotate_left(node)
                    node.parent.color = BLACK
                    grand.color = RED
                    self._rotate_right(grand)
            else:
                uncle = grand.left
                if uncle.color is RED:
                    parent.color = uncle.color = BLACK
                    grand.color = RED
                    node = grand
                else:
                    if node is parent.left:
                        node = parent
                        self._rotate_right(node)
                    node.parent.color = BLACK
                    grand.color = RED
                    self._rotate_left(grand)
        self.root.color = BLACK

    def inorder(self) -> list[int]:
        result, stack, node = [], [], self.root
        while stack or node is not self.nil:
            while node is not self.nil:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.key)
            node = node.right
        return result


if __name__ == "__main__":
    tree = RedBlackTree()
    for key in [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]:
        tree.insert(key)
    assert tree.inorder() == sorted([7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13])
    assert tree.root.color is BLACK
    print("red-black tree ok")
