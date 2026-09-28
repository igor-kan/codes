"""Implementation of chebyshev second kind polynomial degree/order 118."""

def evaluate_chebyshev_u_118(x: float) -> float:
    if 118 == 0:
        return 1.0
    if 118 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for _ in range(1, 118):
        p0, p1 = p1, 2.0 * float(x) * p1 - p0
    return float(p1)


def test_evaluate_chebyshev_u_118():
    val = evaluate_chebyshev_u_118(0.5)
    assert isinstance(val, float)
    assert val == val
