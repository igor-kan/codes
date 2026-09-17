/**
 * Brent's Root Finding in C (Numerical Recipes 3rd Ed. Chapter 9.3)
 */

#include <stdio.h>
#include <math.h>
#include <assert.h>

double brentRoot(double (*f)(double), double a, double b, double tol, int maxIter) {
    double fa = f(a), fb = f(b);
    assert(fa * fb <= 0);

    if (fabs(fa) < fabs(fb)) {
        double t = a; a = b; b = t;
        t = fa; fa = fb; fb = t;
    }

    double c = a, fc = fa, d = 0, s = b;
    int mflag = 1;

    for (int iter = 0; iter < maxIter; iter++) {
        if (fabs(fb) < tol || fabs(b - a) < tol) return b;

        if (fa != fc && fb != fc) {
            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
                (b * fa * fc) / ((fb - fa) * (fb - fc)) +
                (c * fa * fb) / ((fc - fa) * (fc - fb));
        } else {
            s = b - fb * (b - a) / (fb - fa);
        }

        int c1 = (s - (3 * a + b) / 4) * (s - b) > 0;
        int c2 = mflag && fabs(s - b) >= fabs(b - c) / 2;
        int c3 = !mflag && fabs(s - b) >= fabs(c - d) / 2;

        if (c1 || c2 || c3) {
            s = (a + b) / 2;
            mflag = 1;
        } else {
            mflag = 0;
        }

        double fs = f(s);
        d = c; c = b; fc = fb;
        if (fa * fs < 0) { b = s; fb = fs; }
        else { a = s; fa = fs; }

        if (fabs(fa) < fabs(fb)) {
            double t = a; a = b; b = t;
            t = fa; fa = fb; fb = t;
        }
    }
    return b;
}

static double testFunc(double x) { return x * x - 2.0; }

int main(void) {
    double r = brentRoot(testFunc, 0.0, 2.0, 1e-10, 100);
    assert(fabs(r - sqrt(2.0)) < 1e-6);
    printf("C Brent Root Finding verified.\n");
    return 0;
}
