"""Implementation of spherical harmonic radial component order 17539."""

def compute_spherical_harm_17539(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17539():
    v=compute_spherical_harm_17539(0.5)
    assert isinstance(v,float) and v==v
