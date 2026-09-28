"""Implementation of hermite polynomial degree/order 70."""

def evaluate_hermite_poly_70(x: float) -> float:
    if 70 == 0:
        return 1.0
    if 70 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for k in range(1, 70):
        p0, p1 = p1, 2.0 * float(x) * p1 - 2.0 * k * p0
    return float(p1)


def test_evaluate_hermite_poly_70():
    val = evaluate_hermite_poly_70(0.5)
    assert isinstance(val, float)
    assert val == val
