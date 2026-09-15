"""Shoelace formula for polygon area and centroid."""
def area(polygon: list[tuple[float, float]]) -> float:
    total = 0.0
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2


def centroid(polygon: list[tuple[float, float]]) -> tuple[float, float]:
    n = len(polygon)
    signed = 0.0
    cx = cy = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        cross = x1 * y2 - x2 * y1
        signed += cross
        cx += (x1 + x2) * cross
        cy += (y1 + y2) * cross
    signed /= 2
    return cx / (6 * signed), cy / (6 * signed)


if __name__ == "__main__":
    assert area([(0, 0), (4, 0), (4, 4), (0, 4)]) == 16
    cx, cy = centroid([(0, 0), (4, 0), (4, 4), (0, 4)])
    assert abs(cx - 2) < 1e-9 and abs(cy - 2) < 1e-9
    print("polygon area ok")
