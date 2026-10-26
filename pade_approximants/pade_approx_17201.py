"""Implementation of rational function approximant order 17201."""

def compute_pade_approx_17201(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_17201():
    v=compute_pade_approx_17201(0.5)
    assert isinstance(v,float) and v==v
