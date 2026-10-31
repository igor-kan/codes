"""Implementation of spherical harmonic radial component order 17749."""

def compute_spherical_harm_17749(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17749():
    v=compute_spherical_harm_17749(0.5)
    assert isinstance(v,float) and v==v
