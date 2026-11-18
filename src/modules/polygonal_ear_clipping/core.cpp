#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_polygonal_ear_clipping {

static double cross2(Vec2 a, Vec2 b, Vec2 c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

static bool pt_in_tri(Vec2 p, Vec2 a, Vec2 b, Vec2 c) {
    return cross2(a, b, p) >= -1e-12 && cross2(b, c, p) >= -1e-12 && cross2(c, a, p) >= -1e-12;
}

double polygon_signed_area2(const std::vector<Vec2>& poly) {
    double s = 0.0;
    int n = static_cast<int>(poly.size());
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        s += poly[i].x * poly[j].y - poly[j].x * poly[i].y;
    }
    return s;
}

std::vector<TriIdx> ear_clip_triangulate(const std::vector<Vec2>& poly) {
    std::vector<int> V(poly.size());
    std::iota(V.begin(), V.end(), 0);
    std::vector<TriIdx> tris;
    while (V.size() > 3) {
        int m = static_cast<int>(V.size());
        bool clipped = false;
        for (int i = 0; i < m; ++i) {
            int i0 = V[(i + m - 1) % m], i1 = V[i], i2 = V[(i + 1) % m];
            if (cross2(poly[i0], poly[i1], poly[i2]) <= 1e-12) continue;
            bool empty = true;
            for (int j = 0; j < m; ++j) {
                int idx = V[j];
                if (idx == i0 || idx == i1 || idx == i2) continue;
                if (pt_in_tri(poly[idx], poly[i0], poly[i1], poly[i2])) { empty = false; break; }
            }
            if (empty) {
                tris.push_back({i0, i1, i2});
                V.erase(V.begin() + i);
                clipped = true;
                break;
            }
        }
        if (!clipped) break;
    }
    if (V.size() == 3) tris.push_back({V[0], V[1], V[2]});
    return tris;
}

} // namespace codes_polygonal_ear_clipping
