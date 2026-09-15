"""Piecewise linear interpolation."""
def linear_interpolation(xs, ys, x):
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    for i in range(1, len(xs)):
        if x <= xs[i]:
            slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1])
            return ys[i - 1] + slope * (x - xs[i - 1])
    return ys[-1]


if __name__ == "__main__":
    assert abs(linear_interpolation([0, 1, 2], [0, 2, 4], 0.5) - 1.0) < 1e-12
    assert abs(linear_interpolation([0, 1, 4], [0, 1, 2], 2.5) - 1.5) < 1e-12
    print("linear interpolation ok")
