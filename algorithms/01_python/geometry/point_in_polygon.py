"""Ray-casting point-in-polygon test."""
def point_in_polygon(point: tuple[float, float], polygon: list[tuple[float, float]]) -> bool:
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            x_intersection = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if x < x_intersection:
                inside = not inside
    return inside


if __name__ == "__main__":
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    assert point_in_polygon((2, 2), square)
    assert not point_in_polygon((5, 5), square)
    print("point in polygon ok")
