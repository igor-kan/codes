"""Ordinary least squares for a straight line."""
def least_squares_linear(xs, ys):
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = sum((x - mean_x) ** 2 for x in xs)
    slope = numerator / denominator
    return mean_y - slope * mean_x, slope


if __name__ == "__main__":
    intercept, slope = least_squares_linear([0, 1, 2, 3], [1, 3, 5, 7])
    assert abs(intercept - 1.0) < 1e-12 and abs(slope - 2.0) < 1e-12
    print("least squares linear ok")
