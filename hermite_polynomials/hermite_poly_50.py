"""Implementation of hermite polynomial degree/order 50."""

def evaluate_hermite_poly_50(x: float) -> float:
    if 50 == 0:
        return 1.0
    if 50 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for k in range(1, 50):
        p0, p1 = p1, 2.0 * float(x) * p1 - 2.0 * k * p0
    return float(p1)


def test_evaluate_hermite_poly_50():
    val = evaluate_hermite_poly_50(0.5)
    assert isinstance(val, float)
    assert val == val
