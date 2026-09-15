"""Gradient descent for univariate linear regression."""
def train(xs: list[float], ys: list[float], lr=0.01, epochs=5000):
    slope, intercept = 0.0, 0.0
    n = len(xs)
    for _ in range(epochs):
        slope_grad = intercept_grad = 0.0
        for x, y in zip(xs, ys):
            error = slope * x + intercept - y
            slope_grad += error * x
            intercept_grad += error
        slope -= lr * slope_grad / n
        intercept -= lr * intercept_grad / n
    return slope, intercept


if __name__ == "__main__":
    xs = [1, 2, 3, 4, 5]
    ys = [2, 4, 6, 8, 10]
    slope, intercept = train(xs, ys)
    assert abs(slope - 2) < 1e-2 and abs(intercept) < 1e-2
    print("gradient descent ok")
