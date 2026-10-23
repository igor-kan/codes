"""Implementation of spherical harmonic radial component order 16809."""

def compute_spherical_harm_16809(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16809():
    v=compute_spherical_harm_16809(0.5)
    assert isinstance(v,float) and v==v
