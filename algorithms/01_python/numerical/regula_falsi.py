"""Regula falsi (false position) root finding (Numerical Recipes 9.2)."""
def regula_falsi(f, a, b, tolerance=1e-12, max_iterations=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("root is not bracketed")
    for _ in range(max_iterations):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(fc) < tolerance:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return c


if __name__ == "__main__":
    root = regula_falsi(lambda x: x * x - 2, 0, 2)
    assert abs(root - 2 ** 0.5) < 1e-9
    print("regula falsi ok")
