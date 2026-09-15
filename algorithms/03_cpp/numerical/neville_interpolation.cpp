#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double nevilleInterpolation(const std::vector<double> &xs, const std::vector<double> &ys, double x) {
    size_t n = xs.size();
    std::vector<double> table = ys;
    for (size_t k = 1; k < n; ++k)
        for (size_t i = 0; i < n - k; ++i)
            table[i] = ((x - xs[i + k]) * table[i] + (xs[i] - x) * table[i + 1]) / (xs[i] - xs[i + k]);
    return table[0];
}

int main() {
    assert(std::abs(nevilleInterpolation({0, 1, 2}, {1, 3, 2}, 1.5) - 2.875) < 1e-12);
    std::cout << "neville interpolation ok\n";
    return 0;
}
