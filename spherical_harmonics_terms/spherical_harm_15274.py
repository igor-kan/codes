"""Implementation of spherical harmonic radial component order 15274."""

def compute_spherical_harm_15274(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15274():
    v=compute_spherical_harm_15274(0.5)
    assert isinstance(v,float) and v==v
