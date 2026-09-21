#include "simpson_adaptive.h"
#include <math.h>

static double simpson_rule(quad_fn f, double a, double b) {
    double c = 0.5 * (a + b);
    double h = b - a;
    return (h / 6.0) * (f(a) + 4.0 * f(c) + f(b));
}

static double adaptive_recursive(quad_fn f, double a, double b, double tol, double whole) {
    double c = 0.5 * (a + b);
    double left = simpson_rule(f, a, c);
    double right = simpson_rule(f, c, b);
    if (fabs(left + right - whole) <= 15.0 * tol) {
        return left + right + (left + right - whole) / 15.0;
    }
    return adaptive_recursive(f, a, c, 0.5 * tol, left) +
           adaptive_recursive(f, c, b, 0.5 * tol, right);
}

double adaptive_simpson(quad_fn f, double a, double b, double tol) {
    return adaptive_recursive(f, a, b, tol, simpson_rule(f, a, b));
}
