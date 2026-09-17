"""
Brent's Root Finding in Python (Numerical Recipes 3rd Ed. Chapter 9.3).
"""

import math

def brent_root(f, a, b, tol=1e-12, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Root not bracketed")

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c, fc = a, fa
    mflag = True
    s, d = b, 0.0

    for _ in range(max_iter):
        if abs(fb) < tol or abs(b - a) < tol:
            return b

        if fa != fc and fb != fc:
            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +                 (b * fa * fc) / ((fb - fa) * (fb - fc)) +                 (c * fa * fb) / ((fc - fa) * (fc - fb))
        else:
            s = b - fb * (b - a) / (fb - fa)

        c1 = (s - (3 * a + b) / 4) * (s - b) > 0
        c2 = mflag and abs(s - b) >= abs(b - c) / 2
        c3 = not mflag and abs(s - b) >= abs(c - d) / 2

        if c1 or c2 or c3:
            s = (a + b) / 2
            mflag = True
        else:
            mflag = False

        fs = f(s)
        d, c, fc = c, b, fb
        if fa * fs < 0:
            b, fb = s, fs
        else:
            a, fa = s, fs

        if abs(fa) < abs(fb):
            a, b = b, a
            fa, fb = fb, fa

    return b

if __name__ == "__main__":
    r = brent_root(lambda x: x**2 - 2.0, 0, 2)
    assert abs(r - math.sqrt(2)) < 1e-8
    print("Python Brent Root Finding verified.")
