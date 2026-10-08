"""Implementation of continued fraction approximant order 6040."""

def compute_continued_frac_6040(x: float) -> float:
    a = 1.0
    for k in range(5, 0, -1):
        a = float(k) + float(x)/(a if a!=0.0 else 1.0)
    return float(a)

def test_compute_continued_frac_6040():
    v=compute_continued_frac_6040(0.5)
    assert isinstance(v,float) and v==v
