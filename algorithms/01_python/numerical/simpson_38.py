"""Composite Simpson's 3/8 rule (Numerical Recipes 4.1)."""
def simpson_38(function, a, b, n):
    if n % 3 != 0:
        n += 3 - n % 3
    h = (b - a) / n
    total = function(a) + function(b)
    for i in range(1, n):
        total += (3.0 if i % 3 != 0 else 2.0) * function(a + i * h)
    return 3.0 * h / 8.0 * total


if __name__ == "__main__":
    assert abs(simpson_38(lambda x: x * x, 0.0, 1.0, 999) - 1.0 / 3.0) < 1e-12
    print("simpson 3/8 ok")
