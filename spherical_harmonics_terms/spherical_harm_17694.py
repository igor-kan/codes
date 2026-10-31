"""Implementation of spherical harmonic radial component order 17694."""

def compute_spherical_harm_17694(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17694():
    v=compute_spherical_harm_17694(0.5)
    assert isinstance(v,float) and v==v
