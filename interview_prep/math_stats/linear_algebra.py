"""Vector operations: dot, cross, norm and projection."""
import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def cross(a: list[float], b: list[float]) -> list[float]:
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def project(a: list[float], b: list[float]) -> list[float]:
    scale = dot(a, b) / dot(b, b)
    return [scale * value for value in b]


if __name__ == "__main__":
    assert dot([1, 2, 3], [4, 5, 6]) == 32
    assert cross([1, 0, 0], [0, 1, 0]) == [0, 0, 1]
    assert abs(norm([3, 4]) - 5) < 1e-9
    assert project([2, 2], [1, 0]) == [2.0, 0.0]
    print("linear algebra ok")
