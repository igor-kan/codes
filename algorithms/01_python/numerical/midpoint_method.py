"""Midpoint method for ODEs."""
def midpoint_method(f, y0, t0, t1, steps=1000):
    h = (t1 - t0) / steps
    y, t = y0, t0
    for _ in range(steps):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        y += h * k2
        t += h
    return y


if __name__ == "__main__":
    value = midpoint_method(lambda t, y: y, 1.0, 0.0, 1.0)
    assert abs(value - 2.718281828459045) < 1e-4
    print("midpoint method ok")
