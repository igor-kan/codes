"""
Cash-Karp Embedded Runge-Kutta 5(4) with Adaptive Step Size Control.
References: Press et al. - Numerical Recipes (Ch. 17).
"""
import numpy as np

A = [0, 1/5, 3/10, 3/5, 1, 7/8]
B = [
    [],
    [1/5],
    [3/40, 9/40],
    [3/10, -9/10, 6/5],
    [-11/54, 5/2, -70/27, 35/27],
    [1631/55296, 175/512, 575/13824, 44275/110592, 253/4096]
]
C = [37/378, 0, 250/621, 125/594, 0, 512/1771]
C_STAR = [2825/27648, 0, 18575/48384, 13525/55296, 277/14336, 1/4]

def rkf45_step(derivs, t, y, h):
    """Single Cash-Karp step returning 5th order result and 4th order error estimate."""
    k = []
    k.append(derivs(t, y))
    for i in range(1, 6):
        ti = t + A[i] * h
        yi = y.copy()
        for j in range(i):
            yi += h * B[i][j] * k[j]
        k.append(derivs(ti, yi))

    y5 = y.copy()
    y4 = y.copy()
    for i in range(6):
        y5 += h * C[i] * k[i]
        y4 += h * C_STAR[i] * k[i]

    error = np.max(np.abs(y5 - y4))
    return y5, error

def adaptive_rk45_integrate(derivs, y0, t_span, tol=1e-6, h_init=0.01):
    """Integrate from t0 to tf with adaptive step size."""
    t0, tf = t_span
    t = t0
    y = np.array(y0, dtype=float)
    h = h_init
    ts = [t]
    ys = [y.copy()]

    while t < tf:
        if t + h > tf:
            h = tf - t
        y_next, err = rkf45_step(derivs, t, y, h)
        if err <= tol:
            t += h
            y = y_next
            ts.append(t)
            ys.append(y.copy())
            # Increase step size
            h = min(h * 1.5, tf - t) if err == 0 else min(h * (tol / err)**0.2 * 0.9, 2.0 * h)
        else:
            # Decrease step size
            h *= max((tol / err)**0.25 * 0.9, 0.1)

    return np.array(ts), np.array(ys)
