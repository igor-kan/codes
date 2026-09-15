// Nelder-Mead minimisation (Numerical Recipes 10.4).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <vector>

std::vector<double> nelderMead(const std::function<double(const std::vector<double> &)> &f,
                               std::vector<double> start, double step = 0.5,
                               double tolerance = 1e-10, int maxIterations = 2000) {
    int n = static_cast<int>(start.size());
    std::vector<std::vector<double>> simplex{start};
    for (int i = 0; i < n; ++i) {
        std::vector<double> point = start;
        point[i] += step;
        simplex.push_back(point);
    }
    auto value = [&](const std::vector<double> &p) { return f(p); };
    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        std::sort(simplex.begin(), simplex.end(),
                  [&](const std::vector<double> &x, const std::vector<double> &y) { return value(x) < value(y); });
        double spread = 0.0;
        for (int i = 0; i < n; ++i) spread = std::max(spread, std::abs(simplex[0][i] - simplex[n][i]));
        if (spread < tolerance) break;
        std::vector<double> centroid(n, 0.0);
        for (int j = 0; j < n; ++j) for (int i = 0; i < n; ++i) centroid[i] += simplex[j][i] / n;
        std::vector<double> worst = simplex[n];
        std::vector<double> reflected(n), expanded(n), contracted(n);
        for (int i = 0; i < n; ++i) reflected[i] = centroid[i] + (centroid[i] - worst[i]);
        if (value(simplex[0]) <= value(reflected) && value(reflected) < value(simplex[n - 1])) simplex[n] = reflected;
        else if (value(reflected) < value(simplex[0])) {
            for (int i = 0; i < n; ++i) expanded[i] = centroid[i] + 2.0 * (centroid[i] - worst[i]);
            simplex[n] = value(expanded) < value(reflected) ? expanded : reflected;
        } else {
            for (int i = 0; i < n; ++i) contracted[i] = centroid[i] + 0.5 * (worst[i] - centroid[i]);
            if (value(contracted) < value(worst)) simplex[n] = contracted;
            else for (int j = 1; j <= n; ++j)
                for (int i = 0; i < n; ++i) simplex[j][i] = (simplex[0][i] + simplex[j][i]) / 2.0;
        }
    }
    std::sort(simplex.begin(), simplex.end(),
              [&](const std::vector<double> &x, const std::vector<double> &y) { return value(x) < value(y); });
    return simplex[0];
}

int main() {
    auto result = nelderMead([](const std::vector<double> &p) {
        return (p[0] - 3.0) * (p[0] - 3.0) + (p[1] + 2.0) * (p[1] + 2.0);
    }, {0.0, 0.0});
    assert(std::abs(result[0] - 3.0) < 1e-4 && std::abs(result[1] + 2.0) < 1e-4);
    std::cout << "nelder mead ok\n";
    return 0;
}
