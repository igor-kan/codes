"""Intersection of two 2D line segments."""
def orientation(a, b, c) -> int:
    value = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    return 0 if value == 0 else (1 if value > 0 else -1)


def on_segment(a, b, c) -> bool:
    return (min(a[0], c[0]) <= b[0] <= max(a[0], c[0])
            and min(a[1], c[1]) <= b[1] <= max(a[1], c[1]))


def segments_intersect(p1, q1, p2, q2) -> bool:
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    return ((o1 == 0 and on_segment(p1, p2, q1)) or
            (o2 == 0 and on_segment(p1, q2, q1)) or
            (o3 == 0 and on_segment(p2, p1, q2)) or
            (o4 == 0 and on_segment(p2, q1, q2)))


if __name__ == "__main__":
    assert segments_intersect((0, 0), (10, 10), (0, 10), (10, 0))
    assert not segments_intersect((0, 0), (1, 1), (2, 2), (3, 3))
    print("line intersection ok")
