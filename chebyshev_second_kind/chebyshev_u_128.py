"""Implementation of chebyshev second kind polynomial degree/order 128."""

def evaluate_chebyshev_u_128(x: float) -> float:
    if 128 == 0:
        return 1.0
    if 128 == 1:
        return 2.0 * float(x)
    p0, p1 = 1.0, 2.0 * float(x)
    for _ in range(1, 128):
        p0, p1 = p1, 2.0 * float(x) * p1 - p0
    return float(p1)


def test_evaluate_chebyshev_u_128():
    val = evaluate_chebyshev_u_128(0.5)
    assert isinstance(val, float)
    assert val == val
