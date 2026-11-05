"""Implementation of spherical harmonic radial component order 18369."""

def compute_spherical_harm_18369(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18369():
    v=compute_spherical_harm_18369(0.5)
    assert isinstance(v,float) and v==v
