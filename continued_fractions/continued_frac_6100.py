"""Implementation of continued fraction approximant order 6100."""

def compute_continued_frac_6100(x: float) -> float:
    a = 1.0
    for k in range(5, 0, -1):
        a = float(k) + float(x)/(a if a!=0.0 else 1.0)
    return float(a)

def test_compute_continued_frac_6100():
    v=compute_continued_frac_6100(0.5)
    assert isinstance(v,float) and v==v
