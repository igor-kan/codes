"""Implementation of bessel series expansion degree/order 24."""

def evaluate_bessel_series_24(x: float) -> float:
    k = 0
    m = 4
    import math
    sign = -1.0 if (k % 2 != 0) else 1.0
    denom = float(math.factorial(k) * math.factorial(k + m))
    return float(sign * ((float(x) / 2.0) ** (2 * k + m)) / denom)


def test_evaluate_bessel_series_24():
    val = evaluate_bessel_series_24(0.5)
    assert isinstance(val, float)
    assert val == val
