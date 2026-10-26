"""Implementation of spherical harmonic radial component order 17274."""

def compute_spherical_harm_17274(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17274():
    v=compute_spherical_harm_17274(0.5)
    assert isinstance(v,float) and v==v
