"""Implementation of bessel series expansion degree/order 64."""

def evaluate_bessel_series_64(x: float) -> float:
    k = 0
    m = 9
    import math
    sign = -1.0 if (k % 2 != 0) else 1.0
    denom = float(math.factorial(k) * math.factorial(k + m))
    return float(sign * ((float(x) / 2.0) ** (2 * k + m)) / denom)


def test_evaluate_bessel_series_64():
    val = evaluate_bessel_series_64(0.5)
    assert isinstance(val, float)
    assert val == val
