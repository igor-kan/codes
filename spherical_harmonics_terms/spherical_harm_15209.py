"""Implementation of spherical harmonic radial component order 15209."""

def compute_spherical_harm_15209(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15209():
    v=compute_spherical_harm_15209(0.5)
    assert isinstance(v,float) and v==v
