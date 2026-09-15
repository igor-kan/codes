"""Velocity Verlet integration for Newtonian mechanics (Numerical Recipes 17.4)."""
import math


def verlet(acceleration, x0, v0, dt, steps):
    x, v = x0, v0
    for _ in range(steps):
        a = acceleration(x)
        x_new = x + v * dt + 0.5 * a * dt * dt
        a_new = acceleration(x_new)
        v = v + 0.5 * (a + a_new) * dt
        x = x_new
    return x, v


if __name__ == "__main__":
    position, velocity = verlet(lambda x: -x, 1.0, 0.0, 0.001, 10000)
    energy = 0.5 * (velocity * velocity + position * position)
    assert abs(energy - 0.5) < 1e-3
    assert abs(position - math.cos(10.0)) < 1e-2
    print("verlet ok")
