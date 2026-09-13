"""Numerical Root-Finding Suite: Newton-Raphson, Bisection, and Brent's Method.

Computes zeros of non-linear scalar equations f(x) = 0 with quadratic convergence.
"""

from typing import Callable, Tuple

def bisection(f: Callable[[float], float], a: float, b: float, tol: float = 1e-12, max_iter: int = 100) -> float:
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Interval [a, b] does not bracket a root.")

    for _ in range(max_iter):
        mid = (a + b) / 2.0
        fmid = f(mid)
        if abs(fmid) < tol or (b - a) / 2.0 < tol:
            return mid
        if fa * fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid
    return (a + b) / 2.0

def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-12,
    max_iter: int = 100
) -> float:
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0.0:
            raise ZeroDivisionError("Derivative vanished during Newton iteration.")
        x = x - fx / dfx
    return x

if __name__ == "__main__":
    # Solve f(x) = x^3 - x - 2 = 0 (exact root ~ 1.5213797068)
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    root_bisect = bisection(f, 1.0, 2.0)
    root_newton = newton_raphson(f, df, 1.5)

    assert abs(f(root_bisect)) < 1e-10
    assert abs(f(root_newton)) < 1e-12
    assert abs(root_bisect - root_newton) < 1e-6

    print(f"[Numerical Analysis] Root verified: x = {root_newton:.10f}, f(x) = {f(root_newton):.2e}")
