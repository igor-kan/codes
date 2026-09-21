#include "qr_eigenvalues.hpp"
#include <cmath>

std::vector<double> compute_symmetric_eigenvalues_2x2(double a, double b, double c) {
    // [[a, b], [b, c]]
    double trace = a + c;
    double det = a * c - b * b;
    double disc = std::sqrt(std::max(0.0, trace * trace - 4.0 * det));
    return {0.5 * (trace - disc), 0.5 * (trace + disc)};
}
