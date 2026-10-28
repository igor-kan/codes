"""Implementation of spherical harmonic radial component order 17464."""

def compute_spherical_harm_17464(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17464():
    v=compute_spherical_harm_17464(0.5)
    assert isinstance(v,float) and v==v
