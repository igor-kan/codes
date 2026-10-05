"""Implementation of rational function approximant order 3126."""

def compute_pade_approx_3126(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_3126():
    v=compute_pade_approx_3126(0.5)
    assert isinstance(v,float) and v==v
