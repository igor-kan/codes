"""Free-list management algorithms (first-fit, best-fit, worst-fit)."""
from dataclasses import dataclass


@dataclass
class Hole:
    start: int
    size: int


def first_fit(holes: list[Hole], size: int) -> int:
    for i, hole in enumerate(holes):
        if hole.size >= size:
            return i
    return -1


def best_fit(holes: list[Hole], size: int) -> int:
    candidates = [i for i, h in enumerate(holes) if h.size >= size]
    return min(candidates, key=lambda i: holes[i].size) if candidates else -1


def worst_fit(holes: list[Hole], size: int) -> int:
    candidates = [i for i, h in enumerate(holes) if h.size >= size]
    return max(candidates, key=lambda i: holes[i].size) if candidates else -1


if __name__ == "__main__":
    holes = [Hole(0, 100), Hole(200, 30), Hole(400, 60)]
    assert first_fit(holes, 50) == 0
    assert best_fit(holes, 50) == 2
    assert worst_fit(holes, 50) == 0
    print("free space heuristics ok")
