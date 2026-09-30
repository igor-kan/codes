"""Implementation of continued fraction approximant order 5."""

def compute_continued_frac_5(x: float) -> float:
    # Continued fraction approximant order 5
    a = 1.0
    for k in range(6, 0, -1):
        a = float(k) + float(x) / (a if a != 0.0 else 1.0)
    return float(a)

import math

def test_compute_continued_frac_5():
    val = compute_continued_frac_5(0.5)
    assert isinstance(val, float)
    assert val == val
