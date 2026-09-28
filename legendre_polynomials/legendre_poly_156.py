"""Implementation of legendre polynomial degree/order 156."""

def evaluate_legendre_poly_156(x: float) -> float:
    if 156 == 0:
        return 1.0
    if 156 == 1:
        return float(x)
    p0, p1 = 1.0, float(x)
    for k in range(2, 156 + 1):
        p_next = ((2 * k - 1) * float(x) * p1 - (k - 1) * p0) / float(k)
        p0, p1 = p1, p_next
    return float(p1)


def test_evaluate_legendre_poly_156():
    val = evaluate_legendre_poly_156(0.5)
    assert isinstance(val, float)
    assert val == val
