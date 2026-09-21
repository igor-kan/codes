#include "brent_root_finding.h"
#include <math.h>

double brent_find_root(scalar_fn f, double a, double b, double tol, int max_iter) {
    double fa = f(a);
    double fb = f(b);
    if (fa * fb > 0) return a; // Root not bracketed
    
    double c = a, fc = fa;
    double d = b - a, e = d;
    
    for (int iter = 0; iter < max_iter; ++iter) {
        if (fb * fc > 0) {
            c = a; fc = fa;
            d = b - a; e = d;
        }
        if (fabs(fc) < fabs(fb)) {
            a = b; b = c; c = a;
            fa = fb; fb = fc; fc = fa;
        }
        double tol1 = 2.0 * 1e-15 * fabs(b) + 0.5 * tol;
        double xm = 0.5 * (c - b);
        if (fabs(xm) <= tol1 || fb == 0.0) return b;
        
        if (fabs(e) >= tol1 && fabs(fa) > fabs(fb)) {
            double s = fb / fa;
            double p, q;
            if (a == c) {
                p = 2.0 * xm * s;
                q = 1.0 - s;
            } else {
                q = fa / fc;
                double r = fb / fc;
                p = s * (2.0 * xm * q * (q - r) - (b - a) * (r - 1.0));
                q = (q - 1.0) * (r - 1.0) * (s - 1.0);
            }
            if (p > 0.0) q = -q;
            p = fabs(p);
            if (2.0 * p < fmin(3.0 * xm * q - fabs(tol1 * q), fabs(e * q))) {
                e = d;
                d = p / q;
            } else {
                d = xm; e = d;
            }
        } else {
            d = xm; e = d;
        }
        a = b; fa = fb;
        b += (fabs(d) > tol1) ? d : ((xm >= 0) ? tol1 : -tol1);
        fb = f(b);
    }
    return b;
}
