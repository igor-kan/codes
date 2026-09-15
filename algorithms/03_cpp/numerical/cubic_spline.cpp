// Natural cubic spline (Numerical Recipes 3.3).
#include <cassert>
#include <iostream>
#include <vector>

struct Spline { std::vector<double> b, c, d; };

Spline naturalCubicSpline(const std::vector<double> &xs, const std::vector<double> &ys) {
    int n = static_cast<int>(xs.size());
    std::vector<double> h(n - 1), alpha(n, 0.0), l(n, 0.0), mu(n, 0.0), z(n, 0.0);
    for (int i = 0; i < n - 1; ++i) h[i] = xs[i + 1] - xs[i];
    for (int i = 1; i < n - 1; ++i)
        alpha[i] = 3.0 / h[i] * (ys[i + 1] - ys[i]) - 3.0 / h[i - 1] * (ys[i] - ys[i - 1]);
    l[0] = 1.0;
    for (int i = 1; i < n - 1; ++i) {
        l[i] = 2.0 * (xs[i + 1] - xs[i - 1]) - h[i - 1] * mu[i - 1];
        mu[i] = h[i] / l[i];
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i];
    }
    Spline spline;
    spline.b.assign(n - 1, 0.0);
    spline.c.assign(n, 0.0);
    spline.d.assign(n - 1, 0.0);
    for (int j = n - 2; j >= 0; --j) {
        spline.c[j] = z[j] - mu[j] * spline.c[j + 1];
        spline.b[j] = (ys[j + 1] - ys[j]) / h[j] - h[j] * (spline.c[j + 1] + 2.0 * spline.c[j]) / 3.0;
        spline.d[j] = (spline.c[j + 1] - spline.c[j]) / (3.0 * h[j]);
    }
    return spline;
}

double evaluate(const std::vector<double> &xs, const std::vector<double> &ys,
                const Spline &spline, double x) {
    int n = static_cast<int>(xs.size());
    int segment = n - 2;
    for (int i = 0; i < n - 1; ++i) if (xs[i] <= x && x <= xs[i + 1]) { segment = i; break; }
    double dx = x - xs[segment];
    return ys[segment] + spline.b[segment] * dx + spline.c[segment] * dx * dx + spline.d[segment] * dx * dx * dx;
}

int main() {
    std::vector<double> xs{0, 1, 2, 3}, ys{0, 1, 0, 1};
    Spline spline = naturalCubicSpline(xs, ys);
    for (size_t i = 0; i < xs.size(); ++i) assert(std::abs(evaluate(xs, ys, spline, xs[i]) - ys[i]) < 1e-9);
    std::cout << "cubic spline ok\n";
    return 0;
}
