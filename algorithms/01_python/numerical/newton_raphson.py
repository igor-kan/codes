"""Newton-Raphson root finding (Numerical Recipes 9.4)."""
def newton(f, df, x0: float, tol: float = 1e-12, iterations: int = 100) -> float:
    x = x0
    for _ in range(iterations):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x -= fx / df(x)
    return x


if __name__ == "__main__":
    root = newton(lambda x: x * x - 2, lambda x: 2 * x, 1.0)
    assert abs(root - 2 ** 0.5) < 1e-9
    print("newton-raphson ok")
