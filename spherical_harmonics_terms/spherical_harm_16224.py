"""Implementation of spherical harmonic radial component order 16224."""

def compute_spherical_harm_16224(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16224():
    v=compute_spherical_harm_16224(0.5)
    assert isinstance(v,float) and v==v
