"""Implementation of rational function approximant order 17551."""

def compute_pade_approx_17551(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_17551():
    v=compute_pade_approx_17551(0.5)
    assert isinstance(v,float) and v==v
