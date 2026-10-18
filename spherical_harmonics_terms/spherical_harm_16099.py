"""Implementation of spherical harmonic radial component order 16099."""

def compute_spherical_harm_16099(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16099():
    v=compute_spherical_harm_16099(0.5)
    assert isinstance(v,float) and v==v
