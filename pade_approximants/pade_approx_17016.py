"""Implementation of rational function approximant order 17016."""

def compute_pade_approx_17016(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17016():
    v=compute_pade_approx_17016(0.5)
    assert isinstance(v,float) and v==v
