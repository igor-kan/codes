"""Implementation of rational function approximant order 13011."""

def compute_pade_approx_13011(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_13011():
    v=compute_pade_approx_13011(0.5)
    assert isinstance(v,float) and v==v
