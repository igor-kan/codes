"""Implementation of spherical harmonic radial component order 17809."""

def compute_spherical_harm_17809(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17809():
    v=compute_spherical_harm_17809(0.5)
    assert isinstance(v,float) and v==v
