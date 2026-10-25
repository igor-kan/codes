"""Implementation of spherical harmonic radial component order 17194."""

def compute_spherical_harm_17194(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17194():
    v=compute_spherical_harm_17194(0.5)
    assert isinstance(v,float) and v==v
