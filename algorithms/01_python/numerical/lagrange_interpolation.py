"""Lagrange polynomial interpolation (Numerical Recipes 3.1)."""
def lagrange(xs: list[float], ys: list[float], x: float) -> float:
    total = 0.0
    n = len(xs)
    for i in range(n):
        term = ys[i]
        for j in range(n):
            if i != j:
                term *= (x - xs[j]) / (xs[i] - xs[j])
        total += term
    return total


if __name__ == "__main__":
    xs = [0.0, 1.0, 2.0]
    ys = [1.0, 3.0, 2.0]
    assert abs(lagrange(xs, ys, 1.5) - 2.875) < 1e-9
    print("lagrange interpolation ok")
