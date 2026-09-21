#include "b_spline_curve.hpp"

double de_boor_eval(int k, int p, double u, const std::vector<double>& knots, const std::vector<double>& control_points) {
    std::vector<double> d(p + 1);
    for (int j = 0; j <= p; ++j) d[j] = control_points[j + k - p];
    
    for (int r = 1; r <= p; ++r) {
        for (int j = p; j >= r; --j) {
            double alpha = (u - knots[j + k - p]) / (knots[j + 1 + k - r] - knots[j + k - p]);
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j];
        }
    }
    return d[p];
}
