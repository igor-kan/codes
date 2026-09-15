"""Natural cubic spline interpolation (Numerical Recipes 3.3)."""
def natural_cubic_spline(xs, ys):
    n = len(xs)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    alpha = [0.0] * n
    for i in range(1, n - 1):
        alpha[i] = 3.0 / h[i] * (ys[i + 1] - ys[i]) - 3.0 / h[i - 1] * (ys[i] - ys[i - 1])
    l = [0.0] * n
    mu = [0.0] * n
    z = [0.0] * n
    l[0] = 1.0
    for i in range(1, n - 1):
        l[i] = 2.0 * (xs[i + 1] - xs[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
    l[n - 1] = 1.0
    z[n - 1] = 0.0
    c = [0.0] * n
    b = [0.0] * (n - 1)
    d = [0.0] * (n - 1)
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (ys[j + 1] - ys[j]) / h[j] - h[j] * (c[j + 1] + 2.0 * c[j]) / 3.0
        d[j] = (c[j + 1] - c[j]) / (3.0 * h[j])
    return b, c, d


def spline_evaluate(xs, ys, coefficients, x):
    b, c, d = coefficients
    n = len(xs)
    segment = n - 2
    for i in range(n - 1):
        if xs[i] <= x <= xs[i + 1]:
            segment = i
            break
    dx = x - xs[segment]
    return ys[segment] + b[segment] * dx + c[segment] * dx ** 2 + d[segment] * dx ** 3


if __name__ == "__main__":
    xs = [0.0, 1.0, 2.0, 3.0]
    ys = [0.0, 1.0, 0.0, 1.0]
    coefficients = natural_cubic_spline(xs, ys)
    for x, y in zip(xs, ys):
        assert abs(spline_evaluate(xs, ys, coefficients, x) - y) < 1e-9
    print("cubic spline ok")
