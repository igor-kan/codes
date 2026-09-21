#include "nelder_mead_simplex.hpp"
#include <algorithm>

std::vector<double> nelder_mead_minimize(std::function<double(const std::vector<double>&)> f,
                                       std::vector<double> x0,
                                       double step, int max_iter) {
    size_t dim = x0.size();
    std::vector<std::vector<double>> simplex(dim + 1, x0);
    for (size_t i = 0; i < dim; ++i) {
        simplex[i + 1][i] += step;
    }
    
    for (int iter = 0; iter < max_iter; ++iter) {
        std::sort(simplex.begin(), simplex.end(), [&](const auto& a, const auto& b){ return f(a) < f(b); });
        // Centroid of first dim points
        std::vector<double> c(dim, 0.0);
        for (size_t i = 0; i < dim; ++i) {
            for (size_t j = 0; j < dim; ++j) c[j] += simplex[i][j];
        }
        for (size_t j = 0; j < dim; ++j) c[j] /= dim;
        
        // Reflection
        std::vector<double> xr(dim);
        for (size_t j = 0; j < dim; ++j) xr[j] = 2.0 * c[j] - simplex[dim][j];
        if (f(xr) < f(simplex[dim])) {
            simplex[dim] = xr;
        } else {
            // Shrink
            for (size_t i = 1; i <= dim; ++i) {
                for (size_t j = 0; j < dim; ++j) simplex[i][j] = 0.5 * (simplex[0][j] + simplex[i][j]);
            }
        }
    }
    return simplex[0];
}
