"""Splay tree with top-down splaying on access."""
class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key: int) -> None:
        self.key, self.left, self.right = key, None, None


def _rotate_right(node: Node) -> Node:
    left = node.left
    node.left, left.right = left.right, node
    return left


def _rotate_left(node: Node) -> Node:
    right = node.right
    node.right, right.left = right.left, node
    return right


def splay(root: Node | None, key: int) -> Node | None:
    if root is None or root.key == key:
        return root
    if key < root.key:
        if root.left is None:
            return root
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = _rotate_right(root)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = _rotate_left(root.left)
        return _rotate_right(root) if root.left else root
    if root.right is None:
        return root
    if key > root.right.key:
        root.right.right = splay(root.right.right, key)
        root = _rotate_left(root)
    elif key < root.right.key:
        root.right.left = splay(root.right.left, key)
        if root.right.left:
            root.right = _rotate_right(root.right)
    return _rotate_left(root) if root.right else root


def insert(root: Node | None, key: int) -> Node:
    if root is None:
        return Node(key)
    root = splay(root, key)
    if root.key == key:
        return root
    node = Node(key)
    if key < root.key:
        node.left, node.right, root.left = root.left, root, None
    else:
        node.right, node.left, root.right = root.right, root, None
    return node


def inorder(root: Node | None) -> list[int]:
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []


if __name__ == "__main__":
    root = None
    for key in [10, 20, 30, 40, 50, 25]:
        root = insert(root, key)
    assert inorder(root) == [10, 20, 25, 30, 40, 50]
    print("splay tree ok")
