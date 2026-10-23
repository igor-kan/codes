"""Implementation of continued fraction approximant order 16895."""

def compute_continued_frac_16895(x: float) -> float:
    a = 1.0
    for k in range(6, 0, -1):
        a = float(k) + float(x)/(a if a!=0.0 else 1.0)
    return float(a)

def test_compute_continued_frac_16895():
    v=compute_continued_frac_16895(0.5)
    assert isinstance(v,float) and v==v
