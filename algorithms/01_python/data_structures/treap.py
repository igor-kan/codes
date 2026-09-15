"""Treap: BST + heap priorities for expected balance."""
import random


class Node:
    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key: int) -> None:
        self.key, self.priority = key, random.random()
        self.left = self.right = None


def split(root: Node | None, key: int) -> tuple[Node | None, Node | None]:
    if root is None:
        return None, None
    if root.key <= key:
        left, right = split(root.right, key)
        root.right = left
        return root, right
    left, right = split(root.left, key)
    root.left = right
    return left, root


def merge(left: Node | None, right: Node | None) -> Node | None:
    if not left or not right:
        return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    right.left = merge(left, right.left)
    return right


def insert(root: Node | None, key: int) -> Node:
    left, right = split(root, key)
    return merge(merge(left, Node(key)), right)


def inorder(root: Node | None) -> list[int]:
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []


if __name__ == "__main__":
    random.seed(0)
    root = None
    for key in [5, 2, 8, 1, 9, 3]:
        root = insert(root, key)
    assert inorder(root) == [1, 2, 3, 5, 8, 9]
    print("treap ok")
