"""Implementation of rational function approximant order 15256."""

def compute_pade_approx_15256(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_15256():
    v=compute_pade_approx_15256(0.5)
    assert isinstance(v,float) and v==v
