/**
 * Ternary search for a unimodal (single-peak / single-valley) function.
 */

#include <cmath>
#include <cassert>
#include <iostream>

static double f(double x) {
    return (x - 2.0) * (x - 2.0) + 3.0; // minimum at x = 2
}

double ternaryMin(double lo, double hi, double eps = 1e-9) {
    while (hi - lo > eps) {
        double m1 = lo + (hi - lo) / 3.0;
        double m2 = hi - (hi - lo) / 3.0;
        if (f(m1) < f(m2)) hi = m2;
        else lo = m1;
    }
    return (lo + hi) / 2.0;
}

static int g(int x) {
    return -(x - 10) * (x - 10) + 100; // maximum at x = 10
}

int ternaryMaxInt(int lo, int hi) {
    while (hi - lo > 2) {
        int m1 = lo + (hi - lo) / 3;
        int m2 = hi - (hi - lo) / 3;
        if (g(m1) < g(m2)) lo = m1;
        else hi = m2;
    }
    int best = lo;
    for (int i = lo + 1; i <= hi; ++i)
        if (g(i) > g(best)) best = i;
    return best;
}

int main() {
    double x = ternaryMin(-100.0, 100.0);
    assert(std::fabs(x - 2.0) < 1e-6);
    assert(ternaryMaxInt(0, 20) == 10);
    std::cout << "[C++ TernarySearch] Unimodal minimization and maximization verified." << std::endl;
    return 0;
}
