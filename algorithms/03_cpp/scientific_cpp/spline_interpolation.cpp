#include "spline_interpolation.hpp"
#include <algorithm>

CubicSpline::CubicSpline(const std::vector<double>& x, const std::vector<double>& y)
    : x_(x), a_(y) {
    size_t n = x.size() - 1;
    b_.resize(n); d_.resize(n); c_.resize(n + 1, 0.0);
    std::vector<double> h(n);
    for (size_t i = 0; i < n; ++i) h[i] = x[i+1] - x[i];
    
    std::vector<double> alpha(n);
    for (size_t i = 1; i < n; ++i) {
        alpha[i] = (3.0/h[i])*(a_[i+1] - a_[i]) - (3.0/h[i-1])*(a_[i] - a_[i-1]);
    }
    std::vector<double> l(n + 1, 1.0), mu(n + 1, 0.0), z(n + 1, 0.0);
    for (size_t i = 1; i < n; ++i) {
        l[i] = 2.0*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1];
        mu[i] = h[i]/l[i];
        z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i];
    }
    for (int j = n - 1; j >= 0; --j) {
        c_[j] = z[j] - mu[j]*c_[j+1];
        b_[j] = (a_[j+1] - a_[j])/h[j] - h[j]*(c_[j+1] + 2.0*c_[j])/3.0;
        d_[j] = (c_[j+1] - c_[j])/(3.0*h[j]);
    }
}

double CubicSpline::eval(double xi) const {
    size_t n = x_.size() - 1;
    size_t i = 0;
    while (i < n - 1 && xi > x_[i+1]) i++;
    double dx = xi - x_[i];
    return a_[i] + b_[i]*dx + c_[i]*dx*dx + d_[i]*dx*dx*dx;
}
