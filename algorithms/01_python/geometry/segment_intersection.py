"""Intersection point of two lines, if any."""
def intersection(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
    return px, py


if __name__ == "__main__":
    assert intersection(((0, 0), (2, 2)), ((0, 2), (2, 0))) == (1.0, 1.0)
    assert intersection(((0, 0), (1, 1)), ((2, 2), (3, 3))) is None
    print("segment intersection ok")
