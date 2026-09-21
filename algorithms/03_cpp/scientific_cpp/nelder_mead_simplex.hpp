#ifndef NELDER_MEAD_SIMPLEX_HPP
#define NELDER_MEAD_SIMPLEX_HPP

#include <vector>
#include <functional>

std::vector<double> nelder_mead_minimize(std::function<double(const std::vector<double>&)> f,
                                       std::vector<double> x0,
                                       double step = 1.0, int max_iter = 100);

#endif
