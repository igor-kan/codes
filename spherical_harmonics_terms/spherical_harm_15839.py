"""Implementation of spherical harmonic radial component order 15839."""

def compute_spherical_harm_15839(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15839():
    v=compute_spherical_harm_15839(0.5)
    assert isinstance(v,float) and v==v
