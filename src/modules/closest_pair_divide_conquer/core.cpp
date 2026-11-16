#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>

namespace codes_closest_pair_divide_conquer {
static double d2(const Point2D& a, const Point2D& b) {
    double dx = a.x - b.x, dy = a.y - b.y;
    return dx * dx + dy * dy;
}

static PairResult dc_rec(const std::vector<Point2D>& px, std::vector<Point2D>& py, std::vector<Point2D>& tmp, std::size_t l, std::size_t r) {
    std::size_t len = r - l;
    auto cmp_y = [](const Point2D& a, const Point2D& b) { return a.y < b.y; };
    if (len <= 3) {
        PairResult best{px[l].id, px[l + 1].id, d2(px[l], px[l + 1])};
        for (std::size_t i = l; i < r; ++i) {
            for (std::size_t j = i + 1; j < r; ++j) {
                double dist = d2(px[i], px[j]);
                if (dist < best.dist_sq) best = {px[i].id, px[j].id, dist};
            }
        }
        std::sort(py.begin() + static_cast<std::ptrdiff_t>(l), py.begin() + static_cast<std::ptrdiff_t>(r), cmp_y);
        return best;
    }
    std::size_t mid = l + len / 2;
    double midx = px[mid].x;
    PairResult dl = dc_rec(px, py, tmp, l, mid);
    PairResult dr = dc_rec(px, py, tmp, mid, r);
    PairResult best = (dl.dist_sq <= dr.dist_sq) ? dl : dr;
    std::merge(py.begin() + static_cast<std::ptrdiff_t>(l), py.begin() + static_cast<std::ptrdiff_t>(mid),
               py.begin() + static_cast<std::ptrdiff_t>(mid), py.begin() + static_cast<std::ptrdiff_t>(r),
               tmp.begin() + static_cast<std::ptrdiff_t>(l), cmp_y);
    std::copy(tmp.begin() + static_cast<std::ptrdiff_t>(l), tmp.begin() + static_cast<std::ptrdiff_t>(r),
              py.begin() + static_cast<std::ptrdiff_t>(l));
    std::vector<Point2D> strip;
    for (std::size_t i = l; i < r; ++i) {
        double dx = py[i].x - midx;
        if (dx * dx < best.dist_sq) strip.push_back(py[i]);
    }
    for (std::size_t i = 0; i < strip.size(); ++i) {
        for (std::size_t j = i + 1; j < strip.size(); ++j) {
            double dy = strip[j].y - strip[i].y;
            if (dy * dy >= best.dist_sq) break;
            double cand = d2(strip[i], strip[j]);
            if (cand < best.dist_sq) best = {strip[i].id, strip[j].id, cand};
        }
    }
    return best;
}

PairResult closest_pair_dc(std::vector<Point2D> pts) {
    if (validate_points(pts) != Status::Ok) return {};
    for (std::size_t i = 0; i < pts.size(); ++i) pts[i].id = i;
    std::sort(pts.begin(), pts.end(), [](const Point2D& a, const Point2D& b) {
        return (a.x != b.x) ? (a.x < b.x) : (a.y < b.y);
    });
    std::vector<Point2D> py = pts;
    std::vector<Point2D> tmp(pts.size());
    return dc_rec(pts, py, tmp, 0, pts.size());
}
} // namespace codes_closest_pair_divide_conquer
