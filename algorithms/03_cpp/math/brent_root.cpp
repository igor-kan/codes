/**
 * Brent's Root Finding in C++ (Numerical Recipes 3rd Ed. Chapter 9.3)
 */

#include <iostream>
#include <cmath>
#include <cassert>

double brentRoot(double (*f)(double), double a, double b, double tol = 1e-10, int maxIter = 100) {
    double fa = f(a), fb = f(b);
    assert(fa * fb <= 0);

    if (std::abs(fa) < std::abs(fb)) {
        std::swap(a, b);
        std::swap(fa, fb);
    }

    double c = a, fc = fa, d = 0, s = b;
    bool mflag = true;

    for (int iter = 0; iter < maxIter; iter++) {
        if (std::abs(fb) < tol || std::abs(b - a) < tol) return b;

        if (fa != fc && fb != fc) {
            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
                (b * fa * fc) / ((fb - fa) * (fb - fc)) +
                (c * fa * fb) / ((fc - fa) * (fc - fb));
        } else {
            s = b - fb * (b - a) / (fb - fa);
        }

        bool c1 = (s - (3 * a + b) / 4) * (s - b) > 0;
        bool c2 = mflag && std::abs(s - b) >= std::abs(b - c) / 2;
        bool c3 = !mflag && std::abs(s - b) >= std::abs(c - d) / 2;

        if (c1 || c2 || c3) {
            s = (a + b) / 2;
            mflag = true;
        } else {
            mflag = false;
        }

        double fs = f(s);
        d = c; c = b; fc = fb;
        if (fa * fs < 0) { b = s; fb = fs; }
        else { a = s; fa = fs; }

        if (std::abs(fa) < std::abs(fb)) {
            std::swap(a, b);
            std::swap(fa, fb);
        }
    }
    return b;
}

int main() {
    double r = brentRoot([](double x) { return x * x - 2.0; }, 0.0, 2.0);
    assert(std::abs(r - std::sqrt(2.0)) < 1e-6);
    std::cout << "C++ Brent Root Finding verified.\n";
    return 0;
}
