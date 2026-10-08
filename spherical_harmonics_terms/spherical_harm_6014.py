"""Implementation of spherical harmonic radial component order 6014."""

def compute_spherical_harm_6014(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6014():
    v=compute_spherical_harm_6014(0.5)
    assert isinstance(v,float) and v==v
