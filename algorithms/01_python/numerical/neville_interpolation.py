"""Neville's algorithm for polynomial interpolation (Numerical Recipes 3.1)."""
def neville_interpolation(xs, ys, x):
    n = len(xs)
    table = list(ys)
    for k in range(1, n):
        for i in range(n - k):
            table[i] = ((x - xs[i + k]) * table[i] + (xs[i] - x) * table[i + 1]) / (xs[i] - xs[i + k])
    return table[0]


if __name__ == "__main__":
    value = neville_interpolation([0, 1, 2], [1, 3, 2], 1.5)
    assert abs(value - 2.875) < 1e-12
    print("neville interpolation ok")
