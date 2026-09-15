"""Persistent segment tree for range-sum queries over versions."""
class Node:
    __slots__ = ("total", "left", "right")

    def __init__(self, total: int = 0, left=None, right=None) -> None:
        self.total, self.left, self.right = total, left, right


def build(values: list[int], lo: int, hi: int) -> Node:
    if lo == hi:
        return Node(values[lo])
    mid = (lo + hi) // 2
    left = build(values, lo, mid)
    right = build(values, mid + 1, hi)
    return Node(left.total + right.total, left, right)


def update(node: Node, lo: int, hi: int, index: int, value: int) -> Node:
    if lo == hi:
        return Node(value)
    mid = (lo + hi) // 2
    if index <= mid:
        left = update(node.left, lo, mid, index, value)
        return Node(left.total + node.right.total, left, node.right)
    right = update(node.right, mid + 1, hi, index, value)
    return Node(node.left.total + right.total, node.left, right)


def query(node: Node, lo: int, hi: int, left_q: int, right_q: int) -> int:
    if right_q < lo or hi < left_q:
        return 0
    if left_q <= lo and hi <= right_q:
        return node.total
    mid = (lo + hi) // 2
    return query(node.left, lo, mid, left_q, right_q) + query(node.right, mid + 1, hi, left_q, right_q)


if __name__ == "__main__":
    root0 = build([1, 2, 3, 4], 0, 3)
    root1 = update(root0, 0, 3, 1, 10)
    assert query(root0, 0, 3, 0, 3) == 10
    assert query(root1, 0, 3, 0, 3) == 18
    assert query(root0, 0, 3, 1, 2) == 5
    print("persistent segment tree ok")
