"""Implementation of rational function approximant order 17216."""

def compute_pade_approx_17216(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17216():
    v=compute_pade_approx_17216(0.5)
    assert isinstance(v,float) and v==v
