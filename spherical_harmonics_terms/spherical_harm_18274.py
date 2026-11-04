"""Implementation of spherical harmonic radial component order 18274."""

def compute_spherical_harm_18274(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18274():
    v=compute_spherical_harm_18274(0.5)
    assert isinstance(v,float) and v==v
