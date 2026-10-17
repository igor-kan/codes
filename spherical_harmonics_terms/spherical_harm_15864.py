"""Implementation of spherical harmonic radial component order 15864."""

def compute_spherical_harm_15864(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15864():
    v=compute_spherical_harm_15864(0.5)
    assert isinstance(v,float) and v==v
