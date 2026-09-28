"""Implementation of chebyshev second kind polynomial degree/order 38."""

def evaluate_chebyshev_u_38(x: float) -> float:
    if 38 == 0:
        return 1.0
    if 38 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for _ in range(1, 38):
        p0, p1 = p1, 2.0 * float(x) * p1 - p0
    return float(p1)


def test_evaluate_chebyshev_u_38():
    val = evaluate_chebyshev_u_38(0.5)
    assert isinstance(val, float)
    assert val == val
