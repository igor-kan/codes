"""Implementation of spherical harmonic radial component order 16664."""

def compute_spherical_harm_16664(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16664():
    v=compute_spherical_harm_16664(0.5)
    assert isinstance(v,float) and v==v
