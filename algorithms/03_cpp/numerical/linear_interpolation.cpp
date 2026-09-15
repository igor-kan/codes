#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double linearInterpolation(const std::vector<double> &xs, const std::vector<double> &ys, double x) {
    if (x <= xs.front()) return ys.front();
    if (x >= xs.back()) return ys.back();
    for (size_t i = 1; i < xs.size(); ++i) {
        if (x <= xs[i]) {
            double slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1]);
            return ys[i - 1] + slope * (x - xs[i - 1]);
        }
    }
    return ys.back();
}

int main() {
    assert(std::abs(linearInterpolation({0, 1, 2}, {0, 2, 4}, 0.5) - 1.0) < 1e-12);
    assert(std::abs(linearInterpolation({0, 1, 4}, {0, 1, 2}, 2.5) - 1.5) < 1e-12);
    std::cout << "linear interpolation ok\n";
    return 0;
}
