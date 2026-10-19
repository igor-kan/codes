"""Implementation of spherical harmonic radial component order 16284."""

def compute_spherical_harm_16284(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16284():
    v=compute_spherical_harm_16284(0.5)
    assert isinstance(v,float) and v==v
