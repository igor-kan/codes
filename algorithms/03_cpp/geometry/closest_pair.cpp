// Closest pair of points (quadratic brute force).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

int main() {
    std::vector<std::pair<double, double>> pts{{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
    double best = 1e18;
    for (std::size_t i = 0; i < pts.size(); ++i)
        for (std::size_t j = i + 1; j < pts.size(); ++j)
            best = std::min(best, std::hypot(pts[i].first - pts[j].first, pts[i].second - pts[j].second));
    assert(std::abs(best - std::sqrt(2.0)) < 1e-9);
    std::cout << "closest=" << best << '\n';
    return 0;
}
