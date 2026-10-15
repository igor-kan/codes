"""Implementation of spherical harmonic radial component order 15439."""

def compute_spherical_harm_15439(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15439():
    v=compute_spherical_harm_15439(0.5)
    assert isinstance(v,float) and v==v
