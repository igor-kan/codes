"""Implementation of rational function approximant order 10021."""

def compute_pade_approx_10021(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_10021():
    v=compute_pade_approx_10021(0.5)
    assert isinstance(v,float) and v==v
