"""Newton's divided-difference interpolation (Numerical Recipes 3.2)."""
def divided_differences(xs: list[float], ys: list[float]) -> list[float]:
    n = len(xs)
    table = ys[:]
    coefficients = [table[0]]
    for order in range(1, n):
        for i in range(n - order):
            table[i] = (table[i + 1] - table[i]) / (xs[i + order] - xs[i])
        coefficients.append(table[0])
    return coefficients


def evaluate(xs: list[float], coefficients: list[float], x: float) -> float:
    result = coefficients[-1]
    for k in range(len(coefficients) - 2, -1, -1):
        result = result * (x - xs[k]) + coefficients[k]
    return result


if __name__ == "__main__":
    xs = [0.0, 1.0, 2.0, 3.0]
    ys = [1.0, 2.0, 5.0, 10.0]  # y = x^2 + 1
    coeffs = divided_differences(xs, ys)
    assert abs(evaluate(xs, coeffs, 2.5) - 7.25) < 1e-9
    print("newton divided differences ok")
