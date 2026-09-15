"""Pade approximation from a Taylor series (Numerical Recipes 5.12)."""
def pade_coefficients(series, numerator_degree, denominator_degree):
    matrix = [[series[numerator_degree + i - j] for j in range(1, denominator_degree + 1)]
              for i in range(1, denominator_degree + 1)]
    rhs = [-series[numerator_degree + i] for i in range(1, denominator_degree + 1)]
    denominator = _solve(matrix, rhs)
    numerator = []
    for i in range(numerator_degree + 1):
        term = series[i]
        for j in range(1, min(i, denominator_degree) + 1):
            term += denominator[j - 1] * series[i - j]
        numerator.append(term)
    return numerator, denominator


def _solve(matrix, rhs):
    n = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for k in range(col, n + 1):
                a[r][k] -= factor * a[col][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (a[r][n] - sum(a[r][k] * x[k] for k in range(r + 1, n))) / a[r][r]
    return x


def pade_evaluate(numerator, denominator, x):
    return sum(c * x ** i for i, c in enumerate(numerator)) / sum(c * x ** i for i, c in enumerate([1.0] + denominator))


if __name__ == "__main__":
    import math
    series = [1.0 / math.factorial(k) for k in range(5)]
    numerator, denominator = pade_coefficients(series, 2, 2)
    assert abs(pade_evaluate(numerator, denominator, 0.5) - math.exp(0.5)) < 1e-3
    assert abs(pade_evaluate(numerator, denominator, 1.0) - 19.0 / 7.0) < 1e-9
    print("pade approximation ok")
