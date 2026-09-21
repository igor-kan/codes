#include "rk45_dormand_prince.hpp"

double dormand_prince_step(std::function<double(double, double)> f, double t, double y, double h) {
    double k1 = f(t, y);
    double k2 = f(t + h/5.0, y + h*(k1/5.0));
    double k3 = f(t + 3.0*h/10.0, y + h*(3.0*k1/40.0 + 9.0*k2/40.0));
    double k4 = f(t + 4.0*h/5.0, y + h*(44.0*k1/45.0 - 56.0*k2/15.0 + 32.0*k3/9.0));
    double k5 = f(t + 8.0*h/9.0, y + h*(19372.0*k1/6561.0 - 25360.0*k2/2187.0 + 64448.0*k3/6561.0 - 212.0*k4/729.0));
    double k6 = f(t + h, y + h*(9017.0*k1/3168.0 - 355.0*k2/33.0 + 46732.0*k3/5247.0 + 49.0*k4/176.0 - 5103.0*k5/18656.0));
    
    // 5th order solution
    return y + h*(35.0*k1/384.0 + 500.0*k3/1113.0 + 125.0*k4/192.0 - 2187.0*k5/6784.0 + 11.0*k6/84.0);
}
