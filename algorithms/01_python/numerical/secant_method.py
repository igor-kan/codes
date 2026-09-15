"""Secant method root finding (Numerical Recipes 9.2)."""
def secant(f, x0: float, x1: float, tol: float = 1e-12, iterations: int = 100) -> float:
    f0, f1 = f(x0), f(x1)
    for _ in range(iterations):
        if abs(f1) < tol:
            return x1
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        x0, f0, x1, f1 = x1, f1, x2, f(x2)
    return x1


if __name__ == "__main__":
    root = secant(lambda x: x ** 3 - 2 * x - 5, 1.0, 2.0)
    assert abs(root ** 3 - 2 * root - 5) < 1e-9
    print("secant method ok")
