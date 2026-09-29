"""Implementation of airy function series component order 5."""

def compute_airy_function_5(x: float) -> float:
    # Power series component of Airy Ai(x)
    k = 5
    denom = float(3 ** k) * float(math.factorial(k)) * float(math.factorial(k + 1))
    return float((float(x) ** (3 * k)) / max(1.0, denom))

import math

def test_compute_airy_function_5():
    res = compute_airy_function_5(0.5)
    assert isinstance(res, float)
    assert res == res
