// Levenberg-Marquardt least squares (Numerical Recipes 15.5).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <vector>

using Vec = std::vector<double>;

Vec solve(std::vector<Vec> a, Vec b) {
    int n = static_cast<int>(b.size());
    for (int col = 0; col < n; ++col) {
        int pivot = col;
        for (int r = col + 1; r < n; ++r) if (std::abs(a[r][col]) > std::abs(a[pivot][col])) pivot = r;
        std::swap(a[col], a[pivot]);
        std::swap(b[col], b[pivot]);
        for (int r = col + 1; r < n; ++r) {
            double factor = a[r][col] / a[col][col];
            for (int k = col; k < n; ++k) a[r][k] -= factor * a[col][k];
            b[r] -= factor * b[col];
        }
    }
    Vec x(n);
    for (int r = n - 1; r >= 0; --r) {
        double s = b[r];
        for (int k = r + 1; k < n; ++k) s -= a[r][k] * x[k];
        x[r] = s / a[r][r];
    }
    return x;
}

Vec levenbergMarquardt(const std::function<double(double, const Vec &)> &model,
                       const std::function<Vec(double, const Vec &)> &jacobian,
                       const Vec &xs, const Vec &ys, Vec parameters,
                       double damping = 1e-3, int maxIterations = 200) {
    int n = static_cast<int>(xs.size());
    int columns = static_cast<int>(parameters.size());
    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        Vec residuals(n);
        std::vector<Vec> jac(n);
        for (int i = 0; i < n; ++i) { residuals[i] = ys[i] - model(xs[i], parameters); jac[i] = jacobian(xs[i], parameters); }
        std::vector<Vec> jtj(columns, Vec(columns, 0.0));
        Vec jtr(columns, 0.0);
        for (int a = 0; a < columns; ++a) {
            for (int b = 0; b < columns; ++b)
                for (int i = 0; i < n; ++i) jtj[a][b] += jac[i][a] * jac[i][b];
            for (int i = 0; i < n; ++i) jtr[a] += jac[i][a] * residuals[i];
        }
        std::vector<Vec> updated = jtj;
        for (int a = 0; a < columns; ++a) updated[a][a] += damping;
        Vec delta = solve(updated, jtr);
        Vec candidate(columns);
        for (int i = 0; i < columns; ++i) candidate[i] = parameters[i] + delta[i];
        double cost = 0.0, candidateCost = 0.0;
        for (int i = 0; i < n; ++i) {
            cost += residuals[i] * residuals[i];
            double r = ys[i] - model(xs[i], candidate);
            candidateCost += r * r;
        }
        if (candidateCost < cost) parameters = candidate; else damping *= 10.0;
    }
    return parameters;
}

int main() {
    Vec xs{0, 1, 2, 3, 4}, ys;
    for (double x : xs) ys.push_back(1.0 + 2.0 * x + 3.0 * x * x);
    auto model = [](double x, const Vec &p) { return p[0] + p[1] * x + p[2] * x * x; };
    auto jacobian = [](double x, const Vec &) { return Vec{1.0, x, x * x}; };
    Vec fitted = levenbergMarquardt(model, jacobian, xs, ys, Vec{0.0, 0.0, 0.0});
    assert(std::abs(fitted[0] - 1.0) < 1e-6 && std::abs(fitted[1] - 2.0) < 1e-6 && std::abs(fitted[2] - 3.0) < 1e-6);
    std::cout << "levenberg marquardt ok\n";
    return 0;
}
