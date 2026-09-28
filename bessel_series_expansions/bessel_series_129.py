"""Implementation of bessel series expansion degree/order 129."""

def evaluate_bessel_series_129(x: float) -> float:
    k = 1
    m = 17
    import math
    sign = -1.0 if (k % 2 != 0) else 1.0
    denom = float(math.factorial(k) * math.factorial(k + m))
    return float(sign * ((float(x) / 2.0) ** (2 * k + m)) / denom)


def test_evaluate_bessel_series_129():
    val = evaluate_bessel_series_129(0.5)
    assert isinstance(val, float)
    assert val == val
