"""Trapezoidal rule (Numerical Recipes 4.1)."""
def trapezoidal(f, a: float, b: float, n: int = 1000) -> float:
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


if __name__ == "__main__":
    assert abs(trapezoidal(lambda x: x * x, 0, 1, 10_000) - 1 / 3) < 1e-6
    print("trapezoidal integration ok")
