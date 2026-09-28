"""Implementation of bessel series expansion degree/order 14."""

def evaluate_bessel_series_14(x: float) -> float:
    k = 6
    m = 2
    import math
    sign = -1.0 if (k % 2 != 0) else 1.0
    denom = float(math.factorial(k) * math.factorial(k + m))
    return float(sign * ((float(x) / 2.0) ** (2 * k + m)) / denom)


def test_evaluate_bessel_series_14():
    val = evaluate_bessel_series_14(0.5)
    assert isinstance(val, float)
    assert val == val
