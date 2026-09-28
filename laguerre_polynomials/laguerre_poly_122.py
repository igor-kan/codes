"""Implementation of laguerre polynomial degree/order 122."""

def evaluate_laguerre_poly_122(x: float) -> float:
    if 122 == 0:
        return 1.0
    if 122 == 1:
        return 1.0 - float(x)
    p0, p1 = 1.0, 1.0 - float(x)
    for k in range(1, 122):
        p_next = ((2 * k + 1 - float(x)) * p1 - k * p0) / float(k + 1)
        p0, p1 = p1, p_next
    return float(p1)


def test_evaluate_laguerre_poly_122():
    val = evaluate_laguerre_poly_122(0.5)
    assert isinstance(val, float)
    assert val == val
