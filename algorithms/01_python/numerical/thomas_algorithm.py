"""Thomas algorithm for tridiagonal systems (Numerical Recipes 2.4)."""
def thomas_algorithm(lower, diagonal, upper, rhs):
    n = len(diagonal)
    c = [0.0] * n
    d = [0.0] * n
    c[0] = upper[0] / diagonal[0]
    d[0] = rhs[0] / diagonal[0]
    for i in range(1, n):
        denominator = diagonal[i] - lower[i] * c[i - 1]
        c[i] = upper[i] / denominator if i < n - 1 else 0.0
        d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator
    x = [0.0] * n
    x[-1] = d[-1]
    for i in range(n - 2, -1, -1):
        x[i] = d[i] - c[i] * x[i + 1]
    return x


if __name__ == "__main__":
    x = thomas_algorithm([0, -1, -1], [2, 2, 2], [-1, -1, 0], [1, 0, 1])
    assert all(abs(value - 1.0) < 1e-12 for value in x)
    print("thomas algorithm ok")
