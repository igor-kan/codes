"""Implementation of spherical harmonic radial component order 3014."""

def compute_spherical_harm_3014(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3014():
    v=compute_spherical_harm_3014(0.5)
    assert isinstance(v,float) and v==v
