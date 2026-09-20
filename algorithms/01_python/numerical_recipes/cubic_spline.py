"""
Natural Cubic Spline Interpolation.
References: Press et al. - Numerical Recipes (Ch. 3); Kincaid & Cheney (Ch. 6).
"""
import numpy as np
from tridiagonal_solvers import thomas_algorithm

class CubicSpline:
    def __init__(self, x, y):
        self.x = np.asarray(x, dtype=float)
        self.y = np.asarray(y, dtype=float)
        n = len(x)
        h = np.diff(self.x)

        # Tridiagonal system for second derivatives M_i = y''(x_i)
        # Natural spline: M_0 = 0, M_{n-1} = 0
        # Internal system size m = n - 2 (for indices 1 to n-2)
        m = n - 2
        if m == 0:
            # Linear
            self.c = np.zeros(n)
        else:
            sub = h[1:m]  # length m - 1
            sup = h[1:m]  # length m - 1
            diag = 2.0 * (h[:m] + h[1:m + 1])  # length m
            rhs = 6.0 * ((self.y[2:n] - self.y[1:n - 1]) / h[1:n - 1] -
                         (self.y[1:n - 1] - self.y[:n - 2]) / h[:n - 2])

            M_internal = thomas_algorithm(sub, diag, sup, rhs)
            self.M = np.zeros(n)
            self.M[1:-1] = M_internal

        self.h = h

    def evaluate(self, x_eval):
        x_eval = np.asarray(x_eval, dtype=float)
        y_eval = np.zeros_like(x_eval)
        n = len(self.x)
        for idx, val in enumerate(x_eval):
            i = np.searchsorted(self.x, val) - 1
            i = max(0, min(i, n - 2))
            xi = self.x[i]
            xip1 = self.x[i + 1]
            hi = self.h[i]
            Mi = self.M[i]
            Mip1 = self.M[i + 1]
            yi = self.y[i]
            yip1 = self.y[i + 1]

            # Cubic spline interpolation polynomial
            term1 = Mi / (6.0 * hi) * (xip1 - val)**3
            term2 = Mip1 / (6.0 * hi) * (val - xi)**3
            term3 = (yi / hi - Mi * hi / 6.0) * (xip1 - val)
            term4 = (yip1 / hi - Mip1 * hi / 6.0) * (val - xi)
            y_eval[idx] = term1 + term2 + term3 + term4
        return y_eval
