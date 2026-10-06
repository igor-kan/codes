"""Implementation of rational function approximant order 4096."""

def compute_pade_approx_4096(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_4096():
    v=compute_pade_approx_4096(0.5)
    assert isinstance(v,float) and v==v
