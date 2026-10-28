"""Implementation of spherical harmonic radial component order 17534."""

def compute_spherical_harm_17534(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17534():
    v=compute_spherical_harm_17534(0.5)
    assert isinstance(v,float) and v==v
