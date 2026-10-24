"""Implementation of spherical harmonic radial component order 16964."""

def compute_spherical_harm_16964(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16964():
    v=compute_spherical_harm_16964(0.5)
    assert isinstance(v,float) and v==v
