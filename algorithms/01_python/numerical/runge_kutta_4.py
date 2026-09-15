"""Classical fourth-order Runge-Kutta (Numerical Recipes 17.1)."""
def rk4(f, y0: float, t0: float, t1: float, steps: int = 1000) -> float:
    h = (t1 - t0) / steps
    y, t = y0, t0
    for _ in range(steps):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y


if __name__ == "__main__":
    import math
    value = rk4(lambda t, y: y, 1.0, 0.0, 1.0, 1000)
    assert abs(value - math.e) < 1e-9
    print("runge-kutta 4 ok")
