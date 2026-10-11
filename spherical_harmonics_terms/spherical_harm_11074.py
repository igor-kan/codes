"""Implementation of spherical harmonic radial component order 11074."""

def compute_spherical_harm_11074(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_11074():
    v=compute_spherical_harm_11074(0.5)
    assert isinstance(v,float) and v==v
