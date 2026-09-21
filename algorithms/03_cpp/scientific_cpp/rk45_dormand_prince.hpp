#ifndef RK45_DORMAND_PRINCE_HPP
#define RK45_DORMAND_PRINCE_HPP

#include <functional>

double dormand_prince_step(std::function<double(double, double)> f, double t, double y, double h);

#endif
