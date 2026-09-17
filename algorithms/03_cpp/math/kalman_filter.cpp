/**
 * 1D Kalman Filter in C++ (Numerical Recipes 3rd Ed. Chapter 15)
 */

#include <iostream>
#include <cmath>
#include <cassert>

class KalmanFilter1D {
public:
    double x, p, q, r;
    KalmanFilter1D(double x0, double p0, double q0, double r0)
        : x(x0), p(p0), q(q0), r(r0) {}

    void predict() { p += q; }
    double update(double z) {
        double k = p / (p + r);
        x += k * (z - x);
        p = (1.0 - k) * p;
        return x;
    }
};

int main() {
    KalmanFilter1D kf(0.0, 1.0, 0.01, 0.1);
    for (double z : {0.9, 1.1, 0.95, 1.05}) {
        kf.predict();
        kf.update(z);
    }
    assert(std::abs(kf.x - 1.0) < 0.2);
    std::cout << "C++ Kalman Filter verified.\n";
    return 0;
}
