"""2D kd-tree with nearest-neighbour search."""
import math


class Node:
    __slots__ = ("point", "axis", "left", "right")

    def __init__(self, point: tuple[float, float], axis: int) -> None:
        self.point, self.axis = point, axis
        self.left = self.right = None


def build(points: list[tuple[float, float]], depth: int = 0) -> Node | None:
    if not points:
        return None
    axis = depth % 2
    points = sorted(points, key=lambda p: p[axis])
    mid = len(points) // 2
    node = Node(points[mid], axis)
    node.left = build(points[:mid], depth + 1)
    node.right = build(points[mid + 1:], depth + 1)
    return node


def _distance(a, b) -> float:
    return math.dist(a, b)


def nearest(node: Node | None, target: tuple[float, float], best: tuple | None = None):
    if node is None:
        return best
    if best is None or _distance(node.point, target) < best[0]:
        best = (_distance(node.point, target), node.point)
    diff = target[node.axis] - node.point[node.axis]
    near, far = (node.left, node.right) if diff < 0 else (node.right, node.left)
    best = nearest(near, target, best)
    if abs(diff) < best[0]:
        best = nearest(far, target, best)
    return best


if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    tree = build(points)
    assert nearest(tree, (9, 2))[1] == (8, 1)
    print("kd-tree ok")
