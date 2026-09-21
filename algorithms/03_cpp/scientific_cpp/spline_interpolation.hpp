#ifndef SPLINE_INTERPOLATION_HPP
#define SPLINE_INTERPOLATION_HPP

#include <vector>

class CubicSpline {
public:
    CubicSpline(const std::vector<double>& x, const std::vector<double>& y);
    double eval(double xi) const;
private:
    std::vector<double> x_, a_, b_, c_, d_;
};

#endif
