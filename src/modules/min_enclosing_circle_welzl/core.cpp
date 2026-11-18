#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_min_enclosing_circle_welzl {

static double dist2d(Point2D a, Point2D b) {
    return std::hypot(a.x - b.x, a.y - b.y);
}

static bool in_disk(Disk2D d, Point2D p) {
    return dist2d({d.cx, d.cy}, p) <= d.r + 1e-9;
}

Disk2D disk_from_two(Point2D a, Point2D b) {
    return {(a.x + b.x) * 0.5, (a.y + b.y) * 0.5, dist2d(a, b) * 0.5};
}

Disk2D disk_from_three(Point2D a, Point2D b, Point2D c) {
    double d = 2.0 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
    if (std::fabs(d) < 1e-12) return {0, 0, 1e18};
    double a2 = a.x * a.x + a.y * a.y;
    double b2 = b.x * b.x + b.y * b.y;
    double c2 = c.x * c.x + c.y * c.y;
    double ux = (a2 * (b.y - c.y) + b2 * (c.y - a.y) + c2 * (a.y - b.y)) / d;
    double uy = (a2 * (c.x - b.x) + b2 * (a.x - c.x) + c2 * (b.x - a.x)) / d;
    return {ux, uy, dist2d({ux, uy}, a)};
}

Disk2D minimum_enclosing_disk(const std::vector<Point2D>& pts) {
    Disk2D d = {pts[0].x, pts[0].y, 0.0};
    int n = static_cast<int>(pts.size());
    for (int i = 1; i < n; ++i) {
        if (!in_disk(d, pts[i])) {
            d = {pts[i].x, pts[i].y, 0.0};
            for (int j = 0; j < i; ++j) {
                if (!in_disk(d, pts[j])) {
                    d = disk_from_two(pts[i], pts[j]);
                    for (int k = 0; k < j; ++k) {
                        if (!in_disk(d, pts[k])) d = disk_from_three(pts[i], pts[j], pts[k]);
                    }
                }
            }
        }
    }
    return d;
}

} // namespace codes_min_enclosing_circle_welzl
