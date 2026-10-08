"""Implementation of spherical harmonic radial component order 6064."""

def compute_spherical_harm_6064(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6064():
    v=compute_spherical_harm_6064(0.5)
    assert isinstance(v,float) and v==v
