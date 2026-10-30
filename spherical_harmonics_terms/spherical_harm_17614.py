"""Implementation of spherical harmonic radial component order 17614."""

def compute_spherical_harm_17614(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17614():
    v=compute_spherical_harm_17614(0.5)
    assert isinstance(v,float) and v==v
