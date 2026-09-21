#ifndef B_SPLINE_CURVE_HPP
#define B_SPLINE_CURVE_HPP

#include <vector>

double de_boor_eval(int k, int p, double u, const std::vector<double>& knots, const std::vector<double>& control_points);

#endif
