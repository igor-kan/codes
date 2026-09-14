#include <stdio.h>
#include <math.h>

static double f(double x) {
    return -(x - 2.0) * (x - 2.0) + 3.0;
}

double ternary_search_max(double lo, double hi, double eps) {
    while (hi - lo > eps) {
        double m1 = lo + (hi - lo) / 3.0;
        double m2 = hi - (hi - lo) / 3.0;
        if (f(m1) < f(m2)) lo = m1;
        else hi = m2;
    }
    return (lo + hi) / 2.0;
}

int main(void) {
    double x = ternary_search_max(-10.0, 10.0, 1e-9);
    if (fabs(x - 2.0) > 1e-6) {
        printf("[C TernarySearch] FAILED: argmax %f, want 2.0\n", x);
        return 1;
    }
    printf("[C TernarySearch] Unimodal maximum verified at x=2\n");
    return 0;
}
