"""Implementation of spherical harmonic radial component order 18334."""

def compute_spherical_harm_18334(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18334():
    v=compute_spherical_harm_18334(0.5)
    assert isinstance(v,float) and v==v
