"""Bisection root finding (Numerical Recipes 9.1)."""
def bisection(f, a, b, tolerance=1e-12, max_iterations=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("root is not bracketed")
    for _ in range(max_iterations):
        midpoint = 0.5 * (a + b)
        fm = f(midpoint)
        if fm == 0 or (b - a) / 2 < tolerance:
            return midpoint
        if fa * fm < 0:
            b, fb = midpoint, fm
        else:
            a, fa = midpoint, fm
    return 0.5 * (a + b)


if __name__ == "__main__":
    root = bisection(lambda x: x * x - 2, 0, 2)
    assert abs(root - 2 ** 0.5) < 1e-9
    print("bisection ok")
