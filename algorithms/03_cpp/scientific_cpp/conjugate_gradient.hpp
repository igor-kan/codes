#ifndef CONJUGATE_GRADIENT_HPP
#define CONJUGATE_GRADIENT_HPP

#include <vector>

std::vector<double> solve_cg(const std::vector<std::vector<double>>& A,
                            const std::vector<double>& b,
                            double tol = 1e-8, int max_iter = 100);

#endif
