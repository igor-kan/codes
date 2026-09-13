/**
 * Monotone Chain Convex Hull in C++.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

struct Point {
    double x, y;
    bool operator<(const Point& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(const Point& o) const {
        return x == o.x && y == o.y;
    }
};

double cross_product(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

std::vector<Point> convex_hull(std::vector<Point> pts) {
    std::sort(pts.begin(), pts.end());
    pts.erase(std::unique(pts.begin(), pts.end()), pts.end());
    int n = pts.size();
    if (n <= 1) return pts;

    std::vector<Point> hull;

    // Lower hull
    for (int i = 0; i < n; ++i) {
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull.back(), pts[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(pts[i]);
    }

    // Upper hull
    size_t lower_size = hull.size();
    for (int i = n - 2; i >= 0; --i) {
        while (hull.size() > lower_size && cross_product(hull[hull.size() - 2], hull.back(), pts[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(pts[i]);
    }

    hull.pop_back(); // remove duplicate first/last point
    return hull;
}

int main() {
    std::vector<Point> pts = {
        {0.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {2.0, 1.0},
        {3.0, 0.0}, {0.0, 0.0}, {3.0, 3.0}, {1.5, 1.5}
    };

    auto hull = convex_hull(pts);
    assert(hull.size() == 4);
    assert(hull[0] == Point({0.0, 0.0}));
    assert(hull[1] == Point({3.0, 0.0}));
    assert(hull[2] == Point({3.0, 3.0}));
    assert(hull[3] == Point({0.0, 3.0}));

    std::cout << "[C++ Convex Hull] Hull computed with " << hull.size() << " vertices." << std::endl;
    return 0;
}
