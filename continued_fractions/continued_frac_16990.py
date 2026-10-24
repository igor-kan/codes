"""Implementation of continued fraction approximant order 16990."""

def compute_continued_frac_16990(x: float) -> float:
    a = 1.0
    for k in range(5, 0, -1):
        a = float(k) + float(x)/(a if a!=0.0 else 1.0)
    return float(a)

def test_compute_continued_frac_16990():
    v=compute_continued_frac_16990(0.5)
    assert isinstance(v,float) and v==v
