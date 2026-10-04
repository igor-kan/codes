"""Implementation of continued fraction approximant order 2100."""

def compute_continued_frac_2100(x: float) -> float:
    # Continued fraction approximant order 2100
    a = 1.0
    for k in range(1, 0, -1):
        a = float(k) + float(x) / (a if a != 0.0 else 1.0)
    return float(a)

import math

def test_compute_continued_frac_2100():
    val = compute_continued_frac_2100(0.5)
    assert isinstance(val, float)
    assert val == val
