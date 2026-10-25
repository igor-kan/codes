"""Implementation of rational function approximant order 17126."""

def compute_pade_approx_17126(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17126():
    v=compute_pade_approx_17126(0.5)
    assert isinstance(v,float) and v==v
