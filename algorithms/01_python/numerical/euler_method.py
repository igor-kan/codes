"""Forward Euler method for ODEs (Numerical Recipes 17.1)."""
def euler_method(f, y0, t0, t1, steps=1000):
    h = (t1 - t0) / steps
    y, t = y0, t0
    for _ in range(steps):
        y += h * f(t, y)
        t += h
    return y


if __name__ == "__main__":
    value = euler_method(lambda t, y: y, 1.0, 0.0, 1.0)
    assert abs(value - 2.718281828459045) < 0.01
    print("euler method ok")
