"""Romberg integration with Richardson extrapolation (Numerical Recipes 4.3)."""
def romberg(f, a: float, b: float, order: int = 6) -> float:
    table = [[0.0] * order for _ in range(order)]
    h = b - a
    table[0][0] = 0.5 * h * (f(a) + f(b))
    for i in range(1, order):
        h /= 2
        total = sum(f(a + (2 * k - 1) * h) for k in range(1, 2 ** (i - 1) + 1))
        table[i][0] = 0.5 * table[i - 1][0] + h * total
        for j in range(1, i + 1):
            table[i][j] = table[i][j - 1] + (table[i][j - 1] - table[i - 1][j - 1]) / (4 ** j - 1)
    return table[order - 1][order - 1]


if __name__ == "__main__":
    assert abs(romberg(lambda x: x * x, 0, 1) - 1 / 3) < 1e-12
    print("romberg integration ok")
