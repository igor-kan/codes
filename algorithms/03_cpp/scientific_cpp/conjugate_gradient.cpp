#include "conjugate_gradient.hpp"
#include <cmath>

static double dot_prod(const std::vector<double>& u, const std::vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) sum += u[i] * v[i];
    return sum;
}

static std::vector<double> mat_vec(const std::vector<std::vector<double>>& A, const std::vector<double>& x) {
    size_t n = A.size();
    std::vector<double> y(n, 0.0);
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) y[i] += A[i][j] * x[j];
    }
    return y;
}

std::vector<double> solve_cg(const std::vector<std::vector<double>>& A,
                            const std::vector<double>& b,
                            double tol, int max_iter) {
    size_t n = b.size();
    std::vector<double> x(n, 0.0);
    std::vector<double> r = b;
    std::vector<double> p = r;
    double rsold = dot_prod(r, r);
    
    for (int iter = 0; iter < max_iter; ++iter) {
        if (std::sqrt(rsold) < tol) break;
        std::vector<double> Ap = mat_vec(A, p);
        double alpha = rsold / dot_prod(p, Ap);
        for (size_t i = 0; i < n; ++i) x[i] += alpha * p[i];
        for (size_t i = 0; i < n; ++i) r[i] -= alpha * Ap[i];
        double rsnew = dot_prod(r, r);
        for (size_t i = 0; i < n; ++i) p[i] = r[i] + (rsnew / rsold) * p[i];
        rsold = rsnew;
    }
    return x;
}
