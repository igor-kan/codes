#ifndef GAUSSIAN_QUADRATURE_HPP
#define GAUSSIAN_QUADRATURE_HPP

#include <functional>

double integrate_gauss_3point(std::function<double(double)> f, double a, double b);

#endif
