"""Self-balancing AVL tree."""
class Node:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key: int) -> None:
        self.key, self.left, self.right, self.height = key, None, None, 1


def height(node: Node | None) -> int:
    return node.height if node else 0


def update(node: Node) -> None:
    node.height = 1 + max(height(node.left), height(node.right))


def rotate_right(y: Node) -> Node:
    x = y.left
    y.left, x.right = x.right, y
    update(y)
    update(x)
    return x


def rotate_left(x: Node) -> Node:
    y = x.right
    x.right, y.left = y.left, x
    update(x)
    update(y)
    return y


def balance(node: Node) -> Node:
    update(node)
    factor = height(node.left) - height(node.right)
    if factor > 1:
        if height(node.left.left) < height(node.left.right):
            node.left = rotate_left(node.left)
        return rotate_right(node)
    if factor < -1:
        if height(node.right.right) < height(node.right.left):
            node.right = rotate_right(node.right)
        return rotate_left(node)
    return node


def insert(node: Node | None, key: int) -> Node:
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return balance(node)


def inorder(node: Node | None) -> list[int]:
    return inorder(node.left) + [node.key] + inorder(node.right) if node else []


if __name__ == "__main__":
    root = None
    for key in [10, 20, 30, 40, 50, 25]:
        root = insert(root, key)
    assert inorder(root) == [10, 20, 25, 30, 40, 50]
    assert height(root) <= 3
    print("avl tree ok")
