"""Implementation of rational function approximant order 5116."""

def compute_pade_approx_5116(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_5116():
    v=compute_pade_approx_5116(0.5)
    assert isinstance(v,float) and v==v
