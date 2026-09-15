"""k-nearest-neighbours classifier."""
import math
from collections import Counter


def knn(train: list[tuple[list[float], str]], point: list[float], k: int = 3) -> str:
    distances = [
        (math.dist(features, point), label) for features, label in train
    ]
    nearest = sorted(distances)[:k]
    return Counter(label for _, label in nearest).most_common(1)[0][0]


if __name__ == "__main__":
    data = [
        ([1, 1], "a"), ([2, 2], "a"), ([3, 3], "a"),
        ([6, 6], "b"), ([7, 7], "b"), ([8, 8], "b"),
    ]
    assert knn(data, [2, 1]) == "a"
    assert knn(data, [7, 6]) == "b"
    print("knn ok")
