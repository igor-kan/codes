"""Monotone Chain (Andrew's Algorithm) for 2D Convex Hull.

Computes the minimal convex polygon containing a set of 2D points in O(N log N)
using 2D cross products for orientation tests.
"""

from typing import List, Tuple

Point = Tuple[float, float]

def cross_product_orientation(o: Point, a: Point, b: Point) -> float:
    """Returns 2D cross product of vector OA and OB.
    > 0: counter-clockwise turn (left)
    < 0: clockwise turn (right)
    = 0: collinear
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def monotone_chain_convex_hull(points: List[Point]) -> List[Point]:
    """Computes the convex hull in counter-clockwise order."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    # Lower hull
    lower: List[Point] = []
    for p in pts:
        while len(lower) >= 2 and cross_product_orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Upper hull
    upper: List[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross_product_orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull (last point of each is first of other)
    return lower[:-1] + upper[:-1]

if __name__ == "__main__":
    sample_points = [
        (0.0, 3.0), (2.0, 2.0), (1.0, 1.0), (2.0, 1.0),
        (3.0, 0.0), (0.0, 0.0), (3.0, 3.0), (1.5, 1.5)
    ]
    hull = monotone_chain_convex_hull(sample_points)
    expected_hull = [(0.0, 0.0), (3.0, 0.0), (3.0, 3.0), (0.0, 3.0)]
    assert hull == expected_hull, f"Unexpected hull: {hull}"
    print(f"[Python Convex Hull] Computed hull with {len(hull)} vertices: {hull}")
