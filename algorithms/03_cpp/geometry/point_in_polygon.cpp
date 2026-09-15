// Ray-casting point-in-polygon test.
#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

bool inside(const std::vector<std::pair<double, double>> &poly, double px, double py) {
    bool in = false;
    const int n = static_cast<int>(poly.size());
    for (int i = 0, j = n - 1; i < n; j = i++) {
        auto [xi, yi] = poly[i];
        auto [xj, yj] = poly[j];
        if (((yi > py) != (yj > py)) && (px < (xj - xi) * (py - yi) / (yj - yi) + xi)) in = !in;
    }
    return in;
}

int main() {
    std::vector<std::pair<double, double>> square{{0, 0}, {4, 0}, {4, 4}, {0, 4}};
    assert(inside(square, 2, 2) && !inside(square, 5, 5));
    std::cout << "point in polygon ok\n";
    return 0;
}
