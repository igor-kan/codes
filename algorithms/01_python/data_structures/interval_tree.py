"""Interval tree for overlap queries (augmented BST)."""
class Node:
    __slots__ = ("low", "high", "max_high", "left", "right")

    def __init__(self, low: int, high: int) -> None:
        self.low, self.high = low, high
        self.max_high = high
        self.left = self.right = None


def insert(node: Node | None, low: int, high: int) -> Node:
    if node is None:
        return Node(low, high)
    if low < node.low:
        node.left = insert(node.left, low, high)
    else:
        node.right = insert(node.right, low, high)
    node.max_high = max(node.max_high, high)
    return node


def overlap(node: Node | None, low: int, high: int) -> tuple[int, int] | None:
    if node is None:
        return None
    if node.low <= high and low <= node.high:
        return node.low, node.high
    if node.left and node.left.max_high >= low:
        return overlap(node.left, low, high)
    return overlap(node.right, low, high)


if __name__ == "__main__":
    root = None
    for interval in [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]:
        root = insert(root, *interval)
    assert overlap(root, 14, 16) is not None
    assert overlap(root, 100, 110) is None
    print("interval tree ok")
