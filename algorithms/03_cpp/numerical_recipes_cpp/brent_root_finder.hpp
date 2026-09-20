#pragma once
#include <cmath>
#include <functional>
#include <stdexcept>

namespace NumericalRecipes {

inline double brent_find_root(std::function<double(double)> f, double a, double b, double tol = 1e-8, int max_iter = 100) {
    double fa = f(a);
    double fb = f(b);
    if (fa * fb > 0.0) throw std::invalid_argument("Root must be bracketed");

    if (std::abs(fa) < std::abs(fb)) {
        std::swap(a, b);
        std::swap(fa, fb);
    }

    double c = a, fc = fa;
    bool mflag = true;
    double s = b, fs = fb, d = 0.0;

    for (int iter = 0; iter < max_iter; ++iter) {
        if (std::abs(fb) < tol || std::abs(b - a) < tol) return b;

        if (fa != fc && fb != fc) {
            // Inverse quadratic interpolation
            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
                (b * fa * fc) / ((fb - fa) * (fb - fc)) +
                (c * fa * fb) / ((fc - fa) * (fc - fb));
        } else {
            // Secant method
            s = b - fb * (b - a) / (fb - fa);
        }

        bool cond1 = (s < (3.0 * a + b) / 4.0 && s < b) || (s > (3.0 * a + b) / 4.0 && s > b);
        bool cond2 = mflag && std::abs(s - b) >= 0.5 * std::abs(b - c);
        bool cond3 = !mflag && std::abs(s - b) >= 0.5 * std::abs(c - d);
        bool cond4 = mflag && std::abs(b - c) < tol;
        bool cond5 = !mflag && std::abs(c - d) < tol;

        if (cond1 || cond2 || cond3 || cond4 || cond5) {
            s = 0.5 * (a + b);
            mflag = true;
        } else {
            mflag = false;
        }

        fs = f(s);
        d = c;
        c = b;
        fc = fb;

        if (fa * fs < 0.0) {
            b = s;
            fb = fs;
        } else {
            a = s;
            fa = fs;
        }

        if (std::abs(fa) < std::abs(fb)) {
            std::swap(a, b);
            std::swap(fa, fb);
        }
    }
    return b;
}

} // namespace NumericalRecipes
