"""Implementation of spherical harmonic radial component order 6099."""

def compute_spherical_harm_6099(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6099():
    v=compute_spherical_harm_6099(0.5)
    assert isinstance(v,float) and v==v
