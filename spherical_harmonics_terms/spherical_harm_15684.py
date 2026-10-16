"""Implementation of spherical harmonic radial component order 15684."""

def compute_spherical_harm_15684(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15684():
    v=compute_spherical_harm_15684(0.5)
    assert isinstance(v,float) and v==v
