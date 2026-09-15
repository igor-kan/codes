"""Composite Boole's rule (Numerical Recipes 4.1)."""
def boole_rule(function, a, b, n):
    if n % 4 != 0:
        n += 4 - n % 4
    h = (b - a) / n
    total = 7.0 * (function(a) + function(b))
    for i in range(1, n):
        if i % 4 == 0:
            total += 14.0 * function(a + i * h)
        elif i % 2 == 0:
            total += 12.0 * function(a + i * h)
        else:
            total += 32.0 * function(a + i * h)
    return 2.0 * h / 45.0 * total


if __name__ == "__main__":
    assert abs(boole_rule(lambda x: x * x, 0.0, 1.0, 998) - 1.0 / 3.0) < 1e-12
    print("boole rule ok")
