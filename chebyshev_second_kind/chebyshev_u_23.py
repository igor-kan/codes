"""Implementation of chebyshev second kind polynomial degree/order 23."""

def evaluate_chebyshev_u_23(x: float) -> float:
    if 23 == 0:
        return 1.0
    if 23 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for _ in range(1, 23):
        p0, p1 = p1, 2.0 * float(x) * p1 - p0
    return float(p1)


def test_evaluate_chebyshev_u_23():
    val = evaluate_chebyshev_u_23(0.5)
    assert isinstance(val, float)
    assert val == val
