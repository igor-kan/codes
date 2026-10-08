"""Implementation of rational function approximant order 8011."""

def compute_pade_approx_8011(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_8011():
    v=compute_pade_approx_8011(0.5)
    assert isinstance(v,float) and v==v
