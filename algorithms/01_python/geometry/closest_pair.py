"""Closest pair of points by divide and conquer."""
import math


def closest_pair(points: list[tuple[float, float]]) -> float:
    points = sorted(points)

    def brute(pts: list) -> float:
        return min((math.dist(pts[i], pts[j])
                    for i in range(len(pts)) for j in range(i + 1, len(pts))),
                   default=float("inf"))

    def solve(pts: list) -> float:
        if len(pts) <= 3:
            return brute(pts)
        mid = len(pts) // 2
        mid_x = pts[mid][0]
        best = min(solve(pts[:mid]), solve(pts[mid:]))
        strip = [p for p in pts if abs(p[0] - mid_x) < best]
        strip.sort(key=lambda p: p[1])
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= best:
                    break
                best = min(best, math.dist(strip[i], strip[j]))
        return best

    return solve(points)


if __name__ == "__main__":
    pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    assert abs(closest_pair(pts) - math.sqrt(2)) < 1e-9
    print("closest pair ok")
