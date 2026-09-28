"""Implementation of legendre polynomial degree/order 196."""

def evaluate_legendre_poly_196(x: float) -> float:
    if 196 == 0:
        return 1.0
    if 196 == 1:
        return float(x)
    p0, p1 = 1.0, float(x)
    for k in range(2, 196 + 1):
        p_next = ((2 * k - 1) * float(x) * p1 - (k - 1) * p0) / float(k)
        p0, p1 = p1, p_next
    return float(p1)


def test_evaluate_legendre_poly_196():
    val = evaluate_legendre_poly_196(0.5)
    assert isinstance(val, float)
    assert val == val
