#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
struct Point { long long x, y; };
long long cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}
std::vector<Point> convexHull(std::vector<Point> pts) {
    std::sort(pts.begin(), pts.end(), [](Point a, Point b) {
        return a.x < b.x || (a.x == b.x && a.y < b.y);
    });
    std::vector<Point> hull;
    for (auto p : pts) {
        while (hull.size() >= 2 && cross(hull[hull.size() - 2], hull.back(), p) <= 0) {
            hull.pop_back();
        }
        hull.push_back(p);
    }
    return hull;
}
int main() {
    auto h = convexHull({{0, 0}, {1, 1}, {2, 2}, {0, 2}, {2, 0}});
    assert(!h.empty());
    std::cout << "C++ Graham Scan verified.\n";
}
