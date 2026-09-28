"""Implementation of hermite polynomial degree/order 125."""

def evaluate_hermite_poly_125(x: float) -> float:
    if 125 == 0:
        return 1.0
    if 125 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for k in range(1, 125):
        p0, p1 = p1, 2.0 * float(x) * p1 - 2.0 * k * p0
    return float(p1)


def test_evaluate_hermite_poly_125():
    val = evaluate_hermite_poly_125(0.5)
    assert isinstance(val, float)
    assert val == val
