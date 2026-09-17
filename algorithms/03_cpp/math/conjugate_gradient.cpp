/**
 * Conjugate Gradient Linear Solver in C++ (Numerical Recipes 3rd Ed. Chapter 2.7)
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

double dot(const std::vector<double>& a, const std::vector<double>& b) {
    double sum = 0.0;
    for (size_t i = 0; i < a.size(); i++) sum += a[i] * b[i];
    return sum;
}

std::vector<double> matVec(const std::vector<std::vector<double>>& A, const std::vector<double>& v) {
    std::vector<double> res(A.size(), 0.0);
    for (size_t i = 0; i < A.size(); i++) res[i] = dot(A[i], v);
    return res;
}

std::vector<double> conjugateGradient(const std::vector<std::vector<double>>& A, const std::vector<double>& b, double tol = 1e-8, int maxIter = 50) {
    int n = b.size();
    std::vector<double> x(n, 0.0), r = b, p = r;
    double rsOld = dot(r, r);

    for (int iter = 0; iter < maxIter; iter++) {
        if (std::sqrt(rsOld) < tol) break;
        auto Ap = matVec(A, p);
        double alpha = rsOld / dot(p, Ap);
        for (int i = 0; i < n; i++) {
            x[i] += alpha * p[i];
            r[i] -= alpha * Ap[i];
        }
        double rsNew = dot(r, r);
        for (int i = 0; i < n; i++) {
            p[i] = r[i] + (rsNew / rsOld) * p[i];
        }
        rsOld = rsNew;
    }
    return x;
}

int main() {
    std::vector<std::vector<double>> A = {{4.0, 1.0}, {1.0, 3.0}};
    std::vector<double> b = {1.0, 2.0};
    auto x = conjugateGradient(A, b);
    assert(std::abs(x[0] - 1.0 / 11.0) < 1e-5);
    std::cout << "C++ Conjugate Gradient verified.\n";
    return 0;
}
