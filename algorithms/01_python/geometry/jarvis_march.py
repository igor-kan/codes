"""Jarvis march (gift wrapping) convex hull."""
def orientation(o, a, b) -> int:
    value = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    return 0 if value == 0 else (1 if value > 0 else -1)


def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    points = sorted(set(points))
    if len(points) < 3:
        return points
    start = min(points, key=lambda p: (p[1], p[0]))
    hull = []
    current = start
    while True:
        hull.append(current)
        nxt = points[0] if points[0] != current else points[1]
        for candidate in points:
            if candidate == current:
                continue
            turn = orientation(current, nxt, candidate)
            if turn == -1 or (turn == 0 and
                              (candidate[0] - current[0]) ** 2 + (candidate[1] - current[1]) ** 2
                              > (nxt[0] - current[0]) ** 2 + (nxt[1] - current[1]) ** 2):
                nxt = candidate
        current = nxt
        if current == start:
            break
    return hull


if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 2), (3, 0), (3, 3), (0, 3)]
    hull = convex_hull(points)
    assert (1, 1) not in hull and (2, 2) not in hull
    assert len(hull) == 4
    print("jarvis march ok")
