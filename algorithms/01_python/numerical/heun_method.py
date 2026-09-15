"""Heun's (improved Euler) method for ODEs."""
def heun_method(f, y0, t0, t1, steps=1000):
    h = (t1 - t0) / steps
    y, t = y0, t0
    for _ in range(steps):
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        y += 0.5 * h * (k1 + k2)
        t += h
    return y


if __name__ == "__main__":
    value = heun_method(lambda t, y: y, 1.0, 0.0, 1.0)
    assert abs(value - 2.718281828459045) < 1e-4
    print("heun method ok")
