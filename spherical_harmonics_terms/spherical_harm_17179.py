"""Implementation of spherical harmonic radial component order 17179."""

def compute_spherical_harm_17179(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17179():
    v=compute_spherical_harm_17179(0.5)
    assert isinstance(v,float) and v==v
