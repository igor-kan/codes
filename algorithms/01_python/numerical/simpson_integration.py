"""Composite Simpson's rule (Numerical Recipes 4.1)."""
def simpson(f, a: float, b: float, n: int = 1000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3


if __name__ == "__main__":
    assert abs(simpson(lambda x: x * x, 0, 1, 1000) - 1 / 3) < 1e-12
    print("simpson integration ok")
