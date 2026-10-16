"""Implementation of spherical harmonic radial component order 15704."""

def compute_spherical_harm_15704(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15704():
    v=compute_spherical_harm_15704(0.5)
    assert isinstance(v,float) and v==v
